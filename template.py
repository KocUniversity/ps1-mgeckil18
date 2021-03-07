n, B = list(map(int, input().strip().split()))
T = 0
# your code here
i = 1
formulaTime = 0
for i in range(n):
  if i%2 == 0:
    formulaTime += ((2**i + 1)**(n-i))
  elif i%2== 1 :
    formulaTime += ((3**i + 1)**(n-i))  
floor = 0
ceil = 1000
guess = (floor + ceil)/2
while formulaTime*T =! B:
  T = guess
  if formulaTime*T < B:
    floor = guess
  elif formulaTime > B:
    ceil = guess  

  
# please do not modify the input and print statements
# and make sure that your code does not have any other print statements
print(T)