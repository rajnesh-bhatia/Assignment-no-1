import login
import Teacher
import Student
import unittest
import appJar
from appJar import gui
from Tkinter import *
import atexit
import  os
from subprocess import call
import Tkinter as tk
import tkFont


class mytests(unittest.TestCase):

    def test_checkCourses(self):
       self.assertEqual(obj.click(app),True)

    def test_Window_Deletion(self):
        self.assertEqual(obj.end(app), True)

if __name__ == '__main__':
    app = gui("600x500")
    name = "Shumail"
    obj = login.login_page(app)
    unittest.main(verbosity=10)