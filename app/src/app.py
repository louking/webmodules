'''
app.py is only used to support flask commands

server execution from run.py
'''

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
userconfigpath = os.path.join(abspath, 'users.cfg')
# userconfigpath first so configpath can override
configfiles.insert(0, userconfigpath)

# init_for_operation=False because when we create app this would use database and cause
# sqlalchemy.exc.OperationalError if one of the updating tables needs migration
app = create_app(Production(configfiles), configfiles, init_for_operation=False)

# set up flask command processing
migrate = Migrate(app, db, compare_type=True)

if __name__ == "__main__":
    app.run(host ='0.0.0.0', port=5000)