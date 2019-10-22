import random
import time

# -- Count the number of times val occurs in the list nums
def count_num(val, nums):
    count = 0
    for y in nums:
        if val == y:
            count = count + 1
    return count

# -- Has duplicates?
#    Count the number of occurrences of each number
def has_duplicates_1(nums):
    has = False
    for x in nums:
        count = count_num(x, nums)
        if count > 1:
            has = True
    return has

# -- Has duplicates?
#    Assume we know that numbers are between 0 and 10,000
def has_duplicates_2(nums):
    has = False
    for x in range(0,10000):
        count = count_num(x, nums)
        if count > 1:
            has = True
    return has

# -- Has duplicates?
#    Same assumption, but use a table
def has_duplicates_3(nums):
    has = False
    table = [0 for i in range(10001)]
    for y in nums:
        count = table[y]
        count = count + 1
        table[y] = count
        if count > 1:
            has = True
    return has

# -- Has duplicates?
#    Use a special kind of table called a dictionary
def has_duplicates_4(nums):
    has = False
    table = {}
    for y in nums:
        if y in table:
            count = table[y]
            count = count + 1
            table[y] = count
            if count > 1:
                has = True
        else:
            table[y] = 1
    return has

# --- Main program ------------------------

size = input('Enter list length: ')

# -- Make a list of random numbers
numlist = [ int(random.random() * 10000) for _ in range(int(size))]

# -- Run and time one of the algorithms
s = input('Enter algorithm (1-4): ')
choice = int(s)
t1 = time.time()
has = False
if choice == 1:
    has = has_duplicates_1(numlist)
elif choice == 2:
    has = has_duplicates_2(numlist)
elif choice == 3:
    has = has_duplicates_3(numlist)
else:
    has = has_duplicates_4(numlist)

t2 = time.time()
print("Result is " + str(has))
print("Time: " + str(t2 - t1))
