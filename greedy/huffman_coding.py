#Given a string S of distinct character of size N and their corresponding frequency f[ ] i.e. character S[i] has f[i] frequency. 
#Your task is to build the Huffman tree print all the huffman codes in preorder traversal of the tree.

'''
Hufman coding: 
                It is a lossless encoding system where in prfeix codes are used for removing the ambiguity while decoding.
                Most frequently occuring character will have smaller code and vice versa.
'''

class node:
    def __init__(self,freq,symbol,left=None,right=None):
        self.freq=freq
        self.symbol = symbol 
        self.left=left
        self.right=right
        self.huff=''
        
class Solution:
    def huffmanCodes(self,S,f,N):
        # Code here
        ans=[]
        def preorder(node,val=""):
            newval=val+str(node.huff)
            if(node.left):
                preorder(node.left,newval)
            if(node.right):
                preorder(node.right,newval)
            if not node.left and not node.right :
                ans.append(newval)
        nodes=[]
        for i in range(N):
            nodes.append(node(f[i],S[i]))
        while len(nodes)>1:
            sorter = lambda x:x.freq
            nodes = sorted ( nodes, key=sorter )
            left=nodes[0]
            right=nodes[1]
            
            left.huff=0
            right.huff=1
            
            newnode = node(left.freq+right.freq, left.symbol+right.symbol,left,right)
            nodes.remove(left)
            nodes.remove(right)
            nodes.append(newnode)
        preorder(nodes[0])
        return ans
