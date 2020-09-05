
def is_prime(number):

    #base case: number is prime if it equals 1

    # make a list from a range of 1 to the given number
    #for every number in that range:
        #if our input is divisible by given number in range:
            #number isn't prime
        #else:
            #pop i and its multiples from the range using index location
            #reshape range and repeat process until we find our input is divisible by a num in the range
            #or else, the range will complete and we find the item is prime

    #if loop is completed, item is prime