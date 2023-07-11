#!/usr/bin/env python
# coding: utf-8

# In[ ]:


Q - Given three integer arrays arr1, arr2 and arr3 sorted in strictly increasing order, return a sorted array of only the
integers that appeared in all three arrays.


# In[5]:


def find(arr1, arr2, arr3):
    print("Common elements between all three array: ", end="")
    arr1 = set(arr1)
    arr2 = set(arr2)
    arr3 = set(arr3)
    print(arr1 & arr2 & arr3)
array1 = [1, 2, 3, 5]
array2 = [1, 2, 5, 7, 9]
array3 = [1, 3, 4, 5, 8]

print("Array1 = ", array1)
print("Array2 = ", array2)
print("Array3 = ", array3)

find(array1, array2, array3)


# In[ ]:


Q - Given two 0-indexed integer arrays nums1 and nums2, return a list answer of size 2


# In[9]:


array1 = [1, 2, 3]
array2 = [2, 4, 6]
s = set(array2)
temp3 = [x for x in array1 if x not in s]
print(temp3)


# In[ ]:


Q - Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in
    non-decreasing order.


# In[51]:


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


Q - Given the array nums consisting of 2n elements in the form


# In[49]:


def shuffleArray(a, n):
	i, q, k = 0, 1, n
	while(i < n):	
		j = k
		while(j > i + q):
			a[j - 1], a[j] = a[j], a[j - 1]
			j -= 1
		i += 1
		k += 1
		q += 1
a = [1, 3, 5, 7, 2, 4, 6, 8]
n = len(a)
shuffleArray(a, int(n / 2))
for i in range(0, n):
	print(a[i], end = " ")


# In[ ]:


Q - Given an integer array nums of 2n integers, group these integers into n pairs 


# In[ ]:


class Solution(object):
    def arrayPairSum(self, nums):
        nums.sort()
        result = 0
        numsLen = len(nums)
        for i in range(0, numsLen - 1, 2):
            result += nums[i]
        return result


# In[ ]:


Q - Given a 2D integer array matrix, return the transpose of matrix.


# In[52]:


import numpy
l1 =  [[1,2,3],[4,5,6],[7,8,9]]
print(numpy.transpose(l1))


# In[ ]:




