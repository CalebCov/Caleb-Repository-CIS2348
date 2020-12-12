"""Caleb Covington
   1606086     """
import csv
import operator
#import csv and operator
class ItemTypeListController:

    def __init__(self, file_path):   #Initialize attributes of classes
        self.file_path = file_path

    def getSeparatedTypeData(self, inputList): #Creates  a dict usig a key as the type and the array as the value all in respect of its category
        typesDictionary = {}
        for this_type in inputList: #The full inventory will be stored in inputList
            if this_type[2] not in typesDictionary: #If the item is nonexistent in the dict
                typesDictionary[this_type[2]] = [this_type] #Generates and initializes the new item
            else:
                typesDictionary[this_type[2]].append(this_type) #If the item is present then append it to the already existing category in the dict
        return typesDictionary #return the dicts.

    def gettypesOfAllProducts(self):   #function that reads,sorts,and returns the data of the csv file
        reader = csv.reader(open(self.file_path), delimiter=",") #delimiter serves as the seperator in the csv file
        sorted_manufacturer_names = sorted(reader, key=operator.itemgetter(2))
        return self.getSeparatedTypeData(sorted_manufacturer_names)