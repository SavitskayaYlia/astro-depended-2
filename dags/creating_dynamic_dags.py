from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime, timedelta

# Assume we fetch this dictionary from somewhere: database, API, configuration file
databases = {
    'db1': 'UserDatabase',
    'db2': 'ProductDatabase',
    'db3': 'TestDatabase',  # This can change or be updated
}

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2023, 1, 1),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

# Function to create a DAG for each database
def create_dag(dag_id, schedule, default_args, database):
    
    dag = DAG(
        dag_id=dag_id,
        schedule_interval=schedule,
        default_args=default_args,
        catchup=False,
    )

    with dag:
        t1 = BashOperator(
            task_id='backup_database',
            bash_command=f'echo "Backing up {database}" && sleep 10',
        )

    return dag

# Loop through each database and create a DAG
for db_key, db_name in databases.items():
    dag_id = f'backup_{db_key}_dag'

    # Create a DAG for each database
    globals()[dag_id] = create_dag(dag_id, '@daily', default_args, db_name)
