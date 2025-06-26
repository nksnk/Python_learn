a=1
b=1
flag=True
def status_check(a,b,flag):
    if a>0 or b>0 and flag==0:
        print("Check condition1",flag)
        return True
    elif a<0 and b<0 and flag==1:
        print("Check condition 2")
        return True
    else:
        return False
show_result=status_check(a,b,flag)
print(show_result)