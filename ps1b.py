n, B = list(map(int, input().strip().split()))
T = 0
# your code here
i = 1
formulaTime = 0
while i <= n :
  if i%2 == 0:
    formulaTime += ((2**i + 1)**(n-i))
  elif i%2== 1 :
    formulaTime += ((3**i + 1)**(n-i))  
  i += 1  
floor = 0
ceil = 10000
T = (floor + ceil ) /2
while formulaTime*(T -1)> B   or formulaTime*T <  B:
  if formulaTime*(T-1) > B:
    ceil = T
    if (floor + ceil)%2==0:
      T = (floor + ceil)/2    
    elif (floor+ceil)%2 ==1:
      T = (floor + ceil + 1)/2 
  elif formulaTime*T < B:
    floor = T
    if (floor + ceil)%2==0:
      T = (floor + ceil)/2    
    elif (floor+ceil)%2 ==1:
      T = (floor + ceil + 1)/2
  
# please do not modify the input and print statements
# and make sure that your code does not have any other print statements
print(T)