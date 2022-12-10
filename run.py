
from config import app, conn
from flask import session
import register
import routes
from register import register_bp
# Checks if the run.py file has executed directly and not imported
app.register_blueprint(register_bp, url_prefix="/register")  
if __name__ == '__main__':
    app.run(debug=True)
