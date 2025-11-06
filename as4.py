raws =int(input("Enter number of raws: "))
for i in range(1, raws + 1):
    print('* ' * i)

#######################
num = 1
while num <= 100:
    for i in range(10):
        print(f"{num:3}", end=" ")
        num += 1
    print()
########################
for x in range(3,10):
    for y in range(2,5):
        print(f"x ={x} y ={y} x^2-^2={x**2-y**2}", end=" ")
        print()
########################
while True:
    guess = int(input("Enter a number (0 to stop): "))
    if guess == 0:
        print("Game over!")
        break
    else:
        print("You entered:", guess)
########################
def find (lst ,num):
    if num in lst:
        return True
    else:
        return False
my_list = [10, 20, 30, 40, 50]
number = int(input("Enter a number to search: "))
if find(my_list, number):
    print(f"{number} is found in the list.")
else:
    print(f"{number} is not found in the list.")
########################
def drawBlocks(size):
    for i in range(size):
        print("# " * size)

n = int(input("Enter size: "))
drawBlocks(n)
########################
start = int(input("Enter start: "))
end = int(input("Enter end: "))

print("Prime numbers between", start, "and", end, ":")

for num in range(start, end + 1):
    if num > 1:
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                break
        else:
            print(num)
#########################
names = []
grades = []

# ناخد بيانات 3 طلاب
for i in range(3):
    name = input(f"Enter name of student {i+1}: ")
    grade = float(input(f"Enter grade of {name}: "))
    names.append(name)
    grades.append(grade)

# نعرض النتايج
print("\nStudents and their grades:")
for i in range(3):
    print(f"{names[i]}: {grades[i]}")
#########################
numbers = []

for i in range(5):
    num = float(input(f"Enter number {i+1}: "))
    numbers.append(num)

average = sum(numbers) / len(numbers)
maximum = max(numbers)

print("\nAverage =", average)
print("Maximum =", maximum)
#########################
list1 = [1, 2, 3]
list2 = [2, 3, 4]

for a in list1:
    for b in list2:
        if a == b:
            print(f"({a},{b})")
#########################
sentence = input("Enter a sentence: ").lower()
vowels = "aeiou"
count = 0

for char in sentence:
    if char in vowels:
        count += 1

print("Number of vowels:", count)
#########################
email = input("Enter your email: ")

if "@" in email and email.endswith(".com"):
    print("Valid email")
else:
    print("Invalid email")
