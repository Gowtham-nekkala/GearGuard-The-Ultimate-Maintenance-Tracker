# 🛠️ GearGuard – The Ultimate Maintenance Tracker

GearGuard is a lightweight **maintenance management system prototype** designed to help organizations efficiently track assets, assign maintenance responsibilities, and manage repair workflows.

It connects **Equipment**, **Maintenance Teams**, and **Maintenance Requests** into a single, easy-to-use platform, demonstrating how structured workflows can reduce downtime and improve operational visibility.

---

## 🎯 Project Objective

The primary goal of GearGuard is to:

* Maintain a centralized record of company assets
* Streamline the process of reporting and resolving equipment issues
* Automatically assign the correct maintenance team based on equipment
* Provide clear visibility into ongoing and scheduled maintenance tasks

---

## 🧠 Core Concept

```
Equipment  → What needs maintenance
Teams      → Who performs the maintenance
Requests   → The work to be done
```

GearGuard tightly links these three entities to enable smooth and traceable maintenance workflows.

---

## ✨ Key Features

### 🔧 Equipment Management

* Register and manage company assets (machines, vehicles, IT equipment)
* Assign each equipment to a dedicated maintenance team
* Track equipment status: **Active / Scrapped**
* Store essential metadata:

  * Equipment name & serial number
  * Purchase date & warranty details
  * Physical location
  * Ownership (department / employee)

---

### 👥 Maintenance Team Management

* Create specialized maintenance teams (Mechanics, Electricians, IT Support)
* Assign technicians to teams
* Enforce workflow rules so only relevant team members handle assigned requests

---

### 📝 Maintenance Requests

* Create maintenance requests linked to specific equipment
* Supported request types:

  * **Corrective** – Unplanned breakdown repairs
  * **Preventive** – Scheduled routine maintenance
* Auto-fill maintenance team based on selected equipment
* Track request lifecycle:

```
New → In Progress → Repaired → Scrap
```

* Capture repair duration and work details

---

## 📊 Visual Workflow & UI

### 🗂️ Kanban Board

* Primary workspace for technicians
* Drag & drop requests between stages
* Grouped by status:

  * New
  * In Progress
  * Repaired
  * Scrap
* Visual indicators:

  * Assigned technician avatar
  * Overdue task highlighting

---

### 📅 Calendar View

* Displays all **Preventive Maintenance** tasks
* Requests appear on their scheduled date
* Enables quick scheduling of routine maintenance

---

## 🔄 Workflow Overview

### 🔥 Breakdown Maintenance (Corrective)

1. User creates a maintenance request
2. Equipment is selected
3. System auto-assigns the maintenance team
4. Request starts in **New** state
5. Technician picks up the task
6. Work moves to **In Progress**
7. Task is completed and marked **Repaired**

---

### 🧰 Preventive Maintenance

1. Manager schedules a preventive maintenance request
2. Scheduled date is defined
3. Request appears in the Calendar View
4. Technician performs maintenance as planned

---

## 🧱 System Architecture

* **Backend:** Flask (Python)
* **Database:** SQLite
* **Frontend:** HTML, Jinja2 Templates, Bootstrap
* **UI Components:**

  * Kanban Board
  * Calendar View

The system follows a **modular design**, allowing independent development of:

* Equipment
* Maintenance Teams
* Maintenance Requests
* Visualization & UX components

---

## 📁 Project Structure

