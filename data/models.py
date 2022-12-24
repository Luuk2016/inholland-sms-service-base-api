import uuid
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.dialects.postgresql import UUID

db = SQLAlchemy()


class Location(db.Model):
    """The location class is used to store the various locations"""
    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = db.Column(db.String, unique=True, nullable=False)


class Group(db.Model):
    """The group class is used to store the various groups"""
    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = db.Column(db.String, unique=True, nullable=False)
    location_id = db.Column(UUID(as_uuid=True), db.ForeignKey("location.id"), nullable=False)


class Student(db.Model):
    """The student class is used to store the various students"""
    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = db.Column(db.String, nullable=False)
    phone_number = db.Column(db.String, unique=True, nullable=False)
    group_id = db.Column(UUID(as_uuid=True), db.ForeignKey("group.id"), nullable=False)


class Lecturer(db.Model):
    """The lecturer class is used to store the various lecturers"""
    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    email = db.Column(db.String, unique=True, nullable=False)
    password = db.Column(db.String, unique=True, nullable=False)


class LocationMessage(db.Model):
    """The location message class is used to store the various location messages"""
    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    location_id = db.Column(UUID(as_uuid=True), db.ForeignKey("location.id"), nullable=False)
    scheduled_at = db.Column(db.DateTime, nullable=False)
    message = db.Column(db.String, nullable=False)


class GroupMessage(db.Model):
    """The group message class is used to store the various group messages"""
    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    group_id = db.Column(UUID(as_uuid=True), db.ForeignKey("group.id"), nullable=False)
    scheduled_at = db.Column(db.DateTime, nullable=False)
    message = db.Column(db.String, nullable=False)
