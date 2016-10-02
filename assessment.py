# PART ONE

# 1. We have some code which is meant to calculate an item cost
#    by adding tax. Tax is normally 5% but it's higher in
#    California (7%).

#    Turn this into a function. Your function will pass in
#    the default tax amount (5%), a state abbreviation, and the
#    cost amount as parameters.

#    If the state is California, apply a 7% tax within the function.
#    Your function should return the total cost of the item,
#    including tax.

#    If the user does not provide a tax rate it should default to 5% 
def calculate_cost(state, cost, tax = .05):
    """ Calculate item cost by adding tax.

    Total cost is cost + cost * tax. Tax rate is 5 percent unless 
    the state is CA, in which case the tax is 7 percent.
    """
    if state == 'CA':
        tax = .07

    return cost + (cost*tax)
#####################################################################
# PART TWO

# 1. (a) Write a function, `is_berry()`, which takes a fruit name as a string
#        and returns a boolean if the fruit is a "strawberry", "cherry", or 
#        "blackberry".
def is_berry(fruit):
    """ Returns boolean based on fruit entered as parameter.

    Returns true of fruit is stawberry, cherry or blackberry.
    Returns false if input is anything else.
    """
    if fruit == 'strawberry' or fruit == 'cherry' or fruit == 'blackberry':
        return True
    else:
        return False

#    (b) Write another function, shipping_cost(), which calculates shipping cost
#        by taking a fruit name as a string, calling the `is_berry()` function 
#        within the `shipping_cost()` function and returns `0` if ``is_berry()
#        == True``, and `5` if ``is_berry() == False``.
def shipping_cost(fruit):
    """
    Uses is_berry function to return shipping cost of fruit.

    If the fruit is strawberry, cherry or blackberry, the shipping cost is 0.
    If the fruit is anything else, the shipping cost is 5.
    """
    if is_berry(fruit) == True:
        return 0
    else:
        return 5

# 2. (a) Write a function, `is_hometown()`, which takes a town name as a string
#        and evaluates to `True` if it is your hometown, and `False` otherwise.
#
def is_hometown(town):
    """
    Returns a boolean based on town entered as parameter.

    Returns true if town matches my own hometown, Warren.
    Returns false if input is any other town.
    """
    if town == 'Warren':
        return True
    else:
        return False

#    (b) Write a function, `full_name()`, which takes a first and last name as
#        arguments as strings and returns the concatenation of the two names in
#        one string.
#
def full_name(first_name, last_name):
    """
    Returns full name

    Concatenates first and last name given in parameters.
    """
    return first_name + ' ' + last_name

#    (c) Write a function, `hometown_greeting()`, which takes a home town, a
#        first name, and a last name as strings as arguments, calls both
#        `is_hometown()` and `full_name()` and prints "Hi, 'full name here',
#        we're from the same place!", or "Hi 'full name here', where are you 
#        from?" depending on what `is_hometown()` evaluates to.
def hometown_greeting(town, first_name, last_name): 
    """ Creates greeting based on given parameters town and name.

    Calls full_name function to return full name from first and last name.
    Calls is_hometown function to determine if we are from the same place,
    otherwise ask where you are from.
    """
    if is_hometown(town) == True:
        print "Hi, %s, we're from the same place!" % full_name(first_name, last_name)
    else:
        print "Hi, %s, where are you from?" % full_name(first_name, last_name)

#####################################################################

# PART THREE

# 1. Write a function ``increment()`` with a nested inner function, ``add()`` 
#    inside of it. The outer function should take ``x``, an integer which
#    defaults to 1. The inner function should take ``y`` and add ``x`` and ``y`` together.
def increment(x = 1):
    """ Outer function takes input x, if none then defaults to 1.
    """
    def add(y):
        """ Inner function returns sum of input x from increment function, 
        and input y passed into here.
        """
        return x + y
    return add

# 2. Call the function ``increment()`` with x = 5. Assign what is returned to a variable name, addfive. Call 
#    addfive with y = 5. Call again with y = 20.
""" Create a new function called addfive, 
which passes 5 as the x input in increment
"""
addfive = increment(5)
"""Pass in x from outer function increment, 
take y as the parameter and perform inner function add
"""
addfive(5) 
addfive(20)

# 3. Make a function that takes in a number and a list of numbers. It should append
#    the number to the list of numbers and return the list.
def add_number(num, num_list):
    """ Add given number to given number list.

    Use append function to add number to the end of the list.
    """
    num_list.append(num)
    return num_list

#####################################################################