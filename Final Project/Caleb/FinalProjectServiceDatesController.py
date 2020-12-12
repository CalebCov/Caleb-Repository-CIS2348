"""Caleb Covington
   1606086     """
import csv
#import csv
class ServiceDatesListController: #create class

    def __init__(self, file_path): #Initialize attributes of classes
        self.file_path = file_path
    
    def getManufacturersWithServiceDatesOfAllProducts(self, manufacturer_data):
        reader = csv.reader(open(self.file_path), delimiter=",")
        manufacturer_data_with_date = []
        for line in reader:
            for manufacturer_line in manufacturer_data:
                if line[0] == manufacturer_line[0]:
                    manufacturer_line.insert(4,line[1])
                    manufacturer_data_with_date.append(manufacturer_line)
                    break
        return manufacturer_data_with_date
#adds the service date to the already existed manufacturer list with prices. It then matches the IDs to add the correct date to the correct item.