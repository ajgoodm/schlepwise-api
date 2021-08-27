import os


class Config:
    API_VERSION = 0

    DB_NAME = os.environ['DATABASE_NAME']
    # Read/write for API
    SQLALCHEMY_DATABASE_URI = '{dialect}://{username}:{password}@{host}:{port}/{database}'.format(
        dialect='postgresql',
        username=os.environ['DATABASE_USER'],
        password=os.environ['DATABASE_PASSWORD'],
        host=os.environ['DATABASE_HOST'],
        port=os.environ['DATABASE_PORT'],
        database=os.environ['DATABASE_NAME'],
    )
