from typing import Any, List
from pydantic import BaseModel
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from langchain_core.language_models.base import BaseLanguageModel

class Creator:
    
    def __init__(self, llm:BaseLanguageModel = None):
        if llm is None:
            raise ValueError("llm shouldn't be null")
        self.llm = llm
        
    def create_question_variants(self, response_model: BaseModel, questions = List[str], answer = str):
        
        if response_model is None:
            raise ValueError("response_model shouldn't be null")
        
        if questions is None:
            raise ValueError("questions shouldn't be null")
        
        if answer is None:
            raise ValueError("answer shouldn't be null")
        
        output_parser = PydanticOutputParser(pydantic_object=response_model)
        
        prompt = PromptTemplate(
            template="""
            너는 질문과 응답을 생성하는 역할을 담당해. 질문 목록과 하나의 응답을 제공할테니 동일한 응답값을 출력할 수 있는 질문 리스트를 제공해야해.
            질문 리스트는 10개 이상이 될 수 있도록 해줘.\n{format_instructions}\n{query}
            """,
            input_variables=["query"],
            partial_variables={"format_instructions": output_parser.get_format_instructions()}
        )
        
        query = {"query":f"question : {questions}\nresponse : {answer}"}   
        
        chain = prompt | self.llm | output_parser
        result = chain.invoke(query)
        return result
        
    def create_answer_variants(self, response_model=BaseModel, question = str, answers = List[str]):
                
        if response_model is None:
            raise ValueError("response_model shouldn't be null")
        
        if question is None:
            raise ValueError("questions shouldn't be null")
        
        if answers is None:
            raise ValueError("answer shouldn't be null")
        
        output_parser = PydanticOutputParser(pydantic_object=response_model)
        
        prompt = PromptTemplate(
            template="""
            너는 질문과 응답을 생성하는 역할을 담당해. 질문에 맞는 응답 목록을 제공할테니 적절한 응답을 추가해줘.
            응답 리스트는 10개 이상이 될 수 있도록 해줘.\n{format_instructions}\n{query}
            """,
            input_variables=["query"],
            partial_variables={"format_instructions": output_parser.get_format_instructions()}
        )
        
        query = {"query":f"question : {question}\nresponse : {answers}"}   
        
        chain = prompt | self.llm | output_parser
        result = chain.invoke(query)
        return result
        
    def create_dataset_variants(self, response_model=BaseModel, questions = List[str], qa_sample = List[Any], expend_question : bool = True):
        
        if response_model is None:
            raise ValueError("response_model shouldn't be null")
        
        if qa_sample is None:
            raise ValueError("qa_sample shouldn't be null")
        
        if questions is None:
            raise ValueError("questions shouldn't be null")
        
        _prompt_added = ""
        if expend_question:
            _prompt_added="타겟 질문 리스트 외 다른 경우의 수에 대한 질문 및 응답 리스트도 추가적으로 생성해줘"

        output_parser = PydanticOutputParser(pydantic_object=response_model)
        
        prompt = PromptTemplate(
            template="""
            너는 질문과 응답을 생성하는 역할을 담당해. 예시가 되는 질문 목록과 응답 목록인 qa_sample을 제공할테니 이를 참고해서 새로운 질문 및 응답 리스트를 생성해줘.
            타겟이 되는 질문 리스트는df question 항목을 참고하도록 하고, 질문 및 응답 리스트는 10개 이상이 될 수 있도록 해줘. {prompt_added} \n{format_instructions}\n{query}
            """,
            input_variables=["query"],
            partial_variables={
                "format_instructions": output_parser.get_format_instructions(),
                "prompt_added": _prompt_added}
        )
        
        query = {"query":f"#questions\n{questions}\n\n#qa_sample\n{qa_sample}"}   
        
        chain = prompt | self.llm | output_parser
        result = chain.invoke(query)
        return result
        