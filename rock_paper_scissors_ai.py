import random

CHOICES = ["rock", "paper", "scissors"]


transition_history = {
    "rock": {"rock": 0, "paper": 0, "scissors": 0},
    "paper": {"rock": 0, "paper": 0, "scissors": 0},
    "scissors": {"rock": 0, "paper": 0, "scissors": 0}
}

WINNING_MOVES = {
    "rock": "paper",
    "paper": "scissors",
    "scissors": "rock"
}


def get_ai_choice(last_user_move):

    if last_user_move is None:
        return random.choice(CHOICES), "AI used random choice (no data yet)"

    history = transition_history[last_user_move]

    if sum(history.values()) == 0:
        return random.choice(CHOICES), "AI used random choice (learning phase)"

    predicted_move = max(history, key=history.get)

    ai_move = WINNING_MOVES[predicted_move]

    explanation = f"AI predicted you might play '{predicted_move}' after '{last_user_move}'"

    return ai_move, explanation


def determine_winner(user, ai):

    if user == ai:
        return "tie"

    if (
        (user == "rock" and ai == "scissors")
        or (user == "paper" and ai == "rock")
        or (user == "scissors" and ai == "paper")
    ):
        return "user"

    return "ai"


def main():

    print("=================================")
    print(" Rock Paper Scissors AI Game ")
    print("=================================")
    print("Type rock, paper, or scissors")
    print("Type exit to stop the game")

    scores = {"user": 0, "ai": 0, "ties": 0}

    last_user_move = None
    round_number = 1

    while True:

        print(f"\n----- Round {round_number} -----")

        user_move = input("Your move: ").lower().strip()

        if user_move in ["exit", "quit"]:
            break

        if user_move not in CHOICES:
            print("Invalid move. Please choose rock, paper, or scissors.")
            continue

        ai_move, explanation = get_ai_choice(last_user_move)

        if last_user_move is not None:
            transition_history[last_user_move][user_move] += 1

        print(f"AI chose: {ai_move}")
        print(f"AI Logic: {explanation}")

        winner = determine_winner(user_move, ai_move)

        if winner == "tie":
            print("Result: It's a tie!")
            scores["ties"] += 1

        elif winner == "user":
            print("Result: You win this round!")
            scores["user"] += 1

        else:
            print("Result: AI wins this round!")
            scores["ai"] += 1

        print(
            f"Score -> You: {scores['user']} | AI: {scores['ai']} | Ties: {scores['ties']}"
        )

        last_user_move = user_move
        round_number += 1

    print("\n====== FINAL RESULT ======")
    print(f"You: {scores['user']}")
    print(f"AI: {scores['ai']}")
    print(f"Ties: {scores['ties']}")
    print("Thanks for playing!")


if __name__ == "__main__":
    main()