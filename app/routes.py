from app import app


@app.route('/')
def ussd_callback():
    return "Great Docker test worked  :)"
