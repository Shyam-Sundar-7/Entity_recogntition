from datetime import datetime
from langchain.output_parsers.openai_functions import JsonOutputFunctionsParser
from langchain_openai import ChatOpenAI
from typing import List
from pydantic import BaseModel, Field
from langchain_community.utils.openai_functions import convert_pydantic_to_openai_function
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv
load_dotenv()



class Product(BaseModel):
    """Information about a Product."""
    Name: str = Field(None,description="Product Name of a product")
    Price: float = Field(None,description="Total amount of the product")
    
class Extraction_with_products(BaseModel):
    """ Extract the entities from the invoice document"""
    transaction_id :str =Field(None,description="Payment Transaction ID of the invoice document file")
    amount : float = Field(None,description="Total Invoice value of the invoice document file")
    datetime_field: datetime = Field(None,description="The date and time (24-hour format) when the payment was made.")
    mode_of_payment :str=Field(None,description="Tells about the mode of payment the user proceeeded")
    Products:List[Product] =Field(None,description="Tells about the details of list of products")

class Extraction(BaseModel):
    """ Extract the entities from the invoice document"""
    transaction_id :str =Field(None,description="Payment Transaction ID of the invoice document file")
    amount : float = Field(None,description="Total Invoice value of the invoice document file")
    datetime_field: datetime = Field(None,description="The date and time (24-hour format) when the payment was made.")
    mode_of_payment :str=Field(None,description="Tells about the mode of payment the user proceeeded") 
    
     
def extract_features(document):


    model = ChatOpenAI(temperature=0)
    function = [convert_pydantic_to_openai_function(Extraction)]
    prompt_template="""You are tasked with extracting specific fields from an invoice document. The fields you need to extract are:

    1. Transaction ID
    2. Amount
    3. Date and Time (combined)
    4. Mode of Payment

    Please extract the following fields from the given invoice document. If any field cannot be extracted, set its value to `null`. 

    Invoice Document :{Document}
    """
    prompt_template = ChatPromptTemplate.from_template(prompt_template)
    llm_model = (
        prompt_template
        | model.bind(functions=function) 
        | JsonOutputFunctionsParser() 
    )
    return llm_model.invoke({
        "Document":document
    })
    
def extract_features_with_products(document):


    model = ChatOpenAI(temperature=0)
    function = [convert_pydantic_to_openai_function(Extraction_with_products)]
    prompt_template="""You are tasked with extracting specific fields from an invoice document. The fields you need to extract are:

1. Transaction ID
2. Amount
3. Date and Time (combined)
4. Mode of Payment
5. 5. List of Products (each product has a Name and Amount)

Please extract the following fields from the given invoice document. If any field cannot be extracted, set its value to `null`. 

Invoice Document :{Document}
"""
    prompt_template = ChatPromptTemplate.from_template(prompt_template)
    llm_model = (
        prompt_template
        | model.bind(functions=function) 
        | JsonOutputFunctionsParser() 
    )
    return llm_model.invoke({
        "Document":document
    })