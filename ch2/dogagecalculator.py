#Dog Age Calculator:
#1-ask the user for the dog's name.
# prompt the user to enter the dog's name,store in dog_name.
#2-ask the user for the age of the dog in years.
# prompt the user to enter the dog's age,store in dog_years.
#3-Multiply the dog’s age by the number 7 to get 
# the dog’s age in human years.
# human_years = dog_years x 7.

#4-output dog's name and age in human years.
#
# example: Your dog, [name] is
#[human_years] years old in human years.
#
#==============================================

dog_name = input("What is your dog's name? ")
#show  dog's name
#print(dog_name)

dog_age = int(input("What is your dog's age? "))
#show  dog's age dogs years
#print(dog_age)

# calculate the human years
human_years = str(dog_age * 7)
#human_years_string = str(human_years)


print("Your dog, " + dog_name + " is " +  human_years + " years old in human years.")
