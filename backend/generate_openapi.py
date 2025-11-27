import json
import os
from app import app, api  # import your Flask app and Api instance

with app.app_context():
    # flask-smorest stores the spec in api.spec
    if api is None:
        # Defensive guard: create_app should have initialized api; raise a clear error if not
        raise RuntimeError("API has not been initialized. Ensure app.create_app() sets a global Api instance.")
    openapi_spec = api.spec.to_dict()

    output_dir = "interfaces"
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, "openapi.json")

    with open(output_path, "w") as f:
        json.dump(openapi_spec, f, indent=2)
