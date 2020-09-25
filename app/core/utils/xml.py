"""Module containing utility functions for dealing with XML"""
import copy
from typing import Iterator, Iterable, List, Dict, Optional, Union, Any
from xml.etree import cElementTree as ElementTree
from xml.etree.ElementTree import Element


def _get_unique_and_repeated_sub_elements(element: Element):
    """Returns a tuple of (unique_elements_map: Dict, repeated_elements: List,) """
    unique_elements_map: Dict[str, Element] = {}
    repeated_elements: List[Element] = []

    for sub_element in element:
        tag = sub_element.tag

        if tag not in unique_elements_map:
            unique_elements_map[tag] = sub_element
        else:
            unique_elements_map.pop(tag)
            repeated_elements.append(sub_element)

    return unique_elements_map, repeated_elements


def _get_xml_element_attributes_as_dict(xml_element: Element):
    """Add the XML element's attributes as a dictionary"""
    element_attributes = xml_element.items()
    return dict(element_attributes) if element_attributes else {}


class XmlListElement(list):
    """An XML List element"""

    def __init__(self, items: Iterable):
        super().__init__()

        for item in items:
            # items without SubElements return False as __nonzero__method is not defined on Element
            if item:
                unique_elements_map, repeated_elements = _get_unique_and_repeated_sub_elements(item)

                if len(repeated_elements) == 0:
                    # append a dict
                    self.append(XmlDictElement(item))
                else:
                    # append a list
                    for repeated_element in repeated_elements:
                        for _, unique_element in unique_elements_map.items():
                            repeated_element.append(copy.deepcopy(unique_element))

                    self.append(XmlListElement(repeated_elements))

            elif item.text:
                # append a text/number
                text = item.text.strip()
                if text:
                    self.append(text)


class XmlDictElement(dict):
    """An XML dict element"""

    def __init__(self, xml_element: Element):
        super().__init__()
        self.update(_get_xml_element_attributes_as_dict(xml_element))

        for item in xml_element:
            item_attributes_dict = _get_xml_element_attributes_as_dict(item)

            # if the item has sub elements
            if item:
                unique_elements_map, repeated_elements = _get_unique_and_repeated_sub_elements(item)

                if len(repeated_elements) == 0:
                    value = XmlDictElement(item)
                else:
                    unique_tags = set([sub_element.tag for sub_element in repeated_elements])
                    value = {
                        tag: XmlListElement(filter((lambda x: x.tag == tag), repeated_elements))
                        for tag in unique_tags
                    }

                value.update(item_attributes_dict)

            # if item has attributes but n sub elements
            elif len(item_attributes_dict) > 0:
                if item.text:
                    item_attributes_dict['_value'] = item.text

                value = item_attributes_dict

            # if item has no attributes and no sub elements
            else:
                value = item.text

            self.update({item.tag: value})


def convert_xml_element_to_dict(xml_element: Element):
    """Converts an xml element into a dictionary"""
    return XmlDictElement(xml_element)


def read_xml_file(
        file_path: str, records_tag: str, to_dict: Optional[bool] = False, **kwargs) -> Union[Iterator[Element], Iterator[Dict[Any, Any]]]:
    """Reads an XML file element by element and returns an iterator of either dicts or XML elements"""
    with open(file_path, 'rb') as xml_file:
        context = ElementTree.iterparse(xml_file, events=('start', 'end',))
        context = iter(context)
        event, root = context.__next__()

        for event, element in context:

            if event == 'end' and element.tag == records_tag:
                if to_dict:
                    yield convert_xml_element_to_dict(element)
                else:
                    yield element
                # clear the root element to leave it empty and use less memory
                root.clear()


def read_xml_string(xml_string: str, records_tag: str, to_dict: Optional[bool] = False, **kwargs) -> Iterator[Element]:
    """Reads an XML string element by element and returns an iterator of either dicts or XML elements"""
    parser = ElementTree.XMLPullParser(events=('start', 'end',))
    ElementTree.XML(xml_string, parser=parser)

    for event, element in parser.read_events():
        if event == 'end' and element.tag == records_tag:
            if to_dict:
                yield convert_xml_element_to_dict(element)
            else:
                yield element

