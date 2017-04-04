class Django:
    def findEntropy(self,path):
        try:
            file = open(path, "r")
            VariableInResult = []
            VariableInResultCounter = []
            Count = 0
            Control = 0
            i =0
            while True:
                  line = file.readline()
                  if line == '':
                     break
                  line = line.split(',')
                  for i  in range(len(VariableInResult)):
                      if VariableInResult[i] == line[len(line)-4]:
                         VariableInResultCounter[i] +=1
                         Control = 1
                  if Control == 0:
                     VariableInResult.append(line[len(line)-4])
                     VariableInResultCounter.append(1)
                  Control = 0
            for i  in range(len(VariableInResult)):
                      print VariableInResult[i]," ",  VariableInResultCounter[i]
        except Exception as ex:
            print ex
            raw_input()
        

