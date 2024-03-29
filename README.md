# ENPM662 - Project 1
Project1

**Libraries Used:**  

```
- numpy  
- random  
- copy/deepcopy  
- pprint  
```

All librariers were normal libraries, random ended up not being using however can be activated to randomize puzzle positions.

Numpy was also not utilized and can be excluded. Future iterations should use numpy arrays instead of lists to increase runtime dramatically 

Pprint was used to reshape/format lists

Deepcopy was used in order to temporarily change states between moves 

# Running Code  
1) **Download files** and place all 3 in the same directory
2) **Change Directory in cmd** to reflect where all downloaded files have been placed (here we've named the directory 'Project-1')
    ```
    cd ~/User/Project-1
    ```
3) **Open and edit** *NodePath.txt* to reflect test case to be ran. **Input test cases as space separated integers from 0 to 15**
4) **Run** ```
           python plot_path.py
           ```
5) **Wait.** As code executes, once the goal position has been reached, the path will be generated and written to *Nodes.txt* and will look as follows:
```
------------------------
['01', '02', '03', '04']
['05', '06', '07', '08']
['09', '00', '15', '12']
['13', '10', '11', '14']
Move:0
------------------------
------------------------
['01', '02', '03', '04']
['05', '06', '07', '08']
['09', '10', '11', '12']
['13', '15', '00', '14']
Move:x
------------------------
------------------------
['01', '02', '03', '04']
['05', '06', '07', '08']
['09', '10', '11', '12']
['13', '14', '00', '15']
Move:2
------------------------
------------------------
['01', '02', '03', '04']
['05', '06', '07', '08']
['09', '10', '11', '12']
['13', '14', '15', '00']
Move:3
------------------------
```
# Test Cases: 
```
Test Case 1: [[1, 2, 3, 4],[ 5, 6,0, 8], [9, 10, 7, 12] , [13, 14, 11, 15]]

Test Case 2: [[1, 0, 3, 4],[ 5, 2, 7, 8], [9, 6, 10, 11] , [13, 14, 15, 12]]

Test Case 3: [[0, 2, 3, 4],[ 1,5, 7, 8], [9, 6, 11, 12] , [13, 10, 14, 15]]

Test Case 4: [[5, 1, 2, 3],[0,6, 7, 4], [9, 10, 11, 8] , [13, 14, 15, 12]]
Test Case 5: [[1, 6, 2, 3], [9,5, 7, 4], [0, 10, 11, 8] , [13, 14, 15, 12]]
```
