class PostgresConfig:
    def __init__(self, host, user, password, database, port):
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.database = database