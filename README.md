run main.py

endpoints - 

Only /parse-hand right now, returns a hand in this JSON format

{
    "game_info": {
        "table_size": "integer",
        "small_blind": "number",
        "big_blind": "number",
        "dealer_seat": "integer"
    },
    "players": [
        {
            "name": "string",
            "seat": "integer",
            "stack": "number",
            "position": "string",  // "button", "small blind", "big blind", "cutoff", "hijack", "lojack", "utg+2", "utg+1", "utg"
            "is_hero": "boolean",
            "cards": ["string"],  // Optional, for dealt cards
            "final_hand": "string",  // Optional, e.g., "Pair of Kings"
            "final_cards": ["string"]  // Optional, e.g., ["Kh", "Kd", "Ah", "7d", "2c"]
        }
    ],
    "streets": [
        {
            "name": "string",  // "Preflop", "Flop", "Turn", "River"
            "cards": ["string"],  // Community cards for this street
            "actions": [
                {
                    "player_name": "string",
                    "action": "string",  // "Folds", "Checks", "Calls", "Bets", "Raises"
                    "amount": "number",
                    "cards": ["string"]  // Optional, for dealt cards or shown cards
                }
            ]
        }
    ],
    "pot": {
        "amount": "number",
        "rake": "number",
        "distribution": [  // Optional, only if there was a showdown
            {
                "player_name": "string",
                "amount": "number",
                "hand": "string",  // e.g., "Pair of Kings"
                "cards": ["string"]  // e.g., ["Kh", "Kd", "Ah", "7d", "2c"]
            }
        ]
    }
}