import configparser

class Config:
    pass


class DatabaseConfig(Config):

    def load_config(self):

        config = configparser.ConfigParser()
        config.read("db.ini")

        required = ["host", "user", "password", "database"]

        for key in required:
            if key not in config["DATABASE"]:
                print("Missing key:", key)
                return

        print("Database Configuration Loaded")
        print(dict(config["DATABASE"]))


db = DatabaseConfig()
db.load_config()