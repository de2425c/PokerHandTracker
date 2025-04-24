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

hand_parser = LLMHandHistoryParser()

# Store parsed hands in memory (in a real app, you'd use a database)
parsed_hands = {}

@app.get("/")
async def read_root():
    return FileResponse("static/index.html")

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
        
        # Store the hand history
        hand_id = str(datetime.now().timestamp())
        parsed_hands[hand_id] = hand_history
        
        # Add replayer URL to the hand history
        hand_history["replayer_url"] = f"/replayer?hand_id={hand_id}"
        
        return hand_history
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.get("/replayer", response_class=HTMLResponse)
async def get_replayer(hand_id: str):
    if hand_id not in parsed_hands:
        raise HTTPException(status_code=404, detail="Hand not found")
        
    with open("static/replayer.html", "r") as f:
        html_content = f.read()
        
    # Wrap the hand data in the correct structure
    hand_data = {
        "hand_history": parsed_hands[hand_id]
    }
    
    # Inject the hand data into the HTML
    html_content = html_content.replace('</body>', f'''
        <script>
            window.addEventListener('load', function() {{
                console.log('Hand data:', {json.dumps(hand_data)});  // Debug log
                renderHand({json.dumps(hand_data)});
            }});
        </script>
    </body>''')
    
    return html_content

if __name__ == "__main__":
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument("--port", type=int, default=8000, help="Port to run the server on")
    args = arg_parser.parse_args()
    
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=args.port) 