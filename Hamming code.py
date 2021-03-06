
def calcRedundBits(m):

	for i in range(m):
		if(2**i >= m + i + 1):
			return i
def posRedundBits(data, r):
	j = 0
	k = 1
	m = len(data)
	res = ''
	for i in range(1, m + r+1):
		if(i == 2**j):
			res = res + '0'
			j += 1
		else:
			res = res + data[-1 * k]
			k += 1
	return res[::-1]
def calcParityBits(arr, r):
	n = len(arr)
	for i in range(r):
		val = 0
		for j in range(1, n + 1):
			if(j & (2**i) == (2**i)):
				val = val ^ int(arr[-1 * j])
		arr = arr[:n-(2**i)] + str(val) + arr[n-(2**i)+1:]
	return arr
data = '1110101'
m = len(data)
r = calcRedundBits(m)
arr = posRedundBits(data, r)
arr = calcParityBits(arr, r)
print("Data transferred is " + arr)

