# this program illustrates list in python

# creating a list

fruits_name = ["apple", "banana", "cherry", "date", "elderberry"]
print("List of fruits:", fruits_name)

# accessing list elements
print("First fruit:", fruits_name[0]) # index starts from 0
print("Third fruit:", fruits_name[2]) # accessing the third element

# modifying list elements
fruits_name[1] = "blueberry" # changing "banana" to "blueberry"
print("Modified list of fruits:", fruits_name)

# length of the list
#length is method ---> len() ---> len(list_name)
print("Number of fruits in the list:", len(fruits_name))

#adding a element to list
fruits_name.append("fig") # adding "fig" to the end of the list
print("List of fruits after adding fig:", fruits_name)

# removing an element from the list
fruits_name.remove("date") # removing "date" from the list
print("List of fruits after removing date:", fruits_name)

#inserting an element at a specific position
#syntax: insert(index, element_name)
fruits_name.insert(0, "mango") # inserting "mango" at index
print("List of fruits after inserting mango at the beginning:", fruits_name)

#removing an element by index
#syntax: pop(index)
fruits_name.pop(3) # removing the fourth element
print("List of fruits after removing the fourth element:", fruits_name)


#duplicate elements in list
fruits_name.append("apple") # adding another "apple" to the list
print("List of fruits after adding another apple:", fruits_name)

#slicing a list
print("Sliced list of fruits (third element to the sixth element):", 
      fruits_name[2:5]) # slicing from the third element to the fifth element (index 2 to index 4)

print("Sliced list of fruits (fourth element to the end):"
      , fruits_name[3:]) # slicing from the fourth element to the end

print("Sliced list of fruits (beginning to the fifth element):", 
      fruits_name[:5]) # slicing from the beginning to the fifth element (index 0 to index 4)

#sorting a list
fruits_name.sort() # sorting the list in alphabetical order
print("Sorted list of fruits:", fruits_name) 

fruits_name.sort(reverse=True) # sorting the list in reverse alphabetical order
print("Sorted list of fruits in reverse order:", fruits_name)

#creating different tyes of list

#creating a list of integers
marks = [89, 92, 76, 84, 95]
print("List of marks:", marks)

#average of marks
average_marks = sum(marks) / len(marks)
print("Average marks:", average_marks)

#percentage of marks
total_marks = 500 # assuming total marks is 500 
percentage_marks = (sum(marks) / total_marks) * 100
print("Percentage of marks:", percentage_marks)

#creating a list of mixed data types
mixed_list = ["hello", 42, 3.14, True]
print("List of mixed data types:", mixed_list)

#combining a list create a list of cricketers and ranking two lists
cricketers = ["Virat Kohli", "Steve Smith", "Kane Williamson"]
print("List of cricketers:", cricketers)
rankings = [1, 2, 3]
print("List of rankings:", rankings)

new_list=cricketers + rankings
print("Combined list of cricketers and rankings:",new_list)








