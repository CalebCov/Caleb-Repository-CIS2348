"""Caleb Covington"""
import csv
import operator
from ManufacturerListController import *
from PriceListController import *
from ServiceDatesController import *
from ItemTypeListController import *
from datetime import datetime
from datetime import date
#imports csv, operator, date and time as well as all the Controller functions
class ReportsController: #create class
#This py file uses staticmethod to basically organize and avoid the extra step of calling "self" everytime I created a def.
    @staticmethod
    def createFullInventoryList():
        serviceDatesController = ServiceDatesListController('CSV/ServiceDatesList.csv')
        priceController = PriceListController('CSV/PriceList.csv')
        manufacturerController = ManufacturerListController('CSV/ManufacturerList.csv')
    #Generate objects for there control
        manList = manufacturerController.getSortedManufacturersOfAllProducts()
        priceList = priceController.getManufacturersWithPricesOfAllProducts(manList)
        finalOutput = serviceDatesController.getManufacturersWithServiceDatesOfAllProducts(priceList)
    #Initializes list of manufacturer data and appends price and service date
        return sorted(finalOutput, key = operator.itemgetter(1)) 
    #returns sorted by manufacturer name
    
    @staticmethod
    def createItemTypeCSV():
        print("Howdy Texas")

    @staticmethod
    def createFullInventoryCSV():
        ReportsController.writeToFile("CSV/FullInventory.csv", ReportsController.createFullInventoryList())
#writes full inventory to csv file
    @staticmethod
    def createItemInventoryDictionary():
        itemTypeListController = ItemTypeListController('CSV/ManufacturerList.csv')
        priceController = PriceListController('CSV/PriceList.csv')
        serviceDatesController = ServiceDatesListController('CSV/ServiceDatesList.csv')

        itemTypesDictionary = itemTypeListController.gettypesOfAllProducts()
        
        for each_type in itemTypesDictionary.keys():
            itemTypesDictionary[each_type] = priceController.getManufacturersWithPricesOfAllProducts(itemTypesDictionary[each_type])
            itemTypesDictionary[each_type] = serviceDatesController.getManufacturersWithServiceDatesOfAllProducts(itemTypesDictionary[each_type])
        
        return itemTypesDictionary
#create dict of inventory which generates different typeInventory csv file
    @staticmethod
    def writeToFile(fileName, tableData):
        with open(fileName, 'w', newline="") as new_file:
            csv_writer = csv.writer(new_file, delimiter=",")

            for line in tableData:
                csv_writer.writerow(line)
#foundation for writing to file provided with the listed data.
    @staticmethod
    def createPastServicesList():
        fullTable = ReportsController.createFullInventoryList()
        finalOutput = []
        for each_row in fullTable:
            listingDate = datetime.strptime(each_row[4], '%m/%d/%Y').date()
            if listingDate < date.today():
                finalOutput.append(each_row)
        return sorted(finalOutput, key=lambda x: datetime.strptime(x[4], '%m/%d/%Y'), reverse=True) 
#create a list of the past service reocrds using the full inventory list. While looping through each row it sorts the dates and then returns the most recent dates.
    @staticmethod
    def createPastServicesCSV():
        ReportsController.writeToFile("CSV/PastServicesDateInventory.csv", ReportsController.createPastServicesList())
#write function to write the past service date to the file.
    @staticmethod
    def writeAllTypeInventoryListstoCSV():
        finalData = ReportsController.createItemInventoryDictionary()
        for each_type in finalData.keys():
            ReportsController.writeToFile("CSV/"+each_type+"Inventory.csv", finalData[each_type])
#The different TypeInventory are written to csv file and then separated and matched by row. It then itterates through the keys and writes them to a file
    @staticmethod
    def createDamagedInventoryCSV():
        ReportsController.writeToFile("CSV/DamagedInventory.csv", ReportsController.createDamagedInventoryList())
#used to write the damaged inventory to a file
    @staticmethod
    def createDamagedInventoryList():
        fullTable = ReportsController.createFullInventoryList()
        finalOutput = []
        for this_row in fullTable:
            if this_row[5] == "damaged":
                finalOutput.append(this_row)
        return sorted(finalOutput, key = operator.itemgetter(3))
#creates a damaged inventory list, grabs the full inventory and filters if the item is damaged. It aslo sorts the items from most to least expensive.
