import numpy as np 

#q.10
# x = np.ones((3,3))

# x = np.zeros((8,8),dtype = int)

# x[1::2,::2] = 1
# x[::2,1::2]= 1
# print(x)

# #q.20
# Array1 = np.array([0,10,20,40,60,80])
# Array2 = np.array([10,30,40,50,70,90])

# print(np.setdiff1d(Array1,Array2))

# #q.30
# array1 = np.array(["Margery","Betsey","Shelley","Lanell","Genesis"])
# array2 = np.array(['Woolum','Battle','Plotner','Brien','Stahl'])

# x = np.lexsort((array1,array2))
# print(x)


# #q.40
# x = np.ones((3,5),dtype = np.uint) *2
# print(x)

# #q.50
# x = np.array([[2,4,6],[6,8,10]],np.int32)
# print(x.flat[3])

# #q.60
# arr1 = np.array([[10],[20],[30]])
# arr2 = np.array([[40],[50],[60]])
# arr3 = np.dstack((arr1,arr2))
# print(arr3)

# #q.70
# x = np.arange(12).reshape(3,4)
# print(x)
# for i in np.nditer(x) :
#     print(i,end= " ")

# #q.80
# x = np.arange(12).reshape(3,4)
# print(x)
# print(x.tolist())

# #q.90
# x = np.array([[-1,-4,0,2,1,5,-3,-2,5],[-5,-3,-1,3,5,-3,5,-6,-7]])
# print(x)
# x[x<0] = 0
# print(x)

#q.100
x = np.array([[10,10,20,30,30],[30,20,20,40,10]],float)
print(x)
y = np.array([0,40,60],float)
x.put([5,9],y)
print(x)