import math
class Django:

    generalEntropy=0    ## general_entropy
    global columnSize   ## how many columns in file
    filePath = ""       ## file path
    fileRow = 0         ## file row counter
    ColumnEntropys = []
    ColumnInfomationGain = []
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

            for i in range(len(self.ColumnEntropys)):
                natay = self.generalEntropy -  self.ColumnEntropys[i]
                self.ColumnInfomationGain.append(natay)
                
            for i in range(len(self.ColumnInfomationGain)):
                if self.ColumnInfomationGain[i] ==  max(self.ColumnInfomationGain):
                    print i,"  ",max(self.ColumnInfomationGain)
            self.findChild(i)
        except Exception as ex:
            print ex
            raw_input()
    def findChild(self,funcNumber):
        split = []
        if funcNumber == 0:
            split.append(50)
            split.append(60)
            split.append(70)
        if funcNumber == 1:
            split.append(62)
            split.append(63)
            split.append(64)
        if funcNumber == 2:
            split.append(5)
            split.append(10)
            split.append(19)
        childEntropy = []
        dummy = 0
        dummy_2 = 0
        for i in range(len(split)):

            dummy =  self.findEntropyBySplit(funcNumber,split[i],funcNumber,0)
            dummy_2 = self.findEntropyBySplit(funcNumber,split[i],funcNumber,1)
            toplam = dummy+dummy_2
            print split[i],"  -  ", dummy , "  -  " , dummy_2 , "  -  " ,toplam
            childEntropy.append(toplam)

    def findEntropyBySplit(self,ColumnNum,split,funcNumber,control):
         try:
            f = open('C:\\Users\\Taha\\Desktop\\mundi.txt', 'r+')
            f.truncate()
            
            file = open(self.filePath, "r")
            VariableInResult = []
            VariableInResultCounter = []
            VariableInZColumn = []
            VariableInZColumnCounter = []
            Count = 0
            Control = 0
            i,t,m =0,0,0
            count = 0
            while True:
                  line = file.readline()
                  mundi = line
                  if line == '':
                     break
                  line = line.split(',')
                  line = [s.replace('\n', '') for s in line]
                  if control == 1:
                     if float(line[funcNumber]) >= float(split):
                          f.write(mundi)
                          for i  in range(len(VariableInResult)):
                              if VariableInResult[i] == line[len(line)-ColumnNum]:
                                 VariableInResultCounter[i] +=1
                                 Control = 1
                          if Control == 0:
                             VariableInResult.append(line[len(line)-ColumnNum])
                             VariableInResultCounter.append(1)
                  else:
                     if float(line[funcNumber]) < float(split):
                           
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
                a = ( VariableInResultCounter[i] / float(self.fileRow) )
                b = self.CompareZbySplit(self.columnSize-ColumnNum,VariableInResult[i],split,funcNumber,control)
                dummy = a * b
                TotalEntropy = dummy + TotalEntropy
                ##print VariableInResult[i]," ",  VariableInResultCounter[i], " ",dummy
            return TotalEntropy
         except Exception as ex:
            print ex
            raw_input()
    def CompareZbySplit(self,columnNum,columnValue,split,funcNumber,control):
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
                  if control == 1:
                      if float(line[funcNumber]) >= float(split):
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
                  else:
                       if float(line[funcNumber]) < float(split):
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
    
