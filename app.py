from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>DSO101 Assignment IV</h1>
    <p>Deploy Your First Web App using GitHub and Render</p>
    <p>GitHub Actions and Render deployment are working successfully.</p>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)