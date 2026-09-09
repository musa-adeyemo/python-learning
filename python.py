# Conditional Statement
# This is an easier way of writing an IF statement on a line

num = 5
print("Positive" if num >= 0 else "Negative")

score = 80
print("Passed" if score >= 50 else "Failed")

a = 5
b = 9

max_num = a if a > b else b
min_num = a if a < b else b

print(min_num)
print(max_num)

temp = 30

weather_status = "High" if temp > 27 else "Low"

print(weather_status)