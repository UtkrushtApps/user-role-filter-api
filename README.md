## Task Overview

Utkrusht's user management platform needs an API that lists users filtered by their role and status for internal dashboard and reporting tools. Currently, filtering users using multiple query parameters returns incorrect results, making it difficult for administrators to accurately retrieve the user lists they need. The backend team has noticed that the filtering logic is not combining role and status filters as intended, causing the API to return users that do not match both criteria.

## Guidance

You are building a FastAPI backend service that integrates asynchronously with PostgreSQL using SQLAlchemy ORM. The main focus of this task is to ensure that user filtering by multiple query parameters (role and status) works as expected, both functionally and securely. Maintain a modular code structure, using routers and Pydantic models for validation and serialization. Remember to leverage environment variables for configuration, structure database queries clearly, and follow best practices for async programming and error handling. Containerization and orchestration are handled via Docker and Docker Compose, which are included in the project structure. 

## Objectives

- Implement the `/users` GET endpoint to list all users, supporting optional filtering by `role` and `status` via query parameters.
- Ensure that when both filters are provided, only users matching **both** criteria are returned (not either-or).
- Use SQLAlchemy ORM for database interaction with PostgreSQL, handling async session management.
- Validate all request and response data using Pydantic models.
- Provide clear and consistent API responses, handling errors gracefully.
- The API should be containerized and work seamlessly with the provided PostgreSQL service.

## How to Verify

- When the API is running, sending a GET request to `/users?role=admin&status=active` should return only users whose role is "admin" and status is "active".
- Filtering by just one parameter (e.g., `/users?role=member`) should return all users with the role "member" regardless of status.
- Requests without any query parameters should return all users in the database.
- API responses should match the defined Pydantic schema and not include users who do not satisfy all specified filters.
- The application should start successfully in Docker, and PostgreSQL connectivity must be functional.
