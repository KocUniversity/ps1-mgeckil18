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

while formulaTime*T <= B:
  T += 1
# please do not modify the input and print statements
# and make sure that your code does not have any other print statements
print(T)