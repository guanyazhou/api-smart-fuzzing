import socket

print "Hello World! I'm a Python program\n"
x = socket.getfqdn()
print "The local host's name is: " + x + "\n"
print "If you saw this message, the Python interpreter"
print "is installed and the standard library works!"
print "Bye now!"