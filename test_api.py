import requests
import json

def test_hand_history_parser():
    # Test cases
    test_cases = [
        {
            "description": "I opened from the button with Ace-King offsuit for $15, big blind called. Flop came Ten-Seven-Deuce rainbow, I bet $20 and got called. Turn was an Eight, we both checked. River was a King, I bet $50 and got raised to $250",
        },
        {
            "description": "BTN opens to $15 with AKo, BB calls. Flop T72r, hero bets $20, villain calls. Turn 8, check-check. River K, hero bets $50, villain raises to $250",
        }
    ]

    # API endpoint
    url = "http://localhost:8000/parse-hand"

    # Test each case
    for i, test_case in enumerate(test_cases, 1):
        print(f"\nTesting case {i}:")
        print(f"Input: {test_case['description']}")
        
        try:
            response = requests.post(url, json=test_case)
            response.raise_for_status()
            
            # Pretty print the response
            parsed_hand = response.json()
            print("\nResponse:")
            print(json.dumps(parsed_hand, indent=2))
            
        except requests.exceptions.RequestException as e:
            print(f"Error: {e}")
            if hasattr(e, 'response') and e.response:
                print(f"Response: {e.response.text}")

if __name__ == "__main__":
    test_hand_history_parser() 