<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Waiting Lobby - Tic Tac Toe</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
            color: #43e815;
            text-shadow: 0 0 10px #e815e1, 0 0 20px #15cfe8, 0 0 30px #e81554;
            background-color: #111;
            text-align: center;
            display: flex;
        }
        .lobby {
            text-align: center;
        }
        .loader {
            border: 16px solid #111;
            border-radius: 50%;
            border-top: 16px solid #3498db;
            width: 120px;
            height: 120px;
            animation: spin 2s linear infinite;
            margin: 0 auto;
        }
        @keyframes spin {
            0% { transform: rotate(0deg); }
            100% { transform: rotate(360deg); }
        }
        h2 {
            margin-top: 20px;
        }
    </style>
</head>
<body>
    <input type="hidden" name="username" value="{{username}}">
    <input type="hidden" name="game_id" value="{{game_id}}">
    <div class="lobby">
        <div class="loader"></div>
        <h2>Waiting for another player to join...</h2>
    </div>
    <script>
        function checkPlayerJoined() {
            const username = document.querySelector('input[name="username"]').value;
            const game_id = document.querySelector('input[name="game_id"]').value;

            fetch(`/check_player_joined?username=${username}&gameID=${game_id}`)
                .then(response => response.json())
                .then(data => {
                    console.log(data);
                    if (data.playerJoined) {
                        window.location.href = `/game_board?username=${username}&gameID=${game_id}`;
                    } else {
                        setTimeout(checkPlayerJoined, 3000);
                    }
                })
                .catch(error => console.error('Error checking if player joined:', error));
        }
        document.addEventListener('DOMContentLoaded', checkPlayerJoined);
    </script>

</body>
</html>