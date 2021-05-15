class solution:
  def printKPathUtil(self,root, path, k):
    if (not root) :
      return
    path.append(root.data)
    printKPathUtil(root.left, path, k)
    printKPathUtil(root.right, path, k)
    f = 0
    for j in range(len(path) - 1, -1, -1):
      f += path[j]
      if (f == k) :
        printVector(path, j)
	path.pop(-1)
