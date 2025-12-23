# 🥤 **PepsiCo Ad Generator**  
### AI‑Powered Creative Campaign Generator for PepsiCo Brands

<div style="background: linear-gradient(90deg, #005CB4, #E41E2B); padding: 28px; border-radius: 10px; text-align: center; color: white; font-size: 34px; font-weight: bold; margin-bottom: 20px;">
  PepsiCo Ad Generator
</div>

<p align="center">
  <em>AI‑Powered Creative Engine for PepsiCo Products</em><br>
  <em>Built with OpenAI · Gradio · Google Cloud Run</em>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Framework-Gradio-blue?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Language-Python%203.12-yellow?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Cloud-Google%20Cloud%20Run-orange?style=for-the-badge" />
  <img src="https://img.shields.io/badge/LLM-OpenAI%20GPT--3.5--Turbo-green?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Status-Production%20Ready-brightgreen?style=for-the-badge" />
  <img src="https://img.shields.io/badge/License-MIT-lightgrey?style=for-the-badge" />
</p>

---

## 📌 Overview

The **PepsiCo Ad Generator** is a high‑impact, AI‑powered creative assistant designed to generate structured marketing campaigns for PepsiCo products.  
It produces agency‑quality concepts using:

- **OpenAI GPT‑3.5 Turbo**  
- **Gradio** for a clean UI  
- **Google Cloud Run** for scalable deployment  

This project is ideal for enterprise demos, interviews, and real‑world creative workflows.

---

## 🚀 Features

### ✔ Multi‑product selection  
Choose from PepsiCo beverages and snacks.

### ✔ Structured campaign output  
The model returns:

- **Campaign Title**  
- **Hook**  
- **Primary Copy**  
- **Variant A**  
- **Variant B**  
- **Hashtags**  
- **Designer Notes**

### ✔ Marketing brief inputs  
Provide:

- Campaign goal  
- Target audience  
- Tone  
- Channel  
- Promotion  
- Region  
- Extra constraints  

### ✔ Cloud Run optimized  
- Lazy LLM loading  
- Fast cold starts  
- Lightweight dependencies  

---

## 🧠 Tech Stack

| Component | Technology |
|----------|------------|
| UI | Gradio |
| LLM | OpenAI GPT‑3.5 Turbo |
| Backend | Python 3.12 |
| Deployment | Google Cloud Run |
| Container | Docker |
| Infra Automation | Cloud Build |

---

## 📦 Project Structure

```
.
├── app.py
├── requirements.txt
├── Dockerfile
├── .gcloudignore
└── README.md
```

---

## 🛠 Installation (Local)

```bash
pip install -r requirements.txt
python app.py
```

---

## ☁️ Deploying to Google Cloud Run

### 1. Build & push container  
Cloud Build trigger handles this automatically when pushing to GitHub.

### 2. Deploy to Cloud Run  
Set:

- **Port:** 8080  
- **Environment Variable:**  
  - `OPENAI_API_KEY=your_key_here`

### 3. Open the service URL  
Your PepsiCo Ad Generator is live.

---

## 🧪 Example Use Cases

- Social media campaigns  
- In‑store signage concepts  
- Email marketing copy  
- Product launch messaging  
- Creative brainstorming for PepsiCo brands  

---

## 🛡 License

This project is released under the **MIT License**.

---

## 🙌 Author

**Carllos Watts‑Nogueira**  
AI/ML Engineer • LLM Specialist • Prompt Engineer  
