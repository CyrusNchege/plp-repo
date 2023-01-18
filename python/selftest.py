# Create a dictionary named personalDetails with the following information ( 5 marks)
# FisrtName: James
# LastName :Ouko
# Age: 22
# PhoneNumber: 07123456789
# Email: student@gmail.com
# Using the relevant properties and methods do the following;

# Update Age to 55                                       
# Print the LastName                                      
# Print length of the dictionary

personalDetails ={
    "FisrtName":"james",
    "LastName":"Ouko",
    "Age":22,
    "PhoneNumber":"07123456789",
    "Email": "student@gmail.com"
}
#updating age to 55
personalDetails["Age"]=55
print(personalDetails["Age"])

#printing last name
print(personalDetails["LastName"])

# Print length of the dictionary.
print(len(personalDetails))


