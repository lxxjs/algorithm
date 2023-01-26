# can be bad if there is any hash collision
# improve it with Counter() in 'collections' module

def solution(participant, completion):
    hashmap = {}
    sumHash = 0
    for part in participant:
        hashmap[hash(part)] = part
        sumHash += hash(part)

    for comp in completion:
        sumHash -= hash(comp)

    return hashmap[sumHash]
