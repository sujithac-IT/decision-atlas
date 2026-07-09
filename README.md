# Decision Atlas

A comprehensive decision-making platform that leverages AI to help users make informed decisions through data analysis and insights.
## **Project Overview**

### **Decision Atlas – AI Decision Intelligence Platform for Public Development**

**Decision Atlas** is an AI-powered, multilingual public development platform that bridges the gap between citizens and government by transforming scattered public feedback into data-driven development decisions.

Citizens can easily register development requests or complaints through **voice, text, images, GPS location, and messaging platforms** using a mobile application. The platform leverages **Google AI technologies** such as **Gemini, Vertex AI, Speech-to-Text, Cloud Translation API, and Google Maps Platform** to analyze submissions, detect recurring issues, identify demand hotspots, and integrate public datasets, demographic information, and infrastructure gaps.

A **multi-agent AI architecture** automates tasks including multilingual processing, complaint clustering, sentiment analysis, geospatial mapping, explainable project prioritization, and intelligent budget optimization. This enables government authorities to objectively rank development projects based on citizen demand, infrastructure needs, expected social impact, and available budgets.

The web dashboard provides decision-makers with real-time analytics, AI-powered recommendations, demand heatmaps, explainable project rankings, and optimized budget allocation, enabling transparent and evidence-based governance.

To promote transparency and public trust, citizens can **track the complete lifecycle of their requests**—from submission and AI analysis to approval, work progress, and project completion—through real-time notifications and progress updates.

By combining citizen participation with Google's AI ecosystem, **Decision Atlas** empowers governments to make faster, fairer, and more impactful development decisions while ensuring every citizen's voice contributes to the future of their community.

---

### **One-Line Elevator Pitch**

> **Decision Atlas is a Google AI-powered decision intelligence platform that transforms multimodal citizen feedback into explainable, data-driven development recommendations while enabling transparent complaint tracking and optimized public resource allocation.**

---

### **Tagline**

**"Every Citizen's Voice. Every Decision Explained."**

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
