

from binhex import FInfo


LIKED_ITEMS = {}
DISLIKED_ITEMS = {}
FINAL_LIST=[]
def input_func (l,dl):
    liked_items = l.split(' ')
    del liked_items[0]
    
    disliked_items = dl.split(' ')
    del disliked_items[0]
    
    for i in liked_items:
        if i not in LIKED_ITEMS:
            LIKED_ITEMS[i]=1
        elif i in LIKED_ITEMS:
            LIKED_ITEMS[i]+=1
    for i in disliked_items:
        if i not in DISLIKED_ITEMS:
            DISLIKED_ITEMS[i]=1
        elif i in DISLIKED_ITEMS:
            DISLIKED_ITEMS[i]+=1
def main():
    n=int(input()) # The Number of Entries
    for i in range(n):
        l=input()
        dl=input()
        input_func(l,dl)
    for j in LIKED_ITEMS.keys():
        if j not in DISLIKED_ITEMS:
            if j not in FINAL_LIST:
                FINAL_LIST.append(j)
            elif j in FINAL_LIST:
                continue  
                    
        elif j in DISLIKED_ITEMS:
            
            
            if LIKED_ITEMS[j] > DISLIKED_ITEMS[j]:
                FINAL_LIST.append(j)
            elif j in FINAL_LIST:
                continue
        else:
            continue                
    print(len(FINAL_LIST),end=" ")
    for i in range(len(FINAL_LIST)):
        print(FINAL_LIST[i],end=' ')
    print()
main()
