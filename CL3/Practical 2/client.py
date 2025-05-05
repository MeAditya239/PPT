import xmlrpc.client

# Connect to server
proxy = xmlrpc.client.ServerProxy("http://localhost:8000/")

# Input strings
str1 = input("Enter first string: ")
str2 = input("Enter second string: ")

# Call remote method
result = proxy.concatenate(str1, str2)

print("Concatenated result:", result)
