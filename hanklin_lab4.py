# 2026 Fall 95896
# Student: Hank Lin
# Andrew ID: hanklin


'''1. fn. isVowel(c), takes a character c (a str of length one) as a parameter and returns
True if that character's upper case version (convert the parameter to upper case) is an English vowel (A, E, I, O,
or U) and False otherwise. 

The function should do some simple error checking: if c is not a str, return False; if
it is a str but its length is not one, return False. 

Then write a function named testIsVowel( ) that runs hard-coded test cases on isVowel( ); 
it should print True or False for various test values of c. 

For example,
calling isVowel('a') should return true, so running that test in testIsVowel( ) should display True;
calling isVowel('aeiou') should return False.'''


def isVowel(c:str) -> bool:
    if type(c) != str:
        return False
    
    elif len(c) != 1:
        return False
    
    c_upper = c.upper()
    
    if c_upper in ['A','E','I','O','U']:
            return True
    else:
            return False



def testIsVowel() -> None:
    print(isVowel('a'))
    print(isVowel('aeiou'))
    
testIsVowel()



#%%

'''
2. Write a function named countVowels(s) that takes a str parameter s. It should return the number of
vowels (a, e, i, o, u) upper or lower case in the str parameter by calling isVowel() on each character. Test it
with:
print(countVowels('abc123')) # should display 1
print(countVowels('Now is the time')) # should display 5
'''

def countVowels(s:str) -> int:
    
    count = 0
    
    for ch in s:
        if isVowel(ch):
            count += 1
    
    return count


def testcountVowels() -> None:
    print(countVowels('abc123'))
    print(countVowels('Now is the time'))
    
testcountVowels()



#%%
'''
3. Write a function named getVowels(s) that takes a string parameter and uses a list comprehension to
create and return a list containing only the vowels found in the string. The vowels should appear in the same
order as they occur in the original string. '''


def getVowels(s:str) -> list:
    

    vowels = [i for i in s if isVowel(i)]
    
    return vowels
    

def testgetVowels() -> None:
    print(getVowels('AlaskaAirlines'))
    print(getVowels('MakeAmericaGreatAgain'))
    
testgetVowels()


#%%
'''
4. Write a function named toUppercase(words) 
takes a list of strings as a parameter.
Use map() to create and return a new list 
in which every word has been converted to uppercase. Test it with [‘dog’,‘CAt’, ‘mOuSe’].
'''

def toUppercase(words:list) -> list:
    return [word.upper() for word in words]
    
def testtoUppercase() -> None:
    print(toUppercase(['dog','CAt', 'mOuSe']))
    
testtoUppercase()


#%%
'''
5. Write a function named transformNumbers(nums) that takes a list of numbers as a parameter.

Use the map() function together with a lambda expressison 
to create and return a new list 
in which each number is transformed according to the formula 2x + 1, 
where x is the original number.

For example, if nums is [1, 2, 3, 4], the function should return [3, 5, 7, 9]. 
'''


#lambda --> (lambda input: output)(call)
#map --> (function, applied)


def transformNumbers(nums:list) -> list:
    return list(map(lambda x: x * 2 + 1, nums))

def testtransformNumbers() -> None:
    print(transformNumbers([1, 2, 3, 4]))
    
testtransformNumbers()



#%%
'''
6. The file simpleFunctions contains specifications for several functions.
Consider the functions euclid(a,b) and isbn(digits).

Create a file named simplefunctionTests.
Your test cases should be based on the specifications, preconditions, and postconditions given in the document.

For each function, write test cases that demonstrate:
• equivalence partitioning
• boundary testing
• normal cases
Make sure to include at least 5 test cases for each function. Then run the pytest
simpleFunctionTests.py to test the code you wrote. Make sure to import the euclid and isbn
functions in the simpleFunctionTests.py file.
'''




# import os


# os.chdir(r"C:\Users\chihh\OneDrive\...")
# print(os.getcwd())


from simpleFunctions import euclid, isbn

'''euclid'''

'''
pre/postcondition:
    Specification：function purpose
    Precondition：input requirement
    Postcondition: output requirment

validity:
    Normal
    Boundary-valid
    Boundary-invalid
    Equivalence Partition
'''


def test_euclid_normal():
    assert euclid( 30, 12 ) == 6 
    
def test_euclid_coprime():
    assert euclid(5, 7) == 1 

def test_euclid_boundary_valid():
    assert euclid(1, 97) == 1
    
def test_euclid_boundary_invalid():
    assert euclid(0, 97) is None
    
def test_euclid_invalid_a():
    assert euclid(-21, 7) is None

def test_euclid_invalid_b():
    assert euclid(21, -7) is None

def test_euclid_invalid_both():
    assert euclid(-21, -7) is None

test_euclid_normal()
test_euclid_coprime()
test_euclid_boundary_valid()
test_euclid_boundary_invalid()
test_euclid_invalid_a()
test_euclid_invalid_b()
test_euclid_invalid_both()



'''ISBN'''


'''
pre/postcondition:
    Specification：function purpose
    Precondition：input requirement
    Postcondition: output requirment
'''



def test_isbn_normal_valid(): #valid checksum
    assert isbn([0, 3, 0, 6, 4, 0, 6, 1, 5, 2]) is True

def test_isbn_normal_invalid(): #invalid checksum
    assert isbn([0, 3, 0, 6, 4, 0, 6, 1, 5, 3]) is False


def test_isbn_boundary_9(): #9 digits
    assert isbn([0, 3, 0, 6, 4, 0, 6, 1, 5]) is False

def test_isbn_boundary_10(): #10 digits
    assert isbn([0, 3, 0, 6, 4, 0, 6, 1, 5, 2]) is True

def test_isbn_boundary_11(): #11 digits
    assert isbn([0, 3, 0, 6, 4, 0, 6, 1, 5, 2, 9]) is False

test_isbn_normal_valid()
test_isbn_normal_invalid()
test_isbn_boundary_9()
test_isbn_boundary_10()
test_isbn_boundary_11()
























