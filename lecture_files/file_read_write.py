import json
import xml.dom.minidom
import xml.etree.ElementTree as ET
from pprint import pp

data_dict = {
    'person1': {
        'gender': 'm',
        'age': 18,
        'name': 'Vasya',
        'birth': {
            'country': 'Ukraine',
            'city': 'Kyiv',
            'postal': '02222'
        }
    },
    'person2': {
        'gender': 'f',
        'age': 20,
        'name': 'Mary',
        'birth': {
            'country': 'USA',
            'city': 'New York',
            'postal': '01111'
        }
    }
}


def write_json(filename: str, data: dict):
    with open(f'{filename}.json', 'w') as file:
        json.dump(data, file)


def print_json(filename: str):
    with open(filename, 'r') as file:
        pp(json.load(file))


def write_xml(filename: str, data: dict):
    root = ET.Element('users')
    for user_id, user_data in data.items():
        user = ET.SubElement(root, 'user')
        user.attrib['id'] = user_id
        for key, value in user_data.items():
            if isinstance(value, dict):
                sub_element = ET.SubElement(user, key)
                for sub_key, sub_value in value.items():
                    sub_sub_element = ET.SubElement(sub_element, sub_key)
                    sub_sub_element.text = str(sub_value)
            else:
                element = ET.SubElement(user, key)
                element.text = str(value)
    tree = ET.ElementTree(root)
    tree.write(f'{filename}.xml')


def print_xml_data(filename: str):
    tree = ET.parse(filename)
    root = tree.getroot()
    for child in root:
        print(child.tag, child.attrib)
        for sub_child in child:
            print(sub_child.tag, sub_child.text)


def print_xml(filename: str):
    doc = xml.dom.minidom.parse(filename)
    print(doc.toxml())


def print_xml_data(element):
    print(element.tag, element.attrib)
    for child in element:
        print(child.tag, child.text)
        print_xml_data(child)


def traverse_xml(filename):
    tree = ET.parse(filename)
    root = tree.getroot()
    print_xml_data(root)


# Example usage
traverse_xml('my_users.xml')