import numpy as np
import random
from copy import deepcopy
import pprint


#function to find the index of a given array
def index_finder(given_array):
    numstate = (given_array.index(0))
    numstate_i = (numstate % 4) + 1 #left and right
    numstate_j = (numstate // 4) + 1 #up and down 
 
    return numstate, numstate_j, numstate_i
fname = 'nodePath.txt'

#function that converts input list to string with leading 0's

def convert(blah):
    res = (''.join(["{:02d}".format(item) for item in blah]))
    return res

#Conversion to usable output format
def chunks(l, n):
    return [l[i:i+n] for i in range(0, len(l), n)]

#function to unpack our dictionary and find the path from one node to another
def find_path(graph, start, end, path=[]): 
    path = path + [start] 
    if start == end: 
        return path 
    for node in graph[start]: 
        if node not in path: 
            newpath = find_path(graph, node, end, path) 
            if newpath: 
                return newpath 

#Function to reverse the order of a list not using native functions    
def Reverse(lst): 
    new_lst = lst[::-1] 
    return new_lst 

#create a list that will have it's first element deleted when called
sacrifical_list = []
#our puzzle state
content_list = []
with open('nodePath.txt','r+') as f:
    dead_list = f.readline()
    dead_list = dead_list.split()
    nodepaths = f.read().splitlines()
    f.close()
dead_list = list(map(int,dead_list))
content_list.append(dead_list)
print(content_list)


sacrifical_list = content_list.copy()
temp_state = content_list
d = {}

def main():
    sacrifical_list = content_list.copy()
    #define the goal to reach as a string
    goal_state = ('01020304050607080910111213141500')
    goal = 0
    counter = 0
    node = []
    node2 = []
    while True:
        
        #pull out the first element for each new iteration to the queue 
        sacrificed_array = sacrifical_list.pop(0) #THIS IS OUR PARENT NODE 
        print(f'This is the array we want {sacrificed_array}')
        temp_state_set = []
        numstate, numstate_j, numstate_i = index_finder(sacrificed_array)
        
        fixed_numstate = numstate
        print(numstate)
        #Key to move right
        if numstate % 4 != 3: #if we can move right, then swap the elements in the positive direction i.e. right
            temp_actual = deepcopy(sacrificed_array) #deepcopy so we don't affect the original array when swapping, we want to use the same parent node for all 4 possible moves
            temp_actual[fixed_numstate], temp_actual[fixed_numstate + 1] = temp_actual[fixed_numstate + 1], temp_actual[fixed_numstate]

            if temp_actual not in content_list: #if our new parent nodes aren't duplicates, append them
                temp_state_set.append(temp_actual)
                print(f"Moved Right to {temp_state_set}")
                node.append('Right')

        #Key to left
        if numstate % 4 != 0: #if we can move left, do the same as above, but in the opposite direction
            temp_actual = deepcopy(sacrificed_array)
            print(f"Left previous is {temp_actual}") #sanity checks and debugging 

            temp_actual[fixed_numstate], temp_actual[fixed_numstate - 1] = temp_actual[fixed_numstate - 1], temp_actual[fixed_numstate]
            print(f"Shifted Left state is {temp_actual}")
            print(f"Left num is  is {fixed_numstate}")


            if temp_actual not in content_list: #if our new parent nodes aren't duplicates, append them
                temp_state_set.append(temp_actual)
                print(f"Moved Left to {temp_state_set}") #sanity checks and debugging 
                node.append('Left')
    #     #move up
        if numstate < 12:
            temp_actual = deepcopy(sacrificed_array)
            print(f"Up previous is {temp_actual}")

            temp_actual[fixed_numstate], temp_actual[fixed_numstate + 4] = temp_actual[fixed_numstate + 4], temp_actual[fixed_numstate]
            print(f"Shifted Up state is {temp_actual}")
            print(f"Up num is  is {fixed_numstate}")
            if temp_actual not in content_list: #if our new parent nodes aren't duplicates, append them
                temp_state_set.append(temp_actual)
                print(f"Moved Up to {temp_state_set}")
                node.append('Up')


    #     #down
        if numstate > 3:
            temp_actual = deepcopy(sacrificed_array)
            print(f"Down  previous is {temp_actual}")

            temp_actual[fixed_numstate], temp_actual[fixed_numstate - 4] = temp_actual[fixed_numstate - 4], temp_actual[fixed_numstate]
            print(f"Shifted Down state is {temp_actual}")
            print(f"Down num is  is {fixed_numstate}")
            if temp_actual not in content_list: #if our new parent nodes aren't duplicates, append them
                temp_state_set.append(temp_actual)
                print(f"Moved Down to {temp_state_set}")
                node.append('Down')
        print("-----------------------")
        for z in range(len(temp_state_set)): #go through the produced list of possible moves 
            if 1 == 1:
                content_list.append(temp_state_set[z]) #add them to our list of visited nodes 
                sacrifical_list.append(temp_state_set[z]) #copy this to our list that will have elements of it deleted
                y = convert(temp_state_set[z])
                x = {y:[convert(sacrificed_array)]}
                d.update(x)
                print(d)
            if goal_state in convert(content_list[z]): #See if any of our possible moves are to the solution (compare to string to save time), if so, we're almost done!
                print("Goal State Found")
                goal = 1
                break

        if goal == 1:
            break  
        counter = counter + 1
    
    #Writing to file after dicionary lookip to find path from beggining to end 
    path_array = []
    path_array = Reverse(find_path(d, goal_state,convert(content_list[0])))
    reshaped_path = []

    for v in range(len(path_array)):
        reshaped_path.append([path_array[v][i:i+2] for i in range(0, len(path_array[v]), 2)])
    f = open("Nodepath.txt", "w")

    for u in range(len(reshaped_path)):
        f.write('------------------------ \n')
        for b in range(len(chunks(reshaped_path[u], 4))):
            f.write(f'{(chunks(reshaped_path[u],4)[b])} \n')
        f.write(f'Move:{u} \n')
        f.write('------------------------ \n')

    f.close()




    # f = open("Nodes.txt", "w")    


    # last_node = (len(content_list)-1)
    # path_taken = []
    # shortest = []
    # while last_node != -1:
    #     path_taken.insert(0,content_list[last_node])
    #     last_node = int(node2[last_node])
    
    # for x in range(len(path_taken)):
    #     print(path_taken[x])
    #     print()



if __name__ == '__main__':
    main()




