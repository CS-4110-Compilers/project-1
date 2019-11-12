class TrieTable:
    
    maxTransitions = 25
    #stores index if switch uppercase: 0-25, lowercase: 26-51
    switch = [-1]*52
    #stores symbols in id's
    symbol = ['*']*maxTransitions
    #stores index of next id
    nextArr = [-1]*maxTransitions
    #tracks end of symbol array
    symbolPtr = 0
    
    #Function to print the formatted TrieTable.
    #-1 in switch and next represents undefined element.
    #* in symbol represents undefined element.
    def printTrie(self):
        
        capLetters = "  A  B  C  D  E  F  G  H  I  J  K  L  M  N  O  P  Q  R  S  T  U  V  W  X  Y  Z"  
        lowLetters = " a  b  c  d  e  f  g  h  i  j  k  l  m  n  o  p  q  r  s  t  u  v  w  x  y  z"
        letterIndex = ""
        index = ""
        sw = ""
        sym = ""
        nxt = ""
        
        #format strings of table rows
        for i in range(len(self.switch)): 
            sw += "{:3d}".format(self.switch[i])     
        for i in range(len(self.symbol)): 
            index += "{:3d}".format(i)
            sym += "{:3c}".format(ord(self.symbol[i]))
            nxt += "{:3d}".format(self.nextArr[i])
            
        #print formatted strings
        print("") 
        print("        ",capLetters,lowLetters)
        print("switch: ",sw)
        print() 
        print("        ",index)
        print("symbol: ",sym)
        print("next:   ",index)
        print(nxt)
            
    #Function to grow table.
    def growTable(self):
        temp1 = ['*']*self.maxTransitions
        temp2 = [-1]*self.maxTransitions
        self.symbol = self.symbol + temp1
        self.nextArr = self.nextArr + temp2
        self.maxTransitions = self.maxTransitions * 2

    #Funtion that returns the index of the corresponding letter in the switch array.
    #If not in the switch, then it returns -1.
    def switchIndexOfSymbol(self,c):
        asciiValue = ord(c)
        if(asciiValue > 64 and asciiValue < 91):
            return asciiValue-65
        elif(asciiValue > 96 and asciiValue < 123):
            return asciiValue-71
        else:
            return -1
    
    #Helper function for searchAndCreateIDs.
    #Functions to create identifiers.
    def createID(self,identifier,ptr):
        
        #if no id contains this first letter
        if(ptr == -1):
            
            #store index of first undefined symbol in symbol array in switch
            ptr = self.symbolPtr
            self.switch[self.switchIndexOfSymbol(identifier[0])] = ptr
            
            #fill in symbol array
            x = 1
            i = self.symbolPtr
            while((ptr-i) != len(identifier)-1):
                self.symbol[ptr] = identifier[x]
                x += 1
                ptr += 1
                self.symbolPtr += 1
                
                #if its the end of the table, double the size
                if(self.symbolPtr == self.maxTransitions): self.growTable()
            
            #add terminal symbol
            self.symbol[ptr] = '@'
            self.symbolPtr += 1
            
            #if its the end of the table, double the size
            if(self.symbolPtr == self.maxTransitions): self.growTable()
            
        else:
             
            #store index of first undefined symbol in symbol array in nextArr
            self.nextArr[ptr] = self.symbolPtr
            
            #fill in symbol array
            ptr = self.symbolPtr
            i = self.symbolPtr
            x = 0
            
            #while not at the last symbol
            while((ptr-i) != len(identifier)):
                self.symbol[ptr] = identifier[x]
                x += 1
                ptr += 1
                self.symbolPtr += 1
                
                #if its the end of the table, double the size
                if(self.symbolPtr == self.maxTransitions): self.growTable()
            
            #add terminal symbol
            self.symbol[ptr] = '@'
            self.symbolPtr += 1
            #if its the end of the table, double the size
            if(self.symbolPtr == self.maxTransitions): self.growTable()
            
        return
    
    #Function to search if an identifier exists.
    #If not, then create it and returns true.
    #If it exists or if it contains invalid chars, it returns false.
    #Takes a string as a parameter.
    def searchAndCreateIDs(self,identifier):
        
        #if empty return false
        if(not identifier): return False
        
        #switch index of first symbol
        index = 0
        valueOfSymbol = self.switchIndexOfSymbol(identifier[index])
        
        #if identifier does not start with a letter
        if(valueOfSymbol == -1): return False
        
        #if no identifier does starts with this letter, create new identifier
        ptr = self.switch[valueOfSymbol]
        if(ptr == -1): self.createID(identifier,ptr)
        
        #else there exists an identifier that starts with id[0]
        else:
            
            exitLoop = False
            
            #get ascii value of next char in id if its lenght > 1
            if(len(identifier) > 1):
                index += 1
                valueOfSymbol = ord(identifier[index])
            #if unique    
            elif(self.nextArr[self.switch[self.switchIndexOfSymbol(identifier)]] == -1):
                self.nextArr[self.switch[self.switchIndexOfSymbol(identifier)]] = self.symbolPtr
                self.symbol[self.symbolPtr] = '@'
                self.symbolPtr += 1
                
                #if its the end of the table, double the size
                if(self.symbolPtr == self.maxTransitions): self.growTable()
                return True
            else: return False
                 
            
            #compare the chars in id with chars in symbol array
            while(not exitLoop):
                
                #if its not a valid symbol retrun false
                val = ord(identifier[index])
                if(val != 95 and 
                   (val < 65  or val > 90) and 
                   (val < 97  or val > 122) and 
                   (val < 48  or val > 57)): return False
            
                #if symbol array contains current char
                if(ord(self.symbol[ptr]) == valueOfSymbol) :
                    #if current char is not the last char in id, check next char in id
                    if(index != len(identifier)-1):
                        ptr += 1
                        index += 1
                        valueOfSymbol = ord(identifier[index])
                        
                    #else the identifier has no more chars
                    else: 
                        exitLoop = True 
                        nextIndexValue = ptr+1
                        while(self.nextArr[nextIndexValue] != -1): 
                            nextIndexValue = self.nextArr[nextIndexValue]
                        
                        #if identifier is unique add it to table
                        if(self.symbol[nextIndexValue] != '@'):
                            self.nextArr[nextIndexValue] = self.symbolPtr
                            self.symbol[self.symbolPtr] = '@'
                            self.symbolPtr += 1
                            
                            #if its the end of the table, double the size
                            if(self.symbolPtr == self.maxTransitions): self.growTable()
            
                        else: return False
                        
                    
                #else if nextArr[ptr] is defined then check symbol[nextArr[ptr]]
                elif(self.nextArr[ptr] != -1):
                    ptr = self.nextArr[ptr]
                    
                #else create new identifier
                else:
                    self.createID(identifier[index:],ptr)
                    exitLoop = True
                            
        return True

def sampleInputProgram():
    
    listOfReserved = [ "boolean", "break", "class", "double", "else", "extends", "false", "for", "if",
                            "implements", "int", "interface", "new", "newarray", "null", "println", "readln",
                            "return" ,"string", "this", "true", "void", "while"]
    listOfIds = ["Funny","funny","flag","s","a"]
        
    t = TrieTable()
        
    for word in listOfReserved:
        t.searchAndCreateIDs(word)
    for id in listOfIds:
        t.searchAndCreateIDs(id)
            
    t.printTrie()
    print(len(t.symbol))
    
sampleInputProgram()
        