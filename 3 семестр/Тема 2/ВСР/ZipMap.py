def zipmap(*args):
  return list(map(lambda *args: args, *args))

l1 = [2,4,56, 32]
l2 = [1,3,5,6,7,8,0]
l3 = [0, 2, 4, 25]
l4 = [1232141]
print(zipmap(l1,l2,l3,l4))
