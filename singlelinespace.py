'''
3) Write a program to get the tuple elements in a single line separated by spaces and print the number of elements in the given tuple.
Sample Input:
10 20 30
Sample Output:
3
program:
# Input: Read the tuple elements as a single line of space-separated integers
elements = tuple(map(int, input().split()))

# Output: Print the number of elements in the tuple
print(len(elements))
'''
