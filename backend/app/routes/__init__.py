from .maintenance_routes import maintenance_bp

def register_routes(app):
    app.register_blueprint(maintenance_bp, url_prefix="/api")
