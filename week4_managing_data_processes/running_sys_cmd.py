# Obtaining the Output of a System Command

import subprocess

result = subprocess.run(["host", "8.8.8.8"], capture_output=True)

# print(result.returncode)
# return 0

# print(result.stdout)
# b'8.8.8.8.in-addr.arpa domain name pointer dns.google.\n'' # b stands for array of bytes
# This method applies an encoding to transform
# print(result.stdout.decode().split())
# the bytes into a string. By default, it uses a UTF-8 encoding which is what we want. So
# with all that said, let's transform our array of bytes into a string and then split it into several pieces.
['8.8.8.8.in-addr.arpa', 'domain', 'name', 'pointer', 'dns.google.']


'''
So we just looked at the captured standard output. But what about standard error? 
If we use the capture output parameter and the command writes any output to 
standard error, it will be stored in the std or attribute of the completed process 
instance.
'''


result = subprocess.run(["rm", "does_not_exit"], capture_output=True)

# print(result.returncode)  # return 1

# print(result.stderr)  # return b'rm: does_not_exit: No such file or directory\n'
# print(result.stderr.decode().split())
# return  ['rm:', 'does_not_exit:', 'No', 'such', 'file', 'or', 'directory']


# More Advance things we can do with subprocess commands

result2 = subprocess.run(["ls", "-l"])  # doesn't capture output
print(result2)
