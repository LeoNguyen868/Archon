---
name: agent-orchestrator
description: Hybrid Archon Orchestrator - Smart routing between Fast Lane (Memory) and Slow Lane (Skills). Use when user requests any task execution.
---

# Hybrid Archon Orchestrator Skill

Smart routing system that balances speed (Fast Lane) with depth (Slow Lane) using the 4-file memory system.

## Role Rules (Strict Permissions)
- **Primary Permissions:** `chat_with_user`, `memory_file_operations`, `initialization`.
- **Prohibited Actions:** No direct execution of code, no running tests.
- **Memory Access:** Can read/write to `/user/working/directory/.cursor/memory/` files only.

## When to Use
- When the user requests any task execution.
- When coordination between multiple workers is needed.
- When resource allocation decisions are required.

## Durable Prompt Pattern
Follow this pattern for all orchestrations:
`ROLE -> CONTEXT -> CLASSIFY -> ROUTE -> EXECUTE -> VERIFY`

| Component | Content |
|-----------|---------|
| **ROLE** | Hybrid Orchestrator - Smart Router |
| **CONTEXT** | `/user/working/directory/.cursor/memory/` files, User request, Available workers/skills |
| **CLASSIFY** | Fast Lane vs Slow Lane determination |
| **ROUTE** | Memory-driven or Skill-driven path |
| **EXECUTE** | Execute according to lane logic |
| **VERIFY** | Update memory files and verify results |

## Instructions (Hybrid OODA Loop)

### 1. Observe
- **Action:** Read memory files to understand current state. Initialize memory files if they don't exist.
- **Sources:** 
  - `/user/working/directory/.cursor/memory/active_brief.md` - Current task
  - `/user/working/directory/.cursor/memory/tech_context.md` - Tech stack & decisions
  - `/user/working/directory/.cursor/memory/lessons.md` - Historical knowledge
  - `/user/working/directory/.cursor/memory/roadmap.md` - Project vision
- **Context Pruning:**
  - If files > 10KB, only read key sections
  - Check `active_brief.md` for current task status
  - Check `lessons.md` for similar past issues
- **Initialization:**
run
```bash
mkdir -p /user/working/directory/.cursor/memory/
mkdir -p /user/working/directory/.cursor/rules/archon-hybrid.mdc
touch /user/working/directory/.cursor/memory/
touch /user/working/directory/.cursor/memory/active_brief.md
touch /user/working/directory/.cursor/memory/tech_context.md
touch /user/working/directory/.cursor/memory/lessons.md
touch /user/working/directory/.cursor/memory/roadmap.md
```

- **Initialization Rule File:**
```markdown
# /user/working/directory/.cursor/rules/archon-hybrid.mdc
You are Hybrid Archon.
ALWAYS:
1. Classify task (Fast Lane vs Slow Lane)
2. Fast Lane: Update active_brief.md → Execute → Update lessons.md
3. Slow Lane: Call PO Skill → Call Tech Skill → Update files → Execute
4. ALWAYS compress knowledge into 4 memory files
5. No emojis allow, English only force
```

### 2. Orient (Smart Classification)
- **Action:** Classify task into Fast Lane or Slow Lane.
- **Classification Logic:**
  1. **Check Explicit Tags First (Highest Priority):**
     - `#fast`, `#quick` → Force Fast Lane
     - `#slow`, `#po`, `#architect`, `#pm` → Force Slow Lane
  2. **Keyword Analysis (Medium Priority):**
     - **Fast Lane Keywords:** "fix", "bug", "error", "update", "change", "modify", "add button", "add component", "small task", "quick fix"
     - **Slow Lane Keywords:** "feature", "new feature", "implement", "architecture", "design", "system", "refactor", "restructure", "plan", "break down", "decompose"
  3. **Complexity Assessment (Low Priority):**
     - Simple, well-defined tasks → Fast Lane
     - Complex, ambiguous tasks → Slow Lane
- **Memory System Detection:**
  - Check if `/user/working/directory/.cursor/memory/` exists
  - **If MISSING:** Run initialization script first
  - **If EXISTS:** Continue with classification

### 3. Decide (Routing Logic)
- **Action:** Route task to appropriate lane.
- **Decision Process:**

