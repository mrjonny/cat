print('Enter a number:')
n = int(input())
n = bin(n)

c = n.count('1')
print(n[2:])

if(c%2==0):
    print('even')
else:
    print('odd')