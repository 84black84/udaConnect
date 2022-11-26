from __future__ import annotations
from app import db
from sqlalchemy import Column, Integer, String
from flask_restx import fields

class Person(db.Model):
    """ Person Database model

    Args:
        db (Model): SQLAlchemy Database model
    """
    __tablename__ = "person"

    id = Column(Integer, primary_key=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    company_name = Column(String, nullable=False)
    
    @staticmethod
    def get_person_fields(api):
        return api.model('Person', {
            'id': fields.Integer(description='person id', example=1),
            'first_name': fields.String(description="person's first name", example="Tom"),
            'last_name': fields.String(description="person's last name", example="Hood"),
            'company_name': fields.String(description="person's company name", example="The Hood company")
            })