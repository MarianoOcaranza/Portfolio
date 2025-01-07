# Personal Portfolio  

This is a personal portfolio project built using **ReactJS** for the frontend and **Django (Python)** for the backend.  
**Django REST Framework (DRF)** is used to handle API calls.  

## Objective  
Create a dynamic personal website to showcase my projects, with a backend to manage them and a user-friendly interface for visitors.  

---

## Current Status  
**Stage 1: Backend Configuration** - Completed 🎉  

---

## Stage 1: Backend Configuration  

### Technologies Used  
- **Django REST Framework (DRF):** To create RESTful APIs.  
- **SQLite3:** Used as the database for initial development and testing.  

### Project Model  
A `Project` model was created to store project data. It includes the following fields:  
- **`title`** *(CharField)*: The title of the project.  
- **`preview`** *(ImageField)*: A preview image for the project.  
- **`description`** *(TextField)*: A short description of the project (default: "No description added").  
- **`created_at`** *(DateTimeField)*: Date and time when the project was created.  
- **`updated_at`** *(DateTimeField)*: Date and time of the last project update.  

### Custom Serializer  
A custom serializer was implemented to convert the `Project` model data into JSON format for API responses.  

### API Endpoints  
- **Endpoint:** `/api/projects/`  
- **HTTP Method:** `GET`  
- **Response:** Returns all projects in JSON format.  
- **Configuration:** Handled in the app’s `urls.py` and the project’s main `urls.py`.  

### Media Configuration  
- Configured a local media directory to store images uploaded via the Django Admin interface.  
- Images are served locally during development using Django’s `MEDIA_URL` and `MEDIA_ROOT` settings.  

### API Testing  
The API endpoint was tested using **Postman**, ensuring that it returns the expected project data in JSON format.  

---

