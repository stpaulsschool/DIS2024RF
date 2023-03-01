from app import app

app.config["SECRET_KEY"] = "a-string-you-will-never-guess"

if __name__ == "__main__":
    app.run(debug=True)