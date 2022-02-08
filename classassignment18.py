import numpy as np

print("Input row dimension:")

m = int(input())

print("Input column dimension:")

n = int(input())

mat = np.random.randint(10, size=(m,n))

if m==n:
    transMat = mat.transpose()

    dotMat = np.dot(mat, transMat)

    crossMat = np.cross(mat, transMat)
    innerMat = np.inner(mat, transMat)
    outerMat = np.outer(mat, transMat)
    print("The Generated Matrix is:", mat)

    print("The Transpose Matrix is:", transMat)

    print("The dot Matrix is:", dotMat)

    print("The cross Matrix is:", crossMat)
    print("The inner Matrix is:", innerMat)

    print("The outer Matrix is:", outerMat)
    
    fp = open('total_output.txt', 'a')

    np.savetxt(fp, dotMat,fmt='%i', delimiter='\t')
    fp.write("\n")
    np.savetxt(fp, crossMat,fmt='%i', delimiter='\t')
    
    fp.write("\n")
    np.savetxt(fp, innerMat,fmt='%i', delimiter='\t')
    
    fp.write("\n")
    np.savetxt(fp, outerMat,fmt='%i', delimiter='\t')
    
    fp.write("\n")
    fp.close()

else:
    print("To perform necessary operations, row and column dimensions must be same")
