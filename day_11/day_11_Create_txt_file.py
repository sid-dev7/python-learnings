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

# write_file()

def append_file():
    # mode: a
    # - previous contents will be presisted
    file = open("myfile.text","a")

    # perform the operation
    # file.write("new content written")
    file.write("I love watching movies")
    # close the file
    # file.close()
append_file()

def read_file_():
    # open file in read mode
    file = open('myfile.txt','r')
    # perform operations

    data = file.read()

    print(f" data = {data}")

    #close the file

    file.close()
read_file_()