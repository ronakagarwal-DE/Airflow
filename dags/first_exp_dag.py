from airflow.sdk import dag,task

@dag(
    dag_id="first_dag"    
 )

def basic_dag():

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
    
basic_dag()

