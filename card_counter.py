# There are n cards laid out in a row on the table, each card has a natural number written on it. 
# In one move, you are allowed to take a card from either the left or the right end of the row. 
# You can make a total of k moves. 
# The final score is equal to the sum of the numbers on the chosen cards. 
# Determine what maximum score you can get at the end of the game.

#Let's solve the task using the prefix sum.

n = int(input())
k = int(input())
numbers = list(map(int, input().split()))

left_prefix_sum = [0 for i in range(k+1)]
right_prefix_sum = [0 for i in range(k+1)]
max_score = 0

for i in range(1, k + 1):
	left_prefix_sum[i] = left_prefix_sum[i-1] + numbers[i-1]
	right_prefix_sum[i] = right_prefix_sum[i-1] + numbers[-i]

for i in range(k+1):
	max_score = max(max_score, left_prefix_sum[i] + right_prefix_sum[-1 - i])

print(max_score)