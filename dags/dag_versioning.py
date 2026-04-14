from airflow.sdk import dag,task

@dag(
    dag_id="dag_versioning"    
 )

def dag_versioning():

    @task.python
    def first_task():
        print("first task")
    
    @task.python
    def second_task():
        print("second task")
    
    @task.python
    def third_task():
        print("third task")
    
    @task.python
    def version_task():
        print("Versioned Task")

    first=first_task()
    second=second_task()
    third=third_task()
    version=version_task()
    
    first>>second>>third>>version
    
dag_versioning()

