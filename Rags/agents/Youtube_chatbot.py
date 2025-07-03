#%%
import os 
os.environ["OPENAI_API_KEY"]="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"
from youtube_transcript_api import YouTubeTranscriptApi, TranscriptsDisabled
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_community.vectorstores import FAISS
from langchain_core.prompts import PromptTemplate

video_id="FASMejN_5gs"

try:
    transcript_list= YouTubeTranscriptApi.get_transcript(video_id,languages=['en'])
    
    transcript = " ".join(chunk["text"] for chunk in transcript_list)

    print(transcript)
    
except TranscriptsDisabled:
    print(" there is no caption for this video on YT")
    
transcript_list

#%%
splitter=RecursiveCharacterTextSplitter(chunk_size=1000,chunk_overlap=100)
chunks=splitter.create_documents([transcript])

len(chunks)

#%%

chunks[40]

#%%
embedding=OpenAIEmbeddings(model='text-embedding-3-small')
vector_store=FAISS.from_documents(chunks,embedding)


vector_store.index_to_docstore_id
#%%
vector_store.get_by_ids(['1c8f1b4f-d441-4ad2-9afd-2b31deb9e556'])

# %%
retriver=vector_store.as_retriever(search_type='similarity', search_kwargs={"k": 1})

retriver
#%%

retriver.invoke("what is imageNet")
# %%
llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.2)


prompt = PromptTemplate(
    template="""
      You are a helpful assistant.
      Answer ONLY from the provided transcript context.
      If the context is insufficient, just say you don't know.

      {context}
      Question: {question}
    """,
    input_variables = ['context', 'question']
)
#%%
Que=" what is neuralink? explain in details  "
retrieved_docs    = retriver.invoke(Que)
retrival_docs=retriver.invoke(Que)

retrival_docs
#%%
context_text = "\n\n".join(doc.page_content for doc in retrieved_docs)
context_text
final_prompt = prompt.format(context=context_text, question=Que)
final_prompt

#%%
answer = llm.invoke(final_prompt)
print(answer.content)
# %%

from langchain_core.runnables import RunnableParallel, RunnablePassthrough, RunnableLambda
from langchain_core.output_parsers import StrOutputParser

def format_docs(retrieved_docs):
  context_text = "\n\n".join(doc.page_content for doc in retrieved_docs)
  return context_text

parallel_chain = RunnableParallel({
    'context': retriver | RunnableLambda(format_docs),
    'question': RunnablePassthrough()
})


#%%
parallel_chain.invoke(" what is Neuralink study. ")
# %%
parser= StrOutputParser()

final= parallel_chain| prompt| llm|parser

# %%

result = final.invoke("Can you summarize the video")
# %%
print(result)
# %%
