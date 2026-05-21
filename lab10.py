#Analyze with Python --> edit and create 4 files with characters
#1.lsinsulin-seq-clean.txt - 24char
#2.binsulin-seq-clean.txt - 30char
#3.cinsulin-seq-clean.txt - 35char  
#4.ainsulin-seq-clean.txt - 21char

#to perform automation
seq = ""

try:
    with open("preproinsulin-seq-clean.txt") as file:
        seq = file.read()
except:
    print("ERROR")

try:
    with open("lsinsulin-seq-clean.txt", "w") as file1:
        file1.write(seq[:24])
except:
    print("ERROR")
    

try:
    with open("binsulin-seq-clean.txt", "w") as file1:
        file1.write(seq[24:54])
except:
    print("ERROR")
    
    
try:
    with open("cinsulin-seq-clean.txt", "w") as file1:
        file1.write(seq[54:89])
except:
    print("ERROR")
    
    
try:
    with open("ainsulin-seq-clean.txt", "w") as file1:
        file1.write(seq[89:])
except:
    print("ERROR")

