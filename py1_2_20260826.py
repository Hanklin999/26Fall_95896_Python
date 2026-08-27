
# Python String: type --> str
 
'''escape character \ instead:'''
word = 'My dog\'s fleas are terrible'
# or:
word = "My dog\"s fleas are terrible"



'''slicing'''
word = 'Gopher' # word[0] is 'G', word[1] is 'o', etc.
word[2] # 'p'
word[0] # 'G'
word[6] # Error
word[-1] # 'r'; negatives count from the back
word[-2] # 'e'
word[-6] # 'G'


'''split'''
word = 'Bob,Smith,27' # CSV employee record
print(word.split(',')) # prints ['Bob', 'Smith', '27'] (a list)
first = word.split(',')[0] # first is 'Bob'
first, last, age = word.split(',') # first is 'Bob',
# last is 'Smith',
# age is '27' (a string)

word = 'How now brown cow'
a = word.split( ) # a is ['how', 'now, 'brown', 'cow']
# - see list notes
b = 'X'.join(a) # b is 'howXnowXbrownXcow' :
# uses 'char' as separator

word = ' Bob, Smith, 27 '# CSV employee record with spaces
first, last, age = word.split(',')
# first is ' Bob', last is ' Smith',
# age is ' 27' (a string)
print(first.strip()) # prints'Bob',doesn't change first
first = first.strip( ) # changes first to 'Bob'


'''Replace string'''
word = 'Gopher'
print(word.replace('o', 'a')) # prints 'Gapher'
print(word) # prints 'Gopher'
# Again, reassign the string if that's your intention
word = word.replace('o', 'a') # 他會做一個 新的string 而非改舊的
print(word) # prints 'Gapher'


'''find in sting'''
first = 'Sebastian'
print('ast' in first) # prints True
print('beast' in first) # prints False

word = 'Hello in there'
i = word.find('in')
print(i) # prints 6

# str.find( keystring, startingIndex)
# str.find(keystring, startingIndex, endingIndex)
i = word.find('in', 7, 10)
# i is -1: not found between 7 and 10


'''input'''
word = input( ) # Say the user types Gopher, no quotes
print(word) # prints 'Gopher'

age = input('Enter your age: ') # User enters 25
print(age) # prints '25'
print(type(age)) # prints <class 'str'>
age = int(age) # change its type to int
print(age) # prints 25
print(type(age)) # prints <class 'int'>



'''output'''
name = 'Bob'
age = int(input('Enter age: ')) # User enters 25
print(name, 'is', age, 'years old')

'''
displays:
    Bob is 25 years old
    Notice that it put spaces between each part
'''


'''output with seperater'''

'''By default, print( ) uses \n
    To change this, use the named parameter end='<whatever>'
    sep = '<whatever>' is also available as field separator'''
    


'''OUTPUT Formating'''
'''f-sting
f'some string {variable:format}'''

sum = 100
n = 6
average = sum/n
print(f'Sum = {sum} N = {n} Average = {average}')
# System decides on format
# Prints: Sum = 100 N = 6 Average = 16.666666666666668


'''C style
• Use %<letter>, where <letter>'''


'''String templates

< , >, ^ mean left-aligned, right-aligned, and centered, resp., inside a
field
• + to force a sign on numbers; - for negative sign on negative numbers
• use : instead of %
• :<char> uses that char as a fill character
• use { } or {some number} to specify which expressions go where
• .format(expressions) to specify the expressions
• Again, always use print( ) in programs

'''













































