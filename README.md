# To-Do-application-with-react-js-and-fastapi

A full-stack To-Do Application built with React.js, FastAPI, and PostgreSQL using SQLAlchemy ORM. Users can create, update, mark complete, and delete tasks with a secure REST API, persistent database storage, and a clean responsive UI. Designed as a production-ready project showcasing modern backend + frontend architecture, proper API structure, and database modeling.
⚙️ Technology Stack
Backend
Python – Powerful and widely adopted language for building scalable backend APIs.
FastAPI – Modern, fast, and high-performance web framework for building REST APIs.
Uvicorn – ASGI server used to run FastAPI applications.
PostgreSQL – Reliable and popular relational database.
SQLAlchemy – ORM for structured and efficient database interactions.

Frontend
React – Popular JavaScript library for building dynamic UIs.
TypeScript – Statically typed superset of JavaScript for better reliability.
Vite – Fast development bundler with hot reload and optimized builds.

📂 Project Structure
todo-app/
│
├── backend/
│   ├── __init__.py
│   ├── main.py
│   ├── models.py
│   ├── initialize_db.py
│   ├── routers/
│   │   ├── create_task.py
│   │   ├── delete_task.py
│   │   ├── read_tasks.py
│   │   ├── reorder.py
│   │   ├── update_task.py
│   │   ├── __init__.py
│   ├── schemas/
│   │   ├── reorder_request.py
│   │   └── task.py
│   └── requirements.txt
│
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   ├── pages/
│   │   ├── App.tsx
│   │   ├── main.tsx
│   │   └── ...
│   ├── index.html
│   ├── package.json
│   ├── vite.config.ts
│   └── ...
│
├── screenshots/
│
└── README.md
▶️ Running the Project
1️⃣ Backend

Create a PostgreSQL database and add a .env file inside the backend folder:

DB_HOST=localhost
DB_USER=todo_user
DB_PASSWORD=123
DB_NAME=todo_db


(You can rename .env.example to .env and update values)

Activate Virtual Environment

# Windows
.\venv\Scripts\activate  

# macOS / Linux
source venv/bin/activate


Start Backend Server

uvicorn main:app --reload


Backend runs at:
👉 http://127.0.0.1:8000/

2️⃣ Frontend

Install dependencies:

npm install


Run development server:

npm run dev


or:

npx vite


Frontend runs at:
👉 http://127.0.0.1:5173/

🔄 Alternative Start

Run from project root:

Windows

.\start.ps1


Linux

chmod +x start.sh
./start.sh

📝 TO-DO / Future Enhancements

🌟 Upcoming planned features:

Loading spinner on delete

Integrate Ruff linter

Add Mypy static type checking

Docker + CI/CD setup

New modern UI with animations

Edit task description

Task reordering

Smooth exit animations using Framer Motion

Add PWA support
