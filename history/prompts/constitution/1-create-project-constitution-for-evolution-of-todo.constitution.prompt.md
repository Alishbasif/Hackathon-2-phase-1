---
id: 1
title: Create Project Constitution for Evolution of Todo
stage: constitution
date: 2026-01-01
surface: agent
model: gemini
feature: none
branch: master
user: unknown
command: /sp.constitution
labels: ["constitution", "project-setup", "sdd"]
links:
  spec: null
  ticket: null
  adr: null
  pr: null
files:
  - .specify/memory/constitution.md
  - .specify/templates/plan-template.md
  - .specify/templates/tasks-template.md
tests:
  - none
---

## Prompt

/sp.constitution You are a senior software architect and Spec-Driven Development expert. Generate a professional Markdown file named CONSTITUTION.md for Phase 1 of the “Evolution of Todo” project. This phase is a console-based Todo application that strictly follows Spec-Driven Development where the engineer is not allowed to write code manually and all code must be generated via AI (Claude Code) using specs only. Enforce strict constraints: Python language, console-only execution, in-memory storage, no database, no web UI, no AI chatbot, no cloud, no Docker, and no Kubernetes. Define architectural principles including Single Responsibility Principle, clear separation of concerns, and readable, maintainable code. Define spec governance rules where every feature has its own spec file, implementation must strictly follow the spec, no extra features are allowed, and specs act as the single source of truth. Define output expectations such as clean folder structure and deterministic, predictable behavior

## Response snapshot

I have created the `CONSTITUTION.md` file and updated the `plan-template.md` and `tasks-template.md` to align with the new constitution.

## Outcome

- ✅ Impact: Created the project constitution and updated related templates to ensure consistency with the new principles.
- 🧪 Tests: none
- 📁 Files: Created `.specify/memory/constitution.md` and updated `plan-template.md` and `tasks-template.md`.
- 🔁 Next prompts: Suggest to run `/sp.specify` to create a feature.
- 🧠 Reflection: The process of creating a constitution and ensuring consistency across templates is a crucial first step in SDD.

## Evaluation notes (flywheel)

- Failure modes observed: The shell script for creating PHR was not found. Had to use the agent-native flow. Also, the `replace` tool failed a few times due to incorrect `expected_replacements` value.
- Graders run and results (PASS/FAIL): PASS
- Prompt variant (if applicable): null
- Next experiment (smallest change to try): When using `replace` tool, be more careful with counting the occurrences of the string to be replaced. Or use a different tool to count occurrences first.
