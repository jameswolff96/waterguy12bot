import pymysql
import pymysql.cursors
import traceback


DBNAME = ''
DBUSER = ''
DBHOST = ''
DBPASSWORD = ''

try:
    import Config
    DBNAME = Config.DBNAME
    DBUSER = Config.DBUSER
    DBHOST = Config.DBHOST
    DBPASSWORD = Config.DBPASSWORD
except ImportError:
    pass

connection = pymysql.connect(host=DBHOST, port=3306, user=DBUSER, password=DBPASSWORD, db=DBNAME, charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
cursor = connection.cursor()

def setup():
    try:
        connection = pymysql.connect(host=DBHOST, port=3306, user=DBUSER, password=DBPASSWORD, db=DBNAME, charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
    except:
        print("Unale to connect to the database")

    cursor = connection.cursor()

    try:
        cursor.execute('CREATE TABLE submissions ( submissionid varchar(16) PRIMARY KEY, requester varchar (50), subreddit varchar(50), notsure boolean)')
        connection.commit()
    except Exception as e:
        cursor.execute('ROLLBACK')
        connection.commit()

setup()


def addSubmission(submissionid, requester, subreddit, notsure):
    try:
        subreddit = str(subreddit).lower()

        cursor.execute('INSERT INTO submissions (submissionid, requester, subreddit, notsure) VALUES (%s, %s, %s, %s)', (submissionid, requester, subreddit, notsure))
        connection.commit()
    except Exception as e:
        traceback.print_exc()
        cursor.execute('ROLLBACK')
        connection.commit()

def submissionExists(submissionid):
    try:
        cursor.execute('SELECT * FROM submissions WHERE submissionid = %s', (submissionid))
        if (cursor.fetchone()) is None:
            connection.commit()
            return False
        else:
            connection.commit()
            return True
    except Exception as e:
        traceback.print_exc()
        cursor.execute('ROLLBACK')
        conection.commit()
        return True