```bash
.
├── app
│   ├── config.py
│   ├── controllers
│   │   ├── auth_controller.py
│   │   ├── equipment_contoller.py
│   │   ├── __init__.py
│   │   ├── __pycache__
│   │   │   ├── auth_controller.cpython-313.pyc
│   │   │   ├── equipment_contoller.cpython-313.pyc
│   │   │   ├── __init__.cpython-313.pyc
│   │   │   ├── request_controller.cpython-313.pyc
│   │   │   └── team_controller.cpython-313.pyc
│   │   ├── request_controller.py
│   │   └── team_controller.py
│   ├── extensions.py
│   ├── __init__.py
│   ├── models
│   │   ├── employee.py
│   │   ├── equipment.py
│   │   ├── __init__.py
│   │   ├── maintenance_request.py
│   │   ├── maintenance_team.py
│   │   ├── __pycache__
│   │   │   ├── employee.cpython-313.pyc
│   │   │   ├── equipment.cpython-313.pyc
│   │   │   ├── __init__.cpython-313.pyc
│   │   │   ├── maintenance_request.cpython-313.pyc
│   │   │   ├── maintenance_team.cpython-313.pyc
│   │   │   └── users.cpython-313.pyc
│   │   └── users.py
│   ├── __pycache__
│   │   ├── config.cpython-313.pyc
│   │   ├── extensions.cpython-313.pyc
│   │   └── __init__.cpython-313.pyc
│   ├── routes
│   │   ├── auth_route.py
│   │   ├── calendar_route.py
│   │   ├── equipment_route.py
│   │   ├── __init__.py
│   │   ├── kanban_route.py
│   │   ├── maintenance_routes.py
│   │   ├── __pycache__
│   │   │   ├── auth_route.cpython-313.pyc
│   │   │   ├── calendar_route.cpython-313.pyc
│   │   │   ├── equipment_route.cpython-313.pyc
│   │   │   ├── __init__.cpython-313.pyc
│   │   │   ├── kanban_route.cpython-313.pyc
│   │   │   ├── maintenance_routes.cpython-313.pyc
│   │   │   └── view_routes.cpython-313.pyc
│   │   └── view_routes.py
│   ├── services
│   │   ├── assignment_service.py
│   │   ├── auth_service.py
│   │   ├── equipment_service.py
│   │   ├── __init__.py
│   │   ├── maintainance_service.py
│   │   ├── __pycache__
│   │   │   ├── assignment_service.cpython-313.pyc
│   │   │   ├── auth_service.cpython-313.pyc
│   │   │   ├── equipment_service.cpython-313.pyc
│   │   │   ├── __init__.cpython-313.pyc
│   │   │   ├── maintainance_service.cpython-313.pyc
│   │   │   ├── team_service.cpython-313.pyc
│   │   │   └── workflow_service.cpython-313.pyc
│   │   ├── team_service.py
│   │   └── workflow_service.py
│   ├── static
│   │   ├── css
│   │   │   ├── auth.css
│   │   │   └── dashboard.css
│   │   └── js
│   │       └── auth.js
│   ├── templates
│   │   ├── calendar.html
│   │   ├── create-request.html
│   │   ├── dashboard.html
│   │   ├── equipment.html
│   │   ├── index.html
│   │   ├── kanban.html
│   │   ├── login.html
│   │   ├── reporting.html
│   │   ├── signup.html
│   │   └── teams.html
│   └── utils
│       ├── enums.py
│       ├── helpers.py
│       ├── __init__.py
│       └── __pycache__
│           ├── enums.cpython-313.pyc
│           └── __init__.cpython-313.pyc
├── db
│   ├── schema.sql
│   └── seed.sql
├── requirements.txt
└── run.py
```

---

## 🚀 Prototype Scope

This repository contains a **functional prototype** focused on:

* Core data models
* Business logic
* Visual workflow demonstration

Planned future enhancements include:

* Authentication & role-based access
* Notifications & alerts
* Analytics & reporting dashboards
* Advanced automation rules

---

## 📌 Use Cases

* Manufacturing plants tracking machine maintenance
* IT departments managing hardware repairs
* Fleet management and vehicle servicing
* Academic or learning projects for maintenance systems

---

## 🏁 Conclusion

GearGuard demonstrates how a simple yet well-structured maintenance management system can:

* Reduce equipment downtime
* Improve accountability
* Provide clear operational visibility

This project serves as a strong foundation for building a full-scale, enterprise-ready maintenance solution.

---

📐 **Mockup Reference**
Visual design mockups were created using Excalidraw to plan the Kanban and Calendar workflows.
