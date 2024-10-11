def majority_wins(arr,x,y):
        x_counter = 0
        y_counter = 0
        for e in arr:
            if e==x:
                x_counter+=1
            elif e==y:
                y_counter+=1
        if x_counter>y_counter:
            return x
        elif y_counter>x_counter:
            return y
        elif x_counter==y_counter:
            return x if x<y else y
    
arr = [1,2,3,4,5,6,7,8]#[1,1,2,2,3,3,4,4,4,4,5]
x=1
y=7
print(majority_wins(arr,x,y))