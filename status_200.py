# You are given an array of natural numbers Ai.
# Find the number of such pairs of elements (Ai, Aj),
# where |Ai - Aj| % 200 == 0 and i < j

# Let's rewrite the condition as Ai % 200 == Aj % 200, and find the number of such pairs.

n = int(input())
numbers = sorted(list(map(lambda x: int(x) % 200, input().split()))) 

pairs_counter = 0
num_counter = 1 
num = numbers[0]

for i in range(1, n): 
	# Let's find the number of numbers satisfying the condition Ai % 200 == Aj % 200
	if numbers[i] == num:
		num_counter += 1
	else: 
		# And find the number of pairs
		pairs_counter += num_counter * (num_counter - 1) // 2 
		# And reset the number counter
		num_counter = 1
		num = numbers[i]

pairs_counter += num_counter * (num_counter - 1) // 2
print(pairs_counter)