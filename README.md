# 🤖 ElectroMart AI Backend (Flask + Agentic AI)

This repository contains the **AI microservice** for the ElectroMart platform.

It is built using **Flask + LangChain + Google Gemini** and is responsible for handling all **intelligent chatbot interactions**.

---

## 🌐 Live API

* 🔗 AI Backend (Flask):
  https://electromart-ai-backend.onrender.com

---

## 🧠 What is this service?

This is a **dedicated AI backend** that powers the ElectroMart chatbot.

Instead of a simple chatbot, it implements an **Agentic AI system** that:

* Understands user queries
* Decides which tool to use
* Fetches real data from APIs
* Generates intelligent responses

---

# 🧠 AI Workflow

```id="ai-flow"
User Message
   ↓
Flask API (/chat)
   ↓
LLM (Gemini)
   ↓
Agent Decision (LangChain)
   ↓
Tool Execution
   ↓
Next.js APIs
   ↓
MongoDB
   ↓
Final AI Response
```

---

# ⚙️ Features

* 🤖 LLM-powered chatbot (Gemini)
* 🧠 Tool-based reasoning (LangChain Agent)
* 🔗 Integration with Next.js backend APIs
* ⚡ Real-time intelligent responses
* 🧩 Modular tool system (extendable)

---

# 🛠️ AI Tools Implemented

### 🔍 1. Product Search

Fetches relevant products based on user query.

```id="tool1"
search_products(query)
```

---

### 📦 2. Order Tracking

Returns user’s recent orders and status.

```id="tool2"
get_user_orders(user_id)
```

---

### 👤 3. User Insights

Provides user-specific data (name, cart, orders).

```id="tool3"
get_user_details(user_id)
```

---

# 🧪 Tech Stack

* Flask (API server)
* LangChain (Agent + Tools)
* Google Gemini API (LLM)
* Requests (API calls to Next.js backend)
* Gunicorn (Production server)

---

# 🏗️ Architecture

```id="arch"
Frontend (Next.js - Vercel)
        ↓
Flask AI Server (Render)
        ↓
Next.js API (Vercel)
        ↓
MongoDB Atlas
```

---

# 🚀 Run Locally

```bash id="run1"
pip install -r requirements.txt
python app.py
```

Server runs at:

```text id="run2"
http://127.0.0.1:5012
```

---

# ☁️ Deployment

Deployed using **Render**

### Start Command:

```bash id="deploy"
gunicorn app:app --bind 0.0.0.0:$PORT --workers 2 --timeout 120
```

---

# ⚡ Key Highlights

* 🔥 Agentic AI (not rule-based chatbot)
* 🧠 Real-time decision making
* 🔗 Deep integration with backend APIs
* 📦 Production-ready microservice
* ⚙️ Scalable architecture

---

# 📈 Future Improvements

* Memory (chat history awareness)
* Recommendation engine
* Vector DB (semantic search)
* LangGraph for advanced workflows
* Multi-step reasoning chains

