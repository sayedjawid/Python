magicians = ['alice', 'david', 'carolina']

for magician in magicians:
    print(f'{magician.title()}, that was a great trick!')
    print(f"I can't wait to see your next trick, {magician.title()}.\n")

print('Thank you everyone. That was a great magic show!')


print("=======================================================================")



numbers = list(range(1, 6))
print(numbers)

print("=======================================================================")


squares = []
for value in range(1, 11):
    square = value ** 2
    squares.append(square)
print(squares)

print("=======================================================================")



squares = []
for i in range(1,11):
    i = i ** 2
    squares.append(i)
print(squares)

print("=======================================================================")




squares = [value ** 2 for value in range(1, 11)]
print(squares)

print("=======================================================================")



for number in range(1, 21):
    print(number, end=" ")
print("=======================================================================")



squares = [value ** 2 for value in range(1, 11)]
print(squares)

print("=======================================================================")


value = [i for i in range(1,21)]
print(value)

print("=======================================================================")


one_million = [i for i in range(1, 1_000_001)]
print(f'First 10 values: {one_million[:10]}')
print(f'Last 10 values: {one_million[-10:]}')
print(f'Total number: {len(one_million)}')

print("=======================================================================")



import time

start = time.time()

numbers = [i for i in range(1, 1_000_001)]
total = sum(numbers)

end = time.time()

print(f'Min value in this list is: {min(numbers)}')
print(f'Max value in this list is: {max(numbers)}')
print(f'The sum of this list is: {sum(numbers)}')
print(f'Calculation time: {end - start:.5f} seconds')

print("=======================================================================")




numbers = [num for num in range(1, 21) if num % 2 != 0]
print(f'These are odd numbers: {numbers}')

print("=======================================================================")

numbers = [num for num in range(3, 31) if num % 3 == 0]
print(f'Threes list: {numbers}')

print("=======================================================================")


numbers = []
for num in range(3, 31):
    if num % 3 == 0:
        numbers.append(num)
print(f'Threes list: {numbers}')

print("=======================================================================")


cubes = [num ** 3 for num in range(1, 11) ]
print(f'The Cube pwer to 3: {cubes}')

print("=======================================================================")

cubes = [num ** 3 for num in range(1, 11) ]
print(f'The Cube pwer to 3: {cubes}')