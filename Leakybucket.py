storage=0
queries=5
bucket_size=10
input_pktsize=4
output_pktsize=1
i=0

for i in range(0,queries):
     size_left=bucket_size-storage
     if (input_pktsize <= (size_left)):
        storage += input_pktsize
        print(storage,bucket_size,size_left)
     else:
        print("Packet loss =",(input_pktsize-(size_left)))
        storage=bucket_size
        print("Buffer size= ",storage,",out of bucket size= ",bucket_size)

        storage -= output_pktsize
