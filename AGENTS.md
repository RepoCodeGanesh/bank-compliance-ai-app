# Repository Configuration & AI Agent Context

## 🎯 Repository Purpose & Intent
This repository houses the **BankCompliance AI (`bank-compliance-ai-app`)** application codebase — an Enterprise Cloud-Native Banking Regulatory & Compliance Copilot built on **Azure Kubernetes Service (AKS)** and **Azure OpenAI**.

---

## 🔗 Infrastructure Connection & Multi-Repo Mapping

This application connects directly to the infrastructure provisioned by **`terraform-azure-iac`** (`workloads/bank-compliance-ai-aks`):

| Resource Type | Resource Name | Home Subscription | Connection Role |
| :--- | :--- | :--- | :--- |
| **AKS Cluster** | `aks-ht-bankc-p-cin-01` | `Apps-prod` (`f4ffefe1-d689-4059-969c-ccc73e2a11d4`) | Hosts FastAPI Backend, LiteLLM Gateway, and Qdrant DB |
| **Spoke VNet** | `vnet-ht-bankc-p-cin-01` | `Apps-prod` (`f4ffefe1-d689-4059-969c-ccc73e2a11d4`) | Subnet `10.42.1.0/24` with Azure CNI Overlay (`192.168.0.0/16`) |
| **Static Web App** | `stapp-ht-bankc-p-cin-01` | `Apps-prod` (`f4ffefe1-d689-4059-969c-ccc73e2a11d4`) | Hosts React Frontend SPA on **`bank.mytaxbot.site`** |
| **AI Content Safety** | `cs-ht-bankc-p-sea-01` | `Apps-prod` (`f4ffefe1-d689-4059-969c-ccc73e2a11d4`) | Prompt Injection Defense & PII Redaction (`F0` Free Tier) |
| **Azure OpenAI** | `oai-ht-taxb-p-eus-01` | `Apps-prod` (`f4ffefe1-d689-4059-969c-ccc73e2a11d4`) | LLM Inferences via `gpt-5.4-nano` (Sub-second SLA) |
| **APIM Gateway** | `apim-ht-ss-p-cin-01` | `Shared-services` (`859a785c-bd38-402d-b595-1f44f40fb9bf`) | Edge Rate Limiting (20 req/min) & CORS Gateway |
| **Log Analytics** | `law-ht-ss-p-cin-01` | `Shared-services` (`859a785c-bd38-402d-b595-1f44f40fb9bf`) | Central Telemetry & Container Insights |

---

## 🏛️ Architecture & Component Responsibilities

1. **Frontend (`frontend/`)**: Modern React Web SPA deployed on Azure Static Web Apps bound to **`https://bank.mytaxbot.site`**.
2. **Backend API (`backend/`)**: Python FastAPI backend with PII auto-masking (PAN/Aadhaar) and hierarchical RBI Master Direction clause citations.
3. **AI Gateway (`k8s/litellm/`)**: In-cluster LiteLLM proxy managing department token quotas, in-memory KV prompt caching (<20ms repeat answers), and sub-second routing to Azure OpenAI.
4. **Vector Storage (`k8s/qdrant/`)**: Qdrant vector database running on a **4GB Azure Managed Disk (`managed-csi`, ~$0.15/mo)** for permanent persistence across cluster stops.
5. **FinOps & Autoscaling (`k8s/keda/`)**: KEDA event-driven autoscaling with **Scale-to-Zero (`minReplicaCount: 0`)** when no queries are in flight.
6. **Authentication**: Passwordless Azure Workload Identity Federation (OIDC) between AKS service accounts and Entra ID managed identities.
