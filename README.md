# tf-airflow-boilerplate

## Deploy to Airflow Cluster

- The file under ``dags`` folder in this repo should be placed on the ``dags`` folder where your Airflow is hosted
- The py_files folder needs to be placed on the root directory called py_files with all the necessary python files in them.

### Additional information on the DAG

- Dag's start date should be always a day behind from when you are deploying since Airflow scheduler runs pipeline for previous day
    more info on this here https://airflow.apache.org/docs/stable/scheduler.html
- The dag used python operator for running the python functions on the python files, with Airflow you have options of jinja templating more on this https://airflow.apache.org/docs/stable/tutorial.html#templating-with-jinja 
- ```templates_dict``` can be used to pass in parameters to your python function from the DAG file example like run timestamp can be passed as {{ ds }}
    That will automatically be converted into UTC timestamp while the DAG runs
- Please make sure your python function on python file or class have **kwargs present since we have enabled ```provide_context=True``` which send additional parameters for Jinja templating