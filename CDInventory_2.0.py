#------------------------------------------#
# Title: CDInventory_2.0.py
# Desc: Script for Assignment 05
# Change Log: (Who, When, What)
# DBiesinger, 2030-Jan-01, Created File
# WDang, 2020-Feb-20, Modified File
#------------------------------------------#

# use os.path to check if file exist
import os.path

# Declare glable variabls

savedChoice = [] # list of choice user has input
strChoice = '' # User input
lstTbl = []  # list of Dicts to hold data
lstRow = {}  # list of data row
strFileName = 'CDInventory.txt'  # data storage file
objFile = None  # file object

# Get user Input
print('The Magic CD Inventory\n')
while True:
    # 1. Display menu allowing the user to choose:
    print('[l] Load Inventory from file\n[a] Add CD\n[i] Display Current Inventory')
    print('[d] Delete CD from Inventory\n[s] Save Inventory to file\n[x] exit')
    strChoice = input('l, a, i, d, s or x: ').lower()  # convert choice to lower case at time of input
    print()

    if strChoice == 'x':
        # 5. Exit the program if the user chooses so
        break

    if strChoice == 'l':
        # Load existing inventory data saved
        if os.path.exists('CDInventory.txt'): #if file doesn't exist, pass and continue
            objFile = open('CDInventory.txt', 'r')
            lstTbl = [] #clear out temporary data saved in memory, otherwise will append saved data to what is in the memory.
            for row in objFile: #load the saved CDs and cycle through by each row of the data
                savedID = row.strip().split(',') #cycle through each comma separated item of each row
                lstRow = {'ID':savedID[0], 'Title':savedID[1], 'Artist':savedID[2]} #create the 2D-dictionary, values of the matching keys are from the saved data
                lstTbl.append(lstRow) # create the list of dictionaries
            print(lstTbl)
            objFile.close()
            print()
            savedChoice.append(strChoice) # record the user has selcted loading from the saved file
        pass

    elif strChoice == 'a':
        # 2. Add data to the table (2d-list) each time the user wants to add data
        strID = input('Enter an ID: ')
        strTitle = input('Enter the CD\'s Title: ')
        strArtist = input('Enter the Artist\'s Name: ')
        intID = int(strID)
        lstRow = {'ID':intID, 'Title':strTitle, 'Artist':strArtist} # changed from list to dictionary
        lstTbl.append(lstRow)
        print()

    elif strChoice == 'i':
        # 3. Display the current data to the user each time the user wants to display the data
        print('ID, CD Title, Artist')
        for row in lstTbl:
            print(*row.values(), sep = ',') # use values() attribute to display only the values of the CD libraries
        print()

    elif strChoice == 'd':
        # Delete an entire entry of a CD, i.e., ID, Title, and Artist based on CD ID entered
        delID = input('Which CD ID do you want to delete?: ')
        delIdx = -1 # create an index variable to identify the matching index number of the CD to be deleted, it starts from -1, as when the counter starts in the for loop, its value becomes 0, which is the index number of the first CD in the list of CD library.The counter will continue until the match is identified.
        for row in lstTbl:
            delIdx +=1
            if delID in row.values():
                del lstTbl[delIdx]
                print('CD', delID, 'is deleted \n')
            elif delIdx == len(lstTbl)-1: # if no match is found after cycling through the entire inventory list, it is either no matching CD is found or the list is empty.
                print('CD', delID, 'deosn\'t exist' 'OR The inventory is empty \n')

    elif strChoice == 's':
        # 4. Save the data to a text file CDInventory.txt if the user chooses so
        if len(savedChoice) > 0: # if user has selected loading from the saved data, when save new data, in order not to create duplicate records, using w mode of open to overwrite the existing file content
            objFile = open('CDInventory.txt', 'w')
            for row in lstTbl:
                strRow = ''
                for value in row.values():
                    strRow += str(value) + ','
                strRow = strRow[:-1] + '\n'
                objFile.write(strRow)
            objFile.close()
        else: # if user has not yet selected loading from the saved data, only new entries will be added and no duplicate records will be create.
            objFile = open('CDInventory.txt', 'a')
            for row in lstTbl:
                strRow = ''
                for value in row.values():
                    strRow += str(value) + ','
                strRow = strRow[:-1] + '\n'
                objFile.write(strRow)
            objFile.close()

    else:
        print('Please choose either l, a, i, d, s or x!')
