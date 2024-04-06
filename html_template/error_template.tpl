<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Error Page</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #121212;
            color: #fff;
            text-align: center;
            padding: 20px;
        }
        .neon-title {
            font-size: 3em;
            color: #43e815;
            text-shadow: 0 0 10px #e815e1, 0 0 20px #15cfe8, 0 0 30px #e81554;
            margin-bottom: 50px;
        }
        .error-container {
            background-color: #1e1e1e;
            border: 1px solid #2e2e2e;
            padding: 20px;
            margin: 20px auto;
            width: 90%;
            max-width: 600px;
            border-radius: 5px;
        }
        .error-message {
            color: #ff2e2e;
            margin: 15px 0;
        }
        .username {
            display: none;
        }
        .back-button {
            background-color: #0cc4c4;
            color: #fff;
            padding: 10px;
            border: none;
            border-radius: 4px;
            cursor: pointer;
            transition: background 0.3s;
        }
        .back-button:hover {
            background: linear-gradient(45deg, #ff6699, #ffcc00);
        }
    </style>
</head>
<body>
    <div class="error-container">
        <h1 class="neon-title">Error Encountered</h1>
        <p class="error-message">{{message}}</p>
        <form action="/logged_in" method="POST">
            <input type="hidden" name="username" value="{{username}}">
            <button type="submit" class="back-button">Back to Menu</button>
        </form>
    </div>
</body>
</html>
