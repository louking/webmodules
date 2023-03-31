# standard
import os.path

# pypi
from flask import jsonify
from flask_migrate import Migrate
from sqlalchemy.orm import scoped_session, sessionmaker

# homegrown
from webmodules import create_app, appname
from webmodules.settings import Production
from webmodules.model import db

abspath = os.path.abspath('/config')
configpath = os.path.join(abspath, f'{appname}.cfg')
configfiles = [configpath]
# userconfigpath = os.path.join(abspath, 'users.cfg')
# # userconfigpath first so configpath can override
# configfiles.insert(0, userconfigpath)

# init_for_operation=False because when we create app this would use database and cause
# sqlalchemy.exc.OperationalError if one of the updating tables needs migration
app = create_app(Production(configfiles), configfiles, init_for_operation=False)

# set up flask command processing
migrate = Migrate(app, db, compare_type=True)

# adapted from https://github.com/aiordache/demos/blob/c7aa37cc3e2f8800296f668138b4cf208b27380a/dockercon2020-demo/app/src/server.py
# similar to https://github.com/docker/awesome-compose/blob/e6b1d2755f2f72a363fc346e52dce10cace846c8/nginx-flask-mysql/backend/hello.py
class DBManager:
    def __init__(self, database='example', host="db", user="root", password_file=None, **kwargs):
        pf = open(password_file, 'r')
        self.connection = mysql.connector.connect(
            user=user, 
            password=pf.read().strip(),
            host=host,  # name of the mysql service as set in the docker compose file
            database=database,
            auth_plugin='mysql_native_password',
            **kwargs
        )
        pf.close()
        self.cursor = self.connection.cursor()
    
    def populate_db(self):
        self.cursor.execute('DROP TABLE IF EXISTS blog')
        self.cursor.execute('CREATE TABLE blog (id INT AUTO_INCREMENT PRIMARY KEY, title VARCHAR(255))')
        self.cursor.executemany('INSERT INTO blog (id, title) VALUES (%s, %s);', [(i, 'Blog post #%d'% i) for i in range (1,5)])
        self.connection.commit()
    
    def query_titles(self):
        self.cursor.execute('SELECT title FROM blog')
        rec = []
        for c in self.cursor:
            rec.append(c[0])
        return rec

@app.route('/')
def hello_world():
    return 'Hello, Docker!'

@app.route('/blogs')
def listBlog():
    global conn
    if not conn:
        conn = DBManager(host='db', database='webmodules', user='user', password_file='/run/secrets/user-password')
        conn.populate_db()
        
    rec = conn.query_titles()

    result = []
    for c in rec:
        result.append(c)

    return jsonify({"response": result})

if __name__ == "__main__":
    app.run(host ='0.0.0.0', port=5000)