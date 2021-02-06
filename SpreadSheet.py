#Adil Asad
#21-11149


from functools import reduce
import sys
import pickle

class Cursor:
    CursorLocRow = 0
    CursorLocCol = 0

    def __init__(self):
        Cursor.CursorLocRow = 0
        Cursor.CursorLocCol = 0

    def goto(self,row,column):
        Cursor.CursorLocRow = row
        Cursor.CursorLocCol = column
        print('Cursor moved to:',Cursor.CursorLocRow,',',Cursor.CursorLocCol)




class Spreadsheet(Cursor):
    
    def __init__(self,rows,columns):
        self.rows = rows
        self.columns = columns
        self.table = []
        self.CurSelectionRow1 = 0
        self.CurSelectionCol1 = 0
        self.CurSelectionRow2 = 0
        self.CurSelectionCol2 = 0
        self.selection = []

        for i in range(self.rows):
            rows = [None]*self.columns
            self.table.append(rows)
        print(self.table)

    def Insert(self,value):
        self.table[Cursor.CursorLocRow][Cursor.CursorLocCol] = value
        print(self.table)

    def Delete(self):
        self.table[Cursor.CursorLocRow][Cursor.CursorLocCol] = None
        print(self.table)

    def ReadVal(self):
        print(self.table[Cursor.CursorLocRow][Cursor.CursorLocCol])

    def PrintSheet(self):
        print(self.table)

    def Select(self,row,column):
        self.CurSelectionRow1 = Cursor.CursorLocRow
        self.CurSelectionCol1 = Cursor.CursorLocCol
        self.CurSelectionRow2 = row
        self.CurSelectionCol2 = column

        for i in range(self.CurSelectionRow1,self.CurSelectionRow2+1):
            for j in range(self.CurSelectionCol1,self.CurSelectionCol2+1):
                if self.table[i][j] == None:
                    pass
                else:
                    self.selection.append(self.table[i][j])
        print(self.selection)

    def GetSelection(self):
        print('Current Selection:',self.CurSelectionRow1,self.CurSelectionCol1,self.CurSelectionRow2,self.CurSelectionCol2)

    def ClearSelection(self):
        self.selection = []

    def Sum(self,row,column):
        total = 0
        for i in self.selection:
            total += i

        Cursor.CursorLocRow = row
        Cursor.CursorLocCol = column

        self.Insert(total)
        

        print('Sum: ',total)


    def Multiply(self,row,column):
        Answer = reduce(lambda x, y: x*y, self.selection)

        Cursor.CursorLocRow = row
        Cursor.CursorLocCol = column

        self.Insert(Answer)
        
    def Average(self,row,column):
        Answer = sum(self.selection)/len(self.selection)

        Cursor.CursorLocRow = row
        Cursor.CursorLocCol = column

        self.Insert(Answer)

    def Max(self,row,column):
        Answer = max(self.selection)

        Cursor.CursorLocRow = row
        Cursor.CursorLocCol = column

        self.Insert(Answer)
        



def Save(obj,filename):
    with open(filename,'wb') as output:
        pickle.dump(obj,output)


def Load(filename):
    with open(filename,'rb') as input:
        t = pickle.load(input)
        t.PrintSheet()
        

