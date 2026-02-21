from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from app.orchestrator import DarkGPT_Orchestrator
from app.mesh import InnovationMesh

app = FastAPI(title="DarkGPT Pro Global API")

orchestrator = DarkGPT_Orchestrator()
mesh = InnovationMesh()

class ChatRequest(BaseModel):
    query: str
    language: str

class IdeaRequest(BaseModel):
    title: str
    description: str
    author: str

@app.post("/chat")
async def chat(request: ChatRequest):
    try:
        reply = orchestrator.route_query(request.query, request.language)
        return {"response": reply}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/mesh/add")
async def add_idea(request: IdeaRequest):
    status = mesh.add_idea(request.title, request.description, request.author)
    return {"status": status}

@app.get("/mesh/search")
async def search_mesh(query: str):
    results = mesh.search_similar(query)
    return {"matches": results}
