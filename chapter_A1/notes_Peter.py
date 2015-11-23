
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

stephanie phone call
I'll give you a breakdown of what happens the day of your onsite
2-4 individuals over 9-12:30

get updated on your current status

and go through some logistical things
# http://www.watchcartoononline.com/dragon-ball-super-episode-1-english-subbed
# http://kisscartoon.me/Cartoon/Rick-and-Morty-Season-2/Episode-1?id=59846

"""
import sympy

def truthy():
  return True
def truthy2():
  True

class Vector(object):
  def __init__(self, array):
    """
    to initialize send in an array of numbers
    """
    self.values = array

  def add(self, other_vec):
    output = []
    for i in range(len(self.values)):
      output.append(self.values[i]+other_vec.values[i])
    return Vector(output)

  def scalar_mult(self, scalar):
    output = map((lambda x: x*scalar), self.values)
    return Vector(output)

  def scalar_product(self, other_vec):
    output = []
    for i in range(len(self.values)):
      output.append(self.values[i]*other_vec.values[i])
    return reduce((lambda x, y: x+y), output)

  def __mul__(self, scalar):
    output = map((lambda x: x*scalar), self.values)
    return Vector(output)

  def __add__(self, other_vec):
    output = []
    for i in range(len(self.values)):
      output.append(self.values[i]+other_vec.values[i])
    return Vector(output)

  def __eq__(self, other_vec):
    all_eq = True
    for i in range(len(self.values)):
      all_eq = all_eq and self.values[i]==other_vec.values[i]
    return all_eq
