<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Neon Tic Tac Glow - Registration</title>
    <style>
        body {
            font-family: 'Arial', sans-serif;
            background-color: #111;
            color: #fff;
            text-align: center;
            margin: 0;
            display: flex;
            align-items: center;
            justify-content: center;
            flex-direction: column;
            height: 100vh;
        }

        .neon-title {
            font-size: 3em;
            color: #43e815;
            text-shadow: 0 0 10px #e815e1, 0 0 20px #15cfe8, 0 0 30px #e81554;
            margin-bottom: 50px;
        }

        .registration-container {
            width: 400px;
            background-color: #292929;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.5);
            border: 2px solid #d418ed;
        }

        .registration-container h2 {
            color: #00ffcc;
        }

        .registration-form {
            display: flex;
            flex-direction: column;
        }

        .form-group {
            margin-bottom: 15px;
        }

        .form-group label {
            display: block;
            margin-bottom: 8px;
            color: #ddd;
        }

        .form-group input {
            width: 100%;
            padding: 10px;
            box-sizing: border-box;
            border: 2px solid #ffcc00;
            border-radius: 4px;
            font-size: 14px;
            background-color: #333;
            color: #fff;
        }

        .form-group button {
            background-color: #0cc4c4;
            color: #fff;
            padding: 10px;
            border: none;
            border-radius: 4px;
            cursor: pointer;
            transition: background 0.3s;
        }

        .form-group button:hover {
            background: linear-gradient(45deg, #ff6699, #ffcc00);
        }

        .message-container {
            margin-top: 20px;
            font-size: 16px;
            color: #ffcc00;
        }
    </style>
</head>

<body>
    <div class="neon-title">Tic Tac Toe Battle - Registration</div>
    <div class="registration-container">
        <h2>Player Registration</h2>
        <form id="registrationForm" class="registration-form" action="/register" method="post">
            <div class="form-group">
                <label for="username">Username:</label>
                <input type="text" id="username" name="username" required>
            </div>
            <div class="form-group">
                <label for="password">Password:</label>
                <input type="password" id="password" name="password" required>
            </div>
            <div class="form-group">
                <button type="submit">Register</button>
            </div>
        </form>
        <div id="messageContainer" class="message-container">{{message}}</div>
    </div>
</body>

</html>
