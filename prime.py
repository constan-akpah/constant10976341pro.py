lower = 10
upper = 100
print("Print the number's from ",lower," and ",upper,".")
for num in range(lower,upper + 1):
  if num > 1:
    for i in range(2, num):
      if (num % i) == 0:
        break
    else:

     print(num)