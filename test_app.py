import unittest
from app import alert

class TestApp(unittest.TestCase):
   def test_alert(self):
       txt= alert()
       self.assertEqual(txt, "Alert triggered")

if __name__=='__main__':
    unittest.main()
