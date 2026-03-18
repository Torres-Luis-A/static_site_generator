from enum import Enum

class TexType(Enum):
    plain_text = 1
    bold_text = 2
    code_text = 3
    link_text = 4
    images_text = 5

class TextNode:
    def __init__(self, text, text_type, url):
        self.text = text
        self.text_type = text_type
        self.url = url
        
    def __eq__(self, other):
        if self == other:
            return True
        
    def __repr__(TEXT, TEXT_TYPE, URL):
        return f"TextNode(text={TEXT}, text_type={TEXT_TYPE}, url={URL})"
