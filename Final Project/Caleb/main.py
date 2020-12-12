"""Caleb Covington
   1606086     """

import csv   #Call to import CSV files.
import operator #Call to import Operators.
from ReportsController import ReportsController #Calls for Class to import def in Repoerts Controller
from UI import UI #Calls for Class to import def in UI

while(True): #While infinite loop that breaks when the user inputs "q"
    userInput = input("\nSearch for an item by Manufacturer and Type: ") #Prompts user to input
    if userInput.lower() == 'q': #If the user types "q" the loop terminates and the program ends. The input is also case insensitive
        break
    output = UI.getResults(userInput) #A function that grabs the results from the inventory dependent on the user input
    if output is not None: #A checker if the item is not found
        optionToConsider = UI.getYouMayAlsoConsider(output) #If an item is found in the inventory it provides a similar item
        print("Your item is: " + output[0] + ", " + output[1] + ", " + output[2] + ", " + output[3] + "\n") #Output of found item in inventory
        if optionToConsider != None:
            print("You may also consider: " + optionToConsider[0] + ", " + optionToConsider[1] + ", " + optionToConsider[2] + ", " + optionToConsider[3] + "\n")
        else:
            print("No other options similar to consider.\n")
    else:
        print("No such item in inventory\n") #If the item is none the program outputs this for the user
        print("No other options similar to consider.\n")
    print("type q and press enter to quit") #At the end of the loop it always prompts the user how to quit the program.

ReportsController.createFullInventoryCSV()
ReportsController.writeAllTypeInventoryListstoCSV()
ReportsController.createPastServicesCSV()
ReportsController.createDamagedInventoryCSV()
#Line 23-26 calls for other functions within it to generate the appropriate CSV file