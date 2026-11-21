# for i in range(65,91):
#     if chr(i) == "P":
#         continue
#     print(chr(i), end="1 ")


import time
my_time = int(input("Enter the time in seconds: "))

for x in range(my_time, 0, -1):
    seconds = x % 60
    minutes = int(x / 60) % 60
    hours = int(x / 3600) % 60
    print(f"\r{hours:02d}:{minutes:02d}:{seconds:02d}", end="", flush=True)
    time.sleep(1)
print("Time's up!!!")