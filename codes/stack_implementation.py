def MakePush(Package):
    element=input("Enter Package: ")
    Package.append(element)
    print("Element Added Succefully")
    menu()

def MakePop(Package):
    if Package==[]:
        print("Empty Stack")
    else:
        print(f"Popped Element: {Package.pop()}")
    menu()

def Display(Package):
    for i in Package[::-1]:
        print(i)
    menu()
    
Package_stack=["Pkg_1","Pkg_2"]

def menu():
    print("1) Push element")
    print("2) Pop element")
    print("3) Display Stack")
    print("4) Exit")
    choice=int(input("Enter your choice: "))
    if choice==1:
        MakePush(Package_stack)
    elif choice==2:
        MakePop(Package_stack)
    elif choice==3:
        Display(Package_stack)
    elif choice==4:
        quit()
menu()