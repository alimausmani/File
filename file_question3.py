# Aapke paas ek list hai. Iss list mein har string ko ek 
# file-question3.txt naam ki file mein nayi line mein daalo. Aapki list yeh rahi:
banks_list = ["Kotak", "HDFC", "RBL", "SBI", "Bank of Baroda"]

file1 = open("file-question3.txt","w")
file1.write("Kotak\n")
file1.write("HDFC\n")
file1.write("RBL\n")
file1.write("SBI\n")
file1.write("Bank of Barodra\n")

file1 = open("file-question3.txt")
file_data = file1.read()
print (file_data)
file1.close()
