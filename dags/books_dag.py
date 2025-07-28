# dags/books_dag.py

# create DAG file, import all the classes

from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from book_store_etl_logic import main

default_args = {
  'owner': 'kanwei Edward',
  'depends_on_past': False,
  'start_date': datetime(2025, 7, 10),
  'email_on_failure': False,
  'email_on_retry': False,
  'retries': 1,
  'retry_delay': timedelta(minutes=5),
}

dag = DAG(
  'orders_full_load',
  default_args=default_args,
  description= 'My books Table ETL DAG',
  schedule_interval='@daily',
)

run_etl = PythonOperator(
  task_id='run_etl',
  python_callable=main,
  dag=dag,
)
run_etl
