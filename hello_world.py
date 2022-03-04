t_list = [5,10,1,12,3,8,20,14]

def mex(a,b):
    if a>b:
        resurt = a
    else :
        resurt = b
    return resurt

l_mex = t_list[0]
for i in range(len(t_list)):
    l_mex = mex(l_mex,t_list[i])
    if l_mex==t_list[i]:
        c = i
print(c)