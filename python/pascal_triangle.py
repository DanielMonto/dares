def main(limit=10, show_all=True):
    triangle=[]
    for level in range(limit):
        if level==0:
            triangle.append([1])
        elif level==1:
            triangle.append([1,2,1])
        else:
            prev_level=triangle[-1]
            cur_level=[1]
            for (col,num) in enumerate(prev_level):
                if col==len(prev_level)-1:
                    cur_level.append(1)
                    break
                cur_level.append(num+prev_level[col+1])
            triangle.append(cur_level)
    if show_all:
        for (index,level) in enumerate(triangle):
            print(f"{index+1}:{level}")
    else:
        print(f"{limit}:{triangle[limit-1]}")

if __name__=='__main__':
    main(50,False)