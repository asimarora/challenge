import unittest
import requests
import sys
sys.path.append('../service')
import fetch_joke

class TestJokeService(unittest.TestCase):
  def setUp(self):
    pass

  def test_get_random_name(self):
    self.assertNotEqual(fetch_joke.get_random_name(), False)

  def test_get_random_joke(self):
    self.assertEqual(fetch_joke.get_random_joke('Software', 'Engineer'), True)

  def test_joke(self):
    self.assertEqual(fetch_joke.get_random_joke(), True)
  
  def test_(self):
    self.assertEqual(fetch_joke.get_random_joke(), True)

if __name__ == '__main__':
  unittest.main()
