import webbrowser
import threading
import os
import requests
import time
import logging
import argparse
from flask import Flask, request

# Initialize the Flask app
app = Flask(__name__)
# Define the path to the user's home directory
HOME_DIR = os.path.expanduser("~")
TOKEN_FILE = os.path.join(HOME_DIR, ".fermata_token")
# Suppress Flask startup messages
log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)

# Global variable to signal successful login
login_successful = False

# Route to capture and handle the callback from Cognito
@app.route('/callback')
def callback():
    # Return HTML with JavaScript to extract the access token from the URL fragment
    return '''
        <html>
        <head>
            <title>Fermata Login</title>
        </head>
        <body>
            <h1>Processing login...</h1>
            <script type="text/javascript">
                // Extract the access token from the URL fragment
                const fragment = window.location.hash.substr(1);
                const params = new URLSearchParams(fragment);
                const id_token = params.get('id_token');

                // Redirect to the server with the access token as a query parameter
                if (id_token) {
                    window.location.href = "/store_token?id_token=" + id_token;
                } else {
                    document.body.innerHTML = "<h1>Failed to retrieve id_token.</h1>";
                }
            </script>
        </body>
        </html>
    '''

# Store the token in the home directory
@app.route('/store_token')
def store_token():
    id_token = request.args.get('id_token')
    if id_token:
        # Store the token in a hidden file in the user's home directory
        with open(TOKEN_FILE, 'w') as f:
            f.write(id_token)
        print(f"Login successful! The token has been stored in {TOKEN_FILE}.")
        global login_successful
        login_successful = True
        return "Login successful! You can close this window."
    return "Failed to store id_token."

# Function to start the Flask server
def start_server():
    app.run(port=3000)

# Function to trigger the login flow
def login():
    # Cognito login URL
    cognito_login_url = "https://fermata.auth.us-east-1.amazoncognito.com/login?response_type=token&client_id=1a2e6c0t9jpcje3klt8g6dp989&redirect_uri=http://localhost:3000/callback&scope=openid+email"

    # Start the Flask server in the background to capture the token (daemonized)
    server_thread = threading.Thread(target=start_server)
    server_thread.daemon = True
    server_thread.start()

    # Give the server a second to start
    time.sleep(1)

    # Try to open the Cognito login URL in the default browser
    try:
        webbrowser.open_new_tab(cognito_login_url)
        print("Opening the login page in your default browser...")
    except Exception as e:
        print(f"Failed to open browser automatically: {e}")

    # Display the login link for manual use if automatic browser opening fails
    print(f"Please open the following URL in your browser to log in: {cognito_login_url}")

    # Wait for the login to complete
    while not login_successful:
        time.sleep(1)

# Load the token from the user's home directory
def load_token():
    if os.path.exists(TOKEN_FILE):
        with open(TOKEN_FILE, 'r') as f:
            return f.read().strip()
    else:
        return None

# Function to call the Fermata API using the stored token
def call_api(uid, class_id):
    # Retrieve the stored token from the environment variable
    token = load_token()

    if not token:
        print("You need to log in first.")
        return

    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }

    data = {
        "uid": uid,
        "class_id": class_id
    }

    # Make the API call to your endpoint
    response = requests.post('https://p2o6vqftn8.execute-api.us-east-1.amazonaws.com/prod/analyze',
                             headers=headers, json=data)

    if response.status_code == 200:
        print("API call successful:", response.json())
    else:
        print("API call failed:", response.text)

# Main CLI function using argparse
def main():
    parser = argparse.ArgumentParser(description="Fermata CLI")
    subparsers = parser.add_subparsers(dest="command")

    # Login command
    login_parser = subparsers.add_parser('login', help="Log in via Cognito")
    
    # Analyze command
    analyze_parser = subparsers.add_parser('analyze', help="Analyze data")
    analyze_parser.add_argument('--uid', required=True, help="The UID for the data")
    analyze_parser.add_argument('--class_id', required=True, help="The class ID for the data")

    args = parser.parse_args()

    if args.command == "login":
        login()
    elif args.command == "analyze":
        call_api(args.uid, args.class_id)
    else:
        print("Invalid command. Use 'fermata login' or 'fermata analyze'.")

if __name__ == "__main__":
    main()

