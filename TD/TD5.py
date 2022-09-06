#TD5
#EXO1


def tri(l) :
    for n in range(len(l)):
        for i in range(len(l)-1):
            print(n,i,i+1)
            if l[i]>l[i+1]: 
                    l[i],l[i+1] = l[i+1],l[i]
    return l

#a = [1,2,5,2,4]
a = [12,3,54,3,4,43,1]


print(a)
tri(a)
print(a)

#question 2 : NON a cause du for n in range(len(l)-2) (il faut enlever le -2 sinon cela vas pas trier tout la liste

#EXO

