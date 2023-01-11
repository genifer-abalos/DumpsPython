# Lambda = anonymous function

x = 5

# this will create a function to_add with x,y parameters
to_add = lambda x,y: x + y      # the expression after the lambda are the parameters,
                                # while the expression after the : is what the lambda function will return
                                # In this case,
                                # to_add will accept two arguments to_add(1,2)
                                #   then the lambda function will perform 1+2
                                #   then return the result which is 3
# print(to_add(5,6))


# a lambda function within a function
def times_5(x,y):
    add_these = lambda x,y: x + y
    return add_these(x,y) * 5


after_times_5 = times_5(x=5,y=6)        # this will perform the add_these() function first with x=5, y=6
                                        # and then the times_5() function
                                        # this performs like -> times_5(add_these(5,6))
print(after_times_5)
