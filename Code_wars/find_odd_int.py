# Given an array, find the integer that appears an odd number of times.

# There will always be only one integer that appears an odd number of times.

# FUNDAMENTALS

def find_it(numbers):
    b = False
    for i in numbers:
        odd_counter = 0
        for j in numbers:
            if b == True:
                pass
            else:
                if i == j:
                    odd_counter += 1
                    aux = i
        if odd_counter % 2 != 0:
            b = True
            print('The number {number} appeared an od number of times: {times}'.format(
                number=aux, times=odd_counter))
    if b:
        pass
    else:
        print('We couldnt find a number that appaeared an odd number of times')
        # return None


def run():
    numbers = [1, 1, 2, -2, 5, 2, 4, 4, -1, -2, 5]
    find_it(numbers)


if __name__ == "__main__":
    run()
