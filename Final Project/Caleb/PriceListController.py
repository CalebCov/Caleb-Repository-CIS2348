"""Caleb Covington
   1606086     """
import csv
#import csv
class PriceListController: #create a class

    def __init__(self, file_path):  #Initialize attributes of classes
        self.file_path = file_path
    
    def getManufacturersWithPricesOfAllProducts(self, manufacturer_data): #With the created manufacturer list insert the price to the respected IDs
        reader = csv.reader(open(self.file_path), delimiter=",") #open and read file with the delimiter as the seporator
        manufacturer_data_with_price = [] #create empty list
        for line in reader: #loop through each line in the file
            for manufacturer_line in manufacturer_data:
                if line[0] == manufacturer_line[0]: #if the IDs are the same
                    manufacturer_line.insert(3,line[1]) #insert price colom to the row
                    manufacturer_data_with_price.append(manufacturer_line) #insert the array to new array output
                    break
        return manufacturer_data_with_price #returns data with prices after breaking the code for unecessary runtime