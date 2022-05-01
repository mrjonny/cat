def tokenfind():
 c=1
 print("Enter the Number of Packets:")
 p=int(input())

 while (p > 0):
        print("Enter the Number of Tokens:")
        t = int(input())
        if (t == 0):
           print("No Packets can be sent")
           break
        print("Enter the number of seconds:")
        sec = int(input())
        for i in range(0,t):
           p=p-1
           if (p >= 0):
                print(c," Packets Sent .....")
                c=c+1
                print("Sleep(",sec,")")

           if (p <= 0):
               print("All packets Sent Succesfully")


tokenfind()
