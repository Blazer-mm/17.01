teksts = input("ievadi ciparus: ")
def Countnumbers(teksts):
  summa = 0
  for simbols in teksts:
    summa = summa + int(simbols)
  print(summa)
  return summa
Countnumbers(teksts) 