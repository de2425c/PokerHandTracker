# Poker Hand History Parser API

This API converts natural language poker hand history descriptions into a standardized JSON format according to the Open Hand History specification using an LLM for flexible parsing.

## Installation

1. Clone the repository
2. Install dependencies:
```bash
pip install -r requirements.txt
```
3. Create a `.env` file with your OpenAI API key:
```bash
cp .env.example .env
# Edit .env and add your OpenAI API key
```

## Running the API

Start the server:
```bash
python main.py
```

The API will be available at `http://localhost:8000`

## API Usage

Send a POST request to `/parse-hand` with a JSON body containing:

```json
{
    "description": "I opened from the button with Ace-King offsuit for $15, big blind called. Flop came Ten-Seven-Deuce rainbow, I bet $20 and got called. Turn was an Eight, we both checked. River was a King, I bet $50 and got raised to $250",
    ... additional parameters
}
```

Response:
```json
{
    "spec_version": "1.4.7",
    "site_name": "Custom",
    "network_name": "Custom",
    "internal_version": "1.0.0",
    "tournament": false,
    "game_number": "1234567890",
    "start_date_utc": "2024-03-14T12:00:00Z",
    "table_name": "Table 1",
    "table_size": 6,
    "currency": "USD",
    "ante_amount": 0.0,
    "small_blind_amount": 0.5,
    "big_blind_amount": 1.0,
    "bet_limit": {
        "bet_cap": 0.0,
        "bet_type": "NL"
    },
    "hero_player_id": 0,
    "dealer_seat": 0,
    "players": [
        {
            "name": "Hero",
            "id": 0,
            "player_bounty": 0,
            "starting_stack": 100.0,
            "seat": 2
        },
        {
            "name": "Villain",
            "id": 1,
            "player_bounty": 0,
            "starting_stack": 100.0,
            "seat": 1
        }
    ],
    "rounds": [
        {
            "id": 0,
            "street": "Preflop",
            "cards": ["As", "Kd"],
            "actions": [
                {
                    "action_number": 1,
                    "player_id": 0,
                    "action": "Raise",
                    "amount": 15.0,
                    "is_allin": false
                },
                {
                    "action_number": 2,
                    "player_id": 1,
                    "action": "Call",
                    "amount": 15.0,
                    "is_allin": false
                }
            ]
        },
        {
            "id": 1,
            "street": "Flop",
            "cards": ["Ts", "7h", "2d"],
            "actions": [
                {
                    "action_number": 1,
                    "player_id": 0,
                    "action": "Bet",
                    "amount": 20.0,
                    "is_allin": false
                },
                {
                    "action_number": 2,
                    "player_id": 1,
                    "action": "Call",
                    "amount": 20.0,
                    "is_allin": false
                }
            ]
        },
        {
            "id": 2,
            "street": "Turn",
            "cards": ["8c"],
            "actions": [
                {
                    "action_number": 1,
                    "player_id": 0,
                    "action": "Check",
                    "amount": 0.0,
                    "is_allin": false
                },
                {
                    "action_number": 2,
                    "player_id": 1,
                    "action": "Check",
                    "amount": 0.0,
                    "is_allin": false
                }
            ]
        },
        {
            "id": 3,
            "street": "River",
            "cards": ["Ks"],
            "actions": [
                {
                    "action_number": 1,
                    "player_id": 0,
                    "action": "Bet",
                    "amount": 50.0,
                    "is_allin": false
                },
                {
                    "action_number": 2,
                    "player_id": 1,
                    "action": "Raise",
                    "amount": 250.0,
                    "is_allin": false
                }
            ]
        }
    ],
    "pots": []
}
``` 