# -*- coding: utf-8 -*-
from airflow import DAG
from datetime import timedelta

from operators.us_immigration import UpsertOperator


default_args = {
    'owner': 'capstone',
    'depends_on_past': False,
    'start_date': '2016-01-01',
    'end_date': '2017-01-01',
    'email': ['airflow@example.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5)
}

dag = DAG(
    'us_immigration',
    default_args=default_args,
    schedule_interval='5 2 * * *',
)

with dag:
    upsert = UpsertOperator(task_id='upsert')


if __name__ == "__main__":
    dag.cli()
