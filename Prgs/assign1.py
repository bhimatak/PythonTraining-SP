A = [4, 3, 2, 5, 8, 6, 7]

for i in range(len(A)):
    flag = False
    MAX = A[i]
    print("MAX: ", MAX)
    for j in range(0,i+1):
        # print(A[j])
        if MAX <A[j]:
            flag = True
            print("J: ",j)
            break

    if flag == False:
        MIN = A[i]
        print("MIN: ", MIN)
        for k in range(i+1,len(A)):
            if MIN >= A[k]:
                flag = True
                print("K: ", k)
                break
    if flag == False and i != len(A)-1:
        print("PP: ",A[i])
        break
    print(f"========={i}========")
