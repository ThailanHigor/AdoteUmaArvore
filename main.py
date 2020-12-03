from app import db, create_app, mail
from flask_migrate import Migrate
from app.models.User import User
from app.models.Todo import Todo
from flask_mail import Message, Mail

app = create_app("development")
migrate = Migrate(app, db)

@app.shell_context_processor
def make_shell_processor():
    return dict(
        db = db,
        Todo = Todo,
        User = User,
        mail = mail
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0")
