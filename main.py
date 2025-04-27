from fastapi import FastAPI, HTTPException, Request
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse, FileResponse
from typing import Dict, List, Optional, Any
from datetime import datetime
from llm_parser import LLMHandHistoryParser
import json
import argparse

app = FastAPI(title="Poker Hand History Parser")



hand_parser = LLMHandHistoryParser()



@app.post("/parse-hand")
async def parse_hand(hand_input: Dict[str, Any]):
    try:
        if "description" not in hand_input:
            raise HTTPException(status_code=400, detail="Description is required")
            
        # Parse the hand history using the LLM parser
        result = hand_parser.parse_hand_history(
            description=hand_input["description"]
        )
        
        # Extract just the hand history
        hand_history = result["hand_history"]        
        
        return hand_history
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


if __name__ == "__main__":
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument("--port", type=int, default=8000, help="Port to run the server on")
    args = arg_parser.parse_args()
    
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=args.port) 