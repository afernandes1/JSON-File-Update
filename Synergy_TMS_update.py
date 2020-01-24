#-------------------------------------------------------------------------------
# Name:        Synergy_TMS_update
# Purpose:
#
# Author:      afernandes
#
# Created:     20/01/2020
# Copyright:   (c) afernandes 2020
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import csv

# Fuction opens CSV file to read all the content and save it to a variable
def csvfile():

    inputm = []
    each = []
    csvlist = []

    with open(r"C:\TMS Export\tmsexport.csv", "r") as my_file:
        reader = csv.reader(my_file, delimiter="\t")        # this variable will have 4 colums of information but we only want 2 of these

        for row in reader:                                  # reading each of the rows in the table
            inputm.append(row)
            #print(row)
            output_str = []

            for item in row:
                items = item.split(',')                     # CSV file have diferent information split by commas
                output_str.append([items[0], items[2]])     # now saving the 2 colums we want with index 0 and 2 into the variable
                #print(output_str)

                for each in output_str:                     # creating a list to be returned into the main function with the 2 colums we need
                    #print(csvlist)
                    csvlist.append(each)
    return(csvlist)


# Function opens config.json file to get the fiels we want to change - this is the file we want to edit
def jsonfile():
    with open('C:\TMS Export\config.json') as f:
        content = f.readlines()                             # all the lines of the file are saved into the variable

        tmsid = [s for s in content if "TMSId" in s]        # search for lines that contains the word "TMSId"
        tmsid_new = [s.rstrip() for s in tmsid]

        ipaddress = [s for s in content if "SystemIPAddress" in s]  # search for lines that contains the word "SystemIPAddress"
        ipaddress_new = [s.rstrip() for s in ipaddress]

        added = list(zip(tmsid_new, ipaddress_new))         # creates a tuple with a combination of the values saved above

        something = []

        return added

        for something in added:
            abc = something[-1:]
            zxc = something[:-1]
            #print(zxc)
            #print(abc)
            ipsdd = []
            tmsids = []
            cde = []

            for cde in abc:
                ipsdd = cde[32:][:-2]
                #return(ipsdd)
                #print(ipsdd)

            for qwer in zxc:
                tmsids = qwer[21:]


from_csv = []

#Starts here:
#
#
#Step 1 - Calls csvfile function and save information into variable
from_csv = csvfile()

#Step 2 - Call jsonfile function and save information into variable
from_json1 = jsonfile()



csv_tmsID = []
csv_IP = []
for csv_item1 in from_csv:
    csv_tmsID.append(csv_item1[0])                  # creates a list of the TMSId from the CSV File - this value will replace the TMSId on the JSON file
    csv_IP.append(csv_item1[1])                     # creates a list of the IP Addresses from the CSV File


to_csv= []
for each_tt1 in from_json1:
    eachtt2 = each_tt1[1].split("\"")               # creates a list of IP Addresses from JSON file by the order they are on the original file
    to_csv.append(eachtt2[3])                       #

final_list = []

for values in to_csv:                               # reads every IP Address from JSON File
    #print(values)
    if any(values in s for s in csv_IP):            # if any IP Address from JSON file is also inside the CSV File then:
        csvIndex = csv_IP.index(values)             # gets the table index of the IP Address of CSV File
        #print(csvIndex)
        deviceID = csv_tmsID[csvIndex]              # the TMSId from CSV File will have the same table index as the IP Address of CSV File so here we are getting the TMSId
        #print(values + "  " + deviceID)
        #print(values)
        new_value = "            \"TMSId\": " + deviceID + ","      # we will use that TMSId from CSV File to create the new line to replace in the JSON file
        old_value = "            \"TMSId\": 0,"                     # original line on JSON File
        #print(new_value)

        with open(r'C:\TMS Export\config.json', 'r') as file:  # opens original JSON file again as read

            newText = file.read().replace(old_value, new_value, 1)  # finds the FIRST MATCH ONLY and replace the "old_value" with "new_value"
            output = file.read()                                    # when the FOR loop comes here next time, the FIRST MATCH will be the next one as this one has been changec


        with open(r'C:\TMS Export\config.json', "w") as f:     # opens JSON File as writable and saves the new configuration with the variable created above
            f.write(newText)
            output = f.close()




