import re

from bs4 import Tag

from krawl.common.schema.dtypes import HTMLNodeContext, TagEnum


def to_html_context(node: Tag) -> HTMLNodeContext:
    """
    Get relevant HTML context of an item
    """

    # class
    class_attribute = node.get(TagEnum.class_)
    classname = ' '.join(class_attribute) if class_attribute else ""

    # wordcount
    text = node.get_text()
    word_count = len(re.findall(r'\w+', text))

    # href, if exists
    href = node.get(TagEnum.href) if node.name == TagEnum.url else ""

    return HTMLNodeContext(
        tag=node.name,
        classname=classname,
        idname=node.get(TagEnum.id_, ''),
        wordcount=word_count,
        href=href
    )
