# Technical Context

## Project Overview
**Project Name:** acp_testing
**Architecture:** Hybrid Archon System
**Date Initialized:** 2026-01-31

## Tech Stack
- Cursor IDE with Skills system
- Memory-based orchestration (4-file system)
- Hybrid routing: Fast Lane (Memory) vs Slow Lane (Skills)

## Architecture Decisions (ADRs)

### ADR-001: Hybrid Archon Memory System
**Date:** 2026-01-31
**Status:** Active
**Decision:** Use 4-file memory system for context management
- `active_brief.md` - Current task tracking
- `tech_context.md` - Technical decisions and stack
- `lessons.md` - Historical knowledge and patterns
- `roadmap.md` - Project vision and progress

**Rationale:** Balances speed (Fast Lane) with depth (Slow Lane) using System 1 vs System 2 mental model.

## Design Patterns
- OODA Loop (Observe, Orient, Decide, Act)
- Smart routing based on task classification
- Memory-driven execution for routine tasks
- Skill-driven execution for complex tasks

## Notes
- Memory files should be kept concise (< 10KB)
- Always preserve existing content when updating
- Use chronological ordering for new entries
