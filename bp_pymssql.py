import pymssql
import logging
import azure.functions as func
import json
bp_test_pymssql = func.Blueprint()
@bp_test_pymssql.function_name(name = "test_pymssql")
@bp_test_pymssql.route(route="test_pymssql")
def test_pymssql(req: func.HttpRequest) -> func.HttpResponse:
    server = "da-cc-sqldb-fz-test.database.windows.net"
    user = "azureuser"
    password = "Obi@2024"
    database = "rd-cc-sqldb-fzdb-test"
    conn = pymssql.connect(server, user, password, database)
    cursor = conn.cursor(as_dict=True)

    cursor.execute('SELECT [order],[title] FROM [dbo].[ToDo] WHERE Id=%s', '280BBA6B-F3D1-4313-A883-5799AB21286C')
    json_data = []
    for row in cursor:
        logging.info("ID=%s, Name=%s" % (row['order'], row['title']))
        json_data.append({"order":row['order'],"title":row['title']})
        print("ID=%s, Name=%s" % (row['order'], row['title']))
    return func.HttpResponse(
        json.dumps(json_data),
        status_code=200,
        mimetype="application/json"
    )

