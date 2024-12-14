import datetime

def updating_stock(laptop_specs):

    file = open ("laptops.txt","w")

    for values in laptop_specs.values():
        file.write(str(values[0])+","+str(values[1])+","+str(values[2])+","+str(values[3])+","+str(values[4])+","+str(values[5]))
        file.write("\n")

    file.close 

# bill generation for selling to customer

def bill_generation(user_purchased_quantity_list,name,phone_number):

    total = 0 
    shiping_cost = 500
    for i in user_purchased_quantity_list :
        total += int(i[4])
    grand_total = total + shiping_cost 

    print("\n")
    print("\t\t\t\t\t\t XYZ SHOP BILL ") 
    print("\n")
    print("\t\t\t\t\t Kamalpokhari | 01 1234567")
    print("\n")
    print("------------------------------------------------------------------------------------------------------------------------------------------")
    print("laptop details are: ")
    print("------------------------------------------------------------------------------------------------------------------------------------------")
    print("Customer Name : "+str(name))
    print("Customer Contact Number: "+str(phone_number))
    print("------------------------------------------------------------------------------------------------------------------------------------------")
    print("\n")
    print("Purchase Details: ")
    print("------------------------------------------------------------------------------------------------------------------------------------------")
    print("Item name \t\t\t Brand \t\t\t\t Total Qantity \t\t Unit Price \t\t\t Total")
    print("------------------------------------------------------------------------------------------------------------------------------------------")
    for i in user_purchased_quantity_list :
        print(i[0],"\t\t\t",i[1], "\t\t\t", i[2], "\t\t\t","$", i[3], "\t\t\t", "$", i[4])
    print("------------------------------------------------------------------------------------------------------------------------------------------")
    print("Total Amount : ", total) 
    print("Your Shipping cost is: ", shiping_cost)
    print("Grand Total: "+str(grand_total))
    print("*** Note: shipping cost has been added to grand total ***")
    print("\n")
    print("------------------------------------------------------------------------------------------------------------------------------------------")
    print("\n")



    file = open (str(name)+str(phone_number)+".txt","w") 
    file.write("\n")
    file.write("\t\t\t\t\t XYZ SHOP BILL \n")
    file.write("\n")
    file.write("\t\t\t\t Kamalpokhari | 01 1234567 \n")
    file.write("\n")
    file.write("------------------------------------------------------------------------------------------------------------------------------------- \n")
    file.write("Customer Details are: \n")
    file.write("Customer Name : "+str(name)+"\n")
    file.write("Customer Contact Number: "+str(phone_number)+ "\n" )
    file.write("\n")
    file.write("Laptop Purchase Details: \n")
    file.write("------------------------------------------------------------------------------------------------------------------------------------- \n")
    file.write("Item Name \t\t Brand \t\t Total Qantity \t\t Unit Price \t\t\t Total \n")
    file.write("------------------------------------------------------------------------------------------------------------------------------------- \n")
    for i in user_purchased_quantity_list:
        file.write(str(i[0])+"\t\t\t"+str(i[1])+"\t\t\t"+str(i[2])+"\t\t\t"+"$"+str(i[3])+"\t\t\t"+"$"+str(i[4])+"\n")
    file.write("------------------------------------------------------------------------------------------------------------------------------------- \n")
    file.write("\n")
    file.write("Your Shipping cost is: "+str(shiping_cost)+"\n")
    file.write("\n")
    file.write("Grand Total: $"+str (grand_total)+"\n")
    file.write("\n")
    file.write("*** Note: shipping cost has been added to grand total ***"+"\n")
    file.write("\n")
    file.close()


# bill generation for purchased from manuf

def purchased_bill_generation(user_purchased_quantity_list,name,phone_number): 

    total = 0 
    vat = 0.13
    for i in user_purchased_quantity_list :
        total += int(i[4])
    vat_amount = 0.13* total
    grand_total = total + vat_amount

    print("\n")
    print("\t\t\t\t  XYZ MANUFACTURER BILL ")
    print("\n")
    print("\t\t\t\t Putalisadak | 01 7654321 \n")
    print("\n")
    print("------------------------------------------------------------------------------------------------------------------------------------------")
    print("Shop Details are: ")
    print("------------------------------------------------------------------------------------------------------------------------------------------")
    print("Shop Name: "+str(name))
    print("Shop Contact Number: "+str(phone_number))
    print("------------------------------------------------------------------------------------------------------------------------------------------")
    print("\n")
    print("Laptop Purchase details are: ")
    print("------------------------------------------------------------------------------------------------------------------------------------------")
    print("Item name \t\t\t Brand \t\t\t\t Total Qantity \t\t Unit Price \t\t\t Total")
    print("------------------------------------------------------------------------------------------------------------------------------------------")
    for i in user_purchased_quantity_list :
        print(i[0],"\t\t\t",i[1], "\t\t\t", i[2], "\t\t\t","$", i[3], "\t\t\t", "$", i[4])
    print("------------------------------------------------------------------------------------------------------------------------------------------")
    print("Your total amount is: ", total) 
    print("Your vat amount is: ", vat_amount) 
    print("Grand Total: "+str(grand_total))
    print("*** Note: VAT amount has been added to grand total ***")
    print("\n")
    print("------------------------------------------------------------------------------------------------------------------------------------------")


    file = open (str(name)+str(phone_number)+".txt","w")
    file.write("\n")
    file.write("\t\t\t\t  XYZ MANUFACTURER BILL \n")
    file.write("\n")
    file.write("\t\t\t\t Putalisadak | 01 7654321 \n")
    file.write("\n")
    file.write("------------------------------------------------------------------------------------------------------------------------------------- \n")
    file.write("Shop Details are: \n")
    file.write("Shop Name: "+str(name)+"\n")
    file.write("Shop Contact Number: "+str(phone_number)+ "\n" )
    file.write("\n")
    file.write("Laptop Purchase details are: \n")
    file.write("------------------------------------------------------------------------------------------------------------------------------------- \n")
    file.write("Item Name \t\t Brand \t\t Total Qantity \t\t Unit Price \t\t\t Total \n")
    file.write("------------------------------------------------------------------------------------------------------------------------------------- \n")
    for i in user_purchased_quantity_list:
        file.write(str(i[0])+"\t\t\t"+str(i[1])+"\t\t\t"+str(i[2])+"\t\t\t"+"$"+str(i[3])+"\t\t\t"+"$"+str(i[4])+"\n")
    file.write("------------------------------------------------------------------------------------------------------------------------------------- \n")
    file.write("\n")
    file.write("Your VAT amount is: "+str(vat_amount)+"\n")
    file.write("\n")
    file.write("Your Total amount is: "+str(total) + "\n")
    file.write("\n")
    file.write("Grand Total: $"+str (grand_total)+"\n")
    file.write("\n")
    file.close()