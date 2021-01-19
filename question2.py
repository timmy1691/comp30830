# beginning of file
# import packages
import timeit
import os
import platform

start = timeit.default_timer()

#begin with the body of the code

# hostname
print("Device Name:", platform.node())

#operating system name
print("Operating System Provider and Version", platform.system(), platform.release())

#cpu count
print("Number of CPUs:", os.cpu_count())

# getting ram
print(os.sys)

end = timeit.default_timer()
print(end - start)