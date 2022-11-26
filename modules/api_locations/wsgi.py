import os
from app import create_app

"""
    The application is initialized and starts running
"""

app = create_app(os.getenv("FLASK_ENV") or "test")

if __name__ == "__main__":
    app.run(debug=True)