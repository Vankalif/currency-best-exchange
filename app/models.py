from app import db
from datetime import datetime


class Currencies(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String(3), index=True, unique=True)
    name = db.Column(db.String(64), index=True, unique=True)

    def __repr__(self):
        return f'<Currency {self.code}>'


class Rates(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    bank_name = db.Column(db.String(64))
    currency_code = db.Column(db.Integer, db.ForeignKey('currencies.id'))
    buy = db.Column(db.Float, nullable=False)
    sale = db.Column(db.Float, nullable=False)
    timestamp = db.Column(db.DateTime, nullable=False, default=datetime.now())

    def __repr__(self):
        return f'Buy {self.buy}, Sale {self.sale}, Bank {self.bank_name}'
