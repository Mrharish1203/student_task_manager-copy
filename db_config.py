import mysql.connector

def get_database_connection():
    connection = mysql.connector.connect(
        host = 'gateway01.ap-southeast-1.prod.aws.tidbcloud.com',
        user = 'Sxeqwg6J6MPQB6Q.root',
        password = '1OLyTXJgN4xbGEVv',
        database = 'student_task_manager',
        port = 4000
    )

    return connection 