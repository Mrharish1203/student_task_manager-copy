import mysql.connector

def get_database_connection():
    connection = mysql.connector.connect(
        host = 'gateway01.ap-southeast-1.prod.aws.tidbcloud.com',
        user = '2dAAo1GjoN1ER1R.root',
        password = 'l33KohJiJm4kcRMJ',
        database = 'student_task_manager',
        port = 4000
    )

    return connection 