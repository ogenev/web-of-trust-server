from fastapi import FastAPI
from pydantic import BaseModel

from db.qldb import QldbQuery
from trust import TrustScore

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
    3. Run trust score algorithm
    4. Return results
    """
    trust_records = QldbQuery.call()
    result = TrustScore.call(trust_records, request.source, request.destination)

    return {"source": request.source,
            "destination": request.destination,
            "trust_score": result}
