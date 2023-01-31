#Easy
def TwoSum():
	for i in range(len(nums)):
        for j in range(len(nums)):
            if i==j:
                pass
            else:
                if nums[i]+nums[j]==target:
                    return [i,j]


#Medium
def AddTwoNumbers():
	a=0
        c=0
        b=0
        d=0
        while l1 is not None:
            a+=(l1.val)*(10**c)
            c+=1
            l1=l1.next

        while l2 is not None:
            b+=(l2.val)*(10**d)
            d+=1
            l2=l2.next
        stringx = str(a+b)
        stringx = stringx[::-1]


        data = list(stringx)
        tail = head = ListNode(data[0])
        for x in data[1:]:
            tail.next = ListNode(x)
            tail = tail.next
        return head

#Easy

def Palindrome():
	temp = x
    ok = 0
    while(x>0):
        div = x%10
        ok = ok*10+div
        x = x//10
    if temp == ok:
        return True
    else:
        return False

#Easy

def RomanToInteger():
	symbols =  {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
    sumx = 0
    skip = False
    for i in range(len(s)-1,-1,-1):
        if skip == True:
            skip=False
            continue
        if s[i-1] and i!=0:
            if s[i-1] in ["I","X","C"]:

                if s[i]=="V" and s[i-1] =="I":
                    sumx+=4
                    skip = True
                elif s[i]=="X" and s[i-1] =="I":
                    sumx+=9
                    skip = True

                elif s[i]=="L" and s[i-1] =="X":
                    sumx+=40
                    skip = True

                elif s[i]=="C" and s[i-1] =="X":
                    sumx+=90
                    skip = True

                elif s[i]=="D" and s[i-1] =="C":
                    sumx+=400
                    skip = True

                elif s[i]=="M" and s[i-1] =="C":
                    sumx+=900
                    skip = True

                else:

                    sumx+=symbols[s[i]]

            else:
                sumx+=symbols[s[i]]
        else:
                sumx+=symbols[s[i]]
    return sumx
        

#Easy

def LongestCommonPrefix():

    size = len(strs)


    strs.sort()

    end = min(len(strs[0]), len(strs[size - 1]))

    i = 0
    while (i < end and
           strs[0][i] == strs[size - 1][i]):
        i += 1

    if i <=0 :
        return ""
    
    else:
        pre = strs[0][0: i]
        return pre

#Easy

def ValidParenthesis():
    stack=[]
    for i in s:
        if i in ["[","{","("]:
            stack.insert(0,i)
        if i in ["]","}",")"]:
            if len(stack)==0:
                return False
            elif i=="]":
                if stack[0]=="[":
                    stack.pop(0)
                else:
                    return False
            elif i=="}":
                if stack[0]=="{":
                    stack.pop(0) 
                else:
                    return False
            elif i==")":
                if stack[0]=="(":
                    stack.pop(0)
                else:
                    return False
    if len(stack)==0:
        return True
    else:
        return False

#Easy

def MergeTwoSortedLists():
	dummy = ListNode()
    tail = dummy
    
    while list1 and list2:
        if list1.val < list2.val:
            tail.next = list1
            list1 = list1.next
            
        else:
            tail.next = list2
            list2 = list2.next
        
        tail = tail.next
        
    if list1:
        tail.next = list1
    elif list2:
        tail.next = list2
        
    return dummy.next


#Easy

def SearchInsertPosition():
	dummy = ListNode()
    tail = dummy
    
    while list1 and list2:
        if list1.val < list2.val:
            tail.next = list1
            list1 = list1.next
            
        else:
            tail.next = list2
            list2 = list2.next
        
        tail = tail.next
        
    if list1:
        tail.next = list1
    elif list2:
        tail.next = list2
        
    return dummy.next



