

                    # Importing Files and Libraries

from appJar import gui
from data import *
import os
from subprocess import call
import Tkinter as tk
import tkFont
from Tkinter import *



#global variables
i=0

class student:

    #Constructor
    def __init__(self,app,name):
        self.app = app
        self.i = 0
        self.score = 0;
        app.setLabelFont(18, font='Times New Roman')
        self.app.addLabel("Sl1", "Hello!",2,0,colspan= 5)
        self.app.addLabel("Sl2", name, 3, 0, colspan=5)
        st = db.cursor()
        st.execute("Select id from user where username = %s",name)
        self.user_id = st.fetchone()[0]

        sp = db.cursor()
        sp.execute("Select name from course")
        courses = sp.fetchall()

        j=0
        for course in courses:
            self.app.addButton(course[0],self.click,6,(j*4))
            j = j+1


    #Event Occured Button Click
    def click(self,button):
        cur = db.cursor()
        cur.execute("Select id from course c where c.name =  %s", button )
        self.id = cur.fetchone()[0]
        cur.execute("Select * from question q where q.course_id =  %s", self.id)
        rows  = cur.fetchall()
        self.rows = rows
        self.display()
        if(rows):
            return True

    #Matching the answer
    def new(self,app):
        print "Something"
        if self.type == "mcq":
            answer = self.app.getRadioButton("option")
        elif self.type == "True/False":
            answer = self.app.getRadioButton("option1")
        else:
            answer = self.app.getEntry("Answer: ")

        if answer == self.correct:
            self.score+=2


        self.app.removeAllWidgets()
        #print self.rows[self.i][7]
        if self.i < len(self.rows):
            self.display()
        else:
            self.app.addLabel("end","Quiz end" , 0,0)
            self.app.setLabelFont(35, font='Arial')
            self.app.addLabel("score","Your score is: " + str(self.score))
            self.app.addButton("Quit",self.off , 3 , 1)

            data = (self.user_id,self.score,self.id)
            se = db.cursor()
            se.execute("Insert into score(student_id,score,course_id) values(%s,%s,%s)", data)
        return


    #To stop the App
    def off(self,app):
        self.app.stop()


    #To show the Questions
    def display(self):
        self.app.removeAllWidgets()
        print self.rows[self.i][1]
        statement= self.rows[self.i][1]
        option1 = self.rows[self.i][2]
        option2 = self.rows[self.i][3]
        option3 = self.rows[self.i][4]
        option4 = self.rows[self.i][5]
        correct = self.rows[self.i][6]
        type = self.rows[self.i][8]
        self.i +=1
        self.type = type
        self.correct  = correct
        self.app.addLabel("Show", "Question: " + statement, 0, 0, 4)

        if type == "mcq":
            self.app.addRadioButton("option", option1)
            self.app.addRadioButton("option", option2)
            self.app.addRadioButton("option", option3)
            self.app.addRadioButton("option", option4)

        elif type == "True/False":
            self.app.addRadioButton("option1", "True")
            self.app.addRadioButton("option1", "False")

        else:
            self.app.addLabelEntry("Answer: ");

        self.app.addButton("Submit",self.new)

        return;

