def find_max(numbers):
    max_number = numbers[0]
    for number in numbers:
        if number > max_number:
            max_number = number
    return max_number

numbers = input("Enter a list of numbers separated by a comma: ").split(",")
max_num = find_max(numbers)
print("The max number is",max_num)