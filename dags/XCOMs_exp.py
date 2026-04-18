from airflow.sdk import dag,task

@dag(
    dag_id="XCOMs_exp"    
 )

def XCOMs_exp():

    @task.python
    def first_task():
        print("Extracting data:")
        fetched_data = {"data":[1,2,3,4,5]}
        return fetched_data
    
    @task.python
    def second_task(data:dict):
        fetched_data=data["data"]
        transformed_data = [i*2 for i in fetched_data]
        transform_data_dict = {"transform_dict":transformed_data}
        return transform_data_dict
    
    @task.python
    def third_task(data:dict):
        load_task = data
        return load_task

    first = first_task()
    second = second_task(first)
    third = third_task(second)
    
    
XCOMs_exp()

