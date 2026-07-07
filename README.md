# Decision Atlas

A comprehensive decision-making platform that leverages AI to help users make informed decisions through data analysis and insights.

## 🚀 Features

- **AI-Powered Insights**: Real-time decision recommendations
- **Data Analytics**: Comprehensive data visualization and analysis
- **Authentication**: Secure user authentication with Firebase
- **Multi-language Support**: i18n support for global users
- **Responsive Design**: Mobile-first frontend architecture
- **Cloud-Ready**: Docker and cloud deployment ready

## 📋 Prerequisites

- Node.js 18+
- Python 3.9+
- Docker & Docker Compose
- Firebase account
- Git

## 🛠️ Tech Stack

### Frontend
- React with TypeScript
- Vite for fast builds
- TailwindCSS for styling
- React Router for navigation
- Context API for state management

### Backend
- FastAPI (Python)
- SQLAlchemy for ORM
- Pydantic for data validation
- AI integration (OpenAI/Claude)

### Infrastructure
- Firebase (Auth, Firestore, Storage)
- Docker containerization
- GitHub Actions CI/CD

## 📁 Project Structure

```
decision-atlas/
├── frontend/          # React TypeScript application
├── backend/           # FastAPI Python application
├── firebase/          # Firebase configuration & rules
├── docs/              # Documentation
└── .github/workflows/ # CI/CD pipelines
```

## 🚀 Quick Start

### Frontend Setup

```bash
cd frontend
npm install
npm run dev
```

### Backend Setup

```bash
cd backend
pip install -r requirements.txt
python -m uvicorn app.main:app --reload
```

### Using Docker Compose

```bash
docker-compose up -d
```

## 📚 Documentation

- [Architecture Guide](./docs/Architecture.pdf)
- [API Documentation](./docs/API_Documentation.md)

## 📝 License

MIT License - See LICENSE file for details

## 🤝 Contributing

Contributions are welcome! Please read CONTRIBUTING.md for details on our code of conduct and the process for submitting pull requests.

## 📧 Contact

For questions or support, please open an issue on GitHub.