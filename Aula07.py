# SCHOOL SIMULATOR
levels = tuple((
    "6ª série",
    "7ª série",
    "8ª série",
    "9ª série"
))

rooms = tuple((
    "Sala 1",
    "Sala 2",
    "Sala 3",
    "Sala 4",
    "Sala 5"
))

teachers = {}
classes = {}

def addTeacher(name : str, age : int, subjects : list) :
    teachers[name] = {"name" : name, "age" : age, "subjects" : subjects}

def addClass(id : int, level : int, counselor : str, room : int) :
    classes[id] = {"level" : level, "counselor" : counselor, "room" : room}

def printTeacherInfo(name : str) :
    teacher = teachers[name]
    print("Nome:", teacher["name"])
    print("Idade:", teacher["age"])
    print("Matérias:", *teacher["subjects"])

def printClassInfo(id : int) :
    clss = classes[id]
    print("Turma:", id)
    print("Nível:", levels[clss["level"]])
    print("-----------------")
    print("Conselheiro:")
    printTeacherInfo(clss["counselor"])
    print("-----------------")
    print("Sala:", rooms[clss["room"]])

addTeacher("Hanna", 26, ["Religião", "Filosofia", "Sociologia"])
addTeacher("Roger", 32, ["Inglês", "Português", "Literatura"])
addTeacher("Rogerinho", 1, ["Educação Física", "Canto Gutural"])
addTeacher("Rockynho", 5, ["Matemática", "Física", "Química"])
addTeacher("Pâmela", 25, ["Arquitetura"])
addTeacher("Roberto", 62, ["Direito"])

addClass(61, levels.index("6ª série"), "Hanna", rooms.index("Sala 1"))
addClass(62, levels.index("6ª série"), "Roger", rooms.index("Sala 2"))
addClass(71, levels.index("7ª série"), "Rogerinho", rooms.index("Sala 3"))
addClass(81, levels.index("8ª série"), "Rockynho", rooms.index("Sala 4"))
addClass(91, levels.index("9ª série"), "Pâmela", rooms.index("Sala 5"))

printClassInfo(61)