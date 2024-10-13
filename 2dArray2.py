from Array2D import Array2D
# mat1=Array2D(3, 3)
# for i in range(3):
#     for j in range(3):
#         mat1[i,j]=2*i+3*j+4
# mat1.traverse()

def matsum(mat1,mat2):
    if mat1.numrows()!=mat2.numrows() or mat1.numcols()!=mat2.numcols():
        return None
    x=mat1.numrows()
    y=mat1.numcols()
    mat3=Array2D(x, y)
    for i in range(x):
        for j in range(y):
            mat3[i,j]=mat1[i,j]+mat2[i,j]
    return mat3

def matprod(mat1,mat2):
    if mat1.numcols()!=mat2.numrows():
        return None
    x=mat1.numrows()
    y=mat1.numcols()
    z=mat2.numcols()
    mat3=Array2D(x, z)
    mat3.clear(0)
    for i in range(x):
        for j in range(z):
            for k in range(y):
                mat3[i,j]=mat3[i,j]+mat1[i,k]*mat2[k,j]
    return mat3
mat1=[1,2,3],[4,5,6],[7,8,9]
mat2=[1,2,3],[4,5,6],[7,8,9]
print(matprod(mat1,mat2))
def addnum(mat,num):
    mat=Array2D(len(mat),len(mat[0]))
    x=mat.numrows()
    print(x)
    y=mat.numcols()
    print(y)
    mat2=Array2D(x,y)
    mat2.clear(0)
    for i in range(x):
        for j in range(y):
            mat2[i,j]=int(mat[i,j])+num
    return mat2
# print(addnum([[1,2,3],[4,5,6],[7,8,9]],2))