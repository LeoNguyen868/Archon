# ADR-001: Documentation Strategy for Open Source Project

**Status:** Accepted
**Date:** 2026-01-29

## Context
Archon is transitioning to an open source project and needs comprehensive documentation to enable external contributors. The project has a complex skills-centric architecture with OODA loop decision-making that must be clearly documented. Current documentation is scattered across various files and lacks a cohesive structure suitable for external contributors.

## Decision
We will implement a hierarchical documentation structure with four main categories:

1. **Project Overview** (`README.md`, `docs/overview/`)
   - High-level project description
   - Key features and architecture concepts
   - Getting started guide

2. **Technical Architecture** (`docs/architecture/`)
   - Skills-centric architecture explanation
   - OODA loop implementation details
   - Worker orchestration system
   - Context management patterns

3. **Contributor Documentation** (`CONTRIBUTING.md`, `docs/contributing/`)
   - Development environment setup
   - Contribution guidelines and workflows
   - Skill development guide
   - Testing and code review processes

4. **API Documentation** (`docs/api/`)
   - Skill development API
   - Worker orchestration interfaces
   - Context management API
   - Code examples and tutorials

## Consequences

**Positive:**
- Clear documentation hierarchy helps contributors find information quickly
- Skills-centric architecture is properly explained as the core differentiator
- OODA loop documentation enables understanding of decision-making framework
- API documentation facilitates extension development
- Consistent structure across all documentation types

**Negative:**
- Initial documentation creation requires significant effort
- Ongoing maintenance needed to keep docs synchronized with code
- Risk of documentation becoming outdated during rapid development
- Complex architecture concepts may be challenging to explain clearly

**Risks:**
- Contributors may be overwhelmed by documentation complexity
- Documentation maintenance burden on core team
- Potential for documentation to diverge from implementation

**Mitigation:**
- Use automated documentation generation tools where possible
- Integrate documentation validation into CI/CD pipeline
- Establish documentation maintenance as part of development workflow
- Create contributor documentation templates to reduce maintenance burden