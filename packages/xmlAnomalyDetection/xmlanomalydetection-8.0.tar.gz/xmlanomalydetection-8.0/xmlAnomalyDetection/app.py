from fastapi import FastAPI, File, UploadFile

from typing import List

import xml.etree.ElementTree as ET
from langchain.output_parsers.openai_tools import PydanticToolsParser
from pydantic import BaseModel as BaseModelPydantic
from langchain.pydantic_v1 import BaseModel, Field
from typing import Optional, List
from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq
import uvicorn
import json
from langchain_core.output_parsers import StrOutputParser
import yaml
import os
from loguru import logger
from xmlAnomalyDetection.parsers import ParserApplier

os.environ['GROQ_API_KEY']='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'
YAML_PROMPTS_PATH = os.path.join(os.path.dirname(__file__), 'prompts.yaml')
with open(YAML_PROMPTS_PATH, 'r') as file:
    _all_prompts = yaml.safe_load(file)
    logger.debug(f"all prompts: {_all_prompts.keys()}")

app = FastAPI(
    title="Anomaly Detection API",
    description="An API for detecting anomalies in expense data submitted by company's employees.",
    version="1.0.0",
    docs_url="/",

)


class XMLData(BaseModelPydantic):
    xml_string: str


# ======================================================
#      OUTPUT PARSERS 
# ======================================================
def get_parser_class(parser_name: str):
    """
    Get the parser class by its string name
    """
    return parser_classes.get(parser_name)

class anomaly_parser(BaseModel):
    """
    find anomalies in the user entered data
    """
    anomalies: Optional[List[str]] = Field(None, description="List of strings, each string defines an anomaly")
    reason: Optional[List[str]] = Field(None, description="List of reasons stating why is this marked as anomaly")
llm_to_string = StrOutputParser()

parser_classes = {
    "anomaly_parser": anomaly_parser,
    
}



def all_parsers(xml_str):
    """
    apply all the parsers

    Parameters
    ----------
    xml_str : str
        string representation of xml

    Returns
    -------
    str
    """
    parser_applier = ParserApplier()
    result = parser_applier.apply_all_parsers(xml_str)
    return result


def initialize_chain(type_template: str, use_parser: bool = False, parser_name: str = None):
    """
    Initialize the chain for anomaly detection.

    This function sets up the parser, model, prompt, and chain for detecting anomalies in expense data.

    Parameters
    ----------
    type_template : str
        Type of template to use for the chain. It can be "parse_aggregated_data" or "parsed_data_cleaning".
    use_parser : bool, optional
        Whether to use a parser in the chain, by default False.
    parser_name : str, optional
        Name of the parser to use if use_parser is True, by default None.

    Returns
    -------
    Chain
        A chain object that combines the prompt, model, and parser for anomaly detection.

    Notes
    -----
    The function uses the following components:
    - PydanticToolsParser with the specified parser tool (if use_parser is True)
    - ChatGroq model with "llama-3.1-70b-versatile" and temperature 0
    - ChatPromptTemplate from predefined prompts in _all_prompts
    """
    prompt = ChatPromptTemplate.from_messages(
        [("system", _all_prompts[type_template]["system_prompt"]),
         ("user", _all_prompts[type_template]["user_prompt"])
         
         ],
    
    )
    
    if use_parser:
        logger.info(f"using model with parser")
        logger.info(f"parser name: {parser_name}")
        parser_class = get_parser_class(parser_name)
        if parser_class is None:
            raise ValueError(f"Parser class '{parser_name}' not found")
        parser = PydanticToolsParser(tools=[parser_class])
        model = ChatGroq(model="llama-3.1-70b-versatile", temperature=0).bind_tools([parser_class])
        chain = prompt | model | parser
    else:
        logger.info(f"using model without parser")
        model = ChatGroq(model="llama-3.1-70b-versatile", temperature=0)
        chain = prompt | model
    
    return chain




class AnomalyResponse(BaseModelPydantic):
    anomalies: List[str]
    reasons: List[str]

@app.post("/detect_anomaly", tags=["Anomaly Detection"], response_model=AnomalyResponse)
async def detect_anomaly(xml_file: UploadFile = File(...)):
    """
    Detect anomalies in expense data submitted as an XML file.

    This endpoint processes an uploaded XML file containing expense data,
    applies various parsers, and uses a series of language models to detect
    anomalies in the expenses.

    Parameters:
    -----------
    xml_file : UploadFile
        The XML file containing expense data to be analyzed.

    Returns:
    --------
    AnomalyResponse
        An object containing two lists:
        - anomalies: A list of strings describing detected anomalies.
        - reasons: A list of strings providing reasons for each detected anomaly.

    Process:
    --------
    1. Reads and decodes the uploaded XML file.
    2. Applies all parsers to extract and structure the data.
    3. Processes the parsed data through a series of language model chains:
       a. Parses aggregated data
       b. Converts parsed data to a markdown table
       c. Analyzes the markdown table to find anomalies
    4. Writes intermediate results to files for debugging purposes.
    5. Returns the detected anomalies and their reasons.

    Raises:
    -------
    HTTPException
        If there's an error in processing the file or detecting anomalies.

    Notes:
    ------
    - The function uses several external files and models, ensure all
      dependencies are properly set up.
    - Intermediate results are saved in 'parsed_data.txt' and 'markdown_table.md'.
    """
    xml_string = await xml_file.read()
    xml_string = xml_string.decode("utf-8")  # Specify the correct encoding here
    #data_as_dict = extract_data_from_xml(xml_string)
    parsed_string = all_parsers(xml_string)
    logger.info(f"all parsers applied")
    #results = chain.invoke({"xml_extracted": json.dumps(data_as_dict)})
    
    with open("parsed_data.txt", "w") as f:
        f.write(parsed_string)
        
    chain_parse_aggregated_data = initialize_chain("parse_aggregated_data", use_parser=False) | llm_to_string
    logger.info(f"chain initialized for parsing the aggregated data")
    all_parsers_raw_tables = chain_parse_aggregated_data.invoke({"xml_extracted": parsed_string})
    logger.debug(f"results: {all_parsers_raw_tables}")
    
    chain_convert_to_table = initialize_chain("parsed_data_cleaning", use_parser=False) | llm_to_string
    markdown_table = chain_convert_to_table.invoke({"parsed_data": all_parsers_raw_tables})
    logger.debug(f"markdown table: {markdown_table}")

    with open("markdown_table.md", "w") as f:
        f.write(markdown_table)
    logger.info("user expenses cleaned Markdown table written to markdown_table.md")
    
    chain_find_anomalies = initialize_chain("find_anomalies", use_parser=True, parser_name="anomaly_parser")
    anomalies = chain_find_anomalies.invoke({"markdown_table": markdown_table})
    logger.debug(f"anomalies: {anomalies[0]}")
    return {"anomalies": anomalies[0].anomalies, "reasons": anomalies[0].reason}

def runserver():
    uvicorn.run(app, host='0.0.0.0', port=8357, log_level="debug")
