n = int(input("Enter a row"))
for x in range(0,9):
  # if (x==0):
  #   pass
    # for i in range(0,n):
    #   for j in range(0,i+1):
    #     print(end=" ")
    #   for j in range(0,n-i):
    #     print("*",end=" ")
    #   print()
  # else:
    for i in range(0,n):
      for j in range(0,n-i):
        print(end=" ")
      for j in range(0,i+1):
        print("*",end=" ")
      print()