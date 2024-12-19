from flask import Flask, render_template

# Initialize the Flask application

app = Flask(__name__)

# Route for the homepage

@app.route("/")

def home():

# Render the index.html template

   return render_template("index.html")

# Placeholder for additional routes

# Example:

# @app.route("/about")

# def about():

# return render_template("about.html")

if __name__ == "__main__":