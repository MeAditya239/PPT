from xmlrpc.server import SimpleXMLRPCServer

# Function to concatenate two strings
def concatenate(s1, s2):
    return s1 +" "+s2

# Create server
server = SimpleXMLRPCServer(("localhost", 8000))
print("RPC Server listening on port 8000...")

# Register the function
server.register_function(concatenate, "concatenate")

# Run server
server.serve_forever()
