test = [1,2,3,5,6,7,78]
print(test[-1:-4:-1])
test[0],test[-1] = test[-1],test[0]
print(test)