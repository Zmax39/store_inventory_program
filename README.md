                       -------- TITLE --------
                          
                            # Inventory.py

                       -------- ABOUT --------
This project was my last Capstone project for my portfolio from the HyperionDev Software Engineering bootcamp.

In this project I used Object Oriented Programming to create an Inventory Program in Python to manage stock levels at a store. I programmed it so it would read data from a text file and allow the user to search for products by their respective codes, determine the product with the lowest quantity and restock, determine which product had the highest quantity, and calculate the total value of each stock item.

For this program to work I created a class named Shoes and then initialised a variety of attributes, which are as follows:
  - Country
  - Code
  - Product
  - Cost
  - Quantity

Inside the Shoes class I then defined the following methods:
    - Return the cost of the shoes
    - Return the quantity of shoes
    - Return a string representation of the Shoes class
    
Outside of the class I then defined an empty list and a variety of functions, these are as follows:
    - A function to open the text file, read the data and put it all into the empty         list i created.
    - A function that allows the user to enter data about a new shoe and append this         to the empty list i created.
    - A function to view all items in the shoe list i created.
    - A function that finds the item with the lowest quantity in the list and asks the       user if they wouls like to restock (The restock value is then updated in the           list).
    - A function that allows the user to search for shoes by entering the code.
    - A function that calculates the total value for each item / shoe in the list and       prints this.
    - A function that finds the shoe with the highest quantity.
    
I created a Main Menu function that presented the user with a menu for all the options they could use with the program.

I then created a dictionary and used a while loop to map the user inputs for their respective choices to the functions I created above. I then ran the main_menu function to initiialise the program.

                       -------- HOW TO INSTALL --------
To use this file, just fork my repo to your computer and run it using an IDE.

              -------- IMAGES OF THE PROJECT IN ACTION --------
              
<img width="1440" alt="Screenshot 2022-12-29 at 17 58 51" src="https://user-images.githubusercontent.com/93485223/209991641-aae18e4d-7387-4a63-b377-5cdbdfae06b3.png">

<img width="1440" alt="Screenshot 2022-12-29 at 17 59 05" src="https://user-images.githubusercontent.com/93485223/209991751-821a4705-da26-4532-a263-b736ef4c9591.png">

<img width="1440" alt="Screenshot 2022-12-29 at 17 59 13" src="https://user-images.githubusercontent.com/93485223/209991773-6f4d0f95-269c-4080-a23c-a7c83a6bc6b0.png">

