#!/usr/bin/env python
# coding: utf-8

# In[ ]:


Q - Convert 1D Array Into 2D Array


# In[33]:


import numpy as np
arr = np.array([1, 2, 3, 4])
arr1 = arr.reshape(2, 2)
print (arr1)


# In[ ]:


Q - Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in
    non-decreasing order.


# In[10]:


def sortSquare(arr, n):
	for i in range(n):
		arr[i]= arr[i] * arr[i]
	arr.sort()
arr = [-4,-1,0,3,10]
n = len(arr)
print("Before sort")
for i in range(n):
	print(arr[i], end = " ")

print("\n")

sortSquare(arr, n)

print("After sort")
for i in range(n):
	print(arr[i], end = " ")


# In[ ]:


Q - Given two 0-indexed integer arrays nums1 and nums2, return a list answer of size 2


# In[11]:


array1 = [1, 2, 3]
array2 = [2, 4, 6]
s = set(array2)
temp3 = [x for x in array1 if x not in s]
print(temp3)


# In[ ]:


Q - Given two integer arrays arr1 and arr2, and the integer d, return the distance value between the two arrays.


# In[ ]:


class Solution:
        def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        res, buckets = 0, dict() # (minVa, maxVal)
        
        def getKey(val):
            return val // d
        
        def addVal(val):
            key = getKey(val)
            if key in buckets:
                if buckets[key][0] > val: buckets[key][0] = val
                elif buckets[key][1] < val: buckets[key][1] = val
            else:
                buckets[key] = [val, val]
        for val in arr2: addVal(val)
        for val in arr1:
            key = getKey(val)
            if key in buckets: continue #in one bucket all values x < d
            if key - 1 in buckets and val - buckets[key-1][1] <= d: continue #maxVal from the left side is nearest
            if key + 1 in buckets and buckets[key+1][0] - val <= d: continue #minVal from the right side is nearest
            res += 1
        return res


# In[ ]:


Q - Given an integer array nums of length n where all the integers of nums are in the range [1, n] and each integer appears
    once or twice, return an array of all the integers that appears twice.


# In[ ]:


num = [4,3,2,7,8,2,3,1]
arr_size = len(num)
for i in range(arr_size):
	x = num[i] % arr_size
	num[x] = num[x] + arr_size
print("The repeating elements are : ")
for i in range(arr_size):
	if (num[i] >= arr_size*2):
		print(i, " ")


# In[ ]:


Q - Suppose an array of length n sorted in ascending order is rotated between 1 and n times


# In[31]:


def findMin(arr, low, high):
	if high < low:
		return arr[0]
	if high == low:
		return arr[low]
	mid = int((low + high)/2)
	if mid < high and arr[mid+1] < arr[mid]:
		return arr[mid+1]
	if mid > low and arr[mid] < arr[mid - 1]:
		return arr[mid]
	if arr[high] > arr[mid]:
		return findMin(arr, low, mid-1)
	return findMin(arr, mid+1, high)
if __name__ == '__main__':
	arr = [3,4,5,1,2]
	N = len(arr)
	print("The minimum element is " + \
		str(findMin(arr, 0, N-1)))


# In[ ]:


Q - An integer array original is transformed into a doubled array changed by appending twice the value of every element
    in original, and then randomly shuffling the resulting array.


# In[32]:


def findOriginal(arr):
	numFreq = {}
	for i in range(0, len(arr)):
		if (arr[i] in numFreq):
			numFreq[arr[i]] += 1
		else:
			numFreq[arr[i]] = 1
	arr.sort()
	res = []
	for i in range(0, len(arr)):
		freq = numFreq[arr[i]]
		if (freq > 0):
			res.append(arr[i])

			numFreq[arr[i]] -= 1
			twice = 2 * arr[i]
			numFreq[twice] -= 1
	return res
arr = [1,3,4,2,6,8]
res = findOriginal(arr)
for i in range(0, len(res)):
	print(res[i], end=" ")


# In[ ]:




