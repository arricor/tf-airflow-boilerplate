from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.operators.dummy_operator import DummyOperator
from airflow.models import Variable # you will need this if you are defining your variables on WebUi and use them here
from datetime import datetime, timedelta
from py_files.py_1 import print1
from py_files.py_2 import print2
from py_files.py_3 import print3
from py_files.py_4 import print4


# Examples of variables that you can define and use on Airflow

# CONNECTION_ID = Variable.get("connection")
# GCS_BUCKET_ID = 'airflow-pipeline-assets'

# Defining default Airflow Arguments
default_args = {
    'owner': 'luke',
    'depends_on_past': True, # Change this to false, if you don't want your dag to depend on the past dag run
    'start_date': datetime(2020, 5, 11),
    'email': ['luke@luke.com'], # Please update your email address here
    'email_on_failure': True,
    'email_on_retry': True,
    'retries': 3,
    'retry_delay': timedelta(minutes=2),
    'provide_context': True
}

# Creating Dag on Airflow
dag = DAG(
    dag_id='tf_pipeline',
    schedule_interval="0 9 * * *",
    catchup=False,
    default_args=default_args

)

# Adding readme description for the DAG
dag.doc_md = "Runs a python operator to call 4 TF code dependent on each other"

# Dummy Start operator for Airflow Webui Graph
start = DummyOperator(task_id='start', dag=dag)

run_py1_file = PythonOperator(
    task_id='run_py1_file',
    python_callable=print1,
    provide_context=True,
    # templates_dict='', # use this to pass in parameters to your python function as needed
    dag=dag
)

run_py2_file = PythonOperator(
    task_id='run_py2_file',
    python_callable=print2,
    provide_context=True,
    # templates_dict='', # use this to pass in parameters to your python function as needed
    dag=dag
)

run_py3_file = PythonOperator(
    task_id='run_py3_file',
    python_callable=print3,
    provide_context=True,
    # templates_dict='', # use this to pass in parameters to your python function as needed
    dag=dag
)

run_py4_file = PythonOperator(
    task_id='run_py4_file',
    python_callable=print4,
    provide_context=True,
    # templates_dict='', # use this to pass in parameters to your python function as needed
    dag=dag
)


start >> run_py1_file >> run_py2_file >> run_py3_file >> run_py4_file