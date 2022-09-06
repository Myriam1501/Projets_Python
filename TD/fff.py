l=[5,-2,1,2,6,1]
def hop(l):
  y=l[0]
  for x in l:
    if y>abs(x):
      y=abs(x)
    if -y in l:
      y=-y
      
  return y


M = [[0 for j in range(10)] for i in range(10)]

from re import findall
t=(5,6,{(0,0):1,(0,3):3,(2,2):8,(3,0):4})
j=[[1, 0, 0, 3, 0], [0, 0, 0, 0, 0], [0, 0, 8, 0, 0], [4, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]

def d(t):
  M = [[0 for j in range(t[0])] for i in range(t[1])]
  for x,y in t[2].items():
    M[x[0]][x[1]]=y
  return M
s="gvhjk vgbhnjkl   hbdezdjnezjf zef zef e fez fzrjenf cqjl fc fr ej fl    nifbdn djfhs h bjqdh  df djlqhfjddhdjfv f d h cfvgbhnj,k rdftgyhuji fghjk fghj ghjbhc d d d d d ujhzqixdu fgvbhnj, hbjn,k; yguiops etgfdssdf iijij l"

def f(s):
  c=0
  l=[]
  for x in s.split():
    c+=len(x)
    if c<=24:
      l.append(x)
      " ".join(l)
    
  return x
