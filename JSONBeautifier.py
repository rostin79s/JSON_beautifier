import time

b=[]
l=[]
error=False



def balanced(myStr):
    stack = []
    open_list = ["[","{","("]
    close_list = ["]","}",")"]
    for i in myStr:
        if i in open_list:
            stack.append(i)
        elif i in close_list:
            pos = close_list.index(i)
            if ((len(stack) > 0) and
                (open_list[pos] == stack[len(stack)-1])):
                stack.pop()
            else:
                return "Unbalanced"
    if len(stack) == 0:
        return "Balanced"
    else:
        return "Unbalanced"



def check(n,indent):
    global error
    global l
    if n=="null":
        l.append(f'{" "*indent}None')
    elif n=="true":
        l.append(f'{" "*indent}True')
    elif n=="false":
        l.append(f'{" "*indent}False')
    elif n=="[]":
        l.append(f'{" "*indent}[]')
    elif n=="{}":
        l.append(f'{" "*indent}{{}}')
    
    else:
        if n[0]=="'":
            error=True
        elif n[0]=='"':
            l.append(f'{" "*indent}{n}')
            if n[-1]!='"':
                error=True
            return 1
        else:
            try: 
                float(n)
            except ValueError:
                error=True
            l.append(f'{" "*indent}{n}')
    return 0




def json(n,indent):
    global b
    global l
    global error
    bracket=0 ; curly=0 ; i=0 ; temp=[] ; colon=1
    if n[i]!='[' and n[i]!='{':
        check(n,0)
        return
    while i<len(n):
        if n[i]=='[':
            b.append('[')
            if n[i+1]!=']':
                bracket+=1
                l.append(f'{" "*indent*colon}[\n')
                indent=(bracket+curly)*2
            else:
                b.append(']')
                l.append(f'{" "*indent*colon}[]')
                i+=1
            colon=1


        elif n[i]=='{':
            b.append('{')
            if n[i+1]!='}':
                curly+=1
                l.append(f'{" "*indent*colon}{{\n')
                indent=(bracket+curly)*2
            else:
                b.append('}')
                l.append(f'{" "*indent*colon}{{}}')
                i+=1
            colon=1


        elif n[i]==']':
            b.append(']')
            bracket-=1
            if temp!=[]:
                check(''.join(temp),indent)
            l.append('\n')
            indent=(bracket+curly)*2
            l.append(f'{" "*indent}]')
            temp=[]


        elif n[i]=='}':
            b.append('}')
            curly-=1
            if temp!=[]:
                check(''.join(temp),indent*colon)
            l.append('\n')
            colon=1
            indent=(bracket+curly)*2
            l.append(f'{" "*indent}}}')
            temp=[]



        elif n[i]==',':
            if temp!=[]:
                check("".join(temp),indent*colon)
            colon=1
            l.append(',\n')
            temp=[]

        elif n[i]==':':
            x=check("".join(temp),indent)
            if x!=1:
                error=True
                return
            l.append(': ')
            colon=0
            temp=[]

        else:
            if n[i]!=" ":
                temp.append(n[i])
        i+=1

        if bracket==0 and curly==0:
            break

    # if temp!=[]:
    #     check(''.join(temp),0)

    res=balanced(''.join(b))
    if res=="Unbalanced":
        error=True
        


# f=open('09.txt','r')
# n=f.read()
n=input()
n=n.strip()
# start_time = time.time()
# f.close()
json(n,0)
if error==True:
    print('---')
else:
    print("".join(l))

# print("--- %s seconds ---" % (time.time() - start_time))