def main():
    C = Cursor()
    a = 0
    s = 0
    while True:
        str1 = input('>> ')
        str1 = str1.lower()
        str1 = str1.split()

        if str1[0] == 'createsheet':
            str2 = str1[1]
            str3 = str1[2]
            
            try:
                if int(str2) > 0 and int(str3) > 0:
                    Sheet = Spreadsheet(int(str2),int(str3))
                    a = 1
                    
                else:
                    print('Please enter a positive number')
            except ValueError:
                    print('Input is not a number. Please enter a number.')

        if str1[0] == 'goto':
            str4 = str1[1]
            str5 = str1[2]
            try:
                if int(str4) >= 0 and int(str5) >= 0:
                    if str4 <= str2 and str5 <= str3:
                        C.goto(int(str4),int(str5))
                    else:
                        print('Value(s) entered out of range of spreadsheet')
                else:
                    print('Please enter a positive number')
            except ValueError:
                    print('Input is not a number. Please enter a number.')

        if str1[0] == 'insert':
            if a == 1:
                value = str1[1]
                Sheet.Insert(float(value))

            else:
                print('Please create a sheet')

        if str1[0] == 'delete':
            if a == 1:
                Sheet.Delete()
            else:
                print('Please create a sheet')


        if str1[0] == 'readval':
            if a == 1:
                Sheet.ReadVal()

            else:
                print('Please create a sheet')


        if str1[0] == 'print':
            if a == 1:
                Sheet.PrintSheet()

            else:
                print('Please create a sheet')
           
        if str1[0] == 'select':
            if a == 1:
                row2 = str1[1]
                col2 = str1[2]

                try:
                    if int(row2) >= 0 and int(col2) >= 0:
                        Sheet.Select(int(row2),int(col2))
                        s = 1
                    else:
                        print('Please enter a positive number')
                except ValueError:
                    print('Input is not a number. Please enter a number.')

            else:
                print('Please create a sheet')


        if str1[0] == 'getselection':
            if a == 1:
                if s == 1:
                    Sheet.GetSelection()
                else:
                    print('No selection made')
            else:
                print('Please create a sheet')

        if str1[0] == 'clearselection':
            if a == 1:
                Sheet.ClearSlection()

            else:
                print('Please create sheet')

        if str1[0] == 'sum':
            if a == 1:
                if s == 1:
                    sumrow = str1[1]
                    sumcol = str1[2]
                    try:
                        if int(sumrow) >= 0 and int(sumcol) >= 0:
                            Sheet.Sum(int(sumrow),int(sumcol))
                        else:
                            print('Please enter a positive number')
                    except ValueError:
                        print('Input is not a number. Please enter a number.')

                else:
                    print('Please select data before using this function')

            else:
                print('Please create a sheet')
 
        if str1[0] == 'mul':
            if a == 1:
                if s == 1:
                    mulrow = str1[1] 
                    mulcol = str1[2]
                    try:
                        if int(mulrow) >= 0 and int(mulcol) >= 0:
                            Sheet.Multiply(int(mulrow), int(mulcol))
                        else:
                            print('Please enter a positive number')
                    except ValueError:
                        print('Input is not a number. Please enter a number.')

                else:
                    print('Please select data before using this function')

            else:
                print('Please create a sheet')
                

        if str1[0] == 'avg':
            if a == 1:
                if s == 1:
                    avgrow = str1[1]
                    avgcol = str1[2]
                    try:
                        if int(avgrow) >= 0 and int(avgcol) >= 0:
                            Sheet.Average(int(avgrow), int(avgcol))
                        else:
                            print('Please enter a positive number')
                    except ValueError:
                        print('Input is not a number. Please enter a number.')

                else:
                    print('Please select data before using this function')

            else:
                print('Please create a sheet')


        if str1[0] == 'max':
            if a == 1:
                if s == 1:
                    maxrow = str1[1]
                    maxcol = str1[2]
                    try:
                        if int(maxrow) >= 0 and int(maxcol) >= 0:
                            Sheet.Max(int(maxrow), int(maxcol))
                        else:
                            print('Please enter a positive number')
                    except ValueError:
                        print('Input is not a number. Please enter a number.')

                else:
                    print('Please select data before using this function')

            else:
                print('Please create a sheet')


        if str1[0] == 'save':
            if a == 1:
                file = input('Enter filename: ')
                Save(Sheet,file)
                print('File Saved')

            else:
                print('Please create a sheet before using this function')



        if str1[0] == 'load':
            loadfile = input('Enter filename: ')
            Load(loadfile)


        if str1[0] == 'quit':
            sys.exit(0)

    

main()
