from airflow.models import DagBag


class TestDag:
    def test_dag_validation(self):
        dagbag = DagBag(dag_folder="test_dags/")

        dag = dagbag.get_dag(dag_id="sample_test_dag")

        assert dagbag.import_errors == {}
        assert dag is not None
        assert dag.catchup is False

        expected = ["hello_task", "world_task"]
        actual = sorted([task.task_id for task in dag.tasks])
        assert actual == expected
