from django.shortcuts import render
import openai
import os
from dotenv import load_dotenv
# Create your views here.

load_dotenv()
def qa_view(request):
    answer = None
    print('request.method',request.method)
    if request.method == 'POST':
        question = request.POST.get('question')  # 폼에서 가져옮
        response = openai.chat.completions.create(
            model = 'gpt-4o',
            messages = [
                {'role':'user','content':question}
            ]
        )        
        answer = response.choices[0].message.content        
    return render(request,'qa/index.html',{'answer':answer})