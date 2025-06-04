# GuardsPro Security Patrol System

GuardsPro is a full-stack security guard management system that includes features such as guard tracking, shift management, DAR reports, guided site tours, and more. The system consists of a FastAPI backend, a React-based admin dashboard, and a Flutter mobile application.

---

## 🧱 Project Structure

```
guardspro/
├── backend/              # FastAPI backend (Dockerized)
│   ├── app/
│   │   ├── api/
│   │   │   ├── routes/
│   │   │   │   ├── __init__.py
│   │   │   │   ├── auth.py
│   │   │   │   ├── users.py
│   │   │   │   ├── dar_reports.py
│   │   │   │   └── ... (more route modules)
│   │   ├── core/         # Configs and core logic
│   │   ├── crud/         # DB access functions
│   │   ├── models/       # SQLAlchemy models
│   │   ├── schemas/      # Pydantic schemas
│   │   └── main.py       # Entry point
│   ├── alembic/          # DB migrations
│   ├── alembic.ini
│   └── docker-compose.yml
│
├── admin_dashboard/      # React + Vite + TailwindCSS Admin Panel
│   ├── public/
│   ├── src/
│   └── vite.config.ts
│
├── mobile_app/           # Flutter mobile app
│   ├── lib/
│   └── pubspec.yaml
```

---

## 🐳 Backend Setup (FastAPI + PostgreSQL)

### Requirements

- Docker + Docker Compose

### Setup

```bash
cd backend
docker-compose up --build
```

### Environment

Create a `.env` file in `backend/`:

```env
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
POSTGRES_DB=guards_db
DATABASE_URL=postgresql://postgres:postgres@db:5432/guards_db
SECRET_KEY=supersecretkey
ACCESS_TOKEN_EXPIRE_MINUTES=60
```

### Migrations

```bash
docker-compose exec backend alembic upgrade head
```

---

## 🛠 Admin Dashboard (React + Vite + Tailwind)

### Setup

```bash
cd admin_dashboard
npm install
npm run dev
```

### Environment

Create `.env` in `admin_dashboard`:

```env
VITE_API_BASE_URL=http://localhost:8000
```

---

## 📱 Mobile App (Flutter)

### Requirements

- Flutter SDK
- Android Studio or VS Code with Flutter extension

### Setup

```bash
cd mobile_app
flutter pub get
flutter run
```

---

## 🔐 Features (Planned & Implemented)

- [x] Guard Login & Authentication
- [x] User Roles: Admin / Guard
- [x] Check-in / Check-out with GPS
- [x] Panic Button (SOS)
- [x] Daily Activity Reports (DAR)
- [x] Shift Scheduling & Confirmation
- [x] Open Shifts / Swaps / Time Off
- [x] Visitor Management
- [x] Custom Reporting Templates
- [x] Secure Messaging
- [x] Live View / Watch Mode
- [x] Post Orders & Acknowledgment
- [x] Task Assignments & Checklists
- [x] QR/NFC Guided Site Tours
- [x] Vehicle Patrol Tracking
- [x] Guard Profiles & History
- [x] Dark Mode Support
- [x] Autosave Drafts

---

## 🧪 Testing

Coming soon: automated tests for backend API and mobile app integration.

---

## 🚀 Deployment

Backend and dashboard can be containerized and deployed using:

```bash
docker-compose -f backend/docker-compose.yml up -d
```

To serve the React dashboard on a specific port (e.g., 8001), configure `vite.config.ts` or proxy through Apache/Nginx.

---

## 📌 Notes

- Backend is served on port **8000**
- Admin Dashboard on port **8001**
- DB is PostgreSQL running in container named `db`
- Alembic used for DB schema migrations
- Mobile app integrates via the backend's public API

---

## 🧑‍💻 Authors

Developed by [Your Team Name / Company Name]

---

## 📄 License

MIT License. See `LICENSE` file for details.
