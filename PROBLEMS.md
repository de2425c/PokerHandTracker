Log of problems/error the LLM makes

Testing case 1:
Input: I opened from the button with Ace-King offsuit for $15, big blind called. Flop came Ten-Seven-Deuce rainbow, I bet $20 and got called. Turn was an Eight, we both checked. River was a King, I bet $50 and got raised to $250

Response:
{
  "ohh": {
    "spec_version": "1.2.2",
    "internal_version": "1.2.2",
    "network_name": "Generic Network",
    "site_name": "Generic Site",
    "game_type": "Holdem",
    "table_name": "Generic Table",
    "table_size": 9,
    "game_number": "0",
    "start_date_utc": "0000-00-00T00:00:00",
    "currency": "USD",
    "ante_amount": 0.0,
    "small_blind_amount": 0.0,
    "big_blind_amount": 0.0,
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
        "starting_stack": 0.0,
        "seat": 0
      },
      {
        "name": "Big Blind",
        "id": 1,
        "player_bounty": 0,
        "starting_stack": 0.0,
        "seat": 0
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
        "cards": [
          "Td",
          "7c",
          "2h"
        ],
        "street": "Flop",
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
        "cards": [
          "8s"
        ],
        "street": "Turn",
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
        "cards": [
          "Kd"
        ],
        "street": "River",
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
}