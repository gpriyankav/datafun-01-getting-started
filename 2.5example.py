# Calculate the number of boxes a farmer needed to store 28 eggs
number_of_boxes = 28 // 6

# Calculate the number of eggs in the last uncompleted box
eggs_in_last_box = 28 % 6

# Calculate the number of additional eggs needed to fill the last box
additional_eggs = 6 - eggs_in_last_box

# Print the results
print('Number of boxes needed:', number_of_boxes)   
"""4"""
print('Eggs in last box:', eggs_in_last_box)  
"""4"""
print('Additional eggs needed:', additional_eggs) 
"""2"""