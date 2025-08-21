  def digital_root(n):
     if n == 0:
        return 0
    return 1+ (n-1)%9
    
def most frequent_root(arr):
    freq ={}
    max_count =0
    result = None
    
    for i in arr:
        root = digital_root(i)
        freq[root] = freq.get(root,0) + 1
        
        if freq[root] > max_count:
            max_count = freq[root]
            result = root
    return result