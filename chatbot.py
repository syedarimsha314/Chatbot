import aiml

# Create the kernel and learn AIML files
kernel = aiml.Kernel()
kernel.learn("interrogative.aiml")
# Press CTRL-C to break this loop
while True:
    userinput = input("Enter your message >>")
    output = kernel.respond(userinput)
    print(output)