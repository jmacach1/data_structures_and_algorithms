
def sumToN(num):
  mySum = 0
  for i in range(1, num + 1):
    mySum += i
  return mySum

print(sumToN(10))