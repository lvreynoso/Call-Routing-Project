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
        assert rt.root is not None
        assert rt.size == 4
        assert rt.empty() is False
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


if __name__ == '__main__':
    unittest.main()