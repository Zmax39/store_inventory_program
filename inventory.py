
#========The beginning of the class==========
class Shoe:

    # initialising the attributes
    def __init__(self, country, code, product, cost, quantity):
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity

    # defining a method that gets the cost of the shoes
    def get_cost(self):
        return self.cost

    # defining a method that gets the quantity of the shoes
    def get_quantity(self):
        return self.quantity

    # returns a string representation of the class
    def __str__(self):
        return f"{self.country}, {self.code}, {self.product}, {self.cost}, {self.quantity}"


#=============Shoe list===========

# list called shoe list that is currently empty
shoe_list = []

#==========Functions outside the class==============
#function to open inventory.txt and read the data and put it into a list
def read_shoes_data():
    # opening inventory.txt - splitting up the lines and appending it to the shoe list
    try:
        with open('inventory.txt', 'r', encoding = 'utf-8-sig') as f:
            #skipps the firts line
            next(f)
            for line in f:
                country, code, product, cost, quantity = line.strip().split(",") # splits all items into a list and assigns each one to new variable
                shoe_list.append(Shoe(country, str(code), product, float(cost), int(quantity)))
    except Exception as e:
        print(e)

# function allowing user to enter data about shoe to create a new object and append this data
def capture_shoes():
    # getting user input for each variable in the list
    country = input("\nPlease enter a country name for this shoe: \n")
    code = str(input("\nPlease enter the code for this shoe: \n"))
    product = str(input("\nPlease enter the product name: \n"))
    cost = float(input("\nPlease enter the cost of this shoe in Pounds and Pennies: \n"))
    quantity = int(input("\nPlease enter the quantity of these shoes: \n"))

    # appending details to shoe list
    shoe_list.append(Shoe(country, str(code), product, cost, quantity))

# function to view everything in the shoe list
def view_all():
    # if shoe list is empty
    if not shoe_list:
        print("The inventory is empty!")
    else:
        for shoe in shoe_list:
            print(shoe)

# function that finds the shoe object with the lowest quantity  - asks user if they want to add this quantity of shoes and updates it
def re_stock():
    # finding the lowest quantity and assigning it to a variable
    lowest_quantity = min(shoe_list, key=lambda x: x.quantity) # lambda is anon function that returns the value of an expression. I used this site - https://blogboard.io/blog/knowledge/python-sorted-lambda/
    # asks user if they want to update the stock
    update_stock = input(f"\nDo you want to restock product: {lowest_quantity.product} with code {lowest_quantity.code}? (Y/N): \n")
    # if user chooses to update stock
    if update_stock.lower() == "y":
        # they will be prompted to enter how many to add to stock
        quantity_to_add_to_stock = int(input("Enter the quantity to add to stock: "))
        # the index of shoe list with the lowest quantity will have the user inputted quantity added to its current quantity
        shoe_list[shoe_list.index(lowest_quantity)].quantity += quantity_to_add_to_stock
        
        # opens the txt file and writes the adjusted quantity
        with open("inventory.txt", "w") as f:
            f.write("country,code,product,cost,quantity\n")
            for shoe in shoe_list:
                # writing all items from the shoe list to inventory.txt file
                f.write(f"{shoe.country}, {shoe.code}, {shoe.product}, {shoe.cost}, {shoe.quantity}\n")

# function to search for shoes by code
def search_shoe(code):   
    # iterates through shoe list and if the code is equal to the user inputted code for search it will return the shoe
    for shoe in shoe_list:
        if str(code) == shoe.code:
            return shoe
    # if code is invalid it will return None
    return None

# function that calculates the total value for each item
def value_per_item():
    # total value var starts off = 0
    total_value = 0
    # iterate through shoe list
    for shoe in shoe_list:
        # value of the shoe is equal to the cost multiplied by the quantity
        value = shoe.cost * shoe.quantity
        # setting the total value to = value var above
        total_value += value
        # prints the product name and its individual value
        print(f"{shoe.product}: £{value}")
    # prints the total value
    print(f"Total value: £{total_value}")

# prints this shoe for sale with the highest quantity
def highest_qty():
    # finding the highest quantity and assigning it to a variable
    highest_quantity = max(shoe_list, key=lambda x: x.quantity) # lambda is anon function that returns the value of an expression. I used this site - https://blogboard.io/blog/knowledge/python-sorted-lambda/
    # prints that whatever the product with the highest quantity is is for sale and its quantity
    print(f"{highest_quantity.product} is for sale, we have {highest_quantity.quantity} in stock.")


#==========Main Menu=============

# function for main menu - i will use a while loop and dictionary to map the users input to the functions i created
def main_menu():
    # initialises the function to read the info off inventory.txt file
    read_shoes_data()

    # dictionary called options with all of the user options
    options = {
        "1": capture_shoes,
        "2": view_all,
        "3": re_stock,
        "4": lambda: search_shoe(str(input("Enter the shoe code: "))),
        "5": value_per_item,
        "6": highest_qty,
        "7": exit
    }

    # while the dictionary is true it will print a list of options for the user and let them pick one - when they input a number it will correspond to a function
    while True:
        print("""
        Shoe Inventory Management System
        1. Add shoe data to the system
        2. View all shoes
        3. Re-stock shoe with the lowest quantity
        4. Lookup shoe via code
        5. Calculate the value per shoe
        6. Find the highest quantity for sale
        7. Exit
        """)
        # allows user to input their choice
        choice = str(input("\nEnter an option: \n"))
        # try except that maps user input to the above dictionary
        try:
            #
                options[choice]()
        # excepts key errors of wrong input and prints appropriate message
        except KeyError:
            print("\nPlease choose a valid option!\n")

# runs the main menu function to initiate the program
main_menu()
