WTF_CSRF_ENABLED = True
SECRET_KEY = 'cefalo-web-assignment'

import os
basedir = os.path.abspath(os.path.dirname(__file__))

#mysql://username:password@localhost/database_name
SQLALCHEMY_DATABASE_URI = 'mysql://root:@localhost/newsroom_database'

#'sqlite:///' + os.path.join(basedir, 'app.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')