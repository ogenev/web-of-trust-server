from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class TrustRequest(BaseModel):
    source: str
    destination: str


@app.get("/")
def health_check():
    return {"Ping": "Pong"}


@app.post("/get_trust")
def get_trust(request: TrustRequest):
    """
    1. Load all data from database
    2. Build trust graph
    3. Run algorithm
    4. Return results
    """
    return {"trust_source": request.source, "trust_destination": request.destination}
