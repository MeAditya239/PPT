from xmlrpc.server import SimpleXMLRPCServer

# Define the factorial function
def factorial(n):
    if n < 0:
        return "Invalid input: Negative number"
    elif n == 0 or n == 1:
        return 1
    else:
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result

# Create server
server = SimpleXMLRPCServer(("localhost", 8000))
print("RPC Server listening on port 8000...")

# Register the factorial function
server.register_function(factorial, "factorial")

# Run the server
server.serve_forever()
