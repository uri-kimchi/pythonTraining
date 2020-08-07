myfile = open ('text.txt', mode = "r+")
fl = myfile.read()
print(fl)
myfile.seek(4)
line = "x"
xxx = myfile.write("Uri Was here\n")
while line:
    line = myfile.readline()
    print(line)
myfile.close()
