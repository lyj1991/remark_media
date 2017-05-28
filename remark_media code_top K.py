'''
常见的算法时间复杂度由小到大依次为：
　　O(1)＜O(log2n)＜O(n)＜O(nlog2n)＜O(n2)＜O(n3)
T(n)=T1(n)+T2(n)+T3(n)=klogk 
k是序列中不重复的数目，所以k<=n
所以满足题目要求 T(n)<=O(nlogn)

本次代码思路：
 1）对列表进行频数统计,以字典形式展示   
 2）对字典的值进行堆排序
 3）找到值最大的前k个值，并返回对应的键
 
'''
###############################  code  ##########################################
# T1(n)=n
def frequency_dic(lst):  # 对列表的元素用字典形式统计频数
    list_a=[]            # 生成空列表   
    output=dict()        # 存放
    for i in range(0,len(lst)):        
       if  (lst[i] not in list_a):           
           list_a.append(lst[i])           
           output[lst[i]]=1        
       else:           
           output[lst[i]]+=1  
    return output   #返回元素类别和频数

# T2(n)= klogk     
def heap_sort(lst):
    def sift_down(start, end):
        """最大堆调整"""
        root = start
        while True:
            child = 2 * root + 1
            if child > end:
                break
            if child + 1 <= end and lst[child] < lst[child + 1]:
                child += 1
            if lst[root] < lst[child]:
                lst[root], lst[child] = lst[child], lst[root]
                root = child
            else:
                break

    # 创建最大堆
    for start in range((len(lst) - 2) // 2, -1, -1):
        sift_down(start, len(lst) - 1)

    # 堆排序
    for end in range(len(lst) - 1, 0, -1):
        lst[0], lst[end] = lst[end], lst[0]
        sift_down(0, end - 1)
    return lst
      
# T3(n)=n           
def top_k(lst,k):
    max_k=[]  # 字典中前k个最大的值
    max_k_num=[] 
    output=[] # 存放前k个最大值的对应键
    lst_x= frequency_dic(lst) 
    key_list=[]
    value_list=[]  
    for i,j in lst_x.items():
        key_list.append(i)   
        value_list.append(j)
    value_list_x= heap_sort(value_list.copy()) 
    for i in range(k):
        if len(lst)==0:
            output=[]
            return output
            break     # 添加空值返回
        else:
            max_k.append(value_list_x[len(value_list_x)-i-1]) # 找到前k个值
    for i in range(len(value_list)):
      if  value_list[i] in max_k:
          max_k_num.append(i)
      else:
          continue
    for i in max_k_num:
         output.append(key_list[i])  
    return output
    
################################################################################

# 测试    
top_k([1,1,1,1,2,2,12,12,12,9],2)
top_k(['a','a','a','b','b','b','b','c','c'],1)
top_k([],2)

