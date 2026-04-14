from airflow.sdk import dag,task

@dag(
    dag_id="operators"    
 )

def operators():

    @task.python
    def first_task():
        print("first task")
    
    @task.python
    def second_task():
        print("second task")
    
    @task.python
    def third_task():
        print("third task")
    
    @task.bash
    def bash_task():
       return "echo Airflow Bash Test"

    first=first_task()
    second=second_task()
    third=third_task()
    fourth=bash_task()

    
    first  >> second >> third >> fourth
    
operators()

