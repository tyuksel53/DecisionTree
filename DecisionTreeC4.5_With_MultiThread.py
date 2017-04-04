import clr
clr.AddReference('System.Drawing')
clr.AddReference('System.Windows.Forms')

from Django import Django
from System.Drawing import *
from System.Windows.Forms import Application, Button, Form, Label,OpenFileDialog,TextBox

class MyForm(Form):
    def __init__(self):
        # Create child controls and initialize form
        self.Text = 'Decision Tree'
        self.Name = 'Form'
        self.Width = 512
        self.Height = 512
        self.CenterToScreen()

        self.TextBox = TextBox()
        self.TextBox.Text = ""
        self.TextBox.Location = Point(50, 50)
        self.TextBox.Width = 250
        
        button = Button()
        button.Text = "Choose File"
        button.Location = Point(49, 75)
        button.Click += self.buttonPressed

        self.Controls.Add(button)
        self.Controls.Add(self.TextBox)

        self.count = 0
        self.FilePath = ""

    def buttonPressed(self, sender, args):
        #try:  
        #except Exception as ex:
            #print ex
            #raw_input()
        DjangoUnchained = Django()
        dialog = OpenFileDialog()
        dialog.Filter = "All Files|*.*"
        if dialog.ShowDialog() == True:
           pass
        self.FilePath = dialog.FileName
        self.TextBox.Text = dialog.FileName
        DjangoUnchained.findEntropy(self.FilePath)
        
        

    


Application.EnableVisualStyles()
Application.SetCompatibleTextRenderingDefault(False)

form = MyForm()
Application.Run(form)
