def get_db_uri():
    data_base_URI = "{connectorname}://{username}:{password}@{hostname}/{databasename}".format(
            connectorname="mariadb+mariadbconnector",
            username="root",
            password="pesk-2020",
            hostname="127.0.0.1:3306",
            databasename="ident",
            )
    return data_base_URI

SECRET_KEY = '8b2771f9bdfgdfgw186123sdfsf749ccadad43'
SQLALCHEMY_DATABASE_URI=get_db_uri()
