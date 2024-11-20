#open the file in r+ mode to allow reading and writing
with open("ReadWrite","r+") as file:
    #read the Current Content of the file

    content = file.read()
    print("Original Content:",content)
    #Modeify the Original content with the new data file
    new_content = content.replace("ReadWrite","Newdatareadfile")


    #move the file pointer to the first position/beginning point
    file.seek(0)

    #write the modified content back to file
    file.write(new_content)

    #truncate the rest of values from the old value
    file.truncate()

   # update_content = file.read()
  #  print("Updated Content:", update_content)