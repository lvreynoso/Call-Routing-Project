import scenario1
import unittest

cost = scenario1.findCost

class Scenario1Test(unittest.TestCase):
    
    def test_init(self):
        pass

    def test_ten(self):
        routes = 'data/route-costs-10.txt'
        # find longest route
        assert cost(routes, '+449275049230') == '0.49'
        assert cost(routes, '+449938419843') == None
        assert cost(routes, '+8197753314') == '0.75'

    def test_hundred(self):
        routes = 'data/route-costs-100.txt'
        
    def test_6hundred(self):
        routes = 'data/route-costs-600.txt'
    
    def test_35thousand(self):
        routes = 'data/route-costs-35000.txt'

    def test_106thousand(self):
        routes = 'data/route-costs-106000.txt'

if __name__ == '__main__':
    unittest.main()

    