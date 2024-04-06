<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Welcome Page</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
            background-color: #111;
            color: #fff;
        }

        .welcome-container {
            text-align: center;
        }

        .button {
            display: inline-block;
            margin: 10px;
            padding: 10px 20px;
            background-color: #0cc4c4; /* Neon green */
            color: #fff;
            border: none;
            border-radius: 5px;
            cursor: pointer;
            text-decoration: none;
            transition: background-color 0.3s;
        }

        .button:hover {
            background-color: #ff6699;
        }

        input[type="text"] {
            padding: 10px;
            margin: 10px 0;
            border: 1px solid #fff; /* White border */
            border-radius: 5px;
            background-color: transparent;
            color: #fff;
        }

        .message {
            margin-top: 20px;
            padding: 20px;
            border-radius: 5px;
            background-color: #292929; /* Dark background */
            color: #ffcc00; /* Neon yellow */
        }

        h1 {
            font-size: 3em;
            color: #43e815; /* Neon green */
            text-shadow: 0 0 10px #e815e1, 0 0 20px #15cfe8, 0 0 30px #e81554; /* Neon effect */
            margin-bottom: 30px;
        }
    </style>
</head>

<body>
    <div class="welcome-container">
        <h1>Welcome to the Game {{name}}!</h1>
        <form action="/join_game" method="post">
            <input type="hidden" id="username" name="username" value="{{username}}">
            <input type="text" name="gameID" placeholder="Enter Game Number" required>
            <button type="submit" class="button">Join Game</button>
        </form>
        <form action="/start_game" method="post">
            <input type="hidden" id="username" name="username" value="{{username}}">
            <input type="text" name="gameID" placeholder="Enter New Game Number" required>
            <button type="submit" class="button">Start a New Game</button>
        </form>
        <form action="/user_history" method="post">
            <input type="hidden" id="username" name="username" value="{{username}}">
            <button type="submit" class="button">User History</button>
        </form>
        <div class="message">{{message}}</div>
    </div>
</body>

</html>
