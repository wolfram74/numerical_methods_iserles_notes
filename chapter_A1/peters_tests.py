# import notes_Peter
from notes_Peter import Vector

# raise NotImplementedError(
#         'To customize, remove this line and customize where it says XXX')

import unittest
import random

import os
import sys
sys.path.append('..')      # XXX Probably needed to import your code
def random_vec(dimension):
  array = []
  for i in range(dimension):
    array.append(random.random()-.5)
  return Vector(array)

class test_vector(unittest.TestCase):
  def setUp(self):
    self.vec1 = Vector([1,2])
    self.vec2 = Vector([-3,4])
    self.vec3 = Vector([2,-4])
    ###  XXX code to do setup

  def tearDown(self):
    ###  XXX code to do tear down
    pass

  def test_meta_success(self):
    self.assertTrue(True)

  def test_meta2_failure(self):
    self.assertTrue(False)

  def test_creation(self):
    self.assertEqual(type(self.vec1), Vector)  

  def test_comparison(self):
    array = [1,2,3]
    vec1 = Vector(array)
    vec1p = Vector(array)
    self.assertEqual(vec1, vec1p)

  def test_commutative_addition(self):
    sum1 = self.vec1.add(self.vec2)
    sum2 = self.vec2.add(self.vec1)
    self.assertEqual(sum1, sum2)

  def test_commutative_addition2(self):
    sum1 = self.vec1 + self.vec2
    sum2 = self.vec2 + self.vec1
    self.assertEqual(sum1, sum2)

  def test_scalar_commutative(self):
    a = random.randrange(10)
    sum1 = self.vec1.add(self.vec2)
    result1 = sum1.scalar_mult(a)
    mult1 = self.vec1.scalar_mult(a)
    mult2 = self.vec2.scalar_mult(a)
    result2 = mult1.add(mult2)
    self.assertEqual(result1, result2)

  def test_scalar_commutative2(self):
    a = random.randrange(10)
    sum1 = self.vec1 + self.vec2
    result1 = sum1 * a
    mult1 = self.vec1 * a
    mult2 = self.vec2 * a
    result2 = mult1 + mult2
    self.assertEqual(result1, result2)

  def test_scalar_product_nonegativity(self):
    samples = []
    all_positive = True
    for i in range(10):
      samples.append(random_vec(5))
    for i in samples:
      all_positive =  all_positive and (i.scalar_product(i) >= 0)
    self.assertTrue(all_positive)

  def test_scalar_product_linearity(self):
    a = random.randrange(20)-10
    b = random.randrange(20)-10
    left = ()

  def test_scalar_product_symmetry(self):
    pass

  def test_scalar_product_symmetry(self):
    pass

#  Examples:
  # self.assertEqual(fp.readline(), 'This is a test')
  # self.assertFalse(os.path.exists('a'))
  # self.assertTrue(os.path.exists('a'))
  # self.assertTrue('already a backup server' in c.stderr)
  # self.assertIn('fun', 'disfunctional')
  # self.assertNotIn('crazy', 'disfunctional')
  # with self.assertRaises(Exception):
  # raise Exception('test')
  #
  # Unconditionally fail, for example in a try block that should raise
  # self.fail('Exception was not raised')

# unittest.main()