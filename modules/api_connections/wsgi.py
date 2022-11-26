import os
from app import create_app

"""
    Initialize and start the application.
"""

app = create_app(os.getenv("FLASK_ENV") or "test")

if __name__ == "__main__":
    app.run(debug=True)