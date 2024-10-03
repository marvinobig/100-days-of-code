# takes an integer as input and returns the sum of all the digits in that integer
# bonus - if the sum of the digits is greater than 9, continue summing the digits of the result until you get a single-digit number

def sum_of_digits(n):
    nums_list = [int(char) for char in str(n)]
    total = 0

    for num in nums_list:
        total += num

    if total > 9:
        return sum_of_digits(total)

    return total

print(sum_of_digits(99999))
