from __future__ import annotations
from dataclasses import dataclass
from datetime import datetime
from app import db 
from geoalchemy2 import Geometry
from geoalchemy2.shape import to_shape
from shapely.geometry.point import Point
from sqlalchemy import BigInteger, Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.ext.hybrid import hybrid_property
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

class Location(db.Model):
    """ Location Databade model

    Args:
        db (Model): SQLAlchemy Database model
    """
    __tablename__ = "location"

    id = Column(BigInteger, primary_key=True)
    person_id = Column(Integer, ForeignKey(Person.id), nullable=False)
    coordinate = Column(Geometry("POINT"), nullable=False)
    creation_time = Column(DateTime, nullable=False, default=datetime.utcnow)
    _wkt_shape: str = None

    @property
    def wkt_shape(self) -> str:
        # Persist binary form into readable text
        if not self._wkt_shape:
            point: Point = to_shape(self.coordinate)
            # normalize WKT returned by to_wkt() from shapely and ST_AsText() from DB
            self._wkt_shape = point.wkt.replace("POINT ", "ST_POINT")
        return self._wkt_shape

    @wkt_shape.setter
    def wkt_shape(self, v: str) -> None:
        self._wkt_shape = v

    def set_wkt_with_coords(self, lat: str, long: str) -> str:
        self._wkt_shape = f"ST_POINT({lat} {long})"
        return self._wkt_shape

    @hybrid_property
    def longitude(self) -> str:
        coord_text = self.wkt_shape
        return coord_text[coord_text.find(" ") + 1 : coord_text.find(")")]

    @hybrid_property
    def latitude(self) -> str:
        coord_text = self.wkt_shape
        return coord_text[coord_text.find("(") + 1 : coord_text.find(" ")]
    
    @staticmethod
    def get_location_fields(api):
        return api.model('Person', {
            'id': fields.Integer(description='location id', example=5),
            'person_id': fields.Integer(description="related person's id", example="5"),
            'coordinate': fields.String(description="geometry point", example="	010100000000ADF9F197925EC0FDA19927D7C64240"),
            'creation_time': fields.DateTime(description="location's datetime", example="Tue Aug 18 2020 10:37:06 GMT+0200 (Central European Summer Time)")
            })

@dataclass
class Connection:
    """ Connection data class
    """
    location: Location
    person: Person
    
    
    @staticmethod
    def get_connection_fields(api):
        return api.model('Connection', {
            'person': fields.Nested(api.model('person', Person.get_person_fields(api))),
            'location': fields.Nested(api.model('location', Location.get_location_fields(api)))
            })