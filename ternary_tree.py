class Node: 
    def __init__(self, val):
        self.val = val
        self.left = None
        self.mid = None
        self.right = None
        self.parent = None

    def print(self, lst):
        if not self:
            return
        if self.left:
            self.left.print(lst)
        lst.append(self.val)
        if self.mid:
            self.mid.print(lst)
        if self.right:
            self.right.print(lst)

    def find(self, val):
        if not self:
            return None
        if self.val == val:
            return self
        elif val > self.val:
            if self.right:
                return self.right.find(val)
            return None
        elif val < self.val:
            if self.left:
                return self.left.find(val)
            return None
        
    def insert(self, val):
        if self is None:
            self = Node(val)
        if val < self.val:
            if self.left:
                self.left.insert(val)
            else:
                self.left = Node(val)
                self.left.parent = self
        elif val > self.val:
            if self.right:
                self.right.insert(val)
            else:
                self.right = Node(val)
                self.right.parent = self
        else:
            if self.mid:
                self.mid.insert(val)
            else:
                self.mid = Node(val)
                self.mid.parent = self
                
    def delete(self, val, tree):
        node_to_delete = self.find(val)
        if not node_to_delete:
            return
        else:
            node_to_delete.delete_helper(val, tree)
    
    def delete_helper(self, val, tree):
        if not(self.left or self.mid or self.right): ## no children
            if self.parent:
                self.parent.delete_child(val, None)
            else:
                tree.root = None
        elif self.mid:  ## mid exists
            self.mid.delete_helper(val, tree)
        elif self.left and self.right: ## mid doesn't exist, but both chidren do
            successor = self.find_successor()
            self.val = successor.val
            successor.parent.delete_child(successor.val, successor.left)
        elif self.left:
            if self.parent:
                self.parent.delete_child(val, self.left)
            else:
                tree.root = self.left
                tree.root.parent = None
        elif self.right:
            if self.parent:
                self.parent.delete_child(val, self.right)
            else:
                tree.root = self.right
                tree.root.parent = None

    def find_successor(self):
        r = self.right
        left = self.right.left
        if not left:
            return self.right
        while left.left:
            left = left.left
        return left
   
    def delete_child(self, val, replacement):
        if self.left:
            if self.left.val == val:
                self.left = replacement
                if replacement:
                    replacement.parent = self
        if self.right:
            if self.right.val == val:
                self.right = replacement
                if replacement: 
                    replacement.parent = self
        if self.mid:
            if self.mid.val == val:
                self.mid = replacement
                if replacement:
                    replacement.parent = self

class TernaryTree: 
    def __init__(self):
        self.root = None

    @staticmethod
    def check_args(*args):  
        if any((False if isinstance(x, int) else True for x in args)):
          return False
        return True

    def insert(self,*args):
        if not self.check_args(*args):
            print("This data structure only supports integers")
            return

        if not self.root:
            self.root = Node(args[0])
            for arg in args[1:]:
              self.root.insert(arg)
        else:
            for arg in args:
              self.root.insert(arg)

    def delete(self, *args):
        if not self.check_args(*args):
            print("This data structure only supports integers")
            return
        if not self.root:
            return
        else:
            for arg in args:
                if not self.root:
                    return
                self.root.delete(arg, self)

    def __repr__(self):
      if not self.root:
        return '[]'
      else:
        lst = []
        self.root.print(lst)
        return str(lst)

    def __bool__(self):
      if self.root:
        return True
      return False
tree = TernaryTree()
tree.delete(3)
print(tree)







           