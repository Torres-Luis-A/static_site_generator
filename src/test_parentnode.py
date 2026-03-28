import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode

class TestParentNode(unittest.TestCase):
    def test_to_html(self):
        child1 = LeafNode(tag="p", value="This is a paragraph")
        child2 = LeafNode(tag="p", value="This is another paragraph")
        parent = ParentNode(tag="div", children=[child1, child2])
        self.assertEqual(
            "<div><p>This is a paragraph</p><p>This is another paragraph</p></div>",
            parent.to_html(),
        )

    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",)
        
    def test_to_html_with_props(self):
        child_node = LeafNode("span", "child", props={"class": "my-class"})
        parent_node = ParentNode("div", [child_node], props={"id": "my-id"})