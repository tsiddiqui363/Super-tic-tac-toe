<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Centered Message with Form Button</title>
    <style>
        body, html {
            height: 100%;
            margin: 0;
            display: flex;
            justify-content: center;
            align-items: center;
            font-family: Arial, sans-serif;
            background-color: #111;
            color: #fff;
        }
        .message {
            text-align: center;
            font-size: 24px;
            color: #43e815;
            text-shadow: 0 0 10px #e815e1, 0 0 20px #15cfe8, 0 0 30px #e81554;
        }
        form {
            margin-top: 20px;
        }
        button {
            padding: 10px 20px;
            font-size: 18px;
            border: none;
            border-radius: 5px;
            transition: background-color 0.3s, color 0.3s;
            background-color: #0cc4c4;
            color: #fff;
            padding: 10px;
            border: none;
            cursor: pointer;
        }
        button:hover {
            background-color: #f2f2f2; /* Slightly darker on hover */
            color: #000;
        }
    </style>
</head>
<body>

<div class="message">
    {{message}}
    <form action="/logged_in" method="post">
        <input type="hidden" id="username" name="username" value="{{username}}">
        <button type="submit">Home Page</button>
    </form>
</div>

</body>
</html>
