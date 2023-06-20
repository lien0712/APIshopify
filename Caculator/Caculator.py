sum=0
while(True):
    userInput= input("Entern the price: \n")
    if userInput!= 'q':
        sum= sum+int(userInput)

    else:
        print("Thanks for using our caculator")
        print(sum)
        break
