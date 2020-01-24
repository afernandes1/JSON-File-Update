# JSON-File-Update

For a given JSON file I was asked to update one of the fields with information retrieved from another .csv file. This has to be done for all entries in the file, around 120 times.

Every IP Address from the .csv file has an unique ID, and that ID needs to be populated into the JSON file. The two files don't have the same number of IP Addresses nor these are in the same order so will need to match the IP Addresses from both files.

Finally the JSON file will be edited to include the 'TMSId' field with the correct value from the .csv file, for each IP Address. 
