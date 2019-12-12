import os, dictionary, sequence, survey, data

presurvey = True
postsurvey = False
randomization = False

def name():
  name = input("What is the experiment name? ")
  return name

def lists():
  xlist = []
  numlists = input("How many lists are there? ")
  numlists = int(numlists)
  while numlists != 0:
    alist =[]
    xlist.append(alist)
    numlists -= 1
  return xlist

def blocks():
  blist = []
  numblocks = input("How many blocks are there? ")
  numblocks = int(numblocks)
  while numblocks != 0:
    alist = []
    blist.append(alist)
    numblocks -= 1
  return blist

def objects():
  olist = []
  objs = input("In a comma seperated list, please enter which objects will be used in your LMEDS design: ")

def createdirectory(name):
  try:
    # Create target Directory
    os.mkdir(name)
    print("Directory " , name ,  " Created ") 
  except FileExistsError:
    print("Directory " , name ,  " already exists")

  os.chdir(name)
  os.mkdir("audio")
  os.mkdir("output")

createdirectory(name())
numblock = blocks()
numlist = lists()
numobj = objects()