
import click
from api.models import db, User

"""
In this file, you can add as many commands as you want using the @app.cli.command decorator
Flask commands are usefull to run cronjobs or tasks outside of the API but sill in integration 
with youy database, for example: Import the price of bitcoin every night as 12am
"""
def setup_commands(app):
    
    """ 
    This is an example command "insert-test-users" that you can run from the command line
    by typing: $ flask insert-test-users 5
    Note: 5 is the number of users to add
    """
    # @app.cli.command("insert-test-users") # name of our command
    # @click.argument("count") # argument of out command
    # def insert_test_users(count):
    #     print("Creating test users")
    #     for x in range(1, int(count) + 1):
    #         user = User()
    #         user.email = "test_user" + str(x) + "@test.com"
    #         user.password = "123456"
    #         user.is_active = True
    #         db.session.add(user)
    #         db.session.commit()
    #         print("User: ", user.email, " created.")

    #     print("All test users created")

    @app.cli.command("insert-users")
    def insert_users_data():
        users = [
            {
                "name": "John Doe",
                "email": "john@example.com",
                "password": "$2y$10$ILsnuwcNhB9oMo4/BFKiiukjcjuvliXE4WSEfe3x2SwpdFAL3HP9q",                
            },
            {
                "name": "Jane Smith",
                "email": "jane@example.com",
                "password": "$2y$10$d1NSFyZ0T6nh6SfAvf51YuQWDY0Pge41.GbZGZYbmuqB0j4KQUZ4u",                
            },
            {
                "name": "Michael Johnson",
                "email": "michael@example.com",
                "password": "$2y$10$40E/wNQ1atMEyOYgyNQ1IOLcRIaTS4kpJ7wauKPD7/Yk0NH8F1OKK",                
            },
            
        ]

        for user in users:
            new_user = User()
            new_user.name = user["name"]
            new_user.email = user["email"]
            new_user.password = user["password"]            
            db.session.add(new_user)
            db.session.commit()
            print("user: ", new_user.name, " created.")