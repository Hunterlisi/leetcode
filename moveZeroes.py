# coding=utf-8
"""
@version: 2.7.11
@author: yls
@file: moveZeroes.py
@time: 2016-07-07 10:43
@software: PyCharm
@project: leetcode
"""
"""
Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

For example, given nums = [0, 1, 0, 3, 12], after calling your function, nums should be [1, 3, 12, 0, 0].

Note:
You must do this in-place without making a copy of the array.
Minimize the total number of operations.
"""


def moveZeroes(nums):
    """
    :type nums: List[int]
    :rtype: void Do not return anything, modify nums in-place instead.
    """
    """
    i指针指示当前的检查位，j指示存放位
    从列表开头检查，如果第i位不是0则把该位的值存放在j位，同时j位向后移动
    """
    n = len(nums)
    j = 0
    for i in range(n):
        if nums[i]:
            nums[i], nums[j] = nums[j], nums[i]
            j += 1
            # return nums


def test_it():
    print moveZeroes([0, 0, 1])


if __name__ == '__main__':
    test_it()
