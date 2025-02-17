# -*- coding: utf-8 -*-
"""you_tube_video_summerization.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/11w_g_3weI1a1c2LAhXSzOHangv3RpOq_
"""

#import the requird libraries
from langchain.promts import PromptTemplate
import streamlit,validators as st
from langchain.chains.summarize import load_summarize_chain
from langchain_communiy.document_loaders import YoutubeLoader , UnstructuredURLLoader
from langchain.groq import Chatgroq


#lets create the streamlit app

#creation of the title and the subtitle
st.set_page_config(page_title="summerize yotube video into text",page_icon="")
st.title("summerize the youtubevideo into text")
st.subheader("Summerize urls")

#get the groq api key
with st.sidebar:

  groq_api_key=st.text_input("groq api key" , value="" , type="password")

#taking the url form the youtube or webiste
generic_url=st.text_input("URL" , user_visibility="collapsed")

#loading the model gamma from the grq
llm=ChatGroq(model="gamma-7b-it" ,"groq_api_key"="groq_api_key" )

#ctreate a promt template
prompt_template="""
provider a summary of the follwing context in 300 words:
context:"{text}

"""
#cretion of the promt
promt=PromtTemplate(template=promt_template , input_varible=["text"])

#
if st.button("summerize the content from utube video or website"):

  if not groq_api_key.strip() or not generic_url.strip():
    st.error("please provide the information")

  elif not velidators.url(generic_url):
    st.error("please provide the a valid url  it may be youtube video or website page")
  else:
    try:
      with st.spinner("waiting.."):

        if "youtube.com" in generic_url:
          loader=YoutubeLoader.from_youtube_loader(generic_url , add_video ,info=True)
        else:
          loader=UnstructuredURLLoader(urls=["generic_url"] ,ssl_verify=False , headers={})

        docs=loader.load()

        chain=load_summarize_chain(llm , chain_type='stuff' , prompt=prompt)
        output_summary=chain.run(docs)

        st.success(output_summary)

    except Exception as e:
      st.Exception(f"Exception:e")