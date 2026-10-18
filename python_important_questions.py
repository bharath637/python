# Two sum problem

lst=[1,2,3,4,5,6,7]
target=13
def two_sum(lst,target):
  hash_map={}
  for i in range(len(lst)):
    complement=target-lst[i]
    print(hash_map)
    if complement in hash_map:
      return [hash_map[complement],i]
    hash_map[lst[i]]=i

print(two_sum(lst,target))

#reverse words
def reversed(input):
  reversed_string=""
  for ch in input.split():
    reversed_string=ch+" " +reversed_string
  return reversed_string

print(reversed("kumar bharath "))

# finding duplicate
# most efficient
lst=[1,2,4,3,2]

def is_duplicate(lst):
  seen=set()
  for i in range(len(lst)):
    if lst[i] in seen:
      return True
    seen.add(lst[i])

print(is_duplicate(lst))

# less efficiant
lst=sorted(lst)
j=1
for i in range(len(lst)):
  if j < len(lst):
    if lst[i]==lst[j]:
      print(True)
    j=j+1












