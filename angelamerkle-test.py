import unittest

class TestAngelaMerkle(unittest.TestCase):

    def setup(self):
        self.tree = AngelaMerkle()

    def test_empty_tree_valid(self):
        self.options.parse()
        self.assertEquals(self.options.known.example, 'example-value')

    def test_set_options_example(self):
        self.options.parse(['-x', 'foobar'])
        self.assertEquals(self.options.known.example, 'foobar')
        self.options.parse(['--example', 'not-a-foobar'])
        self.assertEquals(self.options.known.example, 'not-a-foobar')

if __name__ == '__main__':
    unittest.main()
