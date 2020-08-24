#This is a python program
#User inputs string and inputs characters they would like to make disappear
#Program displays string with the missing characters
string = str(input("Enter a sentence: "))
erase = input("Which characters would you like to see disappear?: ")
for i in erase:
    string = string.replace(i, ' ')
print(string)
