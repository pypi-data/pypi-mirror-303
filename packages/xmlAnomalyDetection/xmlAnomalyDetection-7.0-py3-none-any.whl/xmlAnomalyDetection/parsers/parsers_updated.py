import xml.etree.ElementTree as ET

def parse_xml(xml_string):
    try:
        root = ET.fromstring(xml_string)
    except ET.ParseError as e:
        raise ValueError(f"Invalid XML: {e}")

    result = []

    # Parse Detail elements
    for detail in root.findall('.//Detail'):
        item = {}
        for child in detail:
            item[child.tag] = child.text if child is not None and child.text is not None else None
        result.append(item)

    # Parse Detail2 elements
    for detail2 in root.findall('.//Detail2'):
        item = {}
        for child in detail2:
            item[child.tag] = child.text if child is not None and child.text is not None else None
        result.append(item)

    # Parse HeaderData if present
    header_data = root.find('.//HeaderData')
    if header_data is not None:
        header_dict = {}
        for child in header_data:
            header_dict[child.tag] = child.text if child is not None and child.text is not None else None
        result.append({"HeaderData": header_dict})

    return result

def get_safe_text(element, tag):
    child = element.find(tag)
    return child.text if child is not None and child.text is not None else None

def parse_expenses(xml_string):
    try:
        root = ET.fromstring(xml_string)
    except ET.ParseError as e:
        raise ValueError(f"Invalid XML: {e}")

    expenses = []

    for detail in root.findall('.//Detail'):
        expense = {
            'Type': get_safe_text(detail, 'TypeValue'),
            'Expense Type': get_safe_text(detail, 'ExpenseType'),
            'Date': get_safe_text(detail, 'DateValue'),
            'No': get_safe_text(detail, 'No'),
            'Amount': get_safe_text(detail, 'Amount'),
            'Description': get_safe_text(detail, 'DescriptionValue'),
            'Currency': get_safe_text(detail, 'CurrencyValue'),
            'Direct Payment': get_safe_text(detail, 'DirectPayment'),
            'Expense Error': get_safe_text(detail, 'ExpenseError'),
            'No Document': get_safe_text(detail, 'NoDocument'),
            'Verify': get_safe_text(detail, 'Verify'),
            'Feedback': get_safe_text(detail, 'Feedback')  # Added this field
        }
        expenses.append(expense)

    return expenses

def parse_travel(xml_string):
    try:
        root = ET.fromstring(xml_string)
    except ET.ParseError as e:
        raise ValueError(f"Invalid XML: {e}")

    travel_data = []

    for detail in root.findall('.//Detail'):
        travel_item = {
            'No': get_safe_text(detail, 'No'),
            'ExpenseType': get_safe_text(detail, 'ExpenseType'),
            'Description': get_safe_text(detail, 'DescriptionValue'),
            'Value': get_safe_text(detail, 'Amount'),
            'Unit': get_safe_text(detail, 'CurrencyValue'),
            'MilageType': get_safe_text(detail, 'MilageType'),
            'Capacity': get_safe_text(detail, 'Capacity'),
            'Milage': get_safe_text(detail, 'Milage')
        }
        travel_data.append(travel_item)

    for detail2 in root.findall('.//Detail2'):
        travel_item = {
            'MilageType': get_safe_text(detail2, 'MilageType'),
            'MilageError': get_safe_text(detail2, 'MilageError'),
            'Capacity': get_safe_text(detail2, 'Capacity'),
            'DateValue': get_safe_text(detail2, 'DateValue'),
            'No': get_safe_text(detail2, 'No'),
            'Milage': get_safe_text(detail2, 'Milage'),
            'DescriptionValue': get_safe_text(detail2, 'DescriptionValue')
        }
        travel_data.append(travel_item)

    return travel_data