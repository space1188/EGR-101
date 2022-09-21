# Brian Diosan hw3q3

d={'A':1,'B':2,'C':3}

selectedKey = input("Enter a key to check: ")

if selectedKey in d:
    print("The key is present and the value is " + str(d[selectedKey]))
else:
    print("The key is not present")