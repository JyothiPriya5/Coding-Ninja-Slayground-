from typing import List
from collections import Counter
def getFrequencies(v: List[int]) -> List[int]: 
    frequency= Counter(v)
    maxf=max(frequency.values()) 
    minf=min(frequency.values())
    maxitem= min([key for key,value in frequency.items() if value==maxf])
    minitem= min([key for key,value in frequency.items() if value==minf])
    return maxitem, minitem
    
