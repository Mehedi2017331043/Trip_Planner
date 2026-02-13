import os 
import datetime
from dotenv import load_dotenv
from fastapi import FastAPI
from pydantic import BaseModel
from agent.agentic_workflow import GraphBuilder
from starlette.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from utils.save_to_document import save_document 

load_dotenv()
app=FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # set specific origins in prod
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

class QueryRequest(BaseModel):
    question: str

@app.post('/query')
async def query_traval_agent(query: QueryRequest):
    try:
        print('hi')
        graph=GraphBuilder(model_provider='groq')
        print(graph)
        react_app=graph()
        png_graph=react_app.get_graph().draw_mermaid_png()
        with open("my_graph.png", 'wb') as file:
            file.write(png_graph)
        messages = {'messages': [query.question]}
        output = react_app.invoke(messages)

        # If result is dict with messages
        if isinstance(output, dict) and 'messages' in output:
            final_output = output['messages'][-1].content # Last AI response
        else:
            final_output=str(output)
        return {'answer': final_output}
    
    except Exception as e:
        return JSONResponse(status_code=500, content={'error': str(e)})
    
 