# Break statement example
for num in range(1, 10):
    if num == 5:
        print("Breaking the loop at:", num)
        break
    print(num)
    
'''OUTPUT:
1
2
3
4
Breaking the loop at: 5'''

count = 0
while count < 10:
    count += 1
    if count == 3:
        continue  # skip printing 3
    if count == 8:
        break     # stop the loop when count is 8
    print(count)
    
'''OUTPUT:
1
2
4
5
6
7'''
