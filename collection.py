import time

fruits = ["pineapple","Mango","Apple","Orange","Banana"]
format(fruits)

for fruit in fruits:
    print(f"\r{fruit}", end="", flush=True)
    time.sleep(1)