# file handling
# create file
# overwrite contents to the file
# append contents to the file
# read contents from file
# close the file

def write_file():
    # open the file
    file = open('./myfile.text', 'w')
    # perform application
    file.write("India is my country. I love India")

    #close the file
    file.close()

write_file()