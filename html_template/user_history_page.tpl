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
        .neon-title {
            font-size: 3em;
            color: #43e815;
            text-shadow: 0 0 10px #e815e1, 0 0 20px #15cfe8, 0 0 30px #e81554;
            margin-bottom: 50px;
        }
        h3 {
            font-size: 1.5em;
            color: #43e815;
            text-shadow: 0 0 10px #e815e1, 0 0 20px #15cfe8, 0 0 30px #e81554;
        }
        .board, .user-history-table {
            margin: 0 auto;
            max-width: 50%;
        }
        .sub-board {
            display: grid;
            grid-template-columns: repeat(3, minmax(30px, 1fr));
            grid-template-rows: repeat(3, minmax(30px, 1fr));
            border: 1px solid #333;
        }
        .space {
            width: 100%;
            padding-top: 100%;
            position: relative;
            border: 1px solid #333;
        }
        .space input, .space label {
            display: none; /* Adjust as necessary */
        }
        .disabled-space label {
            cursor: not-allowed;
            opacity: 0.5;
        }
        table {
            width: 100%;
            border-collapse: collapse;
        }
        th, td {
            border: 1px solid black;
            padding: 8px;
            text-align: left;
        }
        button {
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

        button:hover {
            background-color: #ff6699;
        }
        
    </style>
</head>
<body>
    <h2 class="neon-title">Super Tic Tac Toe</h2>
    <h3>Game History</h3>
    <table class="user-history-table">
        <tr>
            <th>Game ID</th>
            <th>Win Status</th>
        </tr>
        % for game in user_games:
            <tr>
                <td>{{game['gameID']}}</td>
                <td>{{game['winStatus']}}</td>
            </tr>
        % end
    </table>

    <form action="/logged_in" method="post">
        <input type="hidden" id="username" name="username" value="{{username}}">
        <button type="submit">Back to Menu</button>
    </form>

</body>
</html>