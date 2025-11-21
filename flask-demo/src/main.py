from flask import Flask

# Create a Flask application instance
app = Flask(__name__)

# Define a route for the root URL ("/")
@app.route('/')
def hello_world():
    """
    This function handles requests to the root URL and returns a string.
    """
    return 'Hello, World!'

# Run the Flask application if the script is executed directly
if __name__ == '__main__':
    # debug=True enables debug mode, which provides helpful error messages
    # and automatically reloads the server on code changes.
    app.run(debug=True)