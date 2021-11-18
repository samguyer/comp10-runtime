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
#    Check each number against the remaining ones
def has_duplicates_2(nums):
    has = False
    i = 0
    for x in nums:
        for y in nums[i:]:
            if x == y:
                has = True
        i = i + 1
    return has

# -- Has duplicates?
#    Assume the list is in order
def has_duplicates_3(nums):
    has = False
    n = len(nums)
    for i in range(1,n):
        if nums[i] == nums[i-1]:
            has = True
    return has

# -- Has duplicates?
#    Assume we know that numbers are between 0 and 10,000
def has_duplicates_4(nums):
    has = False
    for x in range(0,10000):
        count = count_num(x, nums)
        if count > 1:
            has = True
    return has

# -- Has duplicates?
#    Same assumption, but use a table
def has_duplicates_5(nums):
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
#    Use a dictionary that maps numbers to counts
def has_duplicates_6(nums):
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

size = int(input('Enter list length: '))

done = False
while not done:
    # -- Run and time one of the algorithms
    s = input('Enter algorithm (1-6): ')
    choice = int(s)
    has = False
    if choice == 1:
        # -- Make a list of random numbers in the range 0 to 1 million
        numlist = [int(random.random() * 1000000) for _ in range(size)]
        print("Start...")
        t1 = time.time()
        has = has_duplicates_1(numlist)
        t2 = time.time()
    elif choice == 2:
        # -- Make a list of random numbers in the range 0 to 1 million
        numlist = [int(random.random() * 1000000) for _ in range(size)]
        print("Start...")
        t1 = time.time()
        has = has_duplicates_2(numlist)
        t2 = time.time()
    elif choice == 3:
        # -- Make a random list in order
        numlist = []
        v = 0
        for i in range(size):
            v = v + int(random.random() * 10)
            numlist.append(v)
        print("Start...")
        t1 = time.time()
        has = has_duplicates_3(numlist)
        t2 = time.time()
    elif choice == 4:
        # -- Make a list of random numbers in the range 0 to 10,000
        numlist = [int(random.random() * 10000) for _ in range(size)]
        print("Start...")
        t1 = time.time()
        has = has_duplicates_4(numlist)
        t2 = time.time()
    elif choice == 5:
        # -- Make a list of random numbers in the range 0 to 10,000
        numlist = [int(random.random() * 10000) for _ in range(size)]
        print("Start...")
        t1 = time.time()
        has = has_duplicates_5(numlist)
        t2 = time.time()
    elif choice == 6:
        # -- Make a list of random numbers in the range 0 to 1 million
        numlist = [int(random.random() * 1000000) for _ in range(size)]
        print("Start...")
        t1 = time.time()
        has = has_duplicates_6(numlist)
        t2 = time.time()
    else:
        done = True

    if not done:
        print("Time: {:.8f} -- result is {}".format(t2 - t1, has))
