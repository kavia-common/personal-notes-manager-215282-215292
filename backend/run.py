from app import app

if __name__ == "__main__":
    # Listen on port 3001 as per setup; host 0.0.0.0 for container accessibility
    app.run(host="0.0.0.0", port=3001)
