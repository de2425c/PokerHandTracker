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
        except Exception as e:
            print(f"Error initializing OpenAI client: {e}")
            raise

        self.system_prompt = """You are a poker hand history parser. Your task is to convert natural language poker hand descriptions into a structured JSON format following the Open Hand History specification.

The output should be a valid JSON object with the following structure.

{
    "ohh": {
        "spec_version": "1.2.2",
        "internal_version": "1.2.2",
        "network_name": "iPoker Network",
        "site_name": "iPoker",
        "game_type": "Holdem",
        "table_name": "Brehuiesti",
        "table_size": 6,
        "game_number": "8599887794",
        "start_date_utc": "2020-04-07T14:32:50",
        "currency": "EUR",
        "ante_amount": 0.00,
        "small_blind_amount": 0.01,
        "big_blind_amount": 0.02,
        "bet_limit": {
            "bet_cap": 0.00,
            "bet_type": "NL"
        },
        "hero_player_id": 3,
        "dealer_seat": 8,
        "players": [
            {
                "name": "Player1",
                "id": 0,
                "player_bounty": 0,
                "starting_stack": 0.80,
                "seat": 1
            },
            {
                "name": "Player3",
                "id": 1,
                "player_bounty": 0,
                "starting_stack": 2.38,
                "seat": 3
            },
            {
                "name": "Player5",
                "id": 2,
                "player_bounty": 0,
                "starting_stack": 2.67,
                "seat": 5
            },
            {
                "name": "Hero",
                "id": 3,
                "player_bounty": 0,
                "starting_stack": 2.00,
                "seat": 6
            },
            {
                "name": "Player8",
                "id": 4,
                "player_bounty": 0,
                "starting_stack": 2.86,
                "seat": 8
            },
            {
                "name": "Player10",
                "id": 5,
                "player_bounty": 0,
                "starting_stack": 2.00,
                "seat": 10
            }
        ],
        "rounds": [
            {
                "id": 0,
                "cards": "",
                "street": "Preflop",
                "actions": [
                    {
                        "action_number": 1,
                        "player_id": 5,
                        "action": "Post SB",
                        "amount": 0.01,
                        "is_allin": false
                    },
                    {
                        "action_number": 2,
                        "player_id": 0,
                        "action": "Post BB",
                        "amount": 0.02,
                        "is_allin": false
                    },
                    {
                        "action_number": 3,
                        "player_id": 3,
                        "cards": [
                            "As",
                            "Tc"
                        ],
                        "action": "Dealt Cards",
                        "amount": 0.00,
                        "is_allin": false
                    },
                    {
                        "action_number": 4,
                        "player_id": 1,
                        "action": "Fold",
                        "amount": 0.00,
                        "is_allin": false
                    },
                    {
                        "action_number": 5,
                        "player_id": 2,
                        "action": "Fold",
                        "amount": 0.00,
                        "is_allin": false
                    },
                    {
                        "action_number": 6,
                        "player_id": 3,
                        "action": "Raise",
                        "amount": 0.06,
                        "is_allin": false
                    },
                    {
                        "action_number": 7,
                        "player_id": 4,
                        "action": "Fold",
                        "amount": 0.00,
                        "is_allin": false
                    },
                    {
                        "action_number": 8,
                        "player_id": 5,
                        "action": "Fold",
                        "amount": 0.00,
                        "is_allin": false
                    },
                    {
                        "action_number": 9,
                        "player_id": 0,
                        "action": "Call",
                        "amount": 0.04,
                        "is_allin": false
                    }
                ]
            },
            {
                "id": 1,
                "cards": [
                    "5c",
                    "7d",
                    "Js"
                ],
                "street": "Flop",
                "actions": [
                    {
                        "action_number": 1,
                        "player_id": 0,
                        "action": "Check",
                        "amount": 0.00,
                        "is_allin": false
                    },
                    {
                        "action_number": 2,
                        "player_id": 3,
                        "action": "Bet",
                        "amount": 0.06,
                        "is_allin": false
                    },
                    {
                        "action_number": 3,
                        "player_id": 0,
                        "action": "Raise",
                        "amount": 0.18,
                        "is_allin": false
                    },
                    {
                        "action_number": 4,
                        "player_id": 3,
                        "action": "Fold",
                        "amount": 0.00,
                        "is_allin": false
                    }
                ]
            }
        ],
        "pots": [
            {
                "number": 0,
                "amount": 0.25,
                "rake": 0.01,
                "player_wins": [
                    {
                        "player_id": 0,
                        "win_amount": 0.24,
                        "contributed_rake": 0.01
                    }
                ]
            }
        ]
    }
}

However THIS IS THE ONLY INFORMATION THAT YOU ABSOLUTELY NEED!

Effective stack size! Positions of the players who are involved in the hand (who do not fold preflop)! The rounds (bet sizes, actions etc. UNTIL THE HAND IS COMPLETED),  the BLINDS, and the RUNOUT. If you don't have this information, prompt for more information. Otherwise all the information should be FILLER (ZERO or NULL VALUES) Always assume it is 9 max, as well. 


For card notation, use the standard format: [Rank][Suit] where:
- Rank: A, K, Q, J, T, 9, 8, 7, 6, 5, 4, 3, 2
- Suit: s (spades), h (hearts), d (diamonds), c (clubs)

For actions, use: "Fold", "Check", "Call", "Bet", "Raise"

For streets, use: "Preflop", "Flop", "Turn", "River"

If you need more information to complete the hand history, respond with a JSON object containing a "need_more_info" field set to true and a "message" field explaining what information is needed."""

    def _call_openai(self, messages: list) -> Tuple[Dict[str, Any], bool]:
        response = self.client.chat.completions.create(
            model="gpt-4-turbo-preview",
            messages=messages,
            temperature=0.1,
            response_format={"type": "json_object"}
        )
        
        parsed_response = json.loads(response.choices[0].message.content)
        
        # Check if more information is needed
        if parsed_response.get("need_more_info", False):
            return parsed_response, True
            
        return parsed_response, False

    def parse_hand_history(self, description: str, currency: str = "USD", max_reprompts: int = 1) -> Dict[str, Any]:
        try:
            print("Sending request to OpenAI...")
            messages = [
                {"role": "system", "content": self.system_prompt},
                {"role": "user", "content": f"Parse this poker hand history: {description}\nCurrency: {currency}"}
            ]
            
            reprompt_count = 0
            while reprompt_count <= max_reprompts:
                response, needs_more_info = self._call_openai(messages)
                
                if not needs_more_info:
                    print("Received complete hand history")
                    return response
                
                if reprompt_count < max_reprompts:
                    print("LLM needs more information:", response.get("message", "Unknown information needed"))
                    # llm specifies what information is needed
                    messages.append({"role": "assistant", "content": json.dumps(response)})

                    # reprompt
                    additional_info = input("Please provide the requested information: ")
                    messages.append({"role": "user", "content": additional_info})
                    reprompt_count += 1
                else:
                    raise Exception("Maximum number of reprompts reached. Could not get complete hand history.")
            
        except Exception as e:
            print(f"Error in parse_hand_history: {e}")
            raise Exception(f"Failed to parse hand history: {str(e)}") 