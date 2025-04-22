from fastapi import FastAPI, HTTPException
from typing import Dict, List, Optional, Any
from datetime import datetime
from llm_parser import LLMHandHistoryParser

app = FastAPI(title="Poker Hand History Parser")
parser = LLMHandHistoryParser()

@app.post("/parse-hand")
async def parse_hand(hand_input: Dict[str, Any]):
    try:
        if "description" not in hand_input:
            raise HTTPException(status_code=400, detail="Description is required")
            
        # Set default values for optional fields (TODO SPECIFY THESE BETTER)
        description = hand_input["description"]
        
        # Parse the hand history using the LLM parser
        parsed_hand = parser.parse_hand_history(
            description=description
        )
        
        return parsed_hand
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000) 