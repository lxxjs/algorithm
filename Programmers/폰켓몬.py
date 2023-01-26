# hash
# able to improve it by using min() and set()

def solution(nums):
    n = len(nums)
    hashmap = {}
    for i in range(n):
        hashmap[nums[i]] = 1
    x = len(hashmap.keys())

    if x < (n / 2):
        answer = x
    else:
        answer = n / 2

    return answer