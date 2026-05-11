# Framework

A goal-driven agent runtime powered by Gemini 3 for real-world challenges.

**Google Cloud Rapid Agent Hackathon 2026 Submission**

## Overview

Framework provides a runtime that captures **decisions**, not just actions. This enables continuous improvement of agent behavior by understanding:

- What the agent was trying to accomplish
- What options it considered
- What it chose and why
- What happened as a result

Built with **Gemini 3** for advanced reasoning and **partner MCP servers** for specialized capabilities.

## Installation

```bash
uv pip install -e .
```

## Agent Building

Agent scaffolding is handled by the `coder-tools` MCP server (in `tools/coder_tools_server.py`), which provides the `initialize_and_build_agent` tool and related utilities. The package generation logic lives directly in `tools/coder_tools_server.py`.

See the [Getting Started Guide](../docs/getting-started.md) for building agents.

## Quick Start

### Calculator Agent

Run an LLM-powered calculator:

```bash
# Run an exported agent
uv run python -m framework run exports/calculator --input '{"expression": "2 + 3 * 4"}'

# Interactive shell session
uv run python -m framework shell exports/calculator

# Show agent info
uv run python -m framework info exports/calculator
```

### Using the Runtime

```python
from framework import Runtime, GeminiProvider

# Initialize with Gemini
provider = GeminiProvider()  # Uses GOOGLE_API_KEY env var
runtime = Runtime("/path/to/storage", llm_provider=provider)

# Start a run
run_id = runtime.start_run("my_goal", "Description of what we're doing")

# Record a decision
decision_id = runtime.decide(
    intent="Choose how to process the data",
    options=[
        {"id": "fast", "description": "Quick processing", "pros": ["Fast"], "cons": ["Less accurate"]},
        {"id": "thorough", "description": "Detailed processing", "pros": ["Accurate"], "cons": ["Slower"]},
    ],
    chosen="thorough",
    reasoning="Accuracy is more important for this task"
)

# Record the outcome
runtime.record_outcome(
    decision_id=decision_id,
    success=True,
    result={"processed": 100},
    summary="Processed 100 items with detailed analysis"
)

# End the run
runtime.end_run(success=True, narrative="Successfully processed all data")
```

### Testing Agents

The framework includes a goal-based testing framework for validating agent behavior.

Tests are generated using MCP tools (`generate_constraint_tests`, `generate_success_tests`) which return guidelines. Claude writes tests directly using the Write tool based on these guidelines.

```bash
# Run tests against an agent
uv run python -m framework test-run <agent_path> --goal <goal_id> --parallel 4

# Debug failed tests
uv run python -m framework test-debug <agent_path> <test_name>

# List tests for an agent
uv run python -m framework test-list <agent_path>
```

For detailed testing workflows, see [developer-guide.md](../docs/developer-guide.md).

### Analyzing Agent Behavior with Builder

The BuilderQuery interface allows you to analyze agent runs and identify improvements:

```python
from framework import BuilderQuery

query = BuilderQuery("/path/to/storage")

# Find patterns across runs
patterns = query.find_patterns("my_goal")
print(f"Success rate: {patterns.success_rate:.1%}")

# Analyze a failure
analysis = query.analyze_failure("run_123")
print(f"Root cause: {analysis.root_cause}")
print(f"Suggestions: {analysis.suggestions}")

# Get improvement recommendations
suggestions = query.suggest_improvements("my_goal")
for s in suggestions:
    print(f"[{s['priority']}] {s['recommendation']}")
```

## Architecture

```
┌─────────────────┐
│  Human Engineer │  ← Supervision, approval
└────────┬────────┘
         │
┌────────▼────────┐
│ Orchestrator    │  ← Gemini 3: Analyzes runs, suggests improvements
│  (Gemini 3)     │
└────────┬────────┘
         │
┌────────▼────────┐
│   Agent Swarm   │  ← Executes tasks, records decisions
│  (Gemini 3 +    │
│   MCP Tools)    │
└─────────────────┘
```

## Key Concepts

- **Decision**: The atomic unit of agent behavior. Captures intent, options, choice, and reasoning.
- **Run**: A complete execution with all decisions and outcomes.
- **Runtime**: Interface agents use to record their behavior.
- **Orchestrator**: Gemini 3-powered reasoning engine that plans and coordinates.

## Requirements

- Python 3.11+
- pydantic >= 2.0
- litellm >= 1.81.0 (for multi-provider LLM support)
- Google API key for Gemini (set GOOGLE_API_KEY env var)
