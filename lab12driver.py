# 2026 Fall, 95896-A
# Student Name: Hank Lin
# Andrew ID: hanklin

'''1 Create a function named problem1() that does the following: prompt the user to enter a day of the week, a
String. If their entry is invalid, print the error message “Bad day entered”; otherwise, print their entry and “Nice
job!”. To tell if the entry is invalid, use this: if entry not in BadWeekday.WEEKDAYS.
Call problem1() from main().'''


from badWeekday import BadWeekday

def problem1() -> None:
    entry = input("Enter a day of the week")
    
    try:
        if entry not in BadWeekday.WEEKDAYS:
            raise BadWeekday
        print(entry)
        print("Nice job!")
    except:
        print("Bad day entered")
    

#def main():
#    problem1()
    


#if __name__ == "__main__":
#    main()



#%%

'''2. Create a function named problem2() that does essentially the same thing as problem1()with these
changes: if the entry is invalid, throw a new BadWeekday exception with the message “Bad day entered” –
don’t print an error message; if it’s valid, print “Nice job”. Call problem2() from main().
Wrap the call in a try/except block.
'''

def problem2() -> None:

    entry = input("Enter a day of the week")
    
    if entry not in BadWeekday.WEEKDAYS:
        raise BadWeekday("Bad day entered")
    print("Nice job!")
    
    

#def main():
#    try:
#        problem2()
#    except Exception as e:
#        print(e)
    


#if __name__ == "__main__":
#    main()



#%%
'''Create a method named problem3( ) that calls problem2() – add a try-catch block around the call. 
'''

def problem3() -> None:
    try:
        problem2()
    except Exception as e:
        print(e)
    #else:
    #    print("Error Shown but not in Exceptions")

#def main():
#    problem3()

#if __name__ == "__main__":
#    main()
    
        

#%%
'''
 Create a function named problem4() that calls problem2() but does not catch the exception. Call
problem4() from main() and surround that call with a try/except block. Print the exception message.
Notice that the exception is passed from problem4() to main().
'''


def problem4() -> None:
    problem2()
    
#def main():
#    try:
#        problem4()
#    except BadWeekday as e:
#        print(e)
    
#if __name__ == "__main__":
#    main()


#%%
'''
5. Create a function named problem5() that calls problem2() using a try/except block. Inside the
except block, print “Caught “ and the exception. Re-raise the exception using raise. Call problem5() from
main(). Wrap the call in another try/except block so the exception is caught a second time.
Observe the order in which the messages are printed.
'''


def problem5() -> None:
    try:
        problem2()
        
    except BadWeekday as e:
        print("Caught",e)
        raise 

#def main():
#    try:
#        problem5()
#    except BadWeekday as e:
#        print(e)
    
#if __name__ == "__main__":
#    main()


#%%
'''
6. Create a function named problem6() that calls problem2() and does not catch the exception. Call
problem6() from main() without a try/except block. Run the program. How is this different from
Problem 4?
'''

def problem6() -> None:
    problem2()

#def main():
#    problem6()

#if __name__ == "__main__":
#    main()

# Problem 6 differs from Problem 4 because the exception is not caught
# by problem6() or main(). Therefore, the exception propagates to the top
# level and the program terminates with a traceback.

def main():

    print("Problem 1")
    problem1()
    print()

    print("Problem 2")
    try:
        problem2()
    except BadWeekday as e:
        print(e)
    print()

    print("Problem 3")
    problem3()
    print()

    print("Problem 4")
    try:
        problem4()
    except BadWeekday as e:
        print(e)
    print()

    print("Problem 5")
    try:
        problem5()
    except BadWeekday as e:
        print(e)
    print()

    print("Problem 6")
    problem6()
    print()


if __name__ == "__main__":
    main()







