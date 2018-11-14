import sys



class rule:
    __head = 0
    __body = 0

    def __init__(self, body, head):
        self.__body = body
        self.__head = head

    def getHead(self):
        return self.__head

    def getBody(self):
        return self.__body

    def printRule(self):
        if len(self.__body) != 0:
            for i in range(len(self.__body)):
                print(self.__body[i], end = "")
                if i is not len(self.__body) - 1:
                    print("^", end = "")
            if len(self.__body) != 0:
                print("=>", end = "")
            print(self.__head, end="\t")
        else:
            print(self.__head, end="\t")


def parse(line):
    result = []
    thehead = ""
    for i in range(len(line)):
        if i == 1:
            thehead = line[i]
        else:
            if line[i].isalpha():
                result.append(line[i])
    return rule(result, thehead)


def solve(Goals, Rules, Solutions, Path, failedPartialPath):
    if len(Goals) == 0:
        return True
    goal = Goals.pop(0)
    for rule in Rules:
        if rule.getHead() == goal:
            Path.append(rule)
            temp = []
            temp.extend(rule.getBody())
            temp.extend(Goals)
            if solve(temp, Rules, Solutions, Path, failedPartialPath):
                Solutions.append(rule)
                return True
            else:
                failedPartialPath.append(rule)
    return False


def solutionForEachQuery(Rules, Goals):
    Solutions = []
    path = []
    failedPartialPath = []


    result = solve(Goals, Rules, Solutions, path, failedPartialPath)
    Solutions.reverse()
    failedPartialPath.reverse()

    if result is True:
        print("Successfully Found the path to the goal... ", "\n")
        print("the solution to the goal is: ")
        for i in Solutions:
            i.printRule()
        print("\n")

        if len(failedPartialPath) != 0:
            print("however, there was a waste of searching of a partial failed path: ")
            for i in failedPartialPath:
                i.printRule()
            print("")
            print("so the entire searched path was: ")
            for i in path:
                i.printRule()
            print("\n")

        else:
            print("the result was found without any waste of failed searches")

    else:
        print("Did NOT Found the path to the goal... ", "\n")
        print("the entire searched path was: ")
        for i in path:
            i.printRule()
        print("")







## Main
filename = None
if len(sys.argv) >= 2:
    filename = sys.argv[1]

Rules = []
if filename is None:
    print("needed a fileName")
    exit()

if filename is not None:
    test_file = open(filename, "r")
    content = test_file.readlines()
    for line in content:
        Rules.append(parse(line))
    test_file.close()

print("The Rules are :")
for i in Rules:
    i.printRule()
print("\n\n")

Goals = []
another = "yes"
while another != "no":
    theInput = input("please enter a query: ")
    Goals.append(theInput)
    another = input("would you like to enter another query in(yes/no): ")

print("User requested queries are: ")
print(Goals, sep = ',')


print("BackwardChaining algorithm started...", "\n\n")


for i in range(len(Goals)):
    goals = []
    goals.append(Goals[i]) 
    print("***solving query ", goals[0])
    print("\n")
    solutionForEachQuery(Rules, goals)
    print("\n\n")








