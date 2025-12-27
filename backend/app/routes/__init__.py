from .equipment_route import equipment_bp
from .maintenance_routes import maintenance_bp
from .kanban_route import kanban_bp
from .calendar_route import calendar_bp
from .view_routes import view_bp

from .auth_route import auth_bp




def register_routes(app):
    # API routes
    app.register_blueprint(equipment_bp, url_prefix="/api/equipment")
    app.register_blueprint(maintenance_bp, url_prefix="/api/maintenance")
    app.register_blueprint(kanban_bp, url_prefix="/api/kanban")
    app.register_blueprint(calendar_bp, url_prefix="/api/calendar")
    app.register_blueprint(auth_bp, url_prefix="/api/auth")

    # UI routes
    app.register_blueprint(view_bp)
