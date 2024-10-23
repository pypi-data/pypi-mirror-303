import xml.etree.ElementTree as ET

def parse_xml(xml_string):
    root = ET.fromstring(xml_string)
    details = root.findall('.//Detail')
    result = []

    for detail in details:
        item = {
            'No': detail.find('No').text,
            'TypeValue': detail.find('TypeValue').text,
            'DirectPayment': detail.find('DirectPayment').text,
            'ExpenseType': detail.find('ExpenseType').text,
            'ExpenseError': detail.find('ExpenseError').text,
            'DateValue': detail.find('DateValue').text,
            'NoDocument': detail.find('NoDocument').text,
            'CurrencyValue': detail.find('CurrencyValue').text,
            'Amount': detail.find('Amount').text,
            'DescriptionValue': detail.find('DescriptionValue').text,
            'Verify': detail.find('Verify').text
        }
        result.append(item)

    return result



def parse_expense_xml(xml_string):
    """
    Parse the XML string and extract the user-entered items.

    Args:
        xml_string (str): The XML string to parse.

    Returns:
        list: A list of dictionaries, where each dictionary represents a user-entered item.
    """
    # Parse the XML
    root = ET.fromstring(xml_string)

    # Extract the user-entered items
    details = root.findall('.//Detail')

    # Create a list to store the user-entered items
    expenses = []

    # Iterate over the details and extract the user-entered items
    for detail in details:
        expense = {
            'Type': detail.find('TypeValue').text,
            'Expense Type': detail.find('ExpenseType').text,
            'Date': detail.find('DateValue').text,
            'No': detail.find('No').text,
            'Amount': detail.find('Amount').text,
            'Description': detail.find('DescriptionValue').text,
            'Currency': detail.find('CurrencyValue').text
        }
        expenses.append(expense)

    return expenses


def parser_headers(xml_string):
    root = ET.fromstring(xml_string)
    core_model = root.find('CoreModel')
    model_process_data = root.find('ModelProcessData')
    header_data = model_process_data.find('HeaderData')
    details = model_process_data.findall('Detail')

    # Extract Header Data
    header_dict = {}
    for child in header_data:
        header_dict[child.tag] = child.text

    # Extract Details
    details_list = []
    for detail in details:
        detail_dict = {}
        for child in detail:
            detail_dict[child.tag] = child.text
        details_list.append(detail_dict)

    return header_dict, details_list




def parse_xml_another(xml_string):
    root = ET.fromstring(xml_string)
    result = []

    for model_process_data in root.findall('.//ModelProcessData'):
        for detail2 in model_process_data.findall('.//Detail2'):
            detail_dict = {}
            for child in detail2:
                detail_dict[child.tag] = child.text
            result.append(detail_dict)

        for detail in model_process_data.findall('.//Detail'):
            detail_dict = {}
            for child in detail:
                detail_dict[child.tag] = child.text
            result.append(detail_dict)

    return result


def travel_parser(xml_string):
    root = ET.fromstring(xml_string)
    data = []

    # Extract expense details
    for detail in root.findall('.//Detail'):
        expense = {
            'No': detail.find('No').text if detail.find('No') is not None else None,
            'ExpenseType': detail.find('ExpenseType').text if detail.find('ExpenseType') is not None else None,
            'Description': detail.find('DescriptionValue').text if detail.find('DescriptionValue') is not None else None,
            'Value': detail.find('Amount').text if detail.find('Amount') is not None else None,
            'Unit': detail.find('CurrencyValue').text if detail.find('CurrencyValue') is not None else None,
            'MilageType': detail.find('MilageType').text if detail.find('MilageType') is not None else None,
            'Capacity': detail.find('Capacity').text if detail.find('Capacity') is not None else None,
            'Milage': detail.find('Milage').text if detail.find('Milage') is not None else None
        }
        data.append(expense)

    return data




def details_parse_xml(xml_string):
    # Parse the XML string
    root = ET.fromstring(xml_string)

    # Initialize the list of dictionaries
    data = []

    # Iterate over the 'Detail' elements
    for detail in root.findall('.//Detail'):
        row = {
            'TypeValue': detail.find('TypeValue').text,
            'DirectPayment': detail.find('DirectPayment').text,
            'Feedback': detail.find('Feedback').text,
            'ExpenseType': detail.find('ExpenseType').text,
            'ExpenseError': detail.find('ExpenseError').text,
            'DateValue': detail.find('DateValue').text,
            'NoDocument': detail.find('NoDocument').text,
            'CurrencyValue': detail.find('CurrencyValue').text,
            'No': detail.find('No').text,
            'Amount': detail.find('Amount').text,
            'DescriptionValue': detail.find('DescriptionValue').text,
            'Verify': detail.find('Verify').text
        }
        data.append(row)

    # Iterate over the 'Detail2' elements
    for detail2 in root.findall('.//Detail2'):
        row = {
            'MilageType': detail2.find('MilageType').text,
            'MilageError': detail2.find('MilageError').text,
            'Capacity': detail2.find('Capacity').text,
            'DateValue': detail2.find('DateValue').text,
            'No': detail2.find('No').text,
            'Milage': detail2.find('Milage').text,
            'DescriptionValue': detail2.find('DescriptionValue').text
        }
        data.append(row)

    return data


