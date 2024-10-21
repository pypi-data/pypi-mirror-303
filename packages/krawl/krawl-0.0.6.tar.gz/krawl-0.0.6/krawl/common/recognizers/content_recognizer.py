from bs4 import Comment, Tag

from krawl.common.soup_utils import TextPostprocessor
from krawl.common.textware import TextFilter

from .base_recognizer import BaseRecognizer

_TAG_INVISIBLE = ['style', 'script', 'head', 'title', 'meta', '[document]']
_TAG_INVISIBLE = ['style', 'script', 'head',
                  'title', 'meta', '[document]', 'noscript']
_TAG_SCRIPT = ["script", "style", "header", "footer", "nav", "aside", "form"]


def is_visible(element: Tag) -> bool:
    # TODO: element can also be NavigableString
    if element.parent.name in _TAG_INVISIBLE:
        return False
    if isinstance(element, Comment):
        return False

    # Exclude elements that are hidden by CSS
    if any(attr in element.parent.attrs for attr in ['hidden', 'aria-hidden', 'style']):
        hidden_attr = element.parent.attrs.get('style', '')
        if 'display:none' in hidden_attr or 'visibility:hidden' in hidden_attr:
            return False

    # Exclude elements within tags that usually contain non-human-readable content
    if element.parent.name in ['code', 'samp', 'kbd', 'pre', 'textarea']:
        return False

    # Ensure the text is within tags commonly associated with readable content
    readable_tags = [
        'p', 'span', 'blockquote', 'em', 'strong', 'b', 'i',
        'tr', 'td', 'th',
        'h1', 'h2', 'h3', 'h4', 'h5', 'h6',
        'li', 'dd', 'dt', 'a'
    ]

    if element.parent.name in readable_tags:
        return True

    # Include text in containers like 'div' or 'section' if they don't contain only inline elements
    if element.parent.name in ['div', 'section']:
        if any(child.name in readable_tags for child in element.parent.children):
            return True

    # text can be just ['&nbsp;', '&lt;', '&gt;', '&amp;', '&quot;', '&apos;', '', '-', '—']

    return True


class MainTextRecognizer(BaseRecognizer):
    def __init__(self):
        pass

    def check(self, node: Tag, base_url: str) -> str:

        # Remove scripts, styles, and other non-visible elements
        for script in node(_TAG_SCRIPT):
            script.decompose()

        # Extract main content by focusing on article tags, divs with main content, etc.
        main_content = node.find('article')
        if not main_content:
            main_content = node.find('main')
        if not main_content:
            main_content = node.find('body')

        # Get only visible text
        text_elements = main_content.find_all(text=True)
        visible_texts = filter(is_visible, text_elements)
        text = TextFilter.remove_noise_in_seq(
            TextPostprocessor.primary_text(txt) for txt in visible_texts
        )
        return text
