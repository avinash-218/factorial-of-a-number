def main():
 p=1
 n=eval(input("Enter a number\n"))
 p=fact(n)
 print(p)



def fact(n):
 if n==0:
  return 1
 else:
  return n*fact(n-1)

main()
