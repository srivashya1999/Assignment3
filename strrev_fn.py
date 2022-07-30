data=input("Enter a string to reverse it: ")
def rev(data):
    temp=''
    for char in data:
        temp=char+temp
    return temp
print("The output is: ",rev(data))