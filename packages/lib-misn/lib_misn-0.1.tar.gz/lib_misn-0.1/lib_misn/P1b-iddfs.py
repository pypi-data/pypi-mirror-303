#AIM: Implement IDDFS(Iterative Deepening Depth-First Search).

import queue as Q
from RMP import dict_gn

start='Arad'
goal='Bucharest'
result=''

def DLS(city, visitedstack, startlimit, endlimit):
    global result
    found=0
    result=result+city+' '
    visitedstack.append(city)
    if city==goal:
        return 1
    if startlimit==endlimit:
        return 0
    for eachcity in dict_gn[city].keys():
        if eachcity not in visitedstack:
            found=DLS(eachcity, visitedstack, startlimit+1, endlimit)
            if found:
                return found

def IDDFS(city, visitedstack, endlimit):
    global result
    for i in range(0, endlimit):
        print("Searching at Limit: ",i)
        found=DLS(city, visitedstack, 0, i)
        if found:
            print("Found")
            break
        else:
            print("Not Found! ")
            print(result)
            print("-----")
            result=' '
            visitedstack=[]

def main():
    visitedstack=[]
    IDDFS(start, visitedstack, 9)
    print("IDDFS Traversal from ",start," to ", goal," is: ")
    print(result)


main()            


"""
OUTPUT:
Searching at Limit:  0
Not Found! 
Arad 
-----
Searching at Limit:  1
Not Found! 
 Arad Zerind Sibiu Timisoara 
-----
Searching at Limit:  2
Not Found! 
 Arad Zerind Oradea Sibiu Rimnicu Fagaras Timisoara Lugoj 
-----
Searching at Limit:  3
Not Found! 
 Arad Zerind Oradea Sibiu Timisoara Lugoj Mehadia 
-----
Searching at Limit:  4
Not Found! 
 Arad Zerind Oradea Sibiu Rimnicu Fagaras Timisoara Lugoj Mehadia Drobeta 
-----
Searching at Limit:  5
Found
IDDFS Traversal from  Arad  to  Bucharest  is: 
 Arad Zerind Oradea Sibiu Rimnicu Pitesti Craiova Fagaras Bucharest 
"""
