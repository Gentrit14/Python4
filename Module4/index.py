names = ["Gentrit" , "Eris" , "Drini"]

for name in names:
    print(name)



###########
sentence = "Hello World"

for character in sentence:
    if character.isalpha():
        print(character)


for number in range(1,6):
    print(number)


    ######

numbers = [12,45,4,123,54,65,13]

maximum = numbers[0]

for num in numbers:
    if num > maximum:
        maximum = num
    print("the maximum value in the list is:", maximum)


##################################

count = 1
while count <= 5:
    print("Iteration", count)
    count +=1

######################

while True:
    user_input = input("Enter a positive number:")


    if user_input.isnumeric():
        nu,ber = int(user_imput)

        if number > 0:
            break
            #
            ##############################
            print("invalid input please try again:")
            ######################################
        print("You have entered a valid positive number:", number)

##############################################

list = [1,2,3,4,5,6,7,8,]
target = 4

for number in list:
    print(number)
    if number == target:
        print("Target found")
        break