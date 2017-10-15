
            #Importing Files and Libraries

from appJar import gui
from data import *
import os
from subprocess import call
import Tkinter as tk
import tkFont
from Tkinter import *


class teacher:

    #CONSTRUCTOR
    def __init__(self, app,name):
        self.app = app
        #self.app.setLabelFont(18, font='Times New Roman')
        self.app.addLabel("Tl1", "Hello!")
        self.app.addLabel("Tl2", name)
        self.app.addLabelEntry("Subject: ")
        self.app.addLabel("Use Full Word for courses no shortcuts")


        #Buttons to perform Functions
        self.app.addButton("Set quiz", self.sett)
        self.app.addButton("Previous Score",self.score)

    #Function to Set the Quiz
    def sett(self,app):
        print "Hello"
        sub = self.app.getEntry("Subject: ")
        self.app.removeAllWidgets()
        obj= db.cursor()

        #Fetching Course ID
        obj.execute("SELECT c.id FROM course c WHERE c.name = %s" , sub)
        course_id = obj.fetchone()[0]
        course_id = int(course_id)
        self.course_id = course_id
        print self.course_id
        self.app.addLabelEntry("Question:", 0, 0, 8)
        self.app.addLabelEntry("Answer", 4, 2)
        a = self.mcq();
        self.app.addButtons(["True/False", "Numeric"], self.click,6,0)
        self.app.addButton("Add",self.adder,6,2)

    #Function to make MCQS
    def mcq(self):
        self.type = "mcq"
        self.app.addLabelEntry(" A", 1, 0, 0)
        self.app.addLabelEntry(" B", 1, 1, 2)
        self.app.addLabelEntry(" C", 2, 0, 0)
        self.app.addLabelEntry(" D", 2, 1, 2)
        return True


    #Function To show score
    def score(self):
        print "ARE"


    #Function to add and Save Question to Database
    def adder(self,app):
        print self.course_id
        ques = self.app.getEntry("Question:")
        if self.type == "mcq":
            optionA = self.app.getEntry(" A")
            optionB = self.app.getEntry(" B")
            optionC = self.app.getEntry(" C")
            optionD = self.app.getEntry(" D")
        answer = self.app.getEntry("Answer")
        self.app.clearAllEntries()

        #Inserting Data
        if self.type == "mcq":
            data_inter = (ques,optionA,optionB,optionC,optionD,answer,int(self.course_id),self.type)
            cur.execute('INSERT INTO question(statement,A,B,C,D,correct,course_id,type) VALUES(%s, %s, %s, %s, %s, %s, %s,%s)',data_inter)

        else:
            data_inter = (ques,answer, int(self.course_id), self.type)
            cur.execute('INSERT INTO question(statement,correct,course_id,type) VALUES(%s, %s, %s, %s)',data_inter)


    #event Click
    def click(self,button):
        self.app.removeAllWidgets()
        self.app.addLabelEntry("Question:", 0, 0, 8)
        self.app.addLabelEntry("Answer", 4,1)

        if button == "Numeric":
            self.type = "Numeric"
            self.app.addButtons(["True/False", "MCQ"], self.click, 6, 0)
            #a = self.app.addLabelEntry("Question:", 0, 0, 8)
            #self.app.addLabelEntry("Answer" ,4,2)
            #a.place.forget()

        elif button == "True/False":
            self.type = "True/False"
            self.app.addButtons(["Numeric", "MCQ"], self.click, 6, 0)

        else:
            self.mcq();
            self.app.addButtons(["Numeric", "True/False"], self.click, 6, 0)

        self.app.addButton("Add", self.adder, 6, 1)
        return
















