import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD,)
        node2 = TextNode("This is a text node", TextType.BOLD,)
        node3 = TextNode("This is a text node", TextType.ITALIC,)
        node4 = TextNode("This is a text node", TextType.BOLD, "https://www.boot.dev")
        node5 = TextNode("This is a text node", TextType.BOLD, "https://www.boot.dev")
        node6 = TextNode("This is a text node", TextType.BOLD, None)
        node7 = TextNode("This is a text node", TextType.BOLD,)
        self.assertEqual(node, node)
        self.assertNotEqual(node, node3)
        self.assertEqual(node5, node5)
        self.assertEqual(node6,node7)



if __name__ == "__main__":
    unittest.main()