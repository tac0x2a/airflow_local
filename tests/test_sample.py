import pytest
from airflow.models import DagBag
import pprint


class TestDag:
    def test_dag_validation(self):
        dagbag = DagBag(dag_folder="test_dags/")

        dag = dagbag.get_dag(dag_id="sample_test_dag")

        assert dagbag.import_errors == {}
        assert dag is not None

        assert dag.catchup is False

        # assert dag.doc_md != ""

        # print(type(dag))
        # print(vars(dag))

        # tasks = dag.tasks
        # task_ids = list(map(lambda task: task.task_id, tasks))
        # print(f"tasks: {task_ids}")
        pass
