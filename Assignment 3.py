#!/usr/bin/env python
# coding: utf-8

# In[ ]:


Q - Given an integer array nums of length n and an integer target, find three integers in nums such that the sum is closest
to the target Return the sum of the three integers.


# In[12]:


import sys
def solution(arr, x):
    closestSum = sys.maxsize
    for i in range (len(arr)) :
        for j in range(i + 1, len(arr)):
            for k in range(j + 1, len( arr)):
                if(abs(x - closestSum) >
                   abs(x - (arr[i] + arr[j] + arr[k]))):closestSum = (arr[i] +arr[j] + arr[k])
                return closestSum
if __name__ == "__main__":
    arr = [ -1, 2, 1, -4 ]
    x = 1
    print(solution(arr, x))


# In[ ]:


Q - Given an array nums of n integers, return an array of all the unique quadruplets


# In[3]:


class Pair:
	def __init__(self, x, y):
		self.index1 = x
		self.index2 = y
def GetQuadruplets(nums, target):
	map = {}
	for i in range(len(nums) - 1):
		for j in range(i + 1, len(nums)):
			# Find the sum of pairs of elements
			sum = nums[i] + nums[j]
			if sum not in map:
				map[sum] = [Pair(i, j)]
			else:
				map[sum].append(Pair(i, j))
	ans = set()
	for i in range(len(nums) - 1):
		for j in range(i + 1, len(nums)):
			lookUp = target - (nums[i] + nums[j])
			if lookUp in map:
				temp = map[lookUp]
				for pair in temp:
					if pair.index1 != i and pair.index1 != j and pair.index2 != i and pair.index2 != j:
						l1 = [nums[pair.index1], nums[pair.index2], nums[i], nums[j]]
						l1.sort()
						ans.add(tuple(l1))
	print(*reversed(list(ans)), sep = '\n')
arr = [1, 0, -1, 0, -2, 2]
K = 0
GetQuadruplets(arr, K)


# In[ ]:


Q - A permutation of an array of integers is an arrangement of its members into a sequence or linear order.


# In[13]:


def swapPositions(list, pos1, pos2):
	list[pos1], list[pos2] = list[pos2], list[pos1]
	return list
def nextPermutation(arr):
	n = len(arr)
	i = 0
	j = 0
	for i in range(n-2, -1, -1):
		if (arr[i] < arr[i + 1]):
			break
	if (i < 0):
		arr.reverse()
	else:
		for j in range(n-1, i, -1):
			if (arr[j] > arr[i]):
				break
		swapPositions(arr, i, j)
		strt, end = i+1, len(arr)
		arr[strt:end] = arr[strt:end][::-1]
if __name__ == "__main__":
	arr = [1, 2, 3]
	nextPermutation(arr)
	for i in arr:
		print(i, end=" ")


# In[ ]:


Q- Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return 
the index where it would be if it were inserted in order.


# In[23]:


def find_index(arr, n, K):
	for i in range(n):
		if arr[i] == K:
			return i
		elif arr[i] > K:
			return i
	return n
arr = [1, 3, 5, 6]
n = len(arr)
K = 5
print(find_index(arr, n, K))


# In[ ]:


Q - You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the
integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does
not contain any leading 0's.


# In[25]:


def AddOne(digits):
	index = len(digits) - 1
	while (index >= 0 and digits[index] == 9):
		digits[index] = 0
		index -= 1
	if (index < 0):
		digits.insert(0, 1)
	else:
		digits[index]+=1
digits =[1,2,3]
AddOne(digits)
for digit in digits:
	print(digit, end =' ')


# In[ ]:


Q - Given an array of meeting time intervals where intervals[i] = [starti, endi], determine if a person could attend all meetings.


# In[ ]:


def CouldAttendMeetings(intervals):       
    intervals.sort(key=lambda a: a.start)
    for i in range(len(intervals)-1):
        if intervals[i].end > intervals[i+1].start:
            return False
    return True


# In[ ]:


Q - Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.


# In[29]:


def findSingle(A, ar_size):
	for i in range(ar_size):

		count = 0
		for j in range(ar_size):
			if(A[i] == A[j]):
				count += 1
		if(count == 1):
			return A[i]
	return -1
ar = [2, 2, 1]
n = len(ar)
print("Element occurring once is", findSingle(ar, n))

