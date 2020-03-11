def fatorial(num):
  if num <= 1:
    return num
  return num * fatorial(num - 1)

print(fatorial(5))

def somatorio(num):
  if num <= 1:
    return num
  return num + somatorio(num - 1)

print(somatorio(5))

def fibonacci(num):
  if num <= 1:
    return num
  return fibonacci(num-1) + fibonacci(num-2)

print(fibonacci(6))

def somatorioJK(j,k):
  if j == k:
    return j
  if j < k:
    return j + somatorioJK(j+1,k)
  else:
    return j + somatorioJK(j-1,k)

print(somatorioJK(3,1))

def isPal(s):
  if s is None:
    return False
  if len(s) < 2: return True
  if s[0] != s[-1]: return False
  return isPal(s[1:-1])

print(isPal("renner"))

def convBase2(num):
  if num == 0:
    return '0'
  return convBase2(num//2) + str(num%2)
  

print(convBase2(2))

def somatorioArray(arr):
  if len(arr) == 1:
    return arr[0]
  if len(arr) == 0 or arr is None:
    return 0
  return arr[0] + somatorioArray(arr[1::])
  

print(somatorioArray([3,4,5]))

def findBiggest(arr):
  print(arr)
  if len(arr) == 1:
    return arr[0]
  if arr[0] > arr[-1]:
    return findBiggest(arr[::-1])
  else:
    return findBiggest(arr[1::])
  

print(findBiggest([3,111,5]))

def findSubStr(s, match):
  print(s[0:len(match)])
  if len(match) > len(s) or len(s) == 0:
    return False
  if s[0:len(match)] == match:
    return True

  return findSubStr(s[1::], match)
  

print(findSubStr("banana", "na"))

def nroDigit(num):
  if num < 10:
    return 1
  return 1 + nroDigit(num/10)

print(nroDigit(1))