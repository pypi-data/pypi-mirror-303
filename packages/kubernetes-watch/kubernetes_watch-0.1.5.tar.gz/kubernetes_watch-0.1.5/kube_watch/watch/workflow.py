from prefect import flow,  get_run_logger, runtime
import asyncio
from typing import List
import secrets
import os
import kube_watch.watch.helpers as helpers
from kube_watch.models.workflow import WorkflowOutput
from kube_watch.enums.workflow import TaskRunners, TaskInputsType


# @TODO: CONCURRENCY DOES NOT WORK PROPERLY AT FLOW LEVEL
def create_flow_based_on_config(yaml_file, run_async=True):
    workflow_config = helpers.load_workflow_config(yaml_file)
    flow_name       = workflow_config.name
    runner          = helpers.resolve_runner(workflow_config.runner)
    random_suffix   = secrets.token_hex(6)
    flow_run_name   = f"{flow_name} - {random_suffix}"

    @flow(name=flow_name, flow_run_name=flow_run_name, task_runner=runner)
    async def dynamic_workflow():
        logger = get_run_logger()
        tasks = {}

        for param in workflow_config.parameters:      
            runtime.flow_run.parameters[param.name] = param.value

        logger.info(f"Starting flow: {flow_name}")
        for task_data in workflow_config.tasks:
            task_name   = task_data.name
            func        = helpers.get_task_function(task_data.module, task_data.task, task_data.plugin_path)
            task_inputs = helpers.prepare_task_inputs(task_data.inputs.parameters) if task_data.inputs else {}

            condition_result = True
            if task_data.conditional:
                condition_result = helpers.resolve_conditional(task_data, tasks)

            if condition_result:
                # Resolve dependencies only if the task is going to be executed
                if task_data.dependency:
                    task_inputs = helpers.prepare_task_inputs_from_dep(task_data, task_inputs, tasks)
                
                task_future = helpers.submit_task(task_name, task_data, task_inputs, func)
                tasks[task_data.name] = task_future
            

        return tasks
    return dynamic_workflow


# SINGLE
def single_run_workflow(yaml_file, return_state=True) -> WorkflowOutput:
    dynamic_flow  = create_flow_based_on_config(yaml_file, run_async=False)
    flow_run = dynamic_flow(return_state=return_state)
    return WorkflowOutput(**{'flow_run': flow_run, 'config': dynamic_flow}) 


# BATCH

@flow(name="Batch Workflow Runner - Sequential")
def batch_run_sequential(batch_config, batch_dir) -> List[WorkflowOutput]:
    # batch_config = helpers.load_batch_config(batch_yaml_file)
    # batch_dir = os.path.dirname(batch_yaml_file)
    flows = []
    for item in batch_config.items:
        yaml_file_path = os.path.join(batch_dir, item.path)
        output = single_run_workflow(yaml_file_path, return_state = True)
        flows.append(output)

    return flows

# @TODO: CONCURRENCY DOES NOT WORK PROPERLY AT FLOW LEVEL
@flow(name="Batch Workflow Runner - Concurrent")
async def batch_run_concurrent(batch_config, batch_dir) -> List[WorkflowOutput]:
    # Asynchronous flow run submissions
    flow_runs = []
    for item in batch_config.items:
        yaml_file_path = os.path.join(batch_dir, item.path)
        # Here you create flow runs but do not await them yet
        flow_function = create_flow_based_on_config(yaml_file_path, run_async=True)
        flow_run_future = flow_function(return_state=True)  # Ensure this is submitted asynchronously
        flow_runs.append(flow_run_future)
        is_async = asyncio.iscoroutinefunction(flow_function)


    # Await all flow runs to finish concurrently
    results = await asyncio.gather(*flow_runs)
    return [WorkflowOutput(**{'flow_run': result, 'config': flow_function}) for result, flow_function in zip(results, flow_runs)]


def batch_run_workflow(batch_yaml_file):
    batch_config = helpers.load_batch_config(batch_yaml_file)
    batch_dir = os.path.dirname(batch_yaml_file)

    if batch_config.runner == TaskRunners.SEQUENTIAL:
        return batch_run_sequential(batch_config, batch_dir)
    
    if batch_config.runner == TaskRunners.CONCURRENT:
        return asyncio.run(batch_run_concurrent(batch_config, batch_dir))

    raise ValueError('Invalid flow runner type')
