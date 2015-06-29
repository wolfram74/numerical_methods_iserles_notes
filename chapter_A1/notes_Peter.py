
"""
A1 covers steaks and linear algebra.
1.1 basic definitions of spaces and vectors
if x1 and x2 are in the space then x1+x2 is also in the space
if x1 is in the space and a is in the field, then a*x1 is also in the space
x1+x2 = x2+x1
(x1+x2)+x3 = x1+(x2+x3)
0 exists such that x+0=x
inverses exist such that xo+xi = 0, or x+(-x)=0
scalar multiplication is communitative, a(bx)=(ab)x
a unit value exists such that 1*x=x
dimensionality is how many linearly independent vectors you can shove into the space
a set of d vectors in a d-dimensional space are basis vectors if you can assemble any vector in the space as a linear sum of the set.

1.2 starts talking about matrices
start with A being a matrix maXna and B being a matrix mbXnb
matrix addition A+B is done element wise, aij+bij, only valid if the dimensions match.
multiplication by a scalar c just leads to c*aij
matrix multiplication A*B is done with rows of A being dotted with columns of B, so the rows must be of the same length as the columns, making multiplication valid only if na=mb, note that this means it is not communitative
"""
import sympy
