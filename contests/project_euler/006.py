import math

n = int(input())

Sum_of_squares = sum([i*i for i in range(1, n + 1)])
Square_of_the_sum = (n * (n + 1) // 2)**2

print(Square_of_the_sum - Sum_of_squares)
