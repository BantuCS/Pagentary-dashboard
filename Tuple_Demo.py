# creating a tuple

fruits_name = ("apple", "banana", "cherry", "date", "elderberry","apple")
print("Tuple of fruits:", fruits_name)

# accessing tuple elements
print("First fruit:", fruits_name[0]) # index starts from 0
print("Third fruit:", fruits_name[2]) # accessing the third element

# modifying tuple elements
# tuples are immutable, so we cannot change their elements directly
#fruits_name[1] = "blueberry" # this will raise an error
#print("Modified tuple of fruits:", fruits_name)


#slicing a tuple
print("Sliced tuple of fruits (third element to the sixth element):",
      fruits_name[2:5]) # slicing from the third element to the fifth element (index 2 to index 4)

print("Sliced tuple of fruits (fourth element to the end):"
      , fruits_name[3:]) # slicing from the fourth element to the end

print("Sliced tuple of fruits (beginning to the fifth element):", 
      fruits_name[:5]) # slicing from the beginning to the fifth element (index 0 to index 4)


#combining a tuple create a tuple of cricketers and ranking two tuples
cricketers = ("Virat Kohli", "Steve Smith", "Kane Williamson")
print("Tuple of cricketers:", cricketers)
rankings = (1, 2, 3)
print("Tuple of rankings:", rankings)

new_tuple=cricketers + rankings
print("Combined tuple of cricketers and rankings:",new_tuple)