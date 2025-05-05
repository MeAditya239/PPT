import xmlrpc.client

# Connect to the server
proxy = xmlrpc.client.ServerProxy("http://localhost:8000/")

# Get input from the user
try:
    num = int(input("Enter a number to compute factorial: "))
    result = proxy.factorial(num)
    print(f"Factorial of {num} is: {result}")
except Exception as e:
    print(f"Error: {e}")
