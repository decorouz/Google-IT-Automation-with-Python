import os
print("HOME: " + os.environ.get("HOME", ""))
print("SHELL: " + os.environ.get("SHELL", ""))
# the getMethod allows us to specify a default value when the key that we're looking for isn't in the dictionary
print("FRUIT: " + os.environ.get("FRUIT", ""))

# we define the variable by just setting a value using the equal sign and leaving no spaces in between. Along with this, the export keyword tells a shell that we want the value we set to be seen by any commands that we call.
# export FRUIT = Pineapple
