import numpy as np

# making the array using loop
arr = np.zeros([6,5])
num = 1
for i in range(6):
    for j in range(5):
        arr[i,j] = num
        num += 1
arr = arr.astype('int32')
print("-------- Question Array ----------")
print(arr,end="\n\n")
        
print("-------- Red ----------")
red_arr = np.array(arr[[0,-2,-1],3:])
print(red_arr,end="\n\n")
print("-------- Blue ----------")
blue_arr = np.array(arr[[2,3],:2])
print(blue_arr,end="\n\n")
print("-------- Green ----------")
green_arr = np.array(arr[[0,1,2,3],[1,2,3,4]])
print(green_arr,end="\n\n")