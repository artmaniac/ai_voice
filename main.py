# 배포할때는 서버에서 따로 쓰므로 주석처리한다.
#from dotenv import find_dotenv, load_dotenv
#load_dotenv(find_dotenv())


from transformers import pipeline
from langchain·prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.chat_models import ChatOpenAI
'''
pip install python-dotenv

'''


# .env 파일에서 읽어온 환경 변수 출력

import os
# .env 파일에서 API_KEY 가져오기
api_key = os.environ.get("API_KEY")

image_text = img2txt( " llama2.png")

# 텍스트를 기반으로 이야기 생성
def story_making(context):
    template = """ 
    당신은 이야기꾼입니다. 
    간단한 스토리에 기반한 짧은 이야기를 생성할 수 있습니다. 이야기는 30단어를 넘지 않아야 합니다. 
    맥락: {context} 
    이야기: 
    """
    prompt = PromptTemplate(template=template, input_variables=["context"])
    story_llm = LLMChain(llm=ChatOpenAI (
        model_name="gpt-3.5-turbo", temperature=0.8)
        , prompt=prompt, verbose=True)

    story = story_llm.predict(context=context, max_length=50)
    print("생성된 이야기:", story)
    return story

# 추출된 텍스트를 사용하여 generate_story 호출
story_making(image_text)