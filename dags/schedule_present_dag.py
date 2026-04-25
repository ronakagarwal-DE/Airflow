from airflow.sdk import dag,task
from pendulum import datetime

@dag(
    dag_id="schedule_present_dag",
    start_date= datetime(year=2026,month=4,day=25,tz="Asia/Calcutta"),
    schedule="@daily",
    is_paused_upon_creation=False
 )

def build_dag():

    @task.python
    def first_task():
        print("first task")
    
    @task.python
    def second_task():
        print("second task")
    
    @task.python
    def third_task():
        print("third task")

    first=first_task()
    second=second_task()
    third=third_task()
    
    first>>second>>third
    
build_dag()