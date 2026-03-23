_ = input() # Line 1: Consume the N
n = input().split() # Line 2: Get the list of strings
print(all(int(i) > 0 for i in n) and any(i == i[::-1] for i in n)) # Line 3: The Logic