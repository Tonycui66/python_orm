import unicodedata

def reverse(list1):
    i,j= 0,len(list1)-1
    while True:
        # i,j= 0,len(list1)-1;i<j;i,j = i+1,j-1:

        if i>=j:
            break
        list1[i],list1[j] = list1[j],list1[i]


        i,j = i+1,j-1
    return list1


def rever_1(list1,n):
    z = [None]*len(list1)
    index=len(list1)-n
    for i in range(0,len(list1)):
        if index >=len(list1):
            index=0
        z[i]=list1[index]
        index+=1
    return z


if __name__ == '__main__':
    s = "Hello world 好！！"
    s_bytes = s.encode(encoding='utf-8')
    print(s_bytes)
    a=[0,1,2,3,4,5]
    a1 = reverse(a[:2])
    print(a)
    a2 =reverse(a[2:])
    a3 = reverse(a1+a2)
    print(a3)
    aa = bytes(10)
    list1 = [1,2,3,4,5,6,7]
    print(rever_1(list1,6))


