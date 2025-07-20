from flask import Flask, render_template, request, session, redirect, url_for
import random

app = Flask(__name__)
app.secret_key = "supersecretkey"

@app.route("/", methods=["GET", "POST"])
def index():
    if "secret" not in session:
        session["secret"] = random.randint(1, 100)
        session["attempts"] = 0

    message = ""
    hint = ""

    if request.method == "POST":
        try:
            guess = int(request.form["guess"])
            session["attempts"] += 1
            attempts_left = 7 - session["attempts"]

            secret = session["secret"]

            if guess == secret:
                message = f"🎉 You guessed it in {session['attempts']} attempts!"
                session.clear()
            elif session["attempts"] >= 7:
                message = f"💀 Game over! The number was {secret}"
                session.clear()
            elif guess < secret:
                message = f"📈 Too low! {attempts_left} attempts left."
            else:
                message = f"📉 Too high! {attempts_left} attempts left."

            # Hints
            difference = abs(guess - secret)
            if difference <= 5:
                hint = "🔥 You're very close!"
            elif difference <= 15:
                hint = "🌡️ Getting warmer..."

        except ValueError:
            message = "❌ Enter a valid number!"

    return render_template("index.html", message=message, hint=hint)

@app.route("/reset")
def reset():
    session.clear()
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)
