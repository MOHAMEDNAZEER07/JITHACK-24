import logging
from django.http import JsonResponse
from django.shortcuts import render
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms.ollama import Ollama


def llm(request):
    if request.method == 'POST':
        
        input_txt = request.POST.get('query')
        if not input_txt:
            return JsonResponse({'error': 'No query provided'}, status=400)
            

        prompt = ChatPromptTemplate.from_messages([
            ("system", "you are a helpful AI assistant. Your name is Plant's Doctor"),
            ("user", "user query: {query}")
        ])
            
        llm = Ollama(model="llama3")
        output_parser = StrOutputParser()
        chain = prompt | llm | output_parser
            
        result = chain.invoke({"query": input_txt})
        return JsonResponse({'result_llm': result}, status=200)
    
    return render(request, 'llm.html')
