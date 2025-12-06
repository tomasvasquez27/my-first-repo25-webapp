# web_app/routes/rps_routes.py

from flask import Blueprint, request, render_template
import random

rps_routes = Blueprint("rps_routes", __name__)

@rps_routes.route("/rps")
def rps_form():
    return render_template("rps_form.html")

@rps_routes.route("/rps/results")
def rps_results():
    user_move = request.args.get("move")
    computer_move = random.choice(["rock", "paper", "scissors"])

    if user_move == computer_move:
        result = "Tie"
    elif (
        (user_move == "rock" and computer_move == "scissors") or
        (user_move == "paper" and computer_move == "rock") or
        (user_move == "scissors" and computer_move == "paper")
    ):
        result = "You win!"
    else:
        result = "You lose!"

    return render_template(
        "rps_results.html",
        user_move=user_move,
        computer_move=computer_move,
        result=result
    )
