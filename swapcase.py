def swap_case(s):
    listt=list(s)
    for i in range(len(listt)):
        if listt[i]==listt[i].upper():
            listt[i]=listt[i].lower()
        else:
            listt[i]=listt[i].upper()
    x=("").join(listt)
    return(x)        
    
if __name__ == '__main__':
