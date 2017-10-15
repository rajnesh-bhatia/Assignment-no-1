    # Importing Files and Libraries

from appJar import gui
from data import *
from Student import student
from Teacher import teacher
import  yappi
import  os
from subprocess import call
import Tkinter as tk
import tkFont

# handle button events

class login_page:

    #Constructor
    def __init__(self,app):
        self.app= app
        self.app.setBg("pink")
        self.app.setLabelFont(20, font='Times New Roman')
        # add & configure widgets - widgets get a name, to help referencing them later
        self.app.addLabel("l1", "Digital Quiz System")
        self.app.setLabelFg("l1", "blue")

        self.app.addButtons(["Login" , "Sign Up"], self.show)
        # start the GUI
        self.app.go()



    #Button Clicked
    def press(self,app):
        if app =="Cancel":
            self.app.stop()
            return False
        else:
            print "Hello"
            u_name = self.app.getEntry("Username")
            #if len(u_name) == 0:

            p_word = self.app.getEntry("Password")
            print("User:", u_name, "Pass:", p_word)
            i=0
            for x in rows:

                if u_name == x[1] and p_word == x[2]:

                    print ("You are logged in")
                    name = x[1]
                    self.app.removeAllWidgets()
                    if x[3] == 'S':

                        student(self.app,name)

                    if x[3] == 'T':
                        teacher(self.app,name)
            i+=1
            print "username or password invalid"
            return False


    #Event Occurred
    def click(self,app):
        print  "Hi"
        a=self.app.getEntry("username")
        b= self.app.getEntry("password")
        c = self.app.getEntry("Confirm Password")
        d= self.app.getEntry("Role")
        if b == c:
            cut = db.cursor()
            cut.execute("Insert into user(username,password,role) values(%s,%s,%s)",(a,b,d))
            self.app.removeAllWidgets()
            self.app.addLabel("li" ,"You are Sucessfully Registered")
            self.app.addButton("Log In" , self.car)
            return  True
        else :
            self.app.removeAllWidgets()
            self.app.addLabel("Match" , "Password don't match")
            self.app.addButton("Quit" , self.end)
        return False

    def car(self,app):
        self.app.removeAllWidgets()
        self.show(app)

    #To sto the GUI
    def end(self,app):
        self.app.stop()
        return True

     #TO SignUp the Users
    def show(self,app):
        if app == "Sign Up":
            self.app.addLabelEntry("username", 1, 0)
            self.app.addLabelSecretEntry("password", 2, 0)
            self.app.addLabelSecretEntry("Confirm Password", 3, 0)
            self.app.addLabelEntry("Role", 4, 0)
            self.app.addButton("Add", self.click)
        else:
            self.app.addLabelEntry("Username", 1, 0)
            self.app.addLabelSecretEntry("Password", 2, 0)
            # link the buttons to the function called press
            self.app.addButtons(["Submit", "Cancel"], self.press)
            self.app.setFocus("Username")



if __name__ == '__main__':

    #Yappi Function for Profiling
    yappi.start()

    # create a GUI variable called app
    app = gui("Login Window", "600x500")

    # Calling constructor
    ob = login_page(app)

#ending yappi
yappi.get_func_stats().print_all()
yappi.get_thread_stats().print_all()
print yappi.get_mem_usage()

