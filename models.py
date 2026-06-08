"""
Database models for the FutureMe AI application.

This file contains the database configuration
and table definitions used to store user
prediction history and future assessment results.

:return: None
:rtype: None
"""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

"""
Create the SQLAlchemy database instance.

This object is used to connect Flask
with the SQLite database and manage
database operations.

:return: SQLAlchemy instance
:rtype: SQLAlchemy
"""

class Prediction(db.Model):
**tablename** = "predictions"

```
id = db.Column(
    db.Integer,
    primary_key=True
)

study_hours = db.Column(
    db.Integer,
    nullable=False
)

sleep_hours = db.Column(
    db.Integer,
    nullable=False
)

exercise_days = db.Column(
    db.Integer,
    nullable=False
)

projects = db.Column(
    db.Integer,
    nullable=False
)

career_score = db.Column(
    db.Integer,
    nullable=False
)

burnout_risk = db.Column(
    db.Integer,
    nullable=False
)

future_status = db.Column(
    db.String(50),
    nullable=False
)

"""
Prediction database model.

Stores user input values and the
generated future prediction results
for later analysis and dashboard display.
"""

def __repr__(self):
    return f"<Prediction {self.id}>"
```
