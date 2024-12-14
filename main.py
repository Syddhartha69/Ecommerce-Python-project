import functions
import read
import write

print("---------------------------------------------------------------------------------------------------------------------------------------")
print("\t\t\t\t Hello there admin! welcome to XYZ electronics ") # display message 
print("---------------------------------------------------------------------------------------------------------------------------------------")
print("\n")

# splitting the main file and importing
read.data_stored_in_dictionary() 

loop = True
while loop == True:
    read.table_data_displaying () 
    
    print("---------------------------------------------------------------------------------------------------------------------------------------")
    print("PRESS OPTION - 1 - TO SELL LAPTOP TO CUSTOMER")
    print("PRESS OPTION - 2 - TO PURCHASE FROM MANUFACTURER")
    print("PRESS OPTION - 3 - TO EXIT THE SYSTEM")
    print("\n")

    loop_check = True # Checking wether the input given by user is number or not
    while loop_check == True :
        try :
            user_input = int(input("Please enter your option: ")) # Taking input from user
            loop_check = False
        except ValueError :
            print("INVALID INPUT ENETR NUMBER ONLY! ")


    # Verifiying and giving output according to the input given by user

    if user_input == 1 : 
        print("\n")
        name = input("Enter customer name: ")
        print("\n")
        phone_number = input("Enter customer phone number: ") 
        print("\n")
        address = input("Enter customer address: ")
        print("\n")
        print("---------------------------------------------------------------------------------------------------------------------------------------")
        print("\n")

        volume_of_user_purchase = [] # all items sold to customer will be stored here 
        further_purchase = True 

        while further_purchase == True:

            print("---------------------------------------------------------------------------------------------------------------------------------------")
            print("S.N. \t\tLaptop Name \t\tCompany Name \t\tPrice \t\tQuantity \tGraphics \t\t Processor")
            print("---------------------------------------------------------------------------------------------------------------------------------------")

            read.table_data_displaying()

            laptop_specs = read.data_stored_in_dictionary () 
            
            laptop_identity = functions.validating_laptop_id(laptop_specs) # asking for laptop identity

            quantity_of_selected_laptop = laptop_specs [laptop_identity] [3] 

            if int(laptop_specs [laptop_identity] [3]) == 0: # checking wether the stock is 0 or not
                print("The laptop you've requested laptop is currently out of stock") 
                continue 
            else :
                user_purchased_quantity = functions.lautau_ko_quantity(quantity_of_selected_laptop) # asking for user quantity and validating
            

                # updating laptop detail stored text file 

                laptop_specs[laptop_identity] [3] = int(laptop_specs[laptop_identity] [3]) - int(user_purchased_quantity)

                write.updating_stock(laptop_specs)



                # getting the user purchased items

                product_name = laptop_specs [laptop_identity] [0] 
                product_brand = laptop_specs [laptop_identity] [1] 
                user_selected_quantity = user_purchased_quantity 
                unit_price = laptop_specs [laptop_identity] [2] .replace("$",'')
                total_price = int(unit_price)*int(user_selected_quantity)

                volume_of_user_purchase.append ([product_name, product_brand, user_selected_quantity, unit_price, total_price]) # storing in 2d list (2d list = list inside list)

                print("\n")
                
                buy_more_laptops = input("Continue to sell to customer ? \nPress Y to continue selling OR press * ENTER * key to proceed to billing: ").upper()

                if buy_more_laptops == "Y" :
                    further_purchase = True 

                else :
                    write.bill_generation(volume_of_user_purchase,name,phone_number)
                    further_purchase = False

    elif user_input == 2 :
        print("\n")
        name = input("Enter shop name: ")
        print("\n")
        phone_number = input("Enter shop phone number: ")
        print("\n")
        address = input("Enter shop address: ")
        print("\n")
        print("---------------------------------------------------------------------------------------------------------------------------------------")
        print("\n")

        volume_of_user_purchase = [] # all items purchased from manufacturer will be stored here 
        further_purchase = True 

        while further_purchase == True:
            print("---------------------------------------------------------------------------------------------------------------------------------------")
            print("S.N. \t\tLaptop Name \t\tCompany Name \t\tPrice \t\tQuantity \tGraphics \t\t Processor")
            print("---------------------------------------------------------------------------------------------------------------------------------------")

            read.table_data_displaying()

            laptop_specs = read.data_stored_in_dictionary ()
            
            laptop_identity = functions.validating_laptop_id(laptop_specs) # asking for laptop identity

            quantity_of_selected_laptop = laptop_specs [laptop_identity] [3] 

           
            
            user_purchased_quantity = functions.lautau_ko_purchased_quantity() # asking for user quantity and validating

            
            # updating laptop detail stored text file  

            laptop_specs[laptop_identity] [3] = int(laptop_specs[laptop_identity] [3]) + int(user_purchased_quantity)

            write.updating_stock(laptop_specs)



            # getting the shop purchased items

            product_name = laptop_specs [laptop_identity] [0] 
            product_brand = laptop_specs [laptop_identity] [1] 
            user_selected_quantity = user_purchased_quantity 
            unit_price = laptop_specs [laptop_identity] [2] .replace("$",'')
            total_price = int(unit_price)*int(user_selected_quantity)

            volume_of_user_purchase.append ([product_name, product_brand, user_selected_quantity, unit_price, total_price]) # storing in 2d list (2d list = list inside list)
            buy_more_laptops = input("Continue buying laptops ? \nPress Y to continue selling OR press * ENTER * key to proceed to billing: ").upper()

            if buy_more_laptops == "Y" :
                further_purchase = True 

            else :
                write.purchased_bill_generation(volume_of_user_purchase,name,phone_number)
                further_purchase = False


    elif user_input == 3 :
        loop = False
        print("Thankyou for connecting with us :)")
