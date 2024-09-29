# takes an integer as input and returns the sum of all the digits in that integer
# bonus - if the sum of the digits is greater than 9, continue summing the digits of the result until you get a single-digit number

def sum_of_digits(n):
    nums1 = [int(char) for char in str(n)]
    count1 = 0
    count2 = 0
    total1 = 0
    total2 = 0

    while count1 < len(nums1):
        total1 += nums1[count1]
        count1 += 1

    if total1 > 9:
        nums2 = [int(char) for char in str(total1)]

        while count2 < len(nums2):
            total2 += nums2[count2]
            count2 += 1

        return total2

    return total1

print(sum_of_digits(456))

# can improve this with recursion