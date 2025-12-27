from flask import Blueprint, render_template

view_bp = Blueprint("views", __name__)

@view_bp.route("/")
def home():
    return render_template("index.html")

@view_bp.route("/login")
def login():
    return render_template("login.html")

@view_bp.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")

@view_bp.route("/equipment")
def equipment():
    return render_template("equipment.html")

@view_bp.route("/kanban")
def kanban():
    return render_template("kanban.html")

@view_bp.route("/calendar")
def calendar():
    return render_template("calendar.html")

@view_bp.route("/teams")
def teams():
    return render_template("teams.html")

@view_bp.route("/reports")
def reports():
    return render_template("reporting.html")


@view_bp.route("/register")
def register():
    return render_template("signup.html")