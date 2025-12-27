🛠️ GearGuard – The Ultimate Maintenance Tracker

GearGuard is a lightweight maintenance management system designed to help organizations efficiently track their assets, assign maintenance responsibilities, and manage repair workflows. The system connects equipment, maintenance teams, and maintenance requests into a single, easy-to-use platform.

This project is built as a functional prototype to demonstrate core maintenance workflows such as breakdown handling, preventive maintenance scheduling, and technician task management.

🎯 Project Objective

The primary goal of GearGuard is to:

Maintain a centralized record of company assets

Streamline the process of reporting and resolving equipment issues

Assign the right maintenance team automatically based on the equipment

Provide clear visibility of ongoing and scheduled maintenance tasks

🧠 Core Concept

Equipment → What needs maintenance
Maintenance Teams → Who performs the maintenance
Maintenance Requests → The work to be done

GearGuard ensures that these three elements are tightly connected to enable a smooth maintenance workflow.

✨ Key Features
🔧 Equipment Management

Register and manage company assets (machines, vehicles, IT equipment)

Assign each equipment to a dedicated maintenance team

Track equipment status (Active / Scrapped)

👥 Maintenance Team Management

Create specialized maintenance teams (Mechanics, Electricians, IT Support)

Assign technicians to teams

Ensure only relevant team members handle assigned requests

📝 Maintenance Requests

Create maintenance requests for equipment

Support two request types:

Corrective (Breakdown repairs)

Preventive (Routine maintenance)

Auto-fill maintenance team based on selected equipment

Track request lifecycle:
New → In Progress → Repaired → Scrap

📊 Visual Workflow

Kanban Board for technicians to manage tasks using drag & drop

Calendar View to display scheduled preventive maintenance

Visual indicators for request status and overdue tasks

🔄 Workflow Overview
Breakdown Maintenance

User creates a maintenance request

Equipment is selected

System auto-assigns the maintenance team

Technician picks up the request

Work is completed and marked as Repaired

Preventive Maintenance

Manager schedules a preventive request

Request appears in the calendar on the scheduled date

Technician performs the maintenance as planned

🧱 System Architecture

Backend: Flask (Python)

Database: SQLite

Frontend: HTML, Jinja2 Templates, Bootstrap

UI Components: Kanban board, Calendar view

The project follows a modular design, allowing independent development of Equipment, Teams, Requests, and Visualization components.

📁 Project Structure
gearguard/
│── app.py
│── models.py
│── templates/
│── static/
│── README.md

🚀 Prototype Scope

This repository contains a working prototype focusing on:

Core data models

Business logic

Visual workflow demonstration

Advanced features such as authentication, notifications, and analytics can be added in future iterations.

📌 Use Cases

Manufacturing plants tracking machine maintenance

IT departments managing hardware repairs

Fleet management and vehicle servicing

Educational or academic maintenance projects

🏁 Conclusion

GearGuard demonstrates how a simple, well-structured system can significantly improve maintenance operations by reducing downtime, improving accountability, and providing clear operational visibility.
