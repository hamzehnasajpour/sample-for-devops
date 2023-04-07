import coverage
import unittest

cov = coverage.Coverage(source=['app.py', 'test_app.py'])
cov.start()

unittest.TextTestRunner(verbosity=2).run(unittest.TestLoader().discover('.', pattern='test_*.py'))

cov.stop()
cov.save()

print('\n\nCoverage Report:\n')
cov.report()
