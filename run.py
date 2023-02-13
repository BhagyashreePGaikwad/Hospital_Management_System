from __init__ import app


if __name__=="__main__":
    app.run(port=8000)
    app.secret_key = "super secret key"
