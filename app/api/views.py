from app import app


@app.get("/")
def test():
    return "APP_NAME"
