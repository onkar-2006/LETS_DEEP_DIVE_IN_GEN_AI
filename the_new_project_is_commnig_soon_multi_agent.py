# -*- coding: utf-8 -*-
"""the new project is commnig soon-multi-agent.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1frTVQBRasQoZsAspwlU6AEPBdQUTrr7O
"""

#lets start to building the project this project is nothing but tte boom all the info about the project a i hve write deep discription of the project



#what is the crewai :the crew ai is the platfrom that have capebility or nothing but the framework that create the multiagent :
#what is the multiagnt : this are the nothing but the similar to our simple angent its work as a  simple human that are perfrom the specific task that have given perfrom

#why we used the cre ai :the crew ai is the frame work which provider  the fuctionlity u can crete ur big project easilty with low code writing
#lets start explore the crew ai

#requirment.txt

crewai
crewai_tools

#agent.py
from tools import yt_tools
from crewai import Agent

import os
from dotenv import load_dotenv
os.environ["openai api key"]=os.getenv("open ai api key")
os.environ["open ai model name"]="chatgpt=4-1025"

#create sinier blog content reasearcher

blog_researcher=Agent(
    role="blog reaseacher from you-tube videos"
    goal="get the relevent video content from the topic{topic} from yt channel"
    verbose=True,
    memory=True,
    backstory=(
       " he is an expert in the data science and also he is the sinier sofwere devopler"
    ),
    tool=[yt_tools]
    allow_delegetion=True,

)

#create a sinier bog writer agent form the yt videos
blog_writer=(
    role="writer",
    goal="narrate compiling the tech stories about the video {topic} from youtube chhanel",
    verbose=True,
    memory=True,
    backstory=("with the flair for the simplify the complex topics  and also engaging the captive and adcive"
    ),
    tools=[yt_tools],
    allow_delegetion=False,
)

#tool.py
from creai_tools import YoutubeChannelSearchTool
yt_tools=YoutubeChannelSearchTool(handler="@krishnaik06")

#task.py
from crewai import Task
from tools import tool
from agents import blog_reasearcher, blog_writer

import os
from dotenv import load_dotenv
os.environ["openai api key"]=os.getenv("open ai api key")
os.environ["open ai model name"]="chatgpt=4-1025"


reasearch_task=Task(
    discription=(
        "identify the video {topic}",
        "get the details info of video from the channel on the topic {topic}",

    ),
    expected_output="a comperesive three paragraph  long report based on the topic  of video of the content",
    tool=[tool_yt],
    agent=blog_researcher
)
writer_task=Task(
    discription=(
        "identify the video {topic}",
        "get the details info of video from the channel on  the topic {topic}",

    ),
    expected_output="summersize the info from the youtube channel video on the topic {topic} and create the content for the blog",
    tool=[tool_yt],
    agent=blog_writer,
    async_execution=False,
    outputfile="new_blog_post.md",


)

#crew.py
from crewai import Crew , Process
from agents import blog_reasearch , blog_writer
from tasks import reaserch_task , write_task

crew=Crew(
    agents=[blog_researcher, blog_writer],
    task=[reasearch_task  ,write_task],
    process=process.sequential
    memort=True,
    cache=True,
    max_rpm=True,
    share_crew=True,


)

result=crew.kickoff(inputs={'topic':'ai vs ml vs ds vs ml'})
print(result)