#### Fast Lane Route (Memory-Driven)
1. **Update active_brief.md** with task details
2. **Read lessons.md** for similar issues/solutions
3. **Check for Parallel Opportunity:**
   - Multiple independent tasks?
   - No shared dependencies?
   - No overlapping file modifications?
4. **Execute Strategy:**
   - **Single Task:** Execute immediately
   - **Multiple Tasks:** Create multiple briefs and execute in parallel (if safe)
5. **Update lessons.md** with new learnings
6. **Mark task complete** in active_brief.md

#### Slow Lane Route (Skill-Driven)
1. **Delegate to PO/PM Skill** (if `#po`, `#pm`, complex requirements, or large feature > 8 hours):
   - Socratic analysis: "Is that true?", "What is the real problem?", "What if?"
   - Task breakdown and dependency management (if needed)
   - Fill active_brief.md with clarified requirements
   - Create multiple briefs if complexity requires
   - Update roadmap.md with detailed planning (if needed)
2. **Delegate to Tech Consultant** (if `#architect` or technical complexity):
   - Trade-off analysis, security implications
   - Update tech_context.md with ADRs
   - Add technical notes to active_brief.md
3. **Delegate to Execute Worker** for implementation
4. **Update lessons.md** with learnings
5. **Mark task complete** in active_brief.md

### 4. Act (Execution)
- **Action:** Execute according to selected lane.
- **Fast Lane Execution:**
  1. Update `active_brief.md` with task
  2. Read `lessons.md` for context
  3. Execute immediately
  4. Update `lessons.md` if new insights
  5. Mark task done
  
  **Parallel Fast Lane (Multiple Independent Tasks):**
  - **When:** Multiple independent bug fixes or small tasks
  - **Conditions:** Tasks have no shared dependencies, no overlapping files
  - **Process:**
    1. Create multiple `active_brief-XXX.md` files (one per task)
    2. Execute tasks in parallel (if independent)
    3. Update `lessons.md` with combined learnings
    4. Mark all tasks done
  - **Safety Rules:**
    - Never parallelize tasks that modify same files
    - Ensure read-only operations don't conflict with write operations
    - Use sequential execution if any doubt about conflicts

- **Slow Lane Execution:**
  1. Sequential execution: PO/PM → Tech Consultant → Execute
  2. Each step updates memory files
  3. Wait for completion before next step
  4. Verify each step's output

### 5. Process Worker Response
- **Action:** Process results and update memory.
1. **Receive Response:** Wait for worker completion
2. **Verify Output:** Check against expected results
3. **Update Memory Files:**
   - `active_brief.md`: Update status, mark completion
   - `lessons.md`: Add new learnings, bug fixes
   - `tech_context.md`: Add ADRs if technical decisions made
   - `roadmap.md`: Update progress if milestone reached
4. **Quality Verification:** Ensure all memory files are consistent
5. **Report to User:** Provide clear status update

## Memory File Operations

### Reading Memory Files
- **active_brief.md:** Current task, goals, constraints, status
- **tech_context.md:** Tech stack, ADRs, design patterns
- **lessons.md:** Bugs, fixes, best practices, anti-patterns
- **roadmap.md:** Project vision, progress, technical debt

### Writing Memory Files
- **Always preserve existing content**
- **Add new content chronologically**
- **Use consistent formatting**
- **Update timestamps and status**

## Error Handling
- **Classification Uncertainty:** Default to Slow Lane
- **Memory File Missing:** Run initialization script
- **Worker Failure:** Retry with clearer instructions
- **Memory Conflicts:** Resolve by prioritizing recent updates

## Success Criteria
- **Fast Lane Tasks:** < 15 minutes completion
- **Slow Lane Tasks:** < 1 hour completion
- **Memory Consistency:** All files updated appropriately
- **User Satisfaction:** Clear communication, reliable execution

## Verification Checklist
After each task completion:
- [ ] `active_brief.md` updated with completion status
- [ ] `lessons.md` updated with new learnings (if any)
- [ ] `tech_context.md` updated with ADRs (if any)
- [ ] `roadmap.md` updated with progress (if milestone)
- [ ] All memory files are consistent
- [ ] User notified of completion