import time
# for i in range(1, 1000):
#      time.sleep(1)
#     print(i)

for i in range(100):
    print("I love to code.")

for number in range(65, 91):
     if number == 70:
          continue
     print(chr(number), end=" ")
print()

fruits = ["Apple", "Banana", "Mango"]
fruit = ("Apple", "Banana", "Mango")
for i in fruits:
     print("I love", i)
for i in fruit:
     print("The fruit name is", i)

for i in range(1, 11):
     print(f"7 * {i} = {7 * i}")

for i in range(1, 7):
     print(f"{'*' * i:<6}".strip())

email = ["dammy@gmail.com", "musa@gmail.com", "musa;gmail.com"]
for i in email:
     if i.find("@") == -1:
          continue
     print(i)