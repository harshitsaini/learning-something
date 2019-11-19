''' TOPICS - setUp and tearDown '''

#  python3 unit_test_2.py

import unittest


class Widget():
    def __init__(self, init_str):
        self.init_str = init_str
        self.sz = (50, 50)

    def resize(self, x, y):
        self.sz = (x, y)

    def size(self):
        return self.sz

    def dispose(self):
        self.init_str = "disposed"


class WidgetTestCase(unittest.TestCase):
    def setUp(self):
        self.widget = Widget('The widget')

    def tearDown(self):
        self.widget.dispose()

    def test_default_widget_size(self):
        self.assertEqual(self.widget.size(), (50, 50),
                         'incorrect default size')

    def test_widget_resize(self):
        self.widget.resize(100, 150)
        self.assertEqual(self.widget.size(), (100, 150),
                         'wrong size after resize')


# if __name__ == '__main__':
#     wt = Widget()
#     print(wt.size())
#     print(wt.resize(10,20))
#     print(wt.size())

def suite():
    suite = unittest.TestSuite()
    suite.addTest(WidgetTestCase('test_default_widget_size'))
    suite.addTest(WidgetTestCase('test_widget_resize'))
    return suite


if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite())
