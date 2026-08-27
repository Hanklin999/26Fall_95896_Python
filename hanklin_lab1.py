#Question 1

#a.
#input =  ? miles per hour (mph)
#output = ? meters per second
#with 1 mph = 0.447 m/s
#output format: ‘60.00 mph = 26.82 m/s’

a_input = input("Input Speed:")

a_input_float = float(a_input)

a_convert = a_input_float *  0.447

print(f"{a_input_float:.2f} mph = {a_convert:.2f} m/s")



#b
# obj travel in 10sec with a's speed
# output = "In 10 seconds, the object travels ?.2f meters."

b_dist = a_convert * 10

print(f"In 10 seconds, the object travels {b_dist:.2f} meters.")




#c
#input =  ? in pounds
#output = ? in kilograms
#with 1 pound = 0.4536 kg
#output format: ‘100.00 pounds = 45.36 kg’

c_input = input("Input Weight:")

c_input_float = float(c_input)

c_convert = c_input_float *  0.4536

print(f"{c_input_float:.2f} pounds = {c_convert:.2f} kg")


#d
#input =  ? in kg from c
#output = ? in grams
#with 1 kg = 1000 g
#output format: ‘100.00 kg = 100000.00 g’

d_input = c_convert

d_convert = d_input *  1000

print(f"{d_input:.2f} kg = {d_convert:.2f} g")


#e
# input:  a first name, a favorite food, a hometown
# output: Alex from Pittsburgh likes pizza.

e_name, e_food, e_hometown = input("Input name, food, hometown:").split(",")

print(f"{e_name} from {e_hometown} likes {e_food}.")





#Question 2
with open('gradebook.txt', 'r') as f:
    total = 0
    count = 0
    
    for line in f:
        name, id, grade = line.split(",")
        
        grade = int(grade)
        
        print(f"Name:{name}, ID:{id}, Grade:{grade}")
        
        
        
        
        total += grade
        count += 1
        
avg = total / count
    
print(f"Average: {avg:.2f}")
    



        
#Question 3

sentence = "Assign the string variable sentence as this sentence."

#Display original
print(sentence)

print(sentence.upper())

# returned by splitting sentence on space.
print(sentence.split(" "))

# returned by splitting sentence on 's'.
print(sentence.split("s"))

# find( ) to display the position of 'ten' in sentence.
print(sentence.find('ten'))

# find( ) to display the position of the second 'ten'.
first_index = sentence.find('ten')

print(sentence.find('ten', first_index + len('ten')))


# replace( ) to change all spaces in sentence into tab characters, but assign this to the variable tabby and display it.

tabby = sentence.replace(" ","\t")

print(tabby)














