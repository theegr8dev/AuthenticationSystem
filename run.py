from Auth import app, db
from Auth.models import User


@app.shell_context_processor
def make_shell_context():
    return dict(app=app, db=db, User=User)


if __name__ == '__main__':
    app.run(debug=True)
