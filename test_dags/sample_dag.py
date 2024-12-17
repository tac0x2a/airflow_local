from airflow import DAG, XComArg
from airflow.decorators import task

with DAG(
    "sample_test_dag",
    tags=["sample"],
    catchup=False,
) as dag:

    @task
    def hello_task() -> str:
        return "Hello,Task"

    @task
    def world_task(h: XComArg):
        return f"{h}, World"

    world_task(hello_task())
