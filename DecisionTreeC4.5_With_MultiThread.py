import clr
clr.AddReference('System.Drawing')
clr.AddReference('System.Windows.Forms')

from System.Drawing import *
from System.Windows.Forms import Application, Button, Form, Label
from Microsoft.Win32 import OpenFileDialog

class MyForm(Form):
    def __init__(self):
        # Create child controls and initialize form
        self.Text = 'Decision Tree'
        self.Name = 'Form'
        self.Width = 512
        self.Height = 512
        self.CenterToScreen()


        self.label = Label()
        self.label.Text = "Please Click Me"
        self.label.Location = Point(50, 50)
        self.label.Height = 30
        self.label.Width = 200

        self.count = 0

        button = Button()
        button.Text = "Click Me"
        button.Location = Point(50, 100)

        button.Click += self.buttonPressed

        self.Controls.Add(self.label)
        self.Controls.Add(button)

    def buttonPressed(self, sender, args):
        self.count += 1
        #self.label.Text = "You have clicked me %s times." % self.count
        #dialog = OpenFileDialog()
        #dialog.Filter = "All Files|*.*"
        #if dialog.showFile() == True:
         #*selectedFile = dialog.FileName;
        #file = open('C:\\Users\\Taha\\Desktop\Result.txt', 'r')
        #print file.read()
        #print selectedFile


Application.EnableVisualStyles()
Application.SetCompatibleTextRenderingDefault(False)

form = MyForm()
Application.Run(form)
