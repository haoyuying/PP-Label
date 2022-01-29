from datetime import datetime

from pplabel.config import db
from ..util import nncol


class Label(db.Model):
    __tablename__ = "label"
    __table_args__ = {"comment": "Contains all the label information"}
    label_id = nncol(db.Integer(), primary_key=True)
    id = nncol(db.Integer())  # TODO: unique within project
    project_id = db.Column(
        db.Integer(), db.ForeignKey("project.project_id", ondelete="CASCADE")
    )
    name = nncol(db.String())
    color = db.Column(db.String())
    comment = db.Column(db.String())
    created = nncol(db.DateTime, default=datetime.utcnow)
    modified = nncol(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
