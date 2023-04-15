# importing libraries

## general libraries
from datetime import datetime, timedelta

## airflow libraries
from airflow.decorators import dag, task
from airflow.operators.dummy import DummyOperator
from airflow.operators.python import PythonOperator
from airflow.utils.helpers import chain, cross_downstream

## defining python tasks
@task
def get_hello():

    return "Hello!!"


@task
def print_hello(hello_object):
    print(hello_object)


@task
def print_hi():
    print('Hi!!')


# default args
default_args = {
	"owner": "Kattson Bastos",
	"retries": 1,
	"retries_delay": 0
}

## defining the DAG
@dag(
    start_date=datetime(2023,4,6),
    schedule=None,
    max_active_runs=1,
    default_args=default_args,
    catchup=False,
    tags=['template']
)
def test_xcoms():
    init = DummyOperator(task_id="init")

    end = DummyOperator(task_id="end")

    data = get_hello()

    chain(init, [data, print_hello(data)], end)
    chain(init, print_hi(), end)


dag = test_xcoms()