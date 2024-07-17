Overview:

The NTT Task Management Portal is a lightweight, web-based application designed to facilitate the tracking and management of development tasks. Built using the Django web framework, it provides an intuitive interface for managing tasks through various stages of development.

Key Features
Task Creation: Users can create tasks with details such as title, start date, due date, and assignee.
Task Management: Tasks can be moved between statuses (Scheduled, In Progress, Completed, Deleted) to reflect their current state.
Team Management: Admins can manage team members, including adding and editing member details.
Technology Stack
Frontend: HTML, CSS, Bootstrap for responsive design.
Backend: Django web framework.
Database: SQLite, chosen for its lightweight nature and ease of integration with Django, making it ideal for small-scale applications like this task management portal.
Setup and Deployment
The application is containerized using Docker, simplifying the deployment process and ensuring consistency across different environments.

Getting Started with Docker

Build the Docker Image:
Navigate to the project directory where the Dockerfile is located and run:
" docker build -t ntt-task-portal . "

Run the Container:
Once the image is built, you can start the container by running:
" docker run -p 8000:8000 ntt-task-portal "
This command maps port 8000 of the container to port 8000 on your host, allowing you to access the application at http://localhost:8000.

Database Usage
SQLite is used as the database for this application due to its simplicity and ability to handle the data needs of a small-scale task management tool without requiring complex setup or maintenance. This makes it an excellent choice for development and testing phases, with the capability to switch to more robust databases like PostgreSQL for production if necessary.

Project Documentation
The project is structured around Django’s design patterns, using the MVC architecture. Here’s a brief on the major components:

Models: Define the data structures for Task and TeamMember.
Views: Handle the business logic and interact with the models to carry data to and from the database.
Templates: Render the data provided by views to display in the user’s browser.

Conclusion
The NTT Task Management Portal exemplifies a practical implementation of Django’s robust capabilities tailored to manage development tasks effectively. It showcases how Django can be used to build functional applications with minimal setup, making it an excellent choice for developers looking to implement fast and efficient solutions.
