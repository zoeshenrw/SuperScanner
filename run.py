
from config import app, conn
from flask import session
import register
import routes
# Checks if the run.py file has executed directly and not imported
if __name__ == '__main__':
    app.run(debug=True)
