import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        node = HTMLNode(props={" href":"https://www.google.com", "target": "_blank",})
        node_string = " href=\"https://www.google.com\" target=\"_blank\""
        
        node2 = HTMLNode(props={"class": "my-class", "id": "my-id"})
        node2_string = " class=\"my-class\" id=\"my-id\""

        node3 = HTMLNode(props=None)
        node3_string = ""
        
        self.assertEqual(node.props_to_html(), node_string)
    

