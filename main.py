from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from typing import Dict, List, Optional, Any
from datetime import datetime
from llm_parser import LLMHandHistoryParser

app = FastAPI(title="Poker Hand History Parser")

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Mount static files
app.mount("/static", StaticFiles(directory="static"), name="static")

parser = LLMHandHistoryParser()

@app.get("/")
async def read_root():
    return {"message": "Welcome to the Poker Hand History Parser API"}

@app.post("/parse-hand")
async def parse_hand(hand_input: Dict[str, Any]):
    try:
        if "description" not in hand_input:
            raise HTTPException(status_code=400, detail="Description is required")
            
        # Set default values for optional fields
        description = hand_input["description"]
        
        # Parse the hand history using the LLM parser
        parsed_hand = parser.parse_hand_history(
            description=description
        )
        
        return {"formatted_history": parsed_hand}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000) 