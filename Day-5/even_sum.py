#Write your code below this row 👇

all_even_nums = []

for i in range(1,101):
    if i % 2 == 0:
        all_even_nums.append(i)

even_sum = 0    
for num in all_even_nums:
    even_sum += num

print(even_sum)
