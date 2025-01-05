# Gulungus-Bot
Gulungus Bot is a Discord bot written in Python, centering around practicing throw-breaks for _Tekken 8_. Users are incentivized through a server-wide economy system, earning currency for successfully breaking throws.

## Gulungus Bot Core Features
- **Throw Break Practice** - Users can practice throw breaks against a variety of characters
- **Leaderboard** - Tracks users' scores and displays rankings
- **SQLite integration** - Leverages SQLite to manage leaderboard, allowing for easy backup and restoration
- **Economy System** - Users may wager their points in games of Blackjack, and also exchange points with others (coming soon)

## Installation
Coming soon!

## Usage
- **!throwtest** - Starts the _Tekken 8_ throw-break practice session, type in chat "1', "2", or "12" for the corresponding throw shown
- **!leaderboard** - Displays the server leaderboard, showcasing the top 10 users with the highest throw-break streaks
- **!balance** - Displays user's balance for Gulungus Bot's economy system
- **!bj <value>** - Starts a game of Blackjack, where the value is the number of points the user is willing to wager
- **!send <username> <value>** - Sends another user Gulungus Bucks from your balance

## Future Plans
- **More Characters** - More characters for users to practice their throw breaks against
- **Challenge Others** - Implement the ability for users to challenge each other to see who can get the longest streak
- **Economy User Interactions** - Allow users to exchange points with eachother, and have server owners create a list of rewards to buy with points
- **Tekken Move Quiz** - Quiz yourself on optimal punishes for popular moves from a varieyt of different characters

## Version 1.1.1
- **New Economy Functionality** - Send money to other users using !send <user> <amount>!
- **Tools to Make Development Easier** - Moving towards implementing Github Actions fully, hopefully resulting in consistency and reliable improvements as I push updates

# Past Patch Notes:
## Version 1.1 Patch Notes and Bugfixes
- **New characters added!** - Jin and Jack-8 have been added to the pool, increasing the total characters up to 5
- **Gulungus Bot DMs** - Gulungus Bot will no longer DM you if you spam question marks (unless you have a particular username :])
- **Proper Balance Showcase** - Gulungus bot now gives double the amount of currency for practicing throwbreaks, and will properly reflect the value
