from dagster import job, op, daily_partitioned_config, sensor, RunRequest
import os
from datetime import datetime

@op
def hello_op1():
    print("hello 1")

@op
def hello_op2():
    print("hello 2")

@daily_partitioned_config(start_date=datetime(2020, 1, 1))
def my_partitioned_config(start: datetime, _end: datetime):
    return {
        "ops": {
            "hello_op1": {"config": {"date": start.strftime("%Y-%m-%d")}},
            "hello_op2": {"config": {"date": start.strftime("%Y-%m-%d")}},
        }
    }


@job(config=my_partitioned_config)
def hello_job():
    hello_op1()
    hello_op2()


MY_DIRECTORY = "./data"


@sensor(job=hello_job)
def my_directory_sensor():
    for filename in os.listdir(MY_DIRECTORY):
        filepath = os.path.join(MY_DIRECTORY, filename)
        if os.path.isfile(filepath):
            yield RunRequest(
                run_key=filename,
                run_config={
                    "ops": {"hello_op1": {"config": {"filename": filename}}}
                },
                op_selection=["hello_op1"]
            )
