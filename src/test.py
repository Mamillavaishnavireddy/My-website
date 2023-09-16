
from collections import defaultdict
nums = [3,1,2,2,2,1,3]

def default_value():
    return 0

seen=defaultdict(default_value,nums)


print(seen)

