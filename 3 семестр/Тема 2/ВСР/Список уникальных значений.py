def unique_func(iterable,seen=None):
 seen = list(seen or [])
 for item in iterable:
   if item not in seen:
     seen.append(item)

 return list(seen)

print(unique_func([2,2,2,23,5],[9]))