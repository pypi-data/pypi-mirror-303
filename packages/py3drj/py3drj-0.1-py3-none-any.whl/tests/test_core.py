import unittest
from py3d.core import Model

class TestModel(unittest.TestCase):

    def test_load_model(self):
        model = Model('py3d/data/large_model1.obj')
        self.assertTrue(len(model.get_vertices()) > 0)
        self.assertTrue(len(model.get_faces()) > 0)

if __name__ == '__main__':
    unittest.main()
