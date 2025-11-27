from flask_smorest import Blueprint
from flask.views import MethodView

blp = Blueprint("Health", "health", url_prefix="/health", description="Health check route")

@blp.route("")
class HealthCheck(MethodView):
    """Health check endpoint."""
    # PUBLIC_INTERFACE
    def get(self):
        """Returns service health status."""
        return {"status": "ok"}
