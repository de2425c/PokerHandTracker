import os
from typing import Dict, Any, List, Optional
from openai import OpenAI
from dotenv import load_dotenv
import json
from datetime import datetime
from models import HandHistory, RawHandHistory

load_dotenv()

class LLMHandHistoryParser:
    def __init__(self):
        try:
            self.client = OpenAI()
            self.ohh_prompt = open("system_prompt.txt", "r").read()
        except Exception as e:
            print(f"Error initializing OpenAI client: {e}")
            raise



    def parse_hand_history(self, description: str) -> Dict[str, Any]:
        try:
            print("Sending request to OpenAI...")
            response = self.client.responses.parse(
                model="gpt-4o-2024-08-06",
                input=[
                    {"role": "system", "content": self.ohh_prompt},
                    {"role": "user", "content": f"Parse this poker hand history: {description}"}
                ],
                text_format=HandHistory
            )
            
            print("Received response from OpenAI")
            
            # Extract the raw hand data from the response
            hand_history = response.output[0].content[0].parsed
            
            try:
                
                
                return {
                    "hand_history": hand_history.raw.dict(),
                    "raw_response": response.output[0].content[0].text
                }
            except Exception as e:
                return {
                    "hand_history": None,
                    "raw_response": response.output[0].content[0].text,
                    "conversion_error": str(e)
                }
            
        except Exception as e:
            print(f"Error in parse_hand_history: {e}")
            raise Exception(f"Failed to parse hand history: {str(e)}") 