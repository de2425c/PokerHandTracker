# Poker Hand History Parser and Replayer

A web application that parses poker hand histories and provides an interactive replayer to visualize the action.

## Features

- Parse poker hand histories from text input
- Interactive hand replayer with:
  - Player positions and stacks
  - Betting action visualization
  - Community cards
  - Action log
  - Dealer button tracking
- Support for 9-max tables
- Proper action ordering based on poker positions

## How to Use

1. **Start the Server**
   ```bash
   python main.py
   ```
   The server will start on `http://localhost:5000`

2. **Parse a Hand**
   - Open `http://localhost:5000` in your browser
   - Paste your poker hand history into the text area
   - Click "Parse Hand"
   - The parsed hand will be displayed in JSON format
   - Click "View Replay" to open the replayer

3. **Using the Replayer**
   - The replayer shows a 9-max table with player positions
   - Player positions are labeled (UTG, UTG+1, UTG+2, Lojack, Hijack, Cutoff, Button, SB, BB)
   - Click "Start Replay" to begin the hand replay
   - Use "Next Action" to progress through the hand
   - The action log on the right shows the sequence of actions
   - Player stacks and bets are updated automatically
   - Community cards are revealed as the hand progresses
   - The dealer button is shown next to the button player's name

4. **Controls**
   - **Start Replay**: Begins the hand replay
   - **Next Action**: Shows the next action in the hand
   - **Reset**: Returns to the start of the hand

## Hand History Format

The parser expects hand histories in a standard format, typically from online poker sites. The hand history should include:
- Game information (blinds, table size)
- Player positions and stacks
- Hole cards
- Betting action for each street
- Community cards
- Showdown information (if applicable)

## Development

The application consists of:
- `main.py`: Flask server and hand history parser
- `static/index.html`: Main interface for parsing hands
- `static/replayer.html`: Interactive hand replayer

## Notes

- The replayer follows standard poker action order:
  - Preflop: Starts from UTG, goes clockwise
  - Postflop: Starts from SB, goes clockwise
- Player positions are fixed based on the dealer button
- All bets and stack updates are tracked automatically
- The replayer supports all standard poker actions (fold, check, call, bet, raise) 