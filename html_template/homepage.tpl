<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Welcome to Tic Tac Glow</title>
    <style>
        body {
            font-family: 'Arial', sans-serif;
            background-color: #111;
            color: #fff;
            display: flex;
            text-align: center;
            margin: 0;
            justify-content: center;
            align-items: center;
            height: 100vh;
        }

        .container {
            text-align: center;
            padding: 40px;
            border-radius: 10px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        }

        h1 {
            font-size: 2em;
            color: #43e815;
            text-shadow: 0 0 10px #e815e1, 0 0 20px #15cfe8, 0 0 30px #e81554;
            margin-bottom: 30px;
        }

        button {
            padding: 10px 20px;
            margin: 10px;
            font-size: 16px;
            border: none;
            border-radius: 5px;
            cursor: pointer;
            transition: background-color 0.3s;
        }

        .login-btn {
            background-color: #43e815;
            color: white;
        }

        .register-btn {
            background-color: #e815e1;
            color: white;
        }

        button:hover {
            opacity: 0.5;
        }
    </style>
</head>

<body>
    <div class="container">
        <h1>Welcome to Tic Tac Toe Battle Glow</h1>
        <button class="login-btn" onclick="location.href='/login_page'">Login</button>
        <button class="register-btn" onclick="location.href='/register_page'">Register</button>
    </div>
</body>

</html>
