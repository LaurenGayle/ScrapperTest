"""
This is the Main module
starting Call Main Project functions here Ie Starting program
"""
import database

__author__ = "Nicholas Blackburn, Lauren Gayle"
__Version__ = "1.0.0-Pre"
__license__ = "MIT"


"""
Put the Main Startup code for the Project Here.
"""
def main():
    # Main Entrypoint of our Program
    print ("starting server")
    database.mysqlConnect()
    print ("push to mysql")
    database.mysqlPush()
    



# Executes Code From main when ran from command line
if __name__ == "__main__":
    main()