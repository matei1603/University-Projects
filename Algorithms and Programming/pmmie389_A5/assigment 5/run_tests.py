import unittest

def run_all():
    loader = unittest.TestLoader()
    suite = loader.discover("./test", pattern = "test_*.py")
    unittest.TextTestRunner().run(suite)

run_all()