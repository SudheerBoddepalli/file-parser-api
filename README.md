# 📂 File Parser CRUD API (FastAPI Project)

A backend API built with **FastAPI** that allows users to upload, parse, and manage files (CSV, Excel, etc.) with progress tracking and authentication.

---

## 🚀 Features
- Upload and parse files (CSV/Excel/PDF supported).
- File upload with progress tracking.
- Authentication using JWT (signup/login).
- Retrieve parsed file contents in JSON format.
- Delete uploaded files securely.
- Real-time progress updates via Server-Sent Events (SSE).
- Includes unit tests for core features.

---

## 📁 Project Structure
file-parser-api/
│── app/
│ ├── init.py
│ ├── main.py # FastAPI entry point
│ ├── db.py # Database setup
│ ├── auth.py # Authentication routes
│
│── tests/ # Unit tests
│── uploads/ # Uploaded files (ignored in GitHub if empty)
│── requirements.txt # Python dependencies
│── sample.csv # Sample CSV file
│── README.md # Documentation

yaml
Copy
Edit

---

## ⚙️ Installation

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/SudheerBoddepalli/file-parser-api.git
cd file-parser-api
2️⃣ Create Virtual Environment
bash
Copy
Edit
python -m venv venv
source venv/bin/activate   # For Linux/Mac
venv\Scripts\activate      # For Windows
3️⃣ Install Dependencies
bash
Copy
Edit
pip install -r requirements.txt
▶️ Run the API
bash
Copy
Edit
uvicorn app.main:app --reload
👉 The API will run at:
http://127.0.0.1:8000

📡 API Endpoints
Auth
POST /auth/signup?email=&password=

POST /auth/login?email=&password=

Files
POST /files → Upload a file (multipart) (requires Authorization: Bearer <token>)

GET /files/{file_id}/progress → Get upload/processing progress

GET /files/{file_id} → Retrieve parsed file contents

GET /files → List all files with metadata

DELETE /files/{file_id} → Delete file (requires auth)

GET /files/{file_id}/events → Real-time progress via SSE

🧪 Running Tests
bash
Copy
Edit
pytest -q
📜 Notes
Uploaded files are stored in /uploads (ignored by GitHub).

For production, configure cloud storage (AWS S3, GCP, etc.) instead of local uploads.

Add .gitkeep inside /uploads if you want GitHub to track the empty folder.

📄 License
This project is licensed under the MIT License.

yaml
Copy
Edit

---

✅ This fixes:
- Correct API endpoints (`/files` instead of `/uploadfile`).  
- Removes duplication.  
- Matches your actual folder structure.  
- Looks professional for interview/demo.  

---

👉 Do you want me to **give you this final cleaned `README.md` file ready-to-commit** so you don’t have to manually edit?