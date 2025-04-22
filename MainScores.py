from flask import Flask
import os

app = Flask(__name__)

SCORES_FILE_NAME = "scores.txt"


def read_score():
    try:
        if os.path.exists(SCORES_FILE_NAME):
            with open(SCORES_FILE_NAME, "r") as file:
                content = file.read().strip()
                return int(content) if content.isdigit() else 0
        return 0
    except Exception as e:
        return f"Error reading score: {e}"


@app.route("/")
def score_server():
    score = read_score()

    if isinstance(score, int):
        html_content = f"""
        <html>
        <head>
            <title>Scores Game</title>
        </head>
        <body>
            <h1>The score is <div id="score">{score}</div></h1>
        </body>
        </html>
        """
    else:
        html_content = f"""
        <html>
        <head>
            <title>Scores Game</title>
        </head>
        <body>
            <h1><div id="score" style="color:red">{score}</div></h1>
        </body>
        </html>
        """

    return html_content


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
