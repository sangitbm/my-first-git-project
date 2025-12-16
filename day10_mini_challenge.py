total_numbers = int(input("Enter the total number of inputs:"))
all_numbers =[]
count = 1
print("\nTotal numbers to be entered:", total_numbers)

while count <= total_numbers:
    
    numbers = int(input("Enter number:"))
    all_numbers.append(numbers)
    count += 1

total = sum(all_numbers)
average = total / total_numbers
highest = max(all_numbers)
lowest = min(all_numbers)

print("\nThe numbers you entered are:", all_numbers)
print("\nThe total is:", total)
print("\nThe average is:", average)
print("\nThe highest numbers is:", highest)
print("\nThe lowest number is:", lowest)

