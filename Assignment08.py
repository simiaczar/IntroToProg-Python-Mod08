# ------------------------------------------------------------------------ #
# Title: Assignment 08
# Description: Working with classes

# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# RRoot,1.1.2030,Added pseudo-code to start assignment 8
# <Your Name>,<Today's Date>,Modified code to complete assignment 8
# ------------------------------------------------------------------------ #

# Data -------------------------------------------------------------------- #
strFileName = 'products.txt'
lstOfProductObjects = []

class Product:
    """Stores data about a product:

    properties:
        product_name: (string) with the products's  name
        product_price: (float) with the products's standard price
    methods:
    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class
        <Your Name>,<Today's Date>,Modified code to complete assignment 8
    """
    ProductName = ''
    ProductPrice = ''

    def __init__(self, product_name, product_price):
        self.ProductName = product_name
        self.ProductPrice = product_price

    def product_name(self):
        return self.__product_name

    def product_name(self,name):
        if name.isnumeric() == False:
            self.__product_name = name
        else:
            raise Exception('Product can not be Numbers')

    def product_price(self):
        return self.__product_price

    def product_price(self, value):
        if value.isalpha() == False:
            self.__product_price = value
        else:
            raise Exception('Price can not be letters')

# Data -------------------------------------------------------------------- #

# Processing  ------------------------------------------------------------- #
class FileProcessor:
    """Processes data to and from a file and a list of product objects:

    methods:
        save_data_to_file(file_name, list_of_product_objects):

        read_data_from_file(file_name): -> (a list of product objects)

    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class
        <Your Name>,<Today's Date>,Modified code to complete assignment 8
    """
    def read_data_from_file(file_name):
        lstofProducts = []
        try:
            file = open(file_name, 'r')
            for line in file:
                data = line.split(' | ')
                product_name = data[0]
                product_price = data[1]
            file.close()
            return lstofProducts
        except FileNotFoundError:
            print('File', file_name, 'Currently does not exist')
            return lstofProducts

    def save_data_to_file( file_name, lstofProducts):
        file = open(file_name, 'w')
        for objProduct in lstofProducts:
            file.write('Product: ' + objProduct.ProductName + 'Price: $' + str(objProduct.ProductPrice))
        file.close()
# Processing  ------------------------------------------------------------- #

# Presentation (Input/Output)  -------------------------------------------- #
class IO:
    # TODO: Add docstring
    pass
    # TODO: Add code to show menu to user
    def DisplayMenu():
        print('''
        Menu of Options
        1) Display Current Data
        2) Add New Product & Price
        3) Save Product & Price and Exit''')

    # TODO: Add code to get user's choice
    def UserChoice():
        strChoice = input('Choose an Option [1 to 3]: ')
        return strChoice

    # TODO: Add code to show the current data from the file to user
    def DisplayProductandPrice(list_of_product_objects):
        for objProduct in list_of_product_objects:
            print('Product: ' + objProduct.ProductName + 'Price: $' + str(objProduct.ProductPrice))

    # TODO: Add code to get product data from user
    def AddProductandPrice():
        product = input('Enter Product: ')
        while True:
            try:
                price = float(input('Enter Price: $'))
                break
            except ValueError:
                print('Try Again: price must use numbers')
                continue
        return Product(product,price)

# Presentation (Input/Output)  -------------------------------------------- #

# Main Body of Script  ---------------------------------------------------- #
# TODO: Add Data Code to the Main body
# Load data from file into a list of product objects when script starts
lstOfProductObjects = FileProcessor.read_data_from_file('product.txt')
while True:
    IO.DisplayMenu()
    # Show user a menu of options

    strChoice = IO.UserChoice()
    # Get user's menu option choice

    if (strChoice.strip() == '1'):
        try:
            IO.DisplayProductandPrice(lstOfProductObjects)
        except ValueError as e:
            print(e)
        continue
        # Show user current data in the list of product objects

    elif (strChoice.strip() == '2'):
        try:
            newline = IO.AddProductandPrice()
            lstOfProductObjects.append(newline)
        except ValueError as e:
            print(e)
            continue
    # Let user add data to the list of product objects
    elif (strChoice.strip() == '3'):
        FileProcessor.save_data_to_file(strFileName, lstOfProductObjects)
        input('Product and Prices saved. Press Enter to quit')
        break
    else:
        print('Try Again')
        continue
    # let user save current data to file and exit program

# Main Body of Script  ---------------------------------------------------- #



