import pendulum

from airflow.providers.standard.operators.bash import BashOperator
from airflow.sdk import DAG, chain

with DAG(
    dag_id="dags_bash_operator",
    schedule=None, #"0 0 0 0 0" 분 시 일 월 요일
    start_date=pendulum.datetime(2021, 1, 1, tz="Asia/Seoul"), # UTC표준시간, 한국보다 9시간 늦음
    catchup=False, # 과저 날짜 소급해버림...
    tags=["example", "example2", "example3"],
) as dag:
    # 객체
    bash_t1 = BashOperator(
        # task 이름
        task_id = "bash_t1",
        bash_command="echo whoami",
    )
    
    bash_t2 = BashOperator(
        # task 이름
        task_id = "bash_t2",
        bash_command="echo $HOSTNAME",
    )

    # 실행순거
    bash_t1 >> bash_t2