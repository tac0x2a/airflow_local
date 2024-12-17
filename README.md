# airflow-local
Sample code for airflow dag local testing.

## Setup

```
$ AIRFLOW_HOME="$(pwd)/airflow_home" uv run airflow db init
```

## Run test
```
$ AIRFLOW_HOME="$(pwd)/airflow_home" uv run pytest
```

## (Optional) Run Airflow local
```
$ AIRFLOW_HOME="$(pwd)/airflow_home" uv run airflow users create --role Admin --username test --email test --firstname test --lastname test --password test

$ AIRFLOW__CORE__DAGS_FOLDER="$(pwd)/test_dags" AIRFLOW_HOME="$(pwd)/airflow_home" uv run airflow scheduler
$ AIRFLOW_HOME="$(pwd)/airflow_home" uv run airflow webserver
```
