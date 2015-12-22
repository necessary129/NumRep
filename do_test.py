from test import support as s
from tests.testv2 import Tester
from tests.test_rst import runt

def testmod(mod):
    import doctest
    mod = __import__(mod)
    err, test = doctest.testmod(m=mod,verbose=True)
    if err > 0:
        return False
    else:
        return True

def main():
    import os
    first = testmod('NumRep')
    if not first:
        sys.exit(1)
    for mod in os.listdir('NumRep'):
        if mod.startswith('__') or mod.endswith('.pyc'):
            continue
        module = 'NumRep.'+mod.replace('.py','')
        test = testmod(module)
        if not test:
            sys.exit(1)

if __name__ == '__main__':
    main()
    s.run_unittest(Tester)
    runt('README.rst')
    runt('CHANGELOG.rst')