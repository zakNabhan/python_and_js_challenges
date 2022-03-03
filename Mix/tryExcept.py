
try:
    print(x)
except NameError:
    print("variable is not defined")
except:
    print("somthing else went wrong")