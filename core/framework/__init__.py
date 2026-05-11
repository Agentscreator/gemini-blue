"""
Gemini Agent Framework: A goal-driven agent runtime for real-world challenges.

Built for the Google Cloud Rapid Agent Hackathon 2026.
Powered by Gemini 3 and partner MCP servers (GitLab, Elastic, MongoDB, Fivetran, Arize).

The runtime is designed around DECISIONS, not just actions. Every significant
choice the agent makes is captured with:
- What it was trying to do (intent)
- What options it considered
- What it chose and why
- What happened as a result
- Whether that was good or bad (evaluated post-hoc)

This gives the orchestrator the information it needs to improve agent behavior.

## Testing Framework

The framework includes a Goal-Based Testing system (Goal → Agent → Eval):
- Generate tests from Goal success_criteria and constraints
- Mandatory user approval before tests are stored
- Parallel test execution with error categorization
- Debug tools with fix suggestions

See `framework.testing` for details.
"""

from framework.llm import GeminiProvider, LLMProvider
from framework.runner import AgentOrchestrator, AgentRunner
from framework.runtime.core import Runtime
from framework.schemas.decision import Decision, DecisionEvaluation, Option, Outcome
from framework.schemas.run import Problem, Run, RunSummary

# Testing framework
from framework.testing import (
    ApprovalStatus,
    DebugTool,
    ErrorCategory,
    Test,
    TestResult,
    TestStorage,
    TestSuiteResult,
)

__all__ = [
    # Schemas
    "Decision",
    "Option",
    "Outcome",
    "DecisionEvaluation",
    "Run",
    "RunSummary",
    "Problem",
    # Runtime
    "Runtime",
    # LLM
    "LLMProvider",
    "GeminiProvider",
    # Runner
    "AgentRunner",
    "AgentOrchestrator",
    # Testing
    "Test",
    "TestResult",
    "TestSuiteResult",
    "TestStorage",
    "ApprovalStatus",
    "ErrorCategory",
    "DebugTool",
]
