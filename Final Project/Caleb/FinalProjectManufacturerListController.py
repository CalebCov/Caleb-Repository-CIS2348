"""Caleb Covington"""
import csv
import operator
#import csv and operator
class ManufacturerListController: #create a class

    def __init__(self, file_path): #Initialize attributes of classes
        self.file_path = file_path

    def gettypesOfAllProducts(self): #function that reads,sorts,and returns the data of the csv file
        reader = csv.reader(open(self.file_path), delimiter=",")   #delimiter serves as the seperator in the csv file
        sorted_manufacturer_names = sorted(reader, key=operator.itemgetter(1))
        manufacturer_names = [] #create list
        for each_name in sorted_manufacturer_names: #loops through and appends each name
            manufacturer_names.append(each_name)
        return manufacturer_names

    def getSortedManufacturersOfAllProducts(self): #Gathers a list of all items from manufacturerList csv
        reader = csv.reader(open(self.file_path), delimiter=",") #reads and sorts the list in manufactuerList based on manufacturer name
        sorted_manufacturer_names = sorted(reader, key=operator.itemgetter(1))
        manufacturer_names = []
        for each_name in sorted_manufacturer_names: #loops through sorted list and appends the names before returning.
            manufacturer_names.append(each_name)
        return manufacturer_names
