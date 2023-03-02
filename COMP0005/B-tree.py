class Node:

    def __init__(self, is_root=False):
        self.root = is_root
        self.keys = []
        self.children = []

class B_tree:

        def __init__(self, lim):
            self.limitation = lim
            self.curRoot = Node()
        
        def insert(self, element):
            inserted = False
            if not self.search(element):
                inserted = True 
                if len(self.curRoot.keys) == 2 * self.limitation - 1:
                    temp = self.curRoot
                    self.curRoot = Node(True)
                    self.curRoot.children.append(temp)
                    self.curRoot.keys.append(temp.keys[0])
                    self.split(temp, self.curRoot)
                    self._insert(self.curRoot, element, None, None)
                else:
                    self._insert(self.curRoot, element, None, None)
            return inserted
        
        def split(self, a, b):
            t = self.limitation
            aux = Node(a.root)
            aux.keys = a.keys[t:2*t]
            a.keys = a.keys[:t]
            if aux.root:
                aux.children = a.children[t:2*t]
                a.children = a.children[:t]
            locate = a.keys[0]
            for i in range(len(b.keys)):
                if locate == b.keys[i]:
                    b.keys.insert(i+1, aux.keys[0])
                    b.children.insert(i+1, aux)
                    break
        
        def _insert(self, curNode, element, prevNode, pos):
            t = self.limitation
            if curNode.root:
                i = 0
                for i in range(len(curNode.keys)):
                    if element < curNode.keys[i]:
                        i -= 1
                        break
                if len(curNode.children[i].keys) == 2 * t - 1:
                    self.split(curNode.children[i], curNode)
                    if element > curNode.keys[i+1]:
                        self._insert(curNode.children[i+1], element, curNode, i+1)
                    else:
                        self._insert(curNode.children[i], element, curNode, i)
                else:
                    self._insert(curNode.children[i], element, curNode, i)
            else:
                i = 0
                for i in range(len(curNode.keys)):
                    if element < curNode.keys[i]:
                        i -= 1
                        break
                if i == -1 and prevNode is not None:
                    curNode.keys.insert(0, element)
                    prevNode.keys[pos] = element
                else:
                    curNode.keys.insert(i+1, element)

        def search(self, element):
            found = False
            r = self.curRoot
            i = 0
            while(True):
                while i < len(r.keys) and element > r.keys[i]:
                    i += 1
                if i < len(r.keys) and element == r.keys[i]:
                    found = True
                    break
                else:
                    i -= 1
                if not r.root:
                    found = False
                    break
                else:
                    r = r.children[i]
                    i = 0
            return found