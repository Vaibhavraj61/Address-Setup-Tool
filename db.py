import dotenv
import os
import oracledb

dotenv.load_dotenv()
user=os.getenv("user")
pwd=os.getenv("passwd")
dsn=os.getenv("dsn_value")

def createConnection():
    oracledb.init_oracle_client()
    try:
        conn=oracledb.connect(user=user,password=pwd,dsn=dsn)
    except Exception as e:
        print("Connection Failed",type(e),str(e))
    else:
        return conn
    
connection=createConnection()

def createSQL(conn):
    corp=7801
    sql=f"select corp,house from ECOMMERCE.OPTM_HOUSE_B where corp={corp} and rownum<=10"
    cursor=conn.cursor()
    result = cursor.execute(sql)
    return result

result = createSQL(connection)

def getDBAccount(res):
    for data in res:
        print(data)

accts = getDBAccount(result)