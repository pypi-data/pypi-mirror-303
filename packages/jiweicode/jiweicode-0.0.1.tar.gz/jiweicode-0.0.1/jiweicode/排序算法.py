print('����������������������      ð������      ������������������')
def bubblesort(arr):
    for i in range(1,len(arr)):
        for j in range(0,len(arr)-i):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]  #�ǳ�����ģ������м�����Ľ�����ʽ....


print('����������������������      ѡ������(ÿ��ѡ����С�Ľ��н���)      ������������������')
def selectaort(arr):
    for i in range(len(arr)-1):
        #��С��������
        minindex=i
        for j in range(i+1,len(arr)):
            if arr[j]<arr[minindex]:
                minindex=j
        # i ���������С������ ����i  ���ҵ�����С���Ľ���
        if i!= minindex:
            arr[i],arr[minindex]=arr[minindex],arr[i]
    return arr

print('����������������������      ��������      ������������������')
#�ڵ�ǰ�����Ͻ��еĴ���...
def insertionsort(arr):
    for i in range(len(arr)):
        preindex=i-1
        current=arr[i]
        #�������ڳ�λ��  ��ǰŲ...   ��Ҫ�Ƚϴ�Ķ�����Ū����Ȼ�����Ǿ��ҵ��˺��ʵ�λ�ã����ȥ����
        while preindex>=0 and arr[preindex]>current:
            arr[preindex+1]=arr[preindex]
            preindex-=1
        arr[preindex+1]=current
    return arr

print('����������������������      ϣ�����򣨵ݼ���������  �����5 .. 3 ..1 �����������������������ֱ�Ӳ�������      ������������������')
import math
def shellsort(arr):
    gap=1
    #�����ǹ��������ϵļ��ֵ��  �����ȼ����ʼgap������gap���ں���ļ�������в��ϼ�С�����ϵı��1��
    #������һ�ֹ��������ķ�ʽ�ɣ���������ѡ��...
    while(gap<len(arr)/3):
        gap=gap*3+1

    while(gap>0):
        #����Ĺ��ɺܺ���⣬������gap��������µ�  ��������
        for i in range(gap,len(arr)):
            temp=arr[i]
            j=i-gap

            while j>=0 and arr[j]>temp:
                arr[j+gap]=arr[j]
                j-=gap
        gap=math.floor(gap/3)
    return arr


print('����������������������      �鲢�����������ڽ������򣬺��Ļ��ǵݹ��˼�룩      ������������������')
def mergesort(arr):

    if(len(arr)<2):
        return arr
    middle=math.floor(len(arr)/2)
    #��һ������ʽ��չ������Ҷ�ӽڵ㲻�ϲ��ϵ����Ͻ��кϲ�...... Խ���Ͻ���merge����Ҫ�ϲ����Ӽ�Խ��
    left,right=arr[0:middle],arr[middle:]
    return merge(mergesort(left),mergesort(right))

def merge(left,right):
    #���￴���򵥵Ķ�����  �б�ĺϲ����ɡ�   ������ߵ�Ĭ������ļ���(����ǵ�һ�εĻ�����Ϊ��һ��) ����������ϲ�
    result=[]
    while left and right:
        if left[0]<=right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
    while left:
        result.append(left.pop(0))
    while right:
        result.append(right.pop(0))

    return result

print('����������������������      �������򣨷ǳ��ǳ����õ�����ʽ��      ������������������')
'''
������֮�У�ѡ��һ��Ԫ����Ϊ����׼����pivot�������߽бȽ�ֵ��
����������Ԫ�ض��������׼ֵ���бȽϣ�����Ȼ�׼ֵС���Ƶ���׼ֵ����ߣ�����Ȼ�׼ֵ����Ƶ���׼ֵ�����Ի�׼ֵ�������ߵ�������Ϊ�����У������ظ���һ���͵ڶ�����ֱ�������Ӽ�ֻʣ��һ��Ԫ��Ϊֹ��
�ٸ����ӣ�������������һ��������Ҫʹ�ÿ���������[11, 99, 33 , 69, 77, 88, 55, 11, 33, 36,39, 66, 44, 22]������������ʹ�ÿ��ŵ���ϸ���裺
ѡȡ�м��66��Ϊ��׼ֵ����׼ֵ�������ѡ��
���дӵ�һ��Ԫ��11��ʼ�ͻ�׼ֵ66���бȽϣ�С�ڻ�׼ֵ����ô����������ߵķ����У��ڶ���Ԫ��99�Ȼ�׼ֵ66�󣬰��������ұߵķ����С�
Ȼ�����ζ������������������ٷ�����ֱ�����ֻ��һ��Ԫ�طֽ������һ��һ�㷵�أ����ع����ǣ���߷���+��׼ֵ+�ұ߷���


�о����鲢������һ�����ưѣ�һ�ַ��ε�˼�룩��ֻ���������ǲ����趨��Ԫ ���е�����С�ڵķ���ߣ����ڵķ��ұߣ��ŵı��ϲ��������򣩣� ���鲢�������������еĺϲ���

emm....�о����鲢�������....  ���������ǰ���Сֵ���ֿ�����ģ����鲢��ֱ�Ӱ��������롢Ȼ�������������...
�кܶ�ʵ�ַ�ʽ������ÿһ�����ŵ�˼�붼��һ�µģ��������һ����Ԫ ����С��λ������ߣ����λ�����ұߣ����������񣩡�


������������������� O(n?)������˵˳�����еĿ��š�������ƽ̯����ʱ���� O(nlogn)���� O(nlogn) 
�Ǻ��������ĳ������Ӻ�С���ȸ��Ӷ��ȶ����� O(nlogn) �Ĺ鲢����ҪС�ܶࡣ���ԣ��Ծ������˳���Խ������������
���ԣ����������������ڹ鲢����
'''

