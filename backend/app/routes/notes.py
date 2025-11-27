from flask_smorest import Blueprint, abort
from flask.views import MethodView
from sqlalchemy.exc import SQLAlchemyError

from ..models import db, Note
from ..schemas import NoteCreateSchema, NoteUpdateSchema, NoteSchema

blp = Blueprint(
    "Notes",
    "notes",
    url_prefix="/api/notes",
    description="CRUD operations for notes"
)

@blp.route("")
class NotesList(MethodView):
    """List and create notes."""

    @blp.response(200, NoteSchema(many=True), description="List all notes")
    def get(self):
        """List all notes."""
        notes = Note.query.order_by(Note.updated_at.desc()).all()
        return [n.to_dict() for n in notes]

    @blp.arguments(NoteCreateSchema, as_kwargs=True)
    @blp.response(201, NoteSchema, description="Create a new note")
    def post(self, title, content):
        """Create a new note."""
        try:
            note = Note(title=title, content=content)
            db.session.add(note)
            db.session.commit()
            return note.to_dict()
        except SQLAlchemyError as e:
            db.session.rollback()
            abort(500, message=f"Database error: {str(e)}")


@blp.route("/<int:note_id>")
class NoteItem(MethodView):
    """Retrieve, update, and delete a single note."""

    @blp.response(200, NoteSchema, description="Retrieve a single note")
    def get(self, note_id: int):
        """Retrieve a note by id."""
        note = Note.query.get(note_id)
        if not note:
            abort(404, message="Note not found")
        return note.to_dict()

    @blp.arguments(NoteUpdateSchema, as_kwargs=True)
    @blp.response(200, NoteSchema, description="Update a note")
    def put(self, note_id: int, **kwargs):
        """Update a note."""
        note = Note.query.get(note_id)
        if not note:
            abort(404, message="Note not found")
        title = kwargs.get("title", None)
        content = kwargs.get("content", None)
        if title is None and content is None:
            abort(400, message="At least one of 'title' or 'content' must be provided")
        if title is not None:
            note.title = title
        if content is not None:
            note.content = content
        try:
            db.session.commit()
            return note.to_dict()
        except SQLAlchemyError as e:
            db.session.rollback()
            abort(500, message=f"Database error: {str(e)}")

    @blp.response(204, description="Delete a note")
    def delete(self, note_id: int):
        """Delete a note."""
        note = Note.query.get(note_id)
        if not note:
            abort(404, message="Note not found")
        try:
            db.session.delete(note)
            db.session.commit()
            return ""
        except SQLAlchemyError as e:
            db.session.rollback()
            abort(500, message=f"Database error: {str(e)}")
