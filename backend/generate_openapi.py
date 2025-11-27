import json
import os

# IMPORTANT:
# - Do NOT instantiate or register any Api/blueprints here.
# - Build an application context using the factory to access the existing spec.
# - This prevents duplicate 'api-docs' blueprint registrations.
from app import create_app  # import factory only


def main():
    """Generate OpenAPI JSON by creating an app context from the factory without re-registering docs."""
    app = create_app()
    # Access the Api instance from the app.extensions registered by flask-smorest
    # flask-smorest stores Api under app.extensions['smorest']
    api = app.extensions.get("smorest")
    if api is None:
        raise RuntimeError("API has not been initialized. Ensure app.create_app() sets the Api instance.")

    with app.app_context():
        openapi_spec = api.spec.to_dict()

        output_dir = "interfaces"
        os.makedirs(output_dir, exist_ok=True)
        output_path = os.path.join(output_dir, "openapi.json")

        with open(output_path, "w") as f:
            json.dump(openapi_spec, f, indent=2)


if __name__ == "__main__":
    main()
