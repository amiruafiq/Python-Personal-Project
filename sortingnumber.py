# Get input from the user
numbers = []

for i in range(5):
    num = float(input(f"Enter number {i + 1}: "))
    numbers.append(num)

# Sort the list of numbers
sorted_numbers = sorted(numbers)

# Display the sorted numbers
print("Sorted numbers:", sorted_numbers)
