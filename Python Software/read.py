def data_stored_in_dictionary ():

    """ creating a list inside dictionary """
# this code just stores in list for displaying the text file 
    file = open("laptops.txt","r")
    laptop_details = {}
    laptop_id = 1
    for line in file :
        line = line.replace("\n","")
        laptop_details.update({laptop_id: line.split(",")}) # {1:[razer,...],2:[xps,...],3:[sdasfd]}
        laptop_id = laptop_id + 1 
    file.close()
    return laptop_details

def table_data_displaying ():
    file = open("laptops.txt","r")
    a = 1
    for line in file :
        print(a, "\t\t" + line.replace("," , "\t\t"))
        a = a + 1
        print("---------------------------------------------------------------------------------------------------------------------------------------")
    file.close()
    print("\n")