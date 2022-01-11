number = input('input: \n')
number1 = input('input: \n')
numberc = input('input: \n')


numbers = {
    "one": 1,
    "two": 2,
    "three":  3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
    "zero": 0,
}

test = number.split()
tester = number1.split()
testing = numberc.split()

j=0
first = []
while j<len(test):
    
    first.append(numbers[test[j]])

    j+=1

k=0
second = []
while k<len(test):
    
    second.append(numbers[tester[k]])

    k+=1

l=0
third = []
while l<len(test):
    
    third.append(numbers[testing[l]])

    l+=1

string1=""
string2=""
string3=""

for t in first:
    string1 = str(string1) + str(t)

for y in second:
    string2 = str(string2) + str(y)
    
for u in third:
    string3 = str(string3) + str(u)
    
x = int(string1)
y = int(string2)
z = int(string3)

array = [x,y,z]


def do():
    i=0
    
    temp2=0
    while i<len(array):

        temp2 = temp2+int(array[i])
        i+=1
    print(temp2)

x=input("ready?")
if x == 'yes':
    do()
