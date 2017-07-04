'''
A function called find_max_min to
find the minimum and maximum elements of an array '''

def find_max_min(numbers):
    #This Ensures that the value passed in is  is a list
    if isinstance(numbers, (list)):
        #This Ensures that all the values in the list are numbers
        if all(isinstance(number, (int)) for number in numbers):
            #Fisrtly, Sort the values in the list
            numbers.sort()
            #First verify whether the max and min numbers are equal and
            #if so return a list containing the length of the list
            if numbers[0] is numbers[-1]:
                return [len(numbers)]
            #Otherwise return a list containing the min and max value of the above list

            else:

                return [numbers[0], numbers[-1]]
        else:
            print ('OOps, no integral values found')
    else:
        raise TypeError