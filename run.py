from app import app
import os


if __name__ == "__main__":
    """ 
        heroku runs the app on a port that is available. in several instannces, it might not be assigned the port
        5000, which means the app crashes. in order to fix this error, we add a condition
    """

    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
