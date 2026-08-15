BankCompliance AI (`bank-compliance-ai-app`)

An Enterprise Cloud-Native Banking Regulatory & Compliance Copilot built on **Azure Kubernetes Service (AKS)** and **Azure OpenAI**, powered by **LiteLLM Gateway**, **Qdrant Vector DB**, and **Azure AI Content Safety**.

Live at: **`https://bank.mytaxbot.site`**

---

### Quick Start (Local Development)

### 1. Backend (FastAPI)
```bash
cd backend
python -m venv .venv
source .venv/bin/activate # On Windows: .venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload --port 8000
```

### 2. Frontend (React + Vite)
```bash
cd frontend
npm install
npm run dev
```

---

## ðŸ›ï¸ Infrastructure Link
Infrastructure is provisioned via Terraform in [`terraform-azure-iac/workloads/bank-compliance-ai-aks`](https://github.com/RepoCodeGanesh/terraform-azure-iac/tree/main/workloads/bank-compliance-ai-aks).
