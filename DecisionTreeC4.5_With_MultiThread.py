import clr
clr.AddReference('System.Drawing')
clr.AddReference('System.Windows.Forms')

from Django import Django
import ctypes 
import os
from System.Drawing import *
from System.Windows.Forms import Application, Button, Form, Label,OpenFileDialog,TextBox

class MyForm(Form):
    def __init__(self):
        # Create child controls and initialize form
        try:
            self.Text = 'Decision Tree'
            self.Name = 'Form'
            self.Width = 430
            self.Height = 200
            self.CenterToScreen()

            self.TextBox = TextBox()
            self.TextBox.Text = ""
            self.TextBox.Location = Point(20, 50)
            self.TextBox.Width = 250
        
            self.LabelAuthors = Label()
            self.LabelAuthors.Text = "Taha Yuksel - Ramazan Demir"
            self.LabelAuthors.Location = Point(300, 50)
            self.LabelAuthors.Height = 100
            self.LabelAuthors.Width = 100

            buttonFile = Button()
            buttonFile.Text = "Choose File"
            buttonFile.Location = Point(19, 75)
            buttonFile.Click += self.buttonPressed

            buttonProcess = Button()
            buttonProcess.Text = "Start Process"
            buttonProcess.Location = Point(195, 75)
            buttonProcess.Click += self.buttonProcessStart

            self.Controls.Add(buttonFile)
            self.Controls.Add(self.TextBox)
            self.Controls.Add(buttonProcess)
            self.Controls.Add(self.LabelAuthors)

            self.FilePath = ""
        except Exception as ex:
            print ex
            raw_input()
    def buttonProcessStart(self,sender,args):
        #clear = lambda: os.system('cls')
        #clear()
        if len(self.FilePath)<5:
            ctypes.windll.user32.MessageBoxW(0, "WOWOOWOWOW you must chose the file", "THE FILE", 1)
        else:
            DjangoUnchained = Django(self.FilePath)
            DjangoUnchained.findAllEntropy()

    def buttonPressed(self, sender, args):
        #try:  
        #except Exception as ex:
            #print ex
            #raw_input()
        dialog = OpenFileDialog()
        dialog.Filter = "All Files|*.*"
        if dialog.ShowDialog() == True:
           pass
        self.FilePath = dialog.FileName
        self.TextBox.Text = dialog.FileName
        
        

    


Application.EnableVisualStyles()
Application.SetCompatibleTextRenderingDefault(False)

form = MyForm()
Application.Run(form)
