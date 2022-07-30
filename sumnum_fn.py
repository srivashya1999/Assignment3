data=int(input("Enter the number of elements in the list: "))
lst=[]
for i in range(data):
    value=int(input("Enter the element: "))
    lst.append(value)
print(lst)
def sum(lst):
    total=0
    for num in lst:
        total+=num
    return total
print(sum(lst))