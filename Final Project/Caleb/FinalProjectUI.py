"""Caleb Covington"""
from datetime import datetime
from datetime import date
import operator
from ReportsController import ReportsController
#Imports date, time, operator, and the functions from the reprots controller
class UI:  #create a class
#used static method to cut out the process of calling "self" in the parameter
    @staticmethod
    def getResults(userInput):
        output = []
        finalOutput = []
        inputSplitIntoWords = userInput.split(' ')
        fullInventory = ReportsController.createFullInventoryList()
        for this_row in fullInventory:
            for word in inputSplitIntoWords:
                if this_row[1].strip() == word:
                    output.append(this_row)
        for this_row in output:
            for word in inputSplitIntoWords:
                if this_row[2].strip() == word or this_row[2].strip() == "laptop" and word == "computer" or this_row[2].strip() == "tower" and word == "computer":
                    finalOutput.append(this_row)
        if len(finalOutput) >= 1:
            return sorted(UI.removePastOrDamagedItems(finalOutput), key = operator.itemgetter(3), reverse=True)[0]
        else:
            return None
#Gets results based on user input
#Creates two empty list
#Splits the words that will then be looped over
#uses an instance of the report controller
#Gets full Inventory and turn the columns in to a list
#Filters through the inventory and compares the words to eachother
#If the system finds a match it then returns the most expensive item, and if there isn't a match return None.

    @staticmethod
    def getYouMayAlsoConsider(selectedItem):
        fullInventory = ReportsController.createFullInventoryList()
        potentialConsiderItem = None
        for this_row in fullInventory:
            if UI.removePastOrDamagedItems([this_row]) != []:
                if selectedItem[0] != this_row[0]:
                    if selectedItem[2] == this_row[2]:
                        if potentialConsiderItem is None:
                            potentialConsiderItem = this_row
                        elif abs(int(potentialConsiderItem[3]) - int(selectedItem[3])) < abs(int(this_row[3]) - int(selectedItem[3])):
                            potentialConsiderItem = this_row
        return potentialConsiderItem
#Filters through inventory and grabs similar items by a different manufacturer that isn't damaged or past service date. The function returns the item closest in value.
    @staticmethod
    def removePastOrDamagedItems(rawFinalOutput):
        cleanFinalOutput = []
        for this_row in rawFinalOutput:
            if datetime.strptime(this_row[4], '%m/%d/%Y').date() >= date.today() and this_row[5] != "damaged":
                cleanFinalOutput.append(this_row)
        return cleanFinalOutput
#If the the item is valid is appends to final output. Otherwise it is removed from potiental options to consider.
