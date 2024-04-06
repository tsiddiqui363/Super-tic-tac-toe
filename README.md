# Super Tic Tac Toe Battle Glow

## Project Overview
The Super Tic Tac Toe Battle Glow project aims to create an engaging online multiplayer version of the classic Tic Tac Toe game with added features and a neon-themed interface. The goal is to provide users with a visually appealing and entertaining gaming experience.

## Installation
To install and run the project locally, follow these steps:
1. Clone the repository from GitHub. `https://github.com/CS2005W24/term-project-teamj.git`
2. Navigate to the project directory.
3. Install dependencies using `pip install bottle` if you dont have bottle framework installed..
4. Run the application using `python serverAPI.py`.

## Usage
1. Access the game by running `serverAPI.py`.
2. Register a new player or log in with guest credentials. `username: guest` and `password: myToeTaccd`
3. Start a new game or join a Lobby.
4. once the registration is done, you can use the credentials to login
5. if by any chance user close the game, user can always join back to the game by entering the lobby number.
7. Play Tic Tac Toe against other players in real-time and chat.
8. Enjoy the neon-themed interface and interactive gameplay.

## Folder Structure
- `applogic`: Contains applogic class for Game logic.
- `docGameFrame`: Contains Game Framework file and image.
- `docs`: Contains project documents, UML diagrams, images etc.
- `game_store` Contains the store class for loading and saving the user.
- `html_templates`: Contains HTML templates for the web application.
- `unit_tests`: Includes unit tests to ensure the functionality of the application.
- `user_inter`: Defines the User class responsible for managing player registration and login. 

## Code Documentation
- `serverAPI.py`: Main application file handling routing and request processing.
- `modules/user.py`: Contains the User class with methods for user management.
- `modules/applogic.py`: Contains the game applogic with applogic class with methods.
- `mnodules/store.py`: Contains the store class with methods for storing and loading the user data.
- `html_template`: HTML templates for different pages in the application.

## Testing
1. Run unit tests using from `unit_tests` folder for each module to test.

## Additional Resources
#### Follow The link to read the rules for the game
- [Super Tic Tac Toe Rules](https://en.wikipedia.org/wiki/Ultimate_tic-tac-toe)

## Architecture Design
The architecture design documents outline how the interface design and code components fit into the overall project structure. UML diagrams and architecture documents describing component interfaces are available in the repository `docs/arch_docs/arch_project.md`.

## Performance Reviews
Performance reviews for all the team member can be found in `docs/performance_reviews.md`.

## Arch Documents
All the Arch documentations for all modules can be found in `docs/arch_docs` folder. 

## Doc Game Framework
Game Frame work doc is in `DocGameFrame` folder.

## End of Sprint docs
End of sprint docs can be found in `docs/process_model.md` folder. 

## MeetingNotes
Meeting Notes can be found in `docs` folder for all the meetings.

## Needs to be done 
- Being able to play on already played spaces which can be fixed by updating applogic and serverAPI or by changing the html to not allow you to click the space
- Add exit button on the main board page which will take the user into the home page.
- Logout button needs to be added as well for user to logout.
