"""
Tasks performed by this DAG:
"""

# import libraries
from datetime import datetime, timedelta
from airflow.decorators import dag, task
from airflow.operators.empty import EmptyOperator

from astro import sql as aql
from astro.files import File
from astro.constants import FileType
from astro.sql.table import Table, Metadata

# connections & variables
SOURCE_CONN_ID = "taxi_gcs_default"
BIGQUERY_CONN_ID = "taxi_bigquery_default"

# default args
default_args = {
    "owner": "Kattson",
    "retries": 1,
    "retry_delay": 0
}

# declare dag
@dag(
    dag_id="load_files_warehouse",
    start_date=datetime(2023, 4, 15),
    schedule_interval="@daily",
    max_active_runs=1,
    catchup=False,
    default_args=default_args,
    tags=['gcs', 'parquet', 'taxi', 'bigquery']
)
# declare main function
def load_files_warehouse():

    # init & finish
    init = EmptyOperator(task_id="init")
    finish = EmptyOperator(task_id="finish")

    taxi_gcs_bigquery = aql.load_file( #
        task_id="taxi_gcs_bigquery", 
        input_file=File(path="gs://k-taxi-landing-zone/taxi/green/green_tripdata_2023-01.parquet", filetype=FileType.PARQUET, conn_id=SOURCE_CONN_ID),
        output_table=Table(name="taxi_green", conn_id=BIGQUERY_CONN_ID),
        if_exists="replace",
        use_native_support=True,
        columns_names_capitalization="original"
    )


    init >> taxi_gcs_bigquery >> finish

#init
dag = load_files_warehouse()