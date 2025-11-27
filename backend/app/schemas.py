from marshmallow import Schema, fields, validate

# PUBLIC_INTERFACE
class NoteCreateSchema(Schema):
    """Schema for creating a new note."""
    title = fields.String(required=True, validate=validate.Length(min=1, max=255), metadata={"description": "Title of the note"})
    content = fields.String(required=True, metadata={"description": "Content of the note"})

# PUBLIC_INTERFACE
class NoteUpdateSchema(Schema):
    """Schema for updating an existing note."""
    title = fields.String(required=False, validate=validate.Length(min=1, max=255), metadata={"description": "Title of the note"})
    content = fields.String(required=False, metadata={"description": "Content of the note"})

# PUBLIC_INTERFACE
class NoteSchema(Schema):
    """Schema for representing a note."""
    id = fields.Int(required=True, dump_only=True, metadata={"description": "Unique identifier"})
    title = fields.String(required=True, metadata={"description": "Title"})
    content = fields.String(required=True, metadata={"description": "Content"})
    created_at = fields.DateTime(required=True, dump_only=True, metadata={"description": "Creation timestamp (UTC)"})
    updated_at = fields.DateTime(required=True, dump_only=True, metadata={"description": "Last updated timestamp (UTC)"})
