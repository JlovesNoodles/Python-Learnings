number = input ('Enter the number: ')


for i in number:
    if int(number) % 2 == 0:
        
        print("The number is Not Prime")
        for num in range (0,int(number),2):
            print(num + 2)
        break
    else:
        print("The number is Prime")
        for num in range (0,int(number),2):
            print(num + 1)
        break
        


        ######################################################################################
def prime_checker(number):
    for i in range (number):
        if number % 2 == 0:
            print ("The number is Not Prime")
            for num in range (0,int(number),2):
                print (num + 2)
            break
        else:
            print ("The number is Prime")
            for num in range (0,int(number),2):
                print(num + 1)
            break
