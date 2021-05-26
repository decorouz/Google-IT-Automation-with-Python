import os
import subprocess

'''
So in this code, we start by calling the copy method of the OS environ dictionary 
that contains the current environment variables.
Calling 'copy' method of the os.environ dictionary will copy the current environment 
variables to store and prepare a new environment.
'''

my_env = os.environ.copy()


'''
This creates a new dictionary that we can change as needed without modifying 
the original environment. The change that we're doing in this script is adding 
one extra directory to the path variable.
'''

my_env["PATH"] = os.pathsep.join(["/opt/myapp/", my_env["PATH"]])

result = subprocess.run(["myapp"], env=my_env)


'''
If we're automating a one-off, well-defined task, we're developing a solution 
quickly is the biggest requirement, then using system commands and subprocesses can help a lot.
'''