def quick_sort(b):
    if len(b)<2:
        return b
    mid=b[len(b)/2]  #��Ԫ��ʼ����ѡ���м�ģ�  ��Ҳ���������
    left ,right=[],[]  #�洢�Ȼ�Ԫ �� �ͱȻ�ԪС��Ԫ��

    b.remove(mid)

    for item in b:
        if item>mid:
            right.append(item)
        else:
            left.append(item)
    return quick_sort(left)+[mid]+quick_sort(right)


#####  �ڶ��ֿ��ŷ�ʽ���Ƚϳ��õ�һ��   **  �ߵ�λָ�� **  ������ӡ��ʼ��еĽ��ͣ���Ȼ�е�С����
def partiton(li, low, high):  #�����ǿ��� ����ĵĺ������֣����Կ�������  �Ļ�Ԫλ��ѡȡ��ֱ��ѡ��� ��ǰ������׸���㣬Ҫע����������ԭ������������������ȷ�Ĵ�С���֡�
    key = li[low]
    while low < high:
        while low < high and li[high] >= key:
            high -= 1
        if low < high:
            li[low], li[high] = li[high], li[low]  #�����ӡ��ʼ��еķ�ʽ�е㲻һ���������ǽ����ģ�ӡ��ʼ�����ֱ���滻��

        while low < high and li[low] < key:
            low += 1
        if low < high:
            li[high], li[low] = li[low], li[high]
    #����ǳ���Ҫ���� ����׼�´�С����� ��־��   С��low����Ķ��Ȼ�׼�£�����low�Ķ��Ȼ�׼��
    return low

def quickSort(li, low, high):
    if low >= high:
        return
    center = partiton(li, low, high)  #�����Ǹ����ģ�����ÿ������   ��Ԫλ�� Ϊ�µĳ����� �� ���з��������򣬶Է��������������ֱַ����   ���ŵ�ͨ�ù���
    #�ڻ�׼������ٽ��з�����⣬��������  ��һ�ַ�ʽ��˼�룬ֻ���� ����֮ǰ�Ļ�׼����ѡ���м�ģ�����Ļ�׼λ���ǲ��̶��ģ����Ƕ���n��
    quickSort(li, low, center - 1)
    quickSort(li, center + 1, high)


#һ�д���ʵ�ֵķ�ʽ��Ҳ��ţ��
quick_sort = lambda array: array if len(array) <= 1 else quick_sort([item for item in array[1:] if item <= array[0]]) + [array[0]] + quick_sort([item for item in array[1:] if item > array[0]])
quick_sort(23,52,41)


#####  �����ֿ��ŷ�ʽ��Ҳ�ǱȽ��й��о��Լ�ϲ���ķ���  ####
def kuaisu(arr):
    #��Ƶ��ߵĿ�������   ������ͦ���ӵġ�  ���ǵ���ܼ򵥣�ÿ���ҵ�һ������Ȼ�����С������ߣ�����������ұߣ��������ʵ�λ��
    #����ʹ�øߵ�λָ��ķ�ʽ
    n=len(arr)-1
    quicksort(arr,0,n)
    return arr
def quicksort(arr,low,high):
    if low<high: #���ж�������Ĺ��̣� ��һ���ɵݹ���С��Χ�Ĺ��̣�  ������Ҳ�õ��˵ݹ飬���Ҫע���°�
        pi=partition(arr,low,high) #����ǿ��ٵĺ��ĵ����� ʵ����piλ��֮ǰ�� ��С��һ������֮��Ķ�����һ����

        quicksort(arr,low,pi-1)
        quicksort(arr,pi+1,high)

def partition(arr,low,high):
    #��ʼ���ĵĵ����Ķ�����̡�  ������ִ�����ڸߵ�ָ���£����Ͻ����ҵ�����λ�õĹ���
    key=arr[low]

    while low<high:
        #������ �Ӻ���ǰ�Ŀ�������С�ľͽ���
        while low<high and arr[high]>key:
            high-=1
        if low<high:
            arr[low],arr[high]=arr[high],arr[low]

        #��������ǰ�����߰�
        while low<high and arr[low]<key:
            low+=1
        if low<high:
            arr[high],arr[low]=arr[low],arr[high]
    return low #���low������λ�þ����м�  λ��


