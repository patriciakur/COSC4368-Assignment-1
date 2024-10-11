import random
import math

# Project class
class Project:
    def __init__(self, name, resourceReq, value):
        self.name = name
        self.resourceReq = resourceReq
        self.value = value

def RandomizedHillClimbingMaximize(projects, maxResources, loop):
    currentResources = 0
    currentBenefit = 0
    currentProjects = []
    iteratedProjectsOrders = []
    
    random.shuffle(projects)
    orderName = []
    for project in projects:
        orderName = orderName + [project.name]
        if currentResources + project.resourceReq <= maxResources:
            currentResources += project.resourceReq
            currentBenefit += project.value
            currentProjects.append(project)
    iteratedProjectsOrders.append(orderName)
                
    for i in range(loop):
        candidateProjects = []
        candidateResources = 0
        candidateBenefit = 0
        
        random.shuffle(projects)
        orderName = [project.name for project in projects]
        if orderName not in iteratedProjectsOrders:
            iteratedProjectsOrders.append(orderName)
            for project in projects:
                if candidateResources + project.resourceReq <= maxResources:
                    candidateResources += project.resourceReq
                    candidateBenefit += project.value
                    candidateProjects.append(project)
            if candidateBenefit > currentBenefit:
                currentResources = candidateResources
                currentBenefit = candidateBenefit
                currentProjects = candidateProjects
        else:
            continue
        
    print("Projects Selected:", [project.name for project in currentProjects])
    print("Total Benefit:", currentBenefit)
    print("Total Resources Used:", currentResources)
    return                
    

def RandomizedHillClimbingMinimize(projects, maxResources, loop):
    currentResources = 0
    currentEstTime = float('inf')
    currentProjects = []
    iteratedProjectsOrders = []
    
    random.shuffle(projects)
    orderName = projects[0].name
    if currentResources + projects[0].resourceReq <= maxResources:
        currentResources += projects[0].resourceReq
        currentEstTime = projects[0].value
        currentProjects.append(projects[0])
    iteratedProjectsOrders.append(orderName)
    
    for i in range(loop):
        candidateProjects = []
        candidateResources = 0
        candidateTime = float('inf')
        
        random.shuffle(projects)
        orderName = projects[0].name
        if orderName not in iteratedProjectsOrders:
            iteratedProjectsOrders.append(orderName)
            if candidateResources + projects[0].resourceReq <= maxResources:
                candidateResources += projects[0].resourceReq
                candidateTime = projects[0].value
                candidateProjects.append(projects[0])
                if candidateTime + projects[0].value < currentEstTime:
                    currentResources = candidateResources
                    currentEstTime = candidateTime
                    currentProjects = candidateProjects
        else:
            continue
                
    print("Projects Selected:", [project.name for project in currentProjects])
    print("Total Est. Time:", currentEstTime)
    print("Total Resources Used:", currentResources)
    return

# Test Case 1, Maximize Benefit
project1 = Project(1, 20, 40)
project2 = Project(2, 30, 50)
project3 = Project(3, 25, 30)
project4 = Project(4, 15, 25)
testCase1Projects = [project1, project2, project3, project4]

# Test Case 2, Minimize total Est. Time
projectA = Project('A', 10, 15)
projectB = Project('B', 40, 60)
projectC = Project('C', 20, 30)
projectD = Project('D', 25, 35)
projectE = Project('E', 5, 10)
testCase2Projects = [projectA, projectB, projectC, projectD, projectE]

# Test Case 3, Maximize Benefit
ProjectX = Project('X', 50, 80)
ProjectY = Project('Y', 30, 45)
ProjectZ = Project('Z', 15, 20)
ProjectW = Project('W', 25, 35)
testCase3Projects = [ProjectX, ProjectY, ProjectZ, ProjectW]

# Run the Randomized Hill Climbing Algorithms
print("Type a number between 1 and 30 for the amount of times you randomly select a neighbor. 30 will almost guarantee the best solution.")
loop = int(input())
print("-----------------")
print("Test Case 1: Maximize Benefit")
RandomizedHillClimbingMaximize(testCase1Projects, 100, loop)
print("-----------------")
print("Test Case 2: Minimize total Est. Time")
RandomizedHillClimbingMinimize(testCase2Projects, 100, loop)
print("-----------------")
print("Test Case 3: Maximize Benefit")
RandomizedHillClimbingMaximize(testCase3Projects, 100, loop)
