# -*- coding: utf-8 -*-
"""its_your_code_assitant_by_using_code_llama.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1zfTFJZGoN6muhXlcLlO9cTqTSUjrRi6f
"""

#HI Rm rM BHAI SARANU
#NOW WHY WE USED THE CHATGPT TO ASK OUR CODE RELETED QUERY INSTED OF THAT LETAS CREATE OUR OWN AGENT THAT WILL ALWAYS STAY EITH U TO HELP U

#LETS STARTT THE IMPLIMENTING ANGENT OR THE OUR OWN ASSITANT

#IN THE REQUEIREMNT.TXT DOWMLOAD -LANGCHAIN, GRADIO
#now after that the creation of the of the requirment.txt ntext step is

#create our modelfile
 FROM codellama

##Set The Tempreture
PARAMETER tempreture 1

#Set The SystemPrompt
SYSTEM"""
you are code convertor from one language of code into anather language  and u are creted by the onkar kshirsagar
answer all the question releted to code
"""

#now our our requiemrnt and the modelfile is ready next step to create the interface and addd the backend fuctionality for the codellama

#so create the app.py
import requests
import gradio as gr
import json

url="http://localhost:11434/api/generate"

headers={
    'Content-Type':'application/json'
}

histroy=[]

def generate_responce(prompt):
  history.append(prompt)
  final_prompt="\n".join(history)

  data={
      "model":"codeguru",
      "prompt":"final_prompt",
      "stream":False

  }

  responce=request.post(url , headers=headers,data=json.dump(data))

  if responce.status_code==200:
    responce=responce.text
    data=json.load(responce)
    actual_responce=data["responce"]
    retrun actual_responce
  else:
    print("error":responce.text)

interface=gr.interface(
    fn=generate_responce,
    input=gr.TextBox(lines=4 , placeholder="entr your prompt"),
    outputs="text"

)

interface.launch()

#first activate your invoriemnt: conda activate venv/

#to run this perticular code just run pip install -r requirment.txt
#run app.py
and u get the link of the output