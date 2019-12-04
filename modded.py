from collections import deque
class Node(object):
  # these will be the nodes of a given tree
  def __init__(self, name):
    # syntax for creating a name Node(name)
    self.name = name
    self.children = []
    self.parent = None
  def addChild(self, name, root):
    #adds a child to a node
    #name is just a string
    #root is the root node of the tree
    child = Node(name)
    if child.name == root.name:
      print("The root cannot have a parent")
    elif child.parent != None:
      print("A node cannot have more than one parent")
    elif len(self.children) < 2:
      self.children.append(child)
      child.parent = self
    elif len(self.children) >= 2:
      print("A node cannot have more than two children")
  def getChild(self, name):
    #get the child of a given node
    for x in self.children:
      if x.name == name:
        return x
  def getChildren(self):
    #get all the children of a given node
    return self.children
  def getName(self):
    #gets the name of a node
    return self.name
  def getParent(self):
    #gets the parent of a node
    return self.parent
  def findNode(self, node):
    #finds the node under another node
    if node == self.name:
      return self
    else:
      try:
        leftChild = self.getChildren()[0]
        left = leftChild.findNode(node)
        if left != -1 and left != None:
          return left
      except:
        pass
      try:
        rightChild = self.getChildren()[1]
        right = rightChild.findNode(node)
        if right != -1:
          return right
      except:
        return -1
  def getAnc(self, anc, root):
    # use to get all the ancestors of a given node in a tree
    # anc is an empty list where the ancestor named will be stored
    # root is the root of the tree

    if self.name == root.name:
      anc.sort()
      return anc
    else:
      parent = self.getParent()
      anc.append(parent.name)
      return parent.getAnc(anc, root)
  def getDesc(self, desc):
    # gets all the descendents of a node
    # desc - list of all the descendents
    try:
      leftChild = self.getChildren()[0]
      desc.append(leftChild.name)
      desc += leftChild.getDesc([])
    except:
      pass

    try:
      rightChild = self.getChildren()[1]
      desc.append(rightChild.name)
      desc += rightChild.getDesc([])
    except:
      pass
    return desc
    





def makeList(root, l):
  #this will be used by isTree to determine if a tree is valid
  #root is the root of a tree
  # l is an empty list initially
  try:
    leftChild = root.getChildren()[0]
    l.append(leftChild.name)
    left = makeList(leftChild, l)
  except:
    return []
  try:
    rightChild = root.getChildren()[1]
    l.append(rightChild.name)
    right = makeList(rightChild, l)
  except:
    return []
    
  return l

def isTree(tree):
  # determines if a tree is a valid tree
  root = tree.getRoot()
  l = makeList(root, [root])
  if len(l) == len(set(l)):
    return True
  else:
    return False
  
class Tree(object):
  #the tree which holds nodes
  def __init__(self, root, name):
    self.name = name
    self.root = Node(root)
    self.ordinalSheet = {1:"first", 2:"second", 3:"third", 4:"fourth", 5:"fifth", 6:"sixth", 7:"seventh", 8:"eight", 9:"ninth", 10:"tenth"}
    self.timesSheet = {1:"once", 2:"twice", 3:"thrice", 4:"four times", 5:"five times", 6:"six times", 7:"seven times", 8:"eight times", 9:"nine times", 10:"ten times"}
  def getName(self):
    return self.name

  def getRoot(self):
    #returns the root of a tree
    return self.root
  def findNode(self, node):
    # finds the node of a given tree
    if node == self.root.name:
      return self.root
    else:
      try:
        leftChild = self.root.getChildren()[0]
        left = leftChild.findNode(node)
      except:
        left = -1
      try:
        rightChild = self.root.getChildren()[1]
        right = rightChild.findNode(node)
      except:
        right = -1
      if left != -1 and left != None:
        return left
      elif right != -1 and right != None:
        return right
      else:
        return -1
  def lca(self, a, alist, b, blist):
    # finds the least common ancestor between two nodes
    aParent = a.getParent()
    bParent = b.getParent()
    if aParent != None:
      alist.append(aParent)
    else:
      aParent = a
    if bParent != None:
      blist.append(bParent)
    else:
      bParent = b
    for p in alist:
      if p in blist:
        return p
    return self.lca(aParent, alist, bParent, blist)
  def findDist(self, anc, young, dist):
    # determines the distance between two nodes
    # dist is initially 0
    # make sure anc is higher in the tree than young
    if anc.name == young.name:
      return dist
    else:
      dist += 1
      return self.findDist(anc, young.getParent(), dist)



  def relationship(self, p1, p2):
    # determines the relationship between p1 and p2
    def Ordinal(n):
      # returns the ordinals value based on n
      return self.ordinalSheet[n]
    def Times(n):
      # returns the times value based on n
      return self.timesSheet[n]
    def Great(n):
      # returns a certain number of great based on n
      if n == 1:
        return ""
      elif n == 2:
        return "great"
      elif n == 3:
        return "great-great"
      else:
        return "great-"*(n-1)
      
    def Term(kind, d1, d2, sex):
      # determines the type of relationship there is between two nodes
      if kind == "child":
        if sex:
          if d1 < d2:
            return "son"
          else:
            return "father"
        else:
          if d1 < d2:
            return "daughter"
          else:
            return "mother"
      elif kind == "nibling":
        if sex:
          if d1 < d2:
            return "nephew"
          else:
            return "uncle"
        else:
          if d1 < d2:
            return "niece"
          else:
            return "aunt"

    l = self.lca(p1, [p1], p2, [p2])
    d1 = self.findDist(l, p1, 0)
    d2 = self.findDist(l, p2, 0)
    nearest = min(d1, d2)
    furthest = max(d1, d2)
    sex = getAttri(attri, p2.name, 'sex')
    if nearest >= 2:
      degree = nearest - 1
      removal = abs(d1 - d2)
      if removal == 0:
        return Ordinal(degree) + "Cousin"
      else:
        return Ordinal(degree) + " cousin, " + Times(removal) + " removed"
    elif nearest == 1:
      if furthest == 1:
        if sex:
          return "brother"
        else:
          return "sister"
      elif furthest == 2:
        return Term("nibling", d1, d2, sex)
      else:
        return Great(furthest) + "grand" + Term("nibling", d1, d2, sex)
    elif nearest == 0:
      if furthest == 1:
        return Term("child", d1, d2, sex)
      else:
        return Great(furthest) + " grand " + Term("child", d1, d2, sex)

  def getLinks(self):
    tree = self
    root = self.getRoot()
    desc = root.getDesc([])
    links = []
    for nodeName in desc:
      node = tree.findNode(nodeName)
      links.append([node.getParent().name, node.name])
    return links






"""
Notes:
The data structure for relationships and characteristics of people are stored in separate dictionaries
"""


def makeAttributes():
  #creates an empty dictionary which represents an empty data structure which maps people's names to their attributes
  return {}
def makePerson(age, sex):
  #creates a dictionary which holds characteristcs of a person
  # we need depth and parent to determine whether the tree being attempted to be created is valid
  return {'age':age, 'sex': sex, "depth":None, "parent": 0}

def addPerson(dictionary, personName, personSpecs):
  #adds a person to a dictionary so long as the person has the following qualities
  #make sure that the string is consisting of uppercase and lowercase letters only, without spaces
  #make sure age is not negative and an integer
  #sex is boolean
  name = personName
  age = personSpecs['age']
  sex = personSpecs['sex']
  
  if not name.isalpha():
    print("The name " + name + " contains a number. Names can only have letters")
    return None
  
  for p in dictionary.keys():
    if p == name:
      print("Cannot add " + name + " to the dictionary because the name already exists in the dictionary.")
      return None
  if type(age) != int:
    print("Cannot add " + name + " to the dictionary because the age has to be an integer.")
    return None
  if age < 0:
    print("Cannot add " + name + " to the dictionary because the age cannot be negative.")
    return None
  if type(sex) != bool:
    print("Cannot add " + name + " to the dictionary because the sex has to be a boolean value.")
    return None
  dictionary[personName] = personSpecs

def getAttri(attri, name, string):
  #gets the associated value of a given person
  #attri is the dictionary that maps names to attributes of the person
  # name is the name of the person
  # string is either sex or age depending on what is needed
  if string == "sex":
    return attri[name]['sex']
  elif string == "age":
    return attri[name]['age']

def loadTree(t):
  with open(t, 'r') as f:
      a = deque(list([line.strip() for line in f]))

  attri = makeAttributes()
  count=0
  links = 0
  temp={}

  if ((a[0].split())[0] == 'family'):
    treeName =(a[0].split())[1]
    a.popleft()

  if ((a[0].split())[0] == 'count'):
    count = int((a[0].split())[1])
    a.popleft()

  if ((a[0].split())[0] == 'name'):
    person = (a[0].split())[1]
    age = int((a[1].split())[1])
    if(a[2].split()[1] == 'true'):
      sex = True
    else:
      sex = False
    p1 = makePerson(age, sex)
    addPerson(attri, person, p1)
    tree = Tree(person,treeName)
    root = tree.getRoot()
    for x in range(3):
      a.popleft()


  for x in range(count-1):
    person = (a[0].split())[1]
    age = int((a[1].split())[1])
    if(a[2].split()[1] == 'true'):
      sex = True
    else:
      sex = False
    p1 = makePerson(age, sex)
    addPerson(attri, person, p1)
    for x in range(3):
      a.popleft()
  print(attri)
  if ((a[0].split())[0] == 'links'):
    links = int((a[0].split())[1])
    a.popleft()
  
  for x in range(links):
    
    person1 = (a[0].split())[1]
    person2 = (a[0].split())[2]
    try:
      print(person1, person2)
      if(tree.findNode(person1).name == person1):
        tree.findNode(person1).addChild(person2, root)
        for u,v in temp.items():
          if(tree.findNode(person2).name == u):
            tree.findNode(u).addChild(v, root)
            temp.pop(u,v)
            print('it works')
        
    except:
      if(bool(temp)==False):
        temp[person1]=person2
        print('a')

    a.popleft()
  print(makeList(root,[root.name]))
  return([tree,attri])
def saveTree(t):
  with open(t, 'w') as f:
    f.write('tree ' + tree.getName() +'\n')
    f.write('count ' + str(len(makeList(tree.getRoot(),[tree.getRoot()]))) +'\n')
    for x,y in  attri.items():
      f.write('name ' + x +'\n')
      f.write('age ' + str(y['age']) +'\n')
      f.write('sex ' + (str(y['sex'])).lower() +'\n')
    f.write('link ' + str(len(makeList(tree.getRoot(),[tree.getRoot()]))-1) +'\n')
    for x in tree.getLinks():
      person1, person2 = x
      f.write('tree ' + person1 +' ' +person2 +'\n')

""" A Tree which holds Nodes to show relationship between nodes """

#Generates nodes in tree

"""
tree = Tree(1, "Fam")
root = tree.getRoot()
tree.findNode(1).addChild(2, root)
tree.findNode(1).addChild(3, root)
tree.findNode(2).addChild(4, root)
tree.findNode(2).addChild(5, root)
tree.findNode(3).addChild(6, root)
tree.findNode(3).addChild(7, root)
tree.findNode(4).addChild(8, root)
tree.findNode(4).addChild(9, root)
tree.findNode(5).addChild(10, root)
tree.findNode(5).addChild(11, root)
tree.findNode(6).addChild(12, root)
tree.findNode(6).addChild(13, root)
tree.findNode(7).addChild(14, root)
tree.findNode(7).addChild(15, root)
tree.findNode(10).addChild(16, root)
tree.findNode(10).addChild(17, root)
tree.findNode(17).addChild(18, root)
tree.findNode(17).addChild(19, root)
tree.findNode(14).addChild(20, root)
tree.findNode(14).addChild(21, root)
"""
#print(tree.getName())
#print(tree.findNode(1).getDesc([]))

"""
Attempt to make invalid for testing purposes:
"""
#tree.findNode(20).addChild(5, root)

#print(tree.findNode(14).addChild(22, root))
#print(tree.findNode(14).getChildren()[0].name)
#print(tree.lca(16,[],19,[]).name)
#print(tree.findDist(anc, young, 0))
#print(makeList(root, [root.name]))
#print(isTree(tree))
#print(tree.findNode(1).getDesc([]))


""" A dictionary that maps people names to people age/sex: """
#generates people attributes
"""
attri = makeAttributes()
p1 = makePerson(17, True)
p2 = makePerson(17, True)
p3 = makePerson(17, True)
p4 = makePerson(17, False)
p5 = makePerson(3, True)
p6 = makePerson(35, False)
p7 = makePerson(2, True)
p8 = makePerson(6, True)
p9 = makePerson(6, True)
p10 = makePerson(17, True)
p11 = makePerson(17, True)
p12 = makePerson(17, False)
p13 = makePerson(87, False)
p14 = makePerson(17, True)
p15 = makePerson(17, False)
p16 = makePerson(17, True)
p17 = makePerson(17, False)
p18 = makePerson(87, False)
p19 = makePerson(17, True)
p20 = makePerson(17, False)
p21 = makePerson(17, True)
"""

#maps names to people attributes
"""
addPerson(attri, 1, p1)
addPerson(attri, 2, p2)
addPerson(attri, 3, p3)
addPerson(attri, 4, p4)
addPerson(attri, 5, p5)
addPerson(attri, 6, p6)
addPerson(attri, 7, p7)
addPerson(attri, 8, p8)
addPerson(attri, 9, p9)
addPerson(attri, 10, p10)
addPerson(attri, 11, p11)
addPerson(attri, 12, p12)
addPerson(attri, 13, p13)
addPerson(attri, 14, p14)
addPerson(attri, 15, p15)
addPerson(attri, 16, p16)
addPerson(attri, 17, p17)
addPerson(attri, 18, p18)
addPerson(attri, 19, p19)
addPerson(attri, 20, p20)
addPerson(attri, 21, p21)
"""

#print(getAttri(attri, 6, 'age'))


a=loadTree('mamamo.ft')
tree, attri = a
saveTree('new.ft')