from sys import getsizeof

bytes_size = getsizeof(3**9090001)
megabytes_size = bytes_size/(1024**2)
print(megabytes_size)
