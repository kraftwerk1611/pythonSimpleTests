###Friz Buzz problem for interview practice
##
##for num in range(1,101):
##    if num%5 ==0 and num%3 ==0:
##        print ("Fizz Buzz")
##
##    elif num%3==0:
##        print ("Fizz")
##
##    elif num%5==0:
##        print("Buzz")
##
##    else:
##        print(num)

print("#"*40)

#Implementing Frizbuzz using list comprehension

print(['fizzbuzz' if not x%5 and not x%3 else 'fizz' if not x%5 else 'buzz' if not x%3 else x for x in range(1,101)])


print("#"*40)
 
###And following is an implementation of Fibonacci
##
##a,b=0,1
##for i in range(0,10):
##    print(a)
##
##    a,b=b,a+b

print("#"*40)

'''implenting Fibonacci using Generator. You could also think of as replacement of callback mechanism
. In some situations you want a function to do a lot of work and occasionally report back to
the caller. Traditionally you'd use a callback function for this. You pass this callback to the
work-function and it would periodically call this callback. The generator approach is that the
work-function (now a generator) knows nothing about the callback, and merely yields whenever it
wants to report something. The caller, instead of writing a separate callback and passing that
to the work-function, does all the reporting work in a little 'for' loop around the generator.
'''

###worker function
##def fib(num):
##    a,b=0,1
##    for i in range(0,num):
##        yield "{}: {} ".format(i+1,a)
##        a,b=b,a+b
##        
###caller function/code
##for item in fib(10):
##    print (item)

print("#"*40)

'''Another Fibonacci example with Generators. n this example, if using the generator version,
the whole 1000000 item list won't be created at all, just one value at a time.
That would not be the case when using the list version, where a list would be created first.
generator version
'''

#worker function
##def fibon(n):
##    a = b = 1
##    for i in range(n):
##        yield a
##        a, b = b, a + b
##
###caller function
##for x in fibon(100):
##    print(x) 

print("#"*40)


###List comprehension example
##
##my_list=[1,2,3,4,5,6,7,8,9,10]
##print (my_list)
##squares=[num*num for num in my_list]
##print (squares)
##

print("#"*40)