print('����������������������      �������ȴ����ѣ��ٲ���ȡ�Ӷ�https://www.jianshu.com/p/d174f1862601��      ������������������')
'''
���Ƚ�����������鹹���һ�������
ȡ���������ѵĶѶ��ڵ�(���ֵ)����ѵ��������ҵ�Ԫ�ؽ��н�����Ȼ���ʣ�µ�Ԫ���ٹ����һ�������
�ظ��ڶ�����ֱ���������ѵĳ���Ϊ1����ʱ�������
'''

from collections import deque
def swap_param(L, i, j):
    L[i], L[j] = L[j], L[i]
    return L

def heap_adjust(L, start, end):#�о��⺯��д�Ĳ���ô��       ���е������ڳ�ʼ�����Ѻ� ����ȡֵ���ر���Ҫ�Ĳ��裬�����ķ�Ҷ�ӽڵ㿪ʼ�Ƚϲ�������
    #���ĵģ����н������ٴε����ɴ���ѵĹ���
    #���������ʵ���ǰ�ÿ�������ĸ��ڵ�ͽϴ���ӽڵ����ֵ��������������������� ��Ȼ�Ǹ��ڵ������¼������е���
    # �� ���߿����Լ�����ͼ�������ξͿ��Ժܺõ�������ĺ����ˡ�
    temp = L[start]
    i = start
    j = 2 * i #ֱ�ӵĺ���λ��

    #�˴������ҵ����µĽ��...  �ҵ����ʵĽ����滻�ķ�ʽ...���Ǹо�������һЩ���...
    while j <= end:
        if (j < end) and (L[j] < L[j + 1]): #�жϺ��ӵ��ֵ��Ƿ��Ϊ��
            j += 1
        if temp < L[j]: #����Һ��Ӵ�Ļ���ֱ������Һ��������㣬 �᲻����������Ǳ�ڴ��ֵ
            L[i] = L[j]
            i = j
            j = 2 * i
        else:
            break
    L[i] = temp #���ȡ�����ģ��������λ�õģ����н����Ľ��..

def heap_sort(L):
    #������ ��������   �������Ϊ�����ߣ��Ƚ�������ȡԪ�أ������жѵ��ٴε�����
    L_length = len(L) - 1 #���븨���ռ�

    first_sort_count = L_length / 2
    # �����е���Ϊһ�������(heap_adjust����)   ���ϵ�����ת�ɴ����... ������4�εĽ����ɣ���4����Ҷ�ӽڵ����Ĳ���
    for i in range(first_sort_count):
        heap_adjust(L, first_sort_count - i, L_length)

    # �ѶѶ�Ԫ�غͶ�ĩβ��Ԫ�ؽ���(swap_param����)��Ȼ���ʣ�µ�Ԫ�ص���Ϊһ������ѡ� ����Ӧ�����Ǻ���.....�����һ���������ٽ����ٴεĵ�����
    for i in range(L_length - 1):
        L = swap_param(L, 1, L_length - i)
        #�������Կ�����������ȫ����������һ�������кܴ�����������ӿ�ͷ����󶼽��в��ҽ���
        heap_adjust(L, 1, L_length - i - 1)
    return [L[i] for i in range(1, len(L))]

def heap_sort_main():
    #ʹ��python�����ṩ������ṹ   �����߰ɣ������ǹ����ѵĹ��̣�ʹ��һ�������ʾ... �ڶ����ǵ����γɴ����... �������ǶԴ���ѽ���ȡ�Ѷ�������
    #python ��list ������insert������߲���0ѽ   ����list��insert����ʱ�临�Ӷ���O(n) deque��O(1)
    L = deque([50, 16, 30, 10, 60,  90,  2, 80, 70])
    L.appendleft(0)
    print(heap_sort(L))

print('����������������������      �������򣨰�λ���򣬴ӵ�λ����λ��...�����Ƿǳ�������Ч�ķ�ʽ��      ������������������')
def radix_sort(list):
    i=0
    #��ȡ���ġ�����ʹ�õ���λ��j
    max_num=max(list)
    d=len(str(max_num))

    for k in range(d):
        s=[[] for i in range(10)] #Ͱ�ĸ���  ������10��Ͱ��ÿ��Ͱ����һ���б��ֱ��ʾ��ͬ��λ��
        for i in list:
            '''����3��Ԫ�ص�����[977, 87, 960]����һ���������Ȱ��ո�λ������ͬ��
                           ����һ��Ͱs[7]=[977],s[7]=[977,87],s[0]=[960]
                           ִ�к�list=[960,977,87].�ڶ��ְ���ʮλ����s[6]=[960],s[7]=[977]
                           s[8]=[87],ִ�к�list=[960,977,87].�����ְ��հ�λ��s[9]=[960]
                           s[9]=[960,977],s[0]=87,ִ�к�list=[87,960,977],������'''
            s[i/(10**k)%10].append(i) #977/10=97(С����ȥ),87/100=0   ��������Ͱ��������
        list=[j for i in s for j in i] #����ǳ��ؼ��������ٷ�λ����ʱ��ʹ�õ�ʮ��λ����õ�������....
    return list

if __name__=='__main__':
    a=[977, 87, 960]
    radix_sort(a)
    print(a)










