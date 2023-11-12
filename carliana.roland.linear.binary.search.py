# Carliana Roland 3/16/23 COMP163
# I AM FINDING THE POSITION AND AMOUNT OF ITERATIONS IN A RANDOMIZED INTEGER LIST USING LINEAR AND BINARY SEARCH
import random
# FINDING THE INTEGER IN THE LIST USING LINEAR SEARCH
input_ = input('ANY KEY TO START. Q TO QUIT: ')
while input_.upper() != 'Q':
    if input_.upper() == 'S':
        pass


    def linear_search(list1, integer):
        count = 0
        for l in range(len(list1)):
            count += 1
            if list1[l] == integer:  # BASE CASE
                print(f'LINEAR SEARCH ITERATIONS: {count}')  # ITERATION COUNT
                return l
        else:
            print('ERROR')
        return integer


# FINDING THE INTEGER IN THE LIST USING BINARY SEARCH


    def binary_search(list1, integer):
        count = 0
        low = 0
        high = len(list1)
        while low <= high:
            count += 1
            middle = (low + high) // 2
            if integer == list1[middle]:  # BASE CASE
                print(f'BINARY SEARCH ITERATIONS: {count}')  # ITERATION COUNT
                return middle
            if integer < list1[middle]:
                high = middle - 1
            else:
                low = middle + 1
        return -1


    # CREATING A SORTED LIST OF 100 RANDOM INTEGERS FOR SEARCHES

    RandomSet = set()
    RandomList = []
    for i in range(101):
        n = random.randint(0, 100)
        RandomSet.add(int(n))

    # CONVERTING SET INTO A LIST FOR NON-DUPLICATE INTEGERS
    for i in RandomSet:
        RandomList.append(int(i))
    print(RandomList)

    User = int(input('ENTER INTEGER HERE: '))

    Result = linear_search(RandomList, User)
    print(f'LINEAR SEARCH POSITION: {Result}')

    Result2 = binary_search(RandomList, User)
    print(f'BINARY NUMBER POSITION: {Result2}')
    input_ = input('S TO START. Q TO QUIT: ')