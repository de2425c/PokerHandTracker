import os
from typing import Dict, Any, Tuple
from openai import OpenAI
from dotenv import load_dotenv
import json

load_dotenv()


class LLMHandHistoryParser:
    def __init__(self):
        try:
            self.client = OpenAI()
            # Load system prompt from file
            with open('system_prompt.txt', 'r') as f:
                self.system_prompt = f.read()
        except Exception as e:
            print(f"Error initializing OpenAI client: {e}")
            raise

    def _call_openai(self, messages: list) -> Tuple[str, bool]:
        """Helper function to call OpenAI API and check if more info is needed"""
        response = self.client.chat.completions.create(
            model="gpt-4-turbo-preview",
            messages=messages,
            temperature=0.1
        )
        
        content = response.choices[0].message.content
        
        # Clean up the response - remove any JSON formatting or markdown
        content = content.replace('```json', '').replace('```', '').strip()
        if content.startswith('{') and content.endswith('}'):
            try:
                # If it's a JSON string, convert it to a list of lines
                json_data = json.loads(content)
                if isinstance(json_data, dict):
                    content = '\n'.join(str(value) for value in json_data.values())
            except json.JSONDecodeError:
                pass
        
        # Check if the response indicates more information is needed
        if "need_more_info" in content.lower() or "please provide" in content.lower():
            return content, True
            
        return content, False

    def parse_hand_history(self, description: str, max_reprompts: int = 1) -> str:
        try:
            print("Sending request to OpenAI...")
            messages = [
                {"role": "system", "content": self.system_prompt},
                {"role": "user", "content": f"Parse this poker hand history: {description}"}
            ]
            
            reprompt_count = 0
            while reprompt_count <= max_reprompts:
                response, needs_more_info = self._call_openai(messages)
                
                if not needs_more_info:
                    print("Received complete hand history")
                    return response
                
                if reprompt_count < max_reprompts:
                    print("LLM needs more information:", response)
                    # Add the LLM's response to the conversation
                    messages.append({"role": "assistant", "content": response})
                    # Add user's response to the additional information request
                    additional_info = input("Please provide the requested information: ")
                    messages.append({"role": "user", "content": additional_info})
                    reprompt_count += 1
                else:
                    raise Exception("Maximum number of reprompts reached. Could not get complete hand history.")
            
        except Exception as e:
            print(f"Error in parse_hand_history: {e}")
            raise Exception(f"Failed to parse hand history: {str(e)}") 