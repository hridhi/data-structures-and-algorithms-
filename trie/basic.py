class trieNode:
    def __init__(self):
        self.children=[None]*26
        self.isEnd=False
class trie:
    def __init__(self):
        self.root=trieNode()
    def insertion(self,word):
        temp=self.root 
        for i in range(len(word)):
            index=ord(word[i])-ord("a")
            if not temp.children[index]:
                temp.children[index]=trieNode()
            temp=temp.children[index]
        temp.isEnd=True
    def finder(self,word):
        temp=self.root
        for i in range(len(word)):
            index=ord(word[i])-ord("a")
            if not temp.children[index]:
                return False
            temp=temp.children[index]
        return temp!=None and temp.isEnd
    def deletion(self,word):
        temp=self.root
        for i in range(len(word)):
            index=ord(word[i])-ord("a")
            if not temp.children[index]:
                return "word wasnt found"
            temp=temp.children[index]
        temp.isEnd=False
        return "deleted"
    #but if we need to cut all the extra branches also then?
    def deletion1(self,word):
        temp = self.root
        path = [temp]
        for letter in word:
            index=ord(word[i])-ord("a")
            if not temp.children[index]:
                return "word wasnt found"
            temp=temp.children[index]
            path.append(temp)
        while(path):
            temp2=path[-1]
            path=path[:len(path)-1]
            if self.child(temp2)>1:
                pass
            else:
                
            
def main():
    keys = ["the","a","there","anaswe","any",
            "by","their"]
    output = ["Not present in trie",
            "Present in trie"]
    t = trie()
    for key in keys:
        t.insertion(key)
    print("{} ---- {}".format("the",output[t.finder("the")]))
    print("{} ---- {}".format("these",output[t.finder("these")]))
    print("{} ---- {}".format("their",output[t.finder("their")]))
    print("{} ---- {}".format("thaw",output[t.finder("thaw")]))
    print("{} ---- {}".format("the",t.deletion("the")))
    print("{} ---- {}".format("the",output[t.finder("the")]))
  
if __name__ == '__main__':
    main()
