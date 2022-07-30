def uprlwr():
  data=input("Enter a string: ")
  lowr=0
  upr=0
  for i in data:
     if(i.islower()):
      lowr=lowr+1
     elif(i.isupper()):
      upr=upr+1
  print("The number of lowercase characters is:",lowr)
  print("The number of uppercase characters is:",upr)
uprlwr()
