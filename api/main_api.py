from fastapi import FastAPI
from pydantic import BaseModel
from api.query_handler import answer_query

app = FastAPI()

#  Add this block to handle root ("/") requests
@app.get("/")
def root():
    return {"message": " ISRO HelpBot is live at /query!"}

class QueryInput(BaseModel):
    query: str

@app.post("/query")
def get_answer(data: QueryInput):
    user_query = data.query
    try:
        response = answer_query(user_query)
        return {"query": user_query, "response": response}
    except Exception as e:
        return {"error": str(e)}
