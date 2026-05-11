<div align="center">

<br/>

```
 ██████╗ ███████╗███╗   ███╗██╗███╗   ██╗██╗
██╔════╝ ██╔════╝████╗ ████║██║████╗  ██║██║
██║  ███╗█████╗  ██╔████╔██║██║██╔██╗ ██║██║
██║   ██║██╔══╝  ██║╚██╔╝██║██║██║╚██╗██║██║
╚██████╔╝███████╗██║ ╚═╝ ██║██║██║ ╚████║██║
 ╚═════╝ ╚══════╝╚═╝     ╚═╝╚═╝╚═╝  ╚═══╝╚═╝
```

### **Intelligent Multi-Agent System Powered by Gemini**

*Building agents that reason, plan, and execute tasks for real-world challenges.*

<br/>

[![License](https://img.shields.io/badge/License-Apache_2.0-4285F4.svg?style=for-the-badge)](LICENSE)
[![Google Cloud](https://img.shields.io/badge/Google_Cloud-Agent_Builder-4285F4?style=for-the-badge&logo=google-cloud&logoColor=white)](https://cloud.google.com)
[![Gemini](https://img.shields.io/badge/Powered_by-Gemini_3-DB4437?style=for-the-badge&logo=google&logoColor=white)](https://deepmind.google/technologies/gemini/)
[![Hackathon](https://img.shields.io/badge/Google_Cloud-Rapid_Agent_Hackathon-0F9D58?style=for-the-badge)](https://google-cloud-rapid-agent.devpost.com/)

<br/>

[![Self-Healing](https://img.shields.io/badge/⚙_Self--Healing-Pipelines-1a0a00?style=flat-square&labelColor=3d1f00&color=6b3300)](.)
[![Multi-Agent](https://img.shields.io/badge/🐝_Multi--Agent-Swarm-1a0a00?style=flat-square&labelColor=3d1f00&color=6b3300)](.)
[![HITL](https://img.shields.io/badge/👁_Human--in--the--Loop-Escalation-1a0a00?style=flat-square&labelColor=3d1f00&color=6b3300)](.)
[![Green](https://img.shields.io/badge/🌿_Green_Agent-Routing-1a0a00?style=flat-square&labelColor=3d1f00&color=6b3300)](.)

</div>

<br/>

---

<br/>

## `>_ what is gemini agent framework`

This is an **autonomous, self-healing multi-agent system** built with **Google Gemini 3** and **Google Cloud Agent Builder**. It demonstrates how AI agents can move beyond simple chatbots to accomplish complex, multi-step tasks across real-world workflows — from DevSecOps automation to data pipeline management.

> Where traditional AI tools answer questions, **these agents take action.**
> They are outcome-driven, not prompt-driven. You define the mission —
> the agents reason about the steps, use the right tools, and get it done.

**Gemini 3 is the orchestrator** — the central reasoning engine that plans, delegates, and coordinates the entire agent swarm using advanced reasoning capabilities and partner MCP servers for specialized tasks.

<br/>

---

<br/>

## `>_ quickstart`

```bash
# 1. Clone
git clone https://github.com/Agentscreator/gemini-agent-framework.git
cd gemini-agent-framework

# 2. Install
./quickstart.sh

# 3. Configure Google Cloud + Partner MCP Server
export GOOGLE_API_KEY=YOUR_GEMINI_API_KEY
export GITLAB_TOKEN=YOUR_GITLAB_TOKEN  # For GitLab track
# OR configure other partner credentials (Elastic, MongoDB, Fivetran, Arize)

# 4. Run an agent
uv run python -m framework run exports/your_agent --input '{"goal": "your mission"}'

# 5. Launch monitoring dashboard
uv run python -m framework server
```

> Agents use Gemini 3 for reasoning and partner MCP servers for specialized capabilities.

<br/>

---

<br/>

## `>_ gitlab environment setup`

Maven reads GitLab credentials from **environment variables** (highest priority) or from `~/.hive/configuration.json` (set by `maven gitlab setup`).

### Environment Variables

| Variable | Required | Description |
|:---|:---:|:---|
| `GITLAB_TOKEN` | ✅ | Personal Access Token with `api` scope |
| `GITLAB_URL` | — | GitLab instance URL (default: `https://gitlab.com`) |
| `GITLAB_PROJECT` | — | Default project in `namespace/name` format |
| `GITLAB_WEBHOOK_SECRET` | — | Secret token for webhook signature verification |

### Minimum Setup

```bash
export GITLAB_TOKEN=glpat-xxxxxxxxxxxxxxxxxxxx
export GITLAB_PROJECT=your-namespace/your-project
```

### Self-Hosted GitLab

```bash
export GITLAB_URL=https://gitlab.your-company.com
export GITLAB_TOKEN=glpat-xxxxxxxxxxxxxxxxxxxx
export GITLAB_PROJECT=your-namespace/your-project
export GITLAB_WEBHOOK_SECRET=your-webhook-secret
```

### Token Permissions

Your GitLab Personal Access Token needs the following scopes:

| Scope | Purpose |
|:---|:---|
| `api` | Read/write access to projects, MRs, issues, pipelines |
| `read_repository` | Clone and read repository contents |

Create a token at: `https://gitlab.com/-/user_settings/personal_access_tokens`

### Interactive Setup

```bash
maven gitlab setup       # guided prompt, saves to ~/.hive/configuration.json
maven gitlab status      # verify connection
maven gitlab test        # full connectivity check (auth, project, pipelines, webhooks)
```

### Webhook Registration

GitLab must be able to reach Maven's server to deliver events. For local development, use a tunnel:

```bash
# Terminal 1 — start tunnel
ngrok http 8787

# Terminal 2 — register webhook using the tunnel URL
maven gitlab register --project your-namespace/your-project \
  --url https://abc123.ngrok.io/webhooks/gitlab
```

For production, set `GITLAB_WEBHOOK_SECRET` to validate that payloads come from GitLab.

<br/>

---

<br/>

## `>_ the challenge`

**Google Cloud Rapid Agent Hackathon: Building Agents for Real-World Challenges**

This project demonstrates how to build functional agents that solve real-world problems using:
- **Gemini 3** for advanced reasoning and planning
- **Google Cloud Agent Builder** for rapid prototyping and orchestration
- **Partner MCP Servers** (GitLab, Elastic, MongoDB, Fivetran, Arize) for specialized capabilities

<br/>

<div align="center">

| Challenge | Agent Solution |
|:---|:---|
| 🎯 **Multi-Step Missions** | Agents plan steps, use tools, and complete complex workflows |
| 🔧 **Partner Integration** | MCP servers provide "superpowers" (GitLab CI/CD, Elastic search, MongoDB data) |
| 🧠 **Advanced Reasoning** | Gemini 3 handles context, makes decisions, adapts to failures |
| 👁️ **Human-in-the-Loop** | Agents escalate when confidence is low, keeping you in control |

</div>

<br/>

> This isn't a chatbot. It's an agent that **gets things done**.

<br/>

---

<br/>

## `>_ how it works`

### The Core Loop

```
  User Mission / Event Trigger
        │
        ▼
  ┌─────────────────────────────────────────┐
  │    Orchestrator Agent (Gemini 3)        │
  │  · Interprets goal → plans steps        │
  │  · Generates agent graph                │
  │  · Evaluates outcomes                   │
  │  · On failure: adapts plan, retries     │
  └──────────────────┬──────────────────────┘
                     │
        ┌────────────▼────────────┐
        │     Agent Swarm         │
        │  (parallel execution)   │
        └────────────┬────────────┘
                     │
        ┌────────────▼────────────┐
        │  Partner MCP Servers    │
        │  (GitLab, Elastic, etc) │
        └────────────┬────────────┘
                     │
          ┌──────────┴──────────┐
          ▼                     ▼
      ✅ Success            ⚠️  Low confidence
   Complete mission        Human-in-the-Loop
   Log & report            Escalation Node
```

<br/>

### Partner Track Examples

<div align="center">

| 🎯 Partner Track | 🤖 Agent Capabilities |
|:---|:---|
| **GitLab** | CI/CD automation · Security patching · Issue triage · MR reviews |
| **Elastic** | Log analysis · Search optimization · Anomaly detection · Index management |
| **MongoDB** | Data pipeline automation · Schema validation · Query optimization |
| **Fivetran** | Data sync monitoring · Connector health checks · Pipeline orchestration |
| **Arize** | Model monitoring · Performance analysis · Drift detection · Observability |

</div>

<br/>

---

<br/>

## `>_ agent architecture`

<br/>

<div align="center">

```
┌──────────────────────────────────────────────────────────────────┐
│                    GEMINI AGENT FRAMEWORK                        │
│                                                                  │
│   🧠  ORCHESTRATOR  (Gemini 3)                                   │
│       Advanced Reasoning · Planning · Coordination               │
│                                                                  │
│   ├── 🔧  Specialized Agents                                     │
│   │       Task-specific agents with domain expertise            │
│   │                                                              │
│   ├── 🔌  Partner MCP Servers                                    │
│   │       GitLab · Elastic · MongoDB · Fivetran · Arize         │
│   │                                                              │
│   ├── 🎯  Goal-Driven Execution                                  │
│   │       Multi-step planning → tool use → outcome validation   │
│   │                                                              │
│   └── 👁️  Human-in-the-Loop                                      │
│           Escalation on low confidence · Approval workflows      │
└──────────────────────────────────────────────────────────────────┘
```

</div>

<br/>

---

<br/>

## `>_ technical architecture`

```
Gemini Agent Framework
├── Event Triggers ──→ Mission Router  (classify & dispatch)
│
├── 🧠 Orchestrator Agent (Gemini 3)
│   ├── Goal interpretation & planning
│   ├── Dynamic agent graph generation
│   ├── Outcome evaluation & validation
│   └── Self-healing / adaptive replanning
│
├── 🤖 Specialized Agent Swarm
│   ├── Domain-specific agents (security, data, ops)
│   ├── Parallel execution with coordination
│   └── Tool orchestration via MCP
│
├── 🔌 Partner MCP Servers
│   ├── GitLab (CI/CD, issues, MRs)
│   ├── Elastic (search, logs, analytics)
│   ├── MongoDB (data operations)
│   ├── Fivetran (data pipelines)
│   └── Arize (ML observability)
│
├── 👁️ Human-in-the-Loop Escalation
│
└── 📊 Real-time Observability Dashboard
    ├── WebSocket streaming
    ├── Cost tracking per agent / mission
    └── Execution logs & decision traces
```

<br/>

### Stack

<div align="center">

| Layer | Technology |
|:---|:---|
| Reasoning Engine | **Gemini 3** (gemini-2.0-flash-exp, gemini-1.5-pro) |
| Agent Builder | **Google Cloud Agent Builder** |
| Runtime | Python 3.11+ |
| LLM Abstraction | LiteLLM (multi-provider support) |
| Tool Protocol | **MCP** — Model Context Protocol |
| Partner Integration | GitLab, Elastic, MongoDB, Fivetran, Arize MCP servers |
| Observability | WebSocket streaming dashboard |
| Credentials | Encrypted store at `~/.hive/credentials` |
| Cost Optimization | Gemini Flash for simple tasks, Pro for complex reasoning |

</div>

<br/>

---

<br/>

## `>_ key features`

<br/>

**`🧠 Gemini 3 Advanced Reasoning`**
Leverages Gemini's extended context windows (up to 2M tokens) and multimodal capabilities for complex planning, decision-making, and tool orchestration across multi-step missions.

**`🔀 Dynamic Agent Graphs`**
No hardcoded workflows. The orchestrator generates a fresh agent graph for every mission based on context. Different problems get different agent configurations and tool chains.

**`👁 Human-in-the-Loop Escalation`**
Every workflow has a configurable confidence threshold. Below it, execution pauses and a structured summary is presented to the user for approval. Timeouts and fallback policies ensure nothing gets stuck.

**`🔌 Partner MCP Integration`**
Seamless integration with partner MCP servers (GitLab, Elastic, MongoDB, Fivetran, Arize) gives agents specialized capabilities without custom API code.

**`💰 Cost-Optimized Routing`**
Tasks are routed by complexity. Simple operations use Gemini Flash (fast, cheap). Complex reasoning uses Gemini Pro. Live cost dashboard tracks spend per agent and mission.

**`🔄 Self-Healing Execution`**
When an agent fails, the orchestrator captures the failure context, reasons about what went wrong, adapts the plan, and retries — automatically, within configurable limits.

**`📊 Real-Time Observability`**
WebSocket-based dashboard shows agent execution in real-time: active missions, tool calls, token usage, costs, and decision traces.

<br/>

---

<br/>

## `>_ configuration`

```yaml
# .hive/policy.yaml

orchestrator:
  model: gemini-2.0-flash-exp  # or gemini-1.5-pro for complex reasoning
  max_retries: 3
  confidence_threshold: 0.75
  max_context_tokens: 1000000  # Gemini's extended context

agents:
  security:
    enabled: true
    auto_commit: true
    require_human_approval_for: ["critical", "high"]
  data_pipeline:
    enabled: true
    partner_mcp: fivetran  # or mongodb, elastic
  observability:
    enabled: true
    partner_mcp: arize
  devops:
    enabled: true
    partner_mcp: gitlab

cost_optimization:
  enabled: true
  simple_tasks_model: gemini-2.0-flash-exp  # Fast, cheap
  complex_tasks_model: gemini-1.5-pro       # Advanced reasoning
  cost_cap_daily_usd: 20.00

human_in_the_loop:
  notification_channel: console  # or slack, email
  escalation_timeout_minutes: 60
  escalation_fallback: log_and_continue

partner_mcp_servers:
  gitlab:
    enabled: true
    token_env: GITLAB_TOKEN
  elastic:
    enabled: false
  mongodb:
    enabled: false
  fivetran:
    enabled: false
  arize:
    enabled: false
```

<br/>

---

<br/>

## `>_ hackathon submission`

**Google Cloud Rapid Agent Hackathon 2026**

This project demonstrates:

✅ **Gemini 3 Integration** — Advanced reasoning and planning with extended context  
✅ **Google Cloud Agent Builder** — Rapid prototyping and orchestration  
✅ **Partner MCP Integration** — GitLab track (primary), extensible to other partners  
✅ **Multi-Step Missions** — Complex workflows with tool orchestration  
✅ **Human-in-the-Loop** — Confidence-based escalation for oversight  
✅ **Real-World Use Cases** — DevSecOps automation, data pipelines, observability  

### Partner Track: GitLab

Primary integration with GitLab MCP server for:
- CI/CD pipeline automation and failure recovery
- Security vulnerability detection and patching
- Issue triage and assignment
- Merge request reviews and compliance checks

### Demo Video

[Link to 3-minute demo video]

### Open Source Repository

[https://github.com/Agentscreator/gemini-agent-framework](https://github.com/Agentscreator/gemini-agent-framework)

### Live Demo

[Link to hosted project if applicable]

<br/>

---

<br/>

<div align="center">

**Gemini Agent Framework** uses [Google Gemini 3](https://deepmind.google/technologies/gemini/) for advanced reasoning,
[Google Cloud Agent Builder](https://cloud.google.com) for orchestration,
and partner MCP servers for specialized capabilities.

<br/>

```
Building agents that don't just answer questions — they accomplish missions.
```

<br/>

*Google Cloud Rapid Agent Hackathon — 2026 Submission*

</div>
