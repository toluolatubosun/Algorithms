numbers = [8, 4, 7, 19, 1, 4, 3, 0, 12, 8, 6]
ordered_numbers = []

while numbers:
    smallest_number = numbers[0]
    for number in numbers:
        if number < smallest_number:
            smallest_number = number
    ordered_numbers.append(smallest_number)
    numbers.remove(smallest_number)

print(ordered_numbers)

# Run the loop as long as the numbers list is not empty
# Assume the smallest number is the first number in the list
# loop through all the numbers in the list
# if a number is found to be less than the smallest number reset the smallest number
# add the smallest number to the ordered_numbers list and remove it from the numbers list

# change the less than sign on line 7 to greater than for descending order
