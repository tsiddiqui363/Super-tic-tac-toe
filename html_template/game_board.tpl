</html>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Super Tic Tac Toe</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #111;
            color: #fff;
            text-align: center;
            margin: 0;
            display: flex;
            align-items: center;
            justify-content: center;
            flex-direction: column;
        }
        h2 {
            text-align: center;
            margin-bottom: 20px;
        }
        .board {
            display: grid;
            grid-template-columns: repeat(3, minmax(100px, 1fr));
            grid-template-rows: repeat(3, minmax(100px, 1fr));
            grid-gap: 10px;
            margin: 0 auto;
            max-width: 50%;
            color: #43e815;
            text-shadow: 0 0 10px #e815e1, 0 0 20px #15cfe8, 0 0 30px #e81554;
            
        }
        .sub-board {
            display: grid;
            grid-template-columns: repeat(3, minmax(30px, 1fr));
            grid-template-rows: repeat(3, minmax(30px, 1fr));
            border: 1px solid #ffffff;
        }
        .space {
            width: 100%;
            padding-top: 100%;
            position: relative;
            border: 1px solid #333;
        }
        .space input {
            display: none;
        }
        .space label {
            position: absolute;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
            font-size: 2em;
            cursor: pointer;
            color: #43e815;
            text-shadow: 0 0 10px #e815e1, 0 0 20px #15cfe8, 0 0 30px #e81554;
        }
        .disabled-space label {
            cursor: not-allowed;
            opacity: 0.5;
        }
        #backToMenuButton {
            display: none;
        }

        .neon-title {
            font-size: 3em;
            color: #43e815;
            text-shadow: 0 0 10px #e815e1, 0 0 20px #15cfe8, 0 0 30px #e81554;
            margin-bottom: 50px;
        }

        .message-container {
            margin-top: 20px;
            font-size: 16px;
            color: #ffcc00;
        }

        #chat {
            background-color: #121212;
            color: #fff;
            border: 1px solid #fff;
            padding: 20px;
            margin: 10px 0;
            margin-top: 30px;
            border-radius: 8px;
            width: 80%;
            max-width: 800px;
            margin-left: auto;
            margin-right: auto;
        }

        #chat p {
            font-family: 'Consolas', 'Courier New', Courier, monospace;
            color: #fff;
            padding: 5px;
            border-bottom: 1px solid #333;
        }

        #chat-messages {
            max-height: 300px;
            overflow-y: auto;
            margin-bottom: 10px;
            text-align: left;
        }

        #chat input[type="text"] {
            width: calc(100% - 120px);
            padding: 10px;
            background-color: #222;
            border: 1px solid #fff;
            color: #fff;
            border-radius: 4px;
        }

        #chat button {
            text-transform: uppercase;
            font-weight: bold;
            border-radius: 4px;
            transition: background-color 0.3s ease;
            background-color: #0cc4c4;
            color: #fff;
            padding: 10px;
            border: none;
            cursor: pointer;
        }

        #chat button:hover {
            background: linear-gradient(45deg, #ff6699, #ffcc00);
            color: #121212;
        }

        #chat form {
            display: flex;
            flex-wrap: wrap;
            gap: 10px;
        }

        #chat input, #chat button {
            flex-grow: 1;
        }

        #chat-messages {
            max-height: 300px;
            overflow-y: auto;
            margin-bottom: 10px;
        }

        #chatTitle {
            font-size: 1em;
            color: #43e815;
            text-shadow: 0 0 10px #e815e1, 0 0 20px #15cfe8, 0 0 30px #e81554;
        }


    </style>
</head>
<body>
    <input type="hidden" id="username" name="username" value="{{username}}">
    <h2 class="neon-title">Super Tic Tac Toe</h2>
    <h3 id="turnMessage" class="message-container">{{message}}</h3>
    <div id="game" class="board">
        % for outer_row in range(3):
            % for outer_col in range(3):
                <div class="sub-board">
                    % for inner_row in range(3):
                        % for inner_col in range(3):
                            <div class="space">
                                <input type="radio" id="board{{outer_row * 3 + outer_col}}space{{inner_row * 3 + inner_col}}" name="move" value="{{outer_row * 3 + outer_col}}_{{inner_row * 3 + inner_col}}">
                                <label for="board{{outer_row * 3 + outer_col}}space{{inner_row * 3 + inner_col}}" data-mark="{{game_state[outer_row * 3 + outer_col][inner_row * 3 + inner_col]}}">{{game_state[outer_row * 3 + outer_col][inner_row * 3 + inner_col]}}</label>
                            </div>
                        % end
                    % end
                </div>
            % end
        % end
    </div>
    <form id="moveForm" action="/make_move" method="post" style="display: none;">
        <input type="hidden" name="gameID" value="{{game.gameID}}">
        <input type="hidden" name="username" value="{{username}}">
        <input type="hidden" id="selectedMove" name="selectedMove" value="">
    </form>

    <div id="chat">
    <h2 id="chatTitle">Chat</h2>
    <div id="chat-messages">
        % for message in chat_messages:
            <p>{{message}}</p>
        % end
    </div>
    <form action="/post_chat_message" method="POST">
        <input type="hidden" name="username" value="{{username}}">
        <input type="hidden" name="gameID" value="{{game.gameID}}">
        <input type="text" name="chat_message" placeholder="Type your message...">
        <button type="submit">Send</button>
    </form>
    </div>

    <script>
        document.addEventListener('DOMContentLoaded', () => {
            const username = document.getElementById('username').value;
            const turnMessageElement = document.getElementById('turnMessage');
            const gameId = document.querySelector('[name="gameID"]').value;
            let awaitingUpdate = true;

            function updateBoardAccessibility(currentTurn) {
                const isUserTurn = currentTurn === username;
                
                document.querySelectorAll('.space input').forEach(input => {
                    input.disabled = !isUserTurn;
                });
                
                document.querySelectorAll('.space').forEach(space => {
                    if (isUserTurn) {
                        space.classList.remove('disabled-space');
                    } else {
                        space.classList.add('disabled-space');
                    }
                });

                console.log(`Board accessibility updated for ${username}: ${isUserTurn}`);
            }

            document.querySelectorAll('.space').forEach(space => {
                space.addEventListener('click', function() {
                    const input = this.querySelector('input[type="radio"]');
                    if (!input.disabled) {
                        const selectedMove = input.value;
                        document.getElementById('selectedMove').value = selectedMove;
                        console.log(`Move selected: ${selectedMove}, submitting form.`);
                        document.getElementById('moveForm').submit();
                    }
                });
            });

            function pollForUpdates() {
                fetch(`/check_game_and_player_status?username=${username}&gameID=${gameId}`)
                    .then(response => response.json())
                    .then(data => {
                        console.log(data);
                        if (data.error) {
                            console.error('Error fetching game status:', data.error);
                            return;
                        }

                        updateBoardAccessibility(data.currentTurn);

                        if (data.update) {
                            setTimeout(function(){
                                window.location.href = `/game_board?username=${username}&gameID=${gameId}`;
                                awaitingUpdate = false;
                                console.log('Game updated. Fetching new state...');
                            }, 1000);
                        } else if (data.currentTurn === username) {
                            updateBoardAccessibility(data.currentTurn);
                        }
                    })
                    .catch(error => console.error('Polling error:', error))
                    .finally(() => {
                        if (awaitingUpdate || data.currentTurn === username) {
                            setTimeout(pollForUpdates, 1000);
                        }
                    });
            }
            pollForUpdates();
        });

    </script>

</body>
</html>