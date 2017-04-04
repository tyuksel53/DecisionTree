import math
class Django:

    generalEntropy=0    ## general_entropy
    global columnSize   ## how many columns in file
    filePath = ""       ## file path
    fileRow = 0         ## file row counter
    ColumnEntropys = []
    def __init__(self,path): ## class constructor
        try:
            self.filePath = path ## adding file path
            self.GetFuncsize()   ## adding columnsize
            self.generalEntropy = self.findGeneralEntropy() ## finding general entropy
        except Exception as ex:
            print ex
            raw_input()

    def GetFuncsize(self):
        try:
            file = open(self.filePath, "r")
            line = file.readline()
            line = line.split(',')
            self.columnSize = len(line) ## Initialize data columnsize
        except Exception as ex:
            print ex
            raw_input()

    def EntropyFormula(self,total,current): ## EntropyFormula definition
        dummy = current/ float(total)
        dummy = dummy * math.log(dummy, 2)
        return dummy * -1
    
    def CompareZ(self,columnNum,columnValue):
        try:
            file = open(self.filePath, "r")
            VariableInResult = [] ## add variables to list
            VariableInResultCounter = [] ## this for count variables
            Count = 0
            Control = 0
            i=0
            RowCount = 0
            while True:
                  line = file.readline()
                  if line == '': ## if it's at the end of file
                     break
                  line = line.split(',')
                  if line[columnNum] == columnValue: ## find specific Area
                      for i  in range(len(VariableInResult)): ## check variable is already added
                          if VariableInResult[i] == line[len(line)-1]: ## if variable is already in the list
                             VariableInResultCounter[i] +=1 ## count up 
                             Control = 1 ## variable is finded
                      if Control == 0: ## if variable is not finded then add variable
                         VariableInResult.append(line[len(line)-1])
                         VariableInResultCounter.append(1)
                      Control = 0
                      RowCount += 1
            total=0
            for i  in range(len(VariableInResult)):
                      total += self.EntropyFormula(RowCount,VariableInResultCounter[i])
            return total
        except Exception as ex:
            print ex
            raw_input()
    def findAllEntropy(self): ## finding all column's entropyes
        try:
            for i in range(self.columnSize-1):
                self.findEntropy(self.columnSize - i)
                print "_______________________________________________________________"

            print "_______________________________________________________________"
            print self.generalEntropy
            print "_______________________________________________________________"
            for i in range(len(self.ColumnEntropys)):
                natay = self.generalEntropy -  self.ColumnEntropys[i]
                print "_______________________________________________________________"
                print  natay
        except Exception as ex:
            print ex
            raw_input()
    def findEntropy(self,ColumnNum): ## finding entropy column by column
        try:
            file = open(self.filePath, "r")
            VariableInResult = []
            VariableInResultCounter = []
            VariableInZColumn = []
            VariableInZColumnCounter = []
            Count = 0
            Control = 0
            i,t,m =0,0,0
            while True:
                  line = file.readline()
                  if line == '':
                     break
                  line = line.split(',')
                  line = [s.replace('\n', '') for s in line]
                  for i  in range(len(VariableInResult)):
                      if VariableInResult[i] == line[len(line)-ColumnNum]:
                         VariableInResultCounter[i] +=1
                         Control = 1
                  if Control == 0:
                     VariableInResult.append(line[len(line)-ColumnNum])
                     VariableInResultCounter.append(1)
                  Control = 0
            TotalEntropy = 0
            for i  in range(len(VariableInResult)):
                a = ( VariableInResultCounter[i] / float(self.fileRow) );
                b = self.CompareZ(self.columnSize-ColumnNum,VariableInResult[i])
                dummy = a *b
                TotalEntropy = dummy + TotalEntropy
                print VariableInResult[i]," ",  VariableInResultCounter[i], " ",dummy
            self.ColumnEntropys.append(TotalEntropy)
        except Exception as ex:
            print ex
            raw_input()
    def findGeneralEntropy(self): ## finding general entropy
        try:
            file = open(self.filePath, "r")
            VariableInResult = [] ## add variables to list
            VariableInResultCounter = [] ## this for count variables
            Count = 0
            Control = 0
            i=0
            while True:
                  line = file.readline()
                  if line == '': ## if it's at the end of file
                     break
                  line = line.split(',')
                  for i  in range(len(VariableInResult)): ## check variable is already added
                      if VariableInResult[i] == line[len(line)-1]: ## if variable is already in the list
                         VariableInResultCounter[i] +=1 ## count up 
                         Control = 1 ## variable is finded
                  if Control == 0: ## if variable is not finded then add variable
                     VariableInResult.append(line[len(line)-1])
                     VariableInResultCounter.append(1)
                  Control = 0
                  self.fileRow += 1 ## file row counter
            total=0
            for i  in range(len(VariableInResult)):
                      total += self.EntropyFormula(self.fileRow,VariableInResultCounter[i])
            return total
        except Exception as ex:
            print ex
            raw_input()
    
