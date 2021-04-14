def recur(start,end,x,atm):
  if start>end or x<0:
    return -1
  elif x==0:
    return 0
  else:
    return min(1+recur(start+1,end,x-atm[start],atm),1+recur(start,end-1,x-atm[end],atm))


def main():
  n=int(input())
  atm=[]
  sumn=0
  for i in range(n):
    h=int(input())
    atm.append(h)
    sumn+=h
  x=int(input())
  if sumn<x:
    print(-1)
  else:
    print(recur(0,n-1,x,atm))


if __name__=="__main__":
  main()
  
