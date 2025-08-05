from flask import Flask
from controllers.member_controller import member_bp
from repositories.member_repository import init_db

app = Flask(__name__)
app.register_blueprint(member_bp, url_prefix="/member")

if __name__ == "__main__":
    init_db()
    app.run(debug=True)