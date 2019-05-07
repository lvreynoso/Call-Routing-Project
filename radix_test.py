#!python

from radix import RadixTree
import unittest


class RadixTreeTest(unittest.TestCase):

    def test_init(self):
        rt = RadixTree()
        assert rt.root is not None
        assert rt.size == 0
        assert rt.empty() is True

    def test_init_with_list(self):
        rt = RadixTree(['+44', '+91', '+4420'])
        assert rt.root is not None
        assert rt.size == 4
        assert rt.empty() is False

    def test_contains(self):
        rt = RadixTree(['+44', '+91', '+4420'])
        assert rt.contains('+44') is True
        assert rt.contains('+91') is True
        assert rt.contains('+4420') is True
        assert rt.contains('+') is True
        assert rt.contains('+96') is False
        assert rt.contains('+4477') is False

    def test_wikipedia_examples(self):
        rt = RadixTree(['tester', 'slow'])
        assert rt.root is not None
        assert rt.size == 2
        assert rt.empty() is False
        rt.insert('water')
        assert rt.size == 3
        assert rt.contains('water') is True
        rt.insert('slower')
        assert rt.size == 4
        assert rt.contains('slower') is True
        rt.insert('test')
        assert rt.size == 5
        assert rt.contains('test') is True
        rt.insert('team')
        assert rt.size == 7
        assert rt.contains('team') is True
        rt.insert('toast')
        assert rt.size == 9
        assert rt.contains('toast') is True

    def test_redundant_insert(self):
        rt = RadixTree(['tester', 'slow', 'water', 'slower', 'test', 'team', 'toast'])
        assert rt.root is not None
        assert rt.size == 9
        assert rt.empty() is False
        rt.insert('test')
        assert rt.size == 9
        assert rt.contains('test') is True
        rt.insert('team')
        assert rt.size == 9
        assert rt.contains('team') is True
        rt.insert('toast')
        assert rt.size == 9
        assert rt.contains('toast') is True

    def test_insert_with_data(self):
        rt = RadixTree()
        rt.insert('+86153', '0.84')
        assert rt.size == 1
        assert rt.contains('+86153') is True
        rt.insert('+449275049', '0.49')
        assert rt.size == 3
        assert rt.contains('+449275049') is True
        rt.insert('+8130', '0.68')
        assert rt.size == 5
        assert rt.contains('+8130') is True
        rt.insert('+4928843955', '0.40')
        assert rt.size == 7
        assert rt.contains('+4928843955') is True
        rt.insert('+449187847', '0.48')
        assert rt.size == 9
        assert rt.contains('+449187847') is True

    def test_lookup(self):
        rt = RadixTree()
        rt.insert('+86153', '0.84')
        rt.insert('+449275049', '0.49')
        rt.insert('+8130', '0.68')
        rt.insert('+4928843955', '0.40')
        rt.insert('+449187847', '0.48')
        assert rt.lookup('+86153') == ['0.84']
        assert rt.lookup('+449275049') == ['0.49']
        assert rt.lookup('+8130') == ['0.68']
        assert rt.lookup('+4928843955') == ['0.40']
        assert rt.lookup('+449187847') == ['0.48']
        with self.assertRaises(KeyError):
            rt.lookup('1800CALLATT')

    def test_lookup_with_unspecified_routes(self):
        rt = RadixTree()
        rt.insert('+86153', '0.84')
        rt.insert('+449275049', '0.49')
        rt.insert('+8130', '0.68')
        rt.insert('+4928843955', '0.40')
        rt.insert('+449187847', '0.48')
        assert rt.lookup('+861532527') == ['0.84']
        assert rt.lookup('+449275049881') == ['0.49']
        assert rt.lookup('+813077489') == ['0.68']
        assert rt.lookup('+492884395520') == ['0.40']
        assert rt.lookup('+449187847610') == ['0.48']




if __name__ == '__main__':
    unittest.main()