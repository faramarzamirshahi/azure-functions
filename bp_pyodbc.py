import pymssql
import logging
import azure.functions as func
import json
import pyodbc
import os
bp_test_pyodbc = func.Blueprint()
@bp_test_pyodbc.function_name(name = "test_pyodbc")
@bp_test_pyodbc.route(route="test_pyodbc")
def test_pyodbc(req: func.HttpRequest) -> func.HttpResponse:
    #conn = pyodbc.connect('DRIVER={ODBC Driver 18 for SQL Server};SERVER=da-cc-sqldb-fz-test.database.windows.net;DATABASE=rd-cc-sqldb-fzdb-test;UID=azureuser;PWD=Obi@2024')
    connectionString = os.environ["pyodbc_connection"]
    print(connectionString)
    conn = pyodbc.connect(connectionString)
    cursor = conn.cursor()

    cursor.execute('SELECT [order],[title] FROM [dbo].[ToDo] WHERE Id=?', '001BC389-B115-403C-9192-1EE079D45B7F')
    rows = cursor.fetchall()

    json_data = []
    for row in rows:
        logging.info("ID=%s, Name=%s" % (row[0], row[1]))
        json_data.append({"order":row[0],"title":row[1]})
        print("ID=%s, Name=%s" % (row[0], row[1]))
    return func.HttpResponse(
        json.dumps(json_data),
        status_code=200,
        mimetype="application/json"
    )