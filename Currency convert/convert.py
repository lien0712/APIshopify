with open('currencyData.txt') as f:
    lines = f.readline()

currencyDict={}
for line in lines:
    parsed= line.split("\t")
    currencyDict[parsed[0]]=parsed[1]

amount= int(input("Enter amount:\n"))
print("Enter the name of currency you want to convert ")
[print(item) for item in currencyDict.keys()]
current= input("Please enter one of these values: ")
print(f"{amount} INR is equal to {amount * float(currencyDict[current])}{current} ")