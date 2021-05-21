#simple function
def my_function():
    print("Hello1")

my_function()

#pass a parameter to a function
def my_function1(in_varname):
    print("The variable passed to the function is: "+in_varname)

my_function1("pass this text to the function")

#pass a parameter to a function with a default value
def my_function1(in_varname="Something"):
    print("The variable passed to the function is: "+in_varname)

#if nothing is pased then default is used
my_function1()

#you can pass arguments as a list
def my_function_list(var_name):
    for i in var_name:
        print (i)

var_values=["1","2","3"]
my_function_list(var_values)
#or you can directly pass a list
my_function_list(["1","2","3"])

#a function should return a value and not print
def my_function(in_varname):
    return "Hello "+in_varname

my_function("Manohar")

#a function can return numbers as well
def my_function(in_varname):
    return 10++in_varname

#the input should be a number then
my_function(5)

#a function is not made to retun anything or you don't know then pass
def my_function(in_varname):
    pass

my_function(1)

#we can multiple arguments to the variables. the numbers must match.
def my_function_multiple_var(in_varname1, in_varname2):
    print("Here is the first argument: " +in_varname1+ " and the second var is: "+in_varname2)

my_function_multiple_var("some text 1","some text 2")

#we can pass keyword arguments
#here the order does not matter, only the names must match
def my_function_multiple_key(in_varname1, in_varname2):
    print("Here is the first argument: " +in_varname1+ " and the second var is: "+in_varname2)

my_function_multiple_key(in_varname1="some text 1",in_varname2="some text 2")
my_function_multiple_key(in_varname2="some text 2",in_varname1="some text 1")

#when we don't know how many arguments we can pass then use **kwargs in the parameters
#and now you can add as many as parameters in the code as kwargs["var_name"]
#it doesnt have to be kwargs. it can be any name but kwargs is the standard.
def my_function_multiple(**kwargs):
    print("Here is the first argument: " +kwargs["in_varname1"]+ " and the second var is: "+kwargs["in_varname2"])

my_function_multiple(in_varname1="some text 1",in_varname2="some text 2")
#this will give an error
my_function_multiple(in_varname2="some text 2")

#similar to keywords argumens, we can do arbitrary args also.
#use *args
def my_function_multipleargs(*args):
    print("Here is the first argument: " +args[0]+ " and the second var is: "+args[1])

#now you can pass arguments as list
my_function_multipleargs("some text 1","some text 2")
#this will give an error
my_function_multipleargs("some text 2")
#this will not give an error
my_function_multipleargs("some text 1","some text 2","some text 3")

