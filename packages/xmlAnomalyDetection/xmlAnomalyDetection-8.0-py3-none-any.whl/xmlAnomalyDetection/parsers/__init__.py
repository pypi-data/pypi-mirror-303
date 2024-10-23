from functools import wraps
from typing import List, Dict
from .all_parsers import *

def apply_parsers(func):
    @wraps(func)
    def wrapper(self, xml_string: str):
        parsed_data = parse_xml(xml_string)
        parse_expense_xml_result = parse_expense_xml(xml_string)
        headers, details = parser_headers(xml_string)
        tables = parse_xml_another(xml_string)
        travel_details = travel_parser(xml_string)
        details_ = details_parse_xml(xml_string)

        # Combine the results into a single string
        combined_results = self._combine_results(parsed_data, parse_expense_xml_result, headers, details, tables,
                                                 travel_details, details_)

        return combined_results

    return wrapper


class ParserApplier:
    def __init__(self):
        self.parsers = [
            parse_xml,
            parse_expense_xml,
            parser_headers,
            parse_xml_another,
            travel_parser,
            details_parse_xml
        ]

    def _combine_results(self, *args):
        combined_results = []
        for arg in args:
            if isinstance(arg, list):
                combined_results.extend(arg)
            else:
                combined_results.append(arg)

        # Convert the list of dictionaries to a string
        result_string = self._dicts_to_string(combined_results)

        return result_string

    def _dicts_to_string(self, dicts: List[Dict]) -> str:
        result_string = ""
        for dict_ in dicts:
            for key, value in dict_.items():
                result_string += f"{key}: {value}\n"
        return result_string

    def apply_all_parsers(self, xml_string: str):
        return self._apply_parsers(xml_string)

    def _apply_parsers(self, xml_string: str):
        parsed_data = parse_xml(xml_string)
        parse_expense_xml_result = parse_expense_xml(xml_string)
        headers, details = parser_headers(xml_string)
        tables = parse_xml_another(xml_string)
        travel_details = travel_parser(xml_string)
        details_ = details_parse_xml(xml_string)

        # Combine the results into a single string
        combined_results = self._combine_results(parsed_data, parse_expense_xml_result, headers, details, tables,
                                                 travel_details, details_)

        return combined_results



#parser_applier = ParserApplier()

#result = parser_applier.apply_all_parsers(df['ModelData'][42])
#print(result)