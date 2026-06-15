# This is a sample Python script.
import pymysql
from flask import Flask

application = Flask(__name__)

@application.route('/')
def home():
    return "Assignment Application Running Successfully"

@application.route('/db-test')
def db_test():
    try:
        conn = pymysql.connect(
            host="awseb-e-qzsm2qgas8-stack-awsebrdsdatabase-x3pkpwlfdqyh.cozueog2an6i.us-east-1.rds.amazonaws.com",
            user="assignmentadmin",
            password="Harrypotter1#harry"
        )

        conn.close()
        return "RDS Connection Successful"

    except Exception as e:
        return f"Connection Failed: {str(e)}"

if __name__ == '__main__':
    application.run()
