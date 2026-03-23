''''You are given a space-separated list of integers. Your task is to determine 
if the following two conditions are both met:
Condition 1: All the integers in the list are positive integers ($> 0$).
Condition 2: At least one integer in the list is  a palindromic integer (an integer that reads the same forwards and backwards).
Input Format 
The first line contains an integer $N$, the total number of integers in the list.
The second line contains the $N$ space-separated integers.'''

length = input()
list = input().split()
print(all(int(i) > 0 for i in list) and any(i == i[::-1] for i in list))


