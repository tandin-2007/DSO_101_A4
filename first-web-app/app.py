from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>DSO101 Assignment IV</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                background-color: #f2f4f8;
                text-align: center;
                padding: 60px;
            }

            .card {
                background: white;
                padding: 40px;
                max-width: 700px;
                margin: auto;
                border-radius: 12px;
                box-shadow: 0 4px 12px rgba(0,0,0,0.1);
            }

            h1 {
                color: #1f2937;
            }

            p {
                color: #4b5563;
                font-size: 18px;
            }

            .success {
                color: green;
                font-weight: bold;
            }
        </style>
    </head>
    <body>
        <div class="card">
            <h1>DSO101 Assignment IV</h1>
            <p>Deploy Your First Web App using GitHub and Render</p>
            <p class="success">GitHub Actions and Render deployment are working successfully.</p>
        </div>
    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
    