import sqlite3

# creating a connection to the db
conn = sqlite3.connect("tutorial.db")

# cursor is used to execute sql queries
cursor = conn.cursor()

"""
 - Class -> Table
 - Attributes -> Table colummns
 - Class instance -> Table row
"""
class User:
    # class attributes
    no_of_eyes = 2

    def __init__(self, name):
        # instance attributes
        self.name = name

    # instance method
    def walk(self):
        print(f"{self.name} is walking")

    # class method
    @classmethod
    def example(cls):
        user = cls("John")
        print(f"{user.name}  Number of eyes is {cls.no_of_eyes}")

    def create_user(self):
        sql = "INSERT INTO users (name) VALUES (?)"

        cursor.execute(sql, (self.name,))
        conn.commit()
        print("User inserted")

    @classmethod
    def create_table(cls):
        sql = """
        CREATE TABLE IF NOT EXISTS users (
            id integer primary key autoincrement,
            name text not null
        )
        """

        cursor.execute(sql)
        conn.commit()
        print("Users table created")

# instance of user class
# user = User("Jane Doe")
# user.walk()
# print(user.name)
# print(user.no_of_eyes)
User.create_table()

user = User("Joseph")
user.create_user()
