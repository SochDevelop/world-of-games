import os

SCORES_FILE_NAME = "scores.txt"
POINTS_OF_WINNING = lambda difficulty: (difficulty * 3) + 5


def add_score(difficulty):
    score = POINTS_OF_WINNING(difficulty)

    try:
        if os.path.exists(SCORES_FILE_NAME):
            with open(SCORES_FILE_NAME, "r") as file:
                content = file.read()
                current_score = int(content) if content.strip().isdigit() else 0
        else:
            current_score = 0

        new_score = current_score + score

        with open(SCORES_FILE_NAME, "w") as file:
            file.write(str(new_score))

        print(f"Your new score is: {new_score}")

    except Exception as e:
        print(f"Error updating score: {e}")
