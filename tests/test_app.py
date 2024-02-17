import unittest
import sys
sys.path.insert(0,"C:/Users/winma/pywork/txtTranslator")
from app import alert

class TestApp(unittest.TestCase):
   def test_alert(self):
       txt= alert()
       self.assertEqual(txt, "Alert triggered")

if __name__=='__main__':
    unittest.main()
