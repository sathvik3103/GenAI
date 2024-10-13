!pip install streamlit

!pip install langchain

!pip install langchain_community

import streamlit as st
from langchain.prompts import PromptTemplate
from langchain_community.llms import CTransformers

## Function to get response from LLAma 2 model

def getLLamaresponse(input_text,no_words,blog_style):

    ### LLama2 model
    llm=CTransformers(model='models/llama-2-7b-chat.ggmlv3.q8_0.bin',
                      model_type='llama',
                      config={'max_new_tokens':256,
                              'temperature':0.01})
    ## Prompt Template

    template = """
You are a {blog_style}. Your task is to write an engaging and informative blog post on the topic: "{input_text}". The blog should be approximately {no_words} words in length.

Guidelines:

Introduction: Start with an attention-grabbing introduction that provides an overview of the topic.
Body: Divide the content into clear, logical sections using subheadings. Provide in-depth information, insights, and analysis relevant to {blog_style}.
Conclusion: Summarize the key points and provide a compelling closing thought or call to action.

Writing Style:

Write in a tone that is professional yet approachable.
Use clear, concise language free of jargon (unless explaining technical terms).
Include real-world examples, statistics, or anecdotes to illustrate key points.
Ensure the content is original and free from plagiarism.

SEO Considerations:

Incorporate relevant keywords naturally throughout the text.
Use meta descriptions and title tags effectively (if applicable).

Proofreading:

Check for grammatical accuracy and correct spelling.
Ensure proper punctuation and sentence structure.

By following these guidelines, produce a high-quality blog post that offers value to readers interested in {input_text} within the {blog_style} industry.
"""


    prompt=PromptTemplate(input_variables=["blog_style","input_text",'no_words'],
                          template=template)

    ## Generate the ressponse from the LLama 2 model
    response=llm(prompt.format(blog_style=blog_style,input_text=input_text,no_words=no_words))
    print(response)
    return response

st.set_page_config(page_title="Generate Blogs",
                    page_icon='🤖',
                    layout='centered',
                    initial_sidebar_state='collapsed')

st.header("Generate Blogs 🤖")

input_text=st.text_input("Enter a Topic on which you would like to generate a Blog")

## creating to more columns for additonal 2 fields

col1,col2=st.columns([5,5])

with col1:
    no_words=st.text_input('No of Words')
with col2:
    blog_style=st.selectbox('Writing the blog for',
                            ('AI Researcher','Graduate Student','Common Man'),index=0)

submit=st.button("Generate")

## Final response
if submit:
    st.write(getLLamaresponse(input_text,no_words,blog_style))
