import uuid
from dataclasses import dataclass
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.dialects.postgresql import UUID

db = SQLAlchemy()


@dataclass
class Location(db.Model):
    """The location class is used to store the various locations"""
    id: UUID(as_uuid=True)  # pylint: disable=c0103
    name: str

    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = db.Column(db.String, unique=True, nullable=False)


@dataclass
class Group(db.Model):
    """The group class is used to store the various groups"""
    id: UUID(as_uuid=True)  # pylint: disable=c0103
    location_id: UUID(as_uuid=True)
    name: str

    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    location_id = db.Column(UUID(as_uuid=True), db.ForeignKey("location.id"), nullable=False)
    name = db.Column(db.String, unique=True, nullable=False)


@dataclass
class Student(db.Model):
    """The student class is used to store the various students"""
    id: UUID(as_uuid=True)  # pylint: disable=c0103
    group_id: UUID(as_uuid=True)
    name: str
    phone_number: str

    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    group_id = db.Column(UUID(as_uuid=True), db.ForeignKey("group.id"), nullable=False)
    name = db.Column(db.String, nullable=False)
    phone_number = db.Column(db.String, unique=True, nullable=False)


@dataclass
class Lecturer(db.Model):
    """The lecturer class is used to store the various lecturers"""
    id: UUID(as_uuid=True)  # pylint: disable=c0103
    email: str
    password: str

    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    email = db.Column(db.String, unique=True, nullable=False)
    password = db.Column(db.String, unique=True, nullable=False)


@dataclass
class LocationMessage(db.Model):
    """The location message class is used to store the various location messages"""
    id: UUID(as_uuid=True)  # pylint: disable=c0103
    location_id: UUID(as_uuid=True)
    scheduled_at: datetime
    message: str

    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    location_id = db.Column(UUID(as_uuid=True), db.ForeignKey("location.id"), nullable=False)
    scheduled_at = db.Column(db.DateTime, nullable=False)
    message = db.Column(db.String, nullable=False)


@dataclass
class GroupMessage(db.Model):
    """The group message class is used to store the various group messages"""
    id: UUID(as_uuid=True)  # pylint: disable=c0103
    group_id: UUID(as_uuid=True)
    scheduled_at: datetime
    message: str

    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    group_id = db.Column(UUID(as_uuid=True), db.ForeignKey("group.id"), nullable=False)
    scheduled_at = db.Column(db.DateTime, nullable=False)
    message = db.Column(db.String, nullable=False)
