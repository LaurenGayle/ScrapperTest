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
    
    
    a =input(" Would you like to auto update database? type yes if want to ")
    b =input(" Would you like to pullfrom database? type pull if want to ")
    
    if(a == 'yes'):
        print ("push to mysql")
        database.mysqlPush()
    else:
        if(b == 'yes'):
            print("pulling data")
            database.mysqlRead()
        else:
            print("error quitting")
            main()



# Executes Code From main when ran from command line
if __name__ == "__main__":
    main()