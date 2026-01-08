def my_function():
    for i in range(1, 21):
        if i == 20:
            print("You got it")


my_function()

# Describe the Problem - Write your answers as comments:
# 1. What is the for loop doing?
# - iterating over i from 1 to 19, if the value of i is 20, then print "You got it"
# 2. When is the function meant to print "You got it"?
# - if the value of i is 20
# 3. What are your assumptions about the value of i?
# - i is never going to reach 20, because the for loop stops when i is 19