from Auth import db


class User(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(length=20), unique=False, nullable=False)
    email = db.Column(db.String(), unique=True, nullable=False)
    password = db.Column(db.String(length=50), nullable=False)

    def repr(self):
        return f'Item {self.username}'
