from random import randint

students=["yuri",
"vitor",
"verena",
"tom",
"simon",
"romulo",
"ritesh",
"rachel",
"pauline",
"nina",
"marco",
"malgorzata",
"majd",
"lupo",
"luis",
"leonardo",
"jamil",
"ivan",
"ieva",
"gabriel",
"gabi",
"eliott",
"eduarda",
"carlos",
"benoit",
"anna",
"angela paola"]
randomPairs=[]
for i in range(len(students)-1,0,-2):
  randomStudentIndex=randint(0,len(students)-1)
  randomStudent2Index=randint(0,len(students)-1)

  while randomStudentIndex == randomStudent2Index:
    randomStudentIndex=randint(0,len(students)-1)
    randomStudent2Index=randint(0,len(students)-1)
  pair={
    "student1":students[randomStudentIndex],
    "student2":students[randomStudent2Index]
  }
  randomPairs.append(pair)

  if randomStudent2Index>randomStudentIndex:
    del students[randomStudent2Index]
    del students[randomStudentIndex]

  else:
    del students[randomStudentIndex]
    del students[randomStudent2Index]



randomPairs.append({"soloMode":students[0]})

for pair in randomPairs:
  print(pair)
