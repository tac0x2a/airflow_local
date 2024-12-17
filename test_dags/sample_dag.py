from airflow import DAG
from airflow.decorators import task

with DAG(
    "sample_test_dag",
    tags=["sample"],
    catchup=False,
) as dag:

    @task
    def hello_task():
        return "Hello,Task"

    hello_task()
