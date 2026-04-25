contactCard= {
"name": "Anil",
"phone": "8482398452",
"email": "bantuanil064@gmail.com"
}

print("Contact Card:", contactCard)

# accessing dictionary values
#syntax: dictionary_name[key]

print("Name:", contactCard["name"])
print("Phone:", contactCard["phone"])
print("Email:", contactCard["email"])   


# updating dictionary values
contactCard["phone"] = int(input("Enter new phone number: "))   # updating the phone number
print("Updated Contact Card:", contactCard)

#adding a new key-value pair to the dictionary called bio
#syntax: dictionary_name[new_key] = new_value
contactCard["bio"] = input("Enter your bio: ")
print("Updated Contact Card with Bio:", contactCard)

#adding a new key-value pair to the dictionary called hobbbies which is a list of hobbies
#syntax: dictionary_name[new_key] = new_value
#splitting the input string into a list of hobbies using the split() method

contactCard["hobbies"] = input("Enter your hobbies (comma separated): ").split(",") 
print("Updated Contact Card with Hobbies:", contactCard)

#removing a key-value pair from the dictionary
#syntax: del dictionary_name[key]
#remove bio from the contact card
del contactCard["bio"]
print("Updated Contact Card after removing Bio:", contactCard)
