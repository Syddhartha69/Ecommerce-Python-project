# validating laptop identity 
def validating_laptop_id (laptop_specs):
    loop_check = True
    while loop_check == True:
        try:
            user_id = int(input("Please enter the laptop id you want to buy: "))
            print("\n")
            loop_check = False
        except ValueError:
            print("Please provide a valid laptop id")
            
    while user_id <= 0 or user_id > len(laptop_specs):
        print("Please provide a valid laptop id")
        print("\n")
        
        try:
            user_id = int(input("Please enter the laptop id you want to buy: "))
            print("\n")
            loop_check = False
        except ValueError:
            print("Please provide a valid laptop id")    
        print("\n")
    return user_id 

def lautau_ko_quantity(quantity_of_selected_laptop):
    loop_check = True 
    while loop_check == True:
        try:
            user_purchased_quantity = int(input("Please enter the quantity you want to purchase: "))
            print("\n")
            loop_check = False
        except ValueError:
            print("INVALID REQUESTED QUANTITY")
   
    while user_purchased_quantity <= 0 or user_purchased_quantity > int(quantity_of_selected_laptop):
        print("INVALID REQUESTED QUANTITY")
        print("\n")

        try:
            user_purchased_quantity = int(input("Please enter the quantity you want to purchase: "))
            print("\n")
            loop_check = False
        except ValueError:
            print("INVALID REQUESTED QUANTITY")
        print("\n")
    return user_purchased_quantity


# for second option ( purchasing from manufracturer )
def lautau_ko_purchased_quantity():
    loop_check = True
    while loop_check == True:
        try:
            user_purchased_quantity = int(input("Please enter the quantity you want to purchase: "))
            print("\n")
            loop_check = False
        except ValueError:
            print("INVALID REQUESTED QUANTITY")
    
    while user_purchased_quantity <= 0:
        print("INVALID REQUESTED QUANTITY")
        print("\n")
        
        try:
            user_purchased_quantity = int(input("Please enter the quantity you want to purchase: "))
            print("\n")
            loop_check = False
        except ValueError:
            print("INVALID REQUESTED QUANTITY")
        print("\n")
    return user_purchased_quantity
