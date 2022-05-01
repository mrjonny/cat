def bitStuffing(N, arr):
    brr = [0 for _ in range(30)]
    k = 0
    i = 0
    j = 0
    count = 1
    while (i < N):
        if (arr[i] == 1):
            brr[j] = arr[i]
            k = i + 1
            while True:
                if not (k < N and arr[k] == 1 and
                        count < 5):
                    break
                j += 1
                brr[j] = arr[k]
                count += 1
                if (count == 5):
                    j += 1
                    brr[j] = 0
                i = k
                k += 1
        else:
            brr[j] = arr[i]
        i += 1
        j += 1
    for i in range(0, j):
        print(brr[i], end=" ")

if __name__ == "__main__":

    arr = []
    N = int(input("Number of elements in array:"))
    print("enter the bits")
    for i in range(0, N):
        l = int(input())
        arr.append(l)
   #arr=[1,1,1,1,1,1]
   #n=5

    bitStuffing(N, arr)