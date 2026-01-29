# Đặc tả Thiết kế: Archon System
## Skills-Centric Architecture, Subagent Workers, and Automation Scripts

---

## Phần 1: Skills Centric Architecture

### 1.1 Tổng quan về Skills-Centric Approach

**Triết lý cốt lõi:** Skills là "knowledge modules" hoặc "expert plugins" mở rộng khả năng của agents với domain-specific knowledge, patterns, và best practices.

**Mental Model: The Agent-Skill-Tool Triangle**

```
                    ┌─────────────────┐
                    │     Agent       │
                    │  (LLM + Loop)   │
                    └────────┬────────┘
                             │
         ┌───────────────────┼───────────────────┐
         │                   │                   │
         ▼                   ▼                   ▼
    ┌─────────┐        ┌─────────┐        ┌─────────┐
    │  Skills │        │  Tools  │        │  Goals  │
    │ (What)  │◄───────► │ (How)   │◄───────► │ (Why)  │
    └─────────┘        └─────────┘        └─────────┘
```

**Nguyên tắc:**
1. **Skills**: Định nghĩa domain knowledge và best practices
2. **Tools**: Định nghĩa executable capabilities (APIs, functions, CLIs)
3. **Goals**: Định nghĩa success criteria

---

### 1.2 Phân loại Skills

Dựa trên usecase_requirement_spec.md và best practices:

#### 1.2.1 High-Level Skills (Specialized, General, Mental Models, System Thinking, Rules, Critical Thinking)

**Đặc điểm:**
- Cần specialized, general, mental models, system thinking, rules, critical thinking
- Dùng cho decision-making phức tạp
- Cần context lớn và reasoning sâu

**Danh sách:**

1. **parent-orchestrator Skill**
   - **Vai trò:** Điều phối toàn bộ hệ thống, phân phối tasks cho workers
   - **Trigger:** Khi người dùng yêu cầu thực hiện bất kỳ task nào
   - **Mental Model:** OODA Loop (Observe-Orient-Decide-Act)
   - **Output:** Decision về việc gọi worker nào với skill nào

2. **tech-consultant Skill**
   - **Vai trò:** Thiết kế giải pháp kỹ thuật, tạo ADRs
   - **Trigger:** Khi cần thiết kế solution cho requirements
   - **Mental Model:** Trade-off Analysis (Pros/Cons), Security First
   - **Output:** Tech Specs, ADRs, Diagrams

3. **po-product-owner Skill**
   - **Vai trò:** Phân tích requirements, tạo user stories
   - **Trigger:** Khi người dùng mô tả yêu cầu tính năng
   - **Mental Model:** Socratic Method (Is that true? What is the real problem? What if?)
   - **Output:** User Stories, Acceptance Criteria

4. **pm-project-manager Skill**
   - **Vai trò:** Quản lý tiến độ, chia nhỏ tasks, tạo backlogs
   - **Trigger:** Khi cần lập kế hoạch triển khai
   - **Mental Model:** Decomposition, Dependencies Management
   - **Output:** Sprint Backlog, Implementation Tickets

#### 1.2.2 Technical Skills (Specialized, Modular)

**Đặc điểm:**
- Cần specialized, modular
- Dùng cho tasks cụ thể, có thể tái sử dụng
- Có thể compose với nhau

**Danh sách:**

1. **review Skill**
   - **Trigger:** Khi cần review code hoặc documents
   - **Scope:** Code quality, security, performance
   - **Output:** Structured feedback with severity levels

2. **delegation Skill**
   - **Trigger:** Khi cần giao việc cho subagents
   - **Scope:** Task decomposition, context passing
   - **Output:** Delegation plan with clear instructions

3. **initialization Skill**
   - **Trigger:** Khi cần khởi tạo cấu trúc dự án
   - **Scope:** Directory creation, template generation
   - **Output:** Project structure initialized

4. **debug Skill**
   - **Trigger:** Khi gặp lỗi cần debug
   - **Scope:** Root cause analysis, error tracing
   - **Output:** Debug report with fixes

5. **report Skill**
   - **Trigger:** Khi cần báo cáo tiến độ
   - **Scope:** Progress synthesis, status reporting
   - **Output:** Progress report

6. **research Skill**
   - **Trigger:** Khi cần tìm kiếm thông tin
   - **Scope:** Codebase analysis, external documentation
   - **Output:** Research findings

#### 1.2.3 General Skills (Shared)

**Đặc điểm:**
- Có thể shared giữa nhiều agents
- Dùng cho common tasks
- Reusable

**Danh sách:**
- File operations (read, write, create)
- Terminal commands execution
- Git operations
- Test execution
- Documentation generation

---

### 1.3 Skill Structure Template

Dựa trên Cursor documentation, mỗi skill phải có cấu trúc chuẩn:

**Frontmatter Fields:**
- **name** (required): Skill identifier. Lowercase letters, numbers, and hyphens only. Must match the parent folder name.
- **description** (required): Describes what the skill does and when to use it. Used by the agent to determine relevance.
- **license** (optional): License name or reference to a bundled license file.
- **compatibility** (optional): Environment requirements (system packages, network access, etc.).
- **metadata** (optional): Arbitrary key-value mapping for additional metadata.
- **disable-model-invocation** (optional): When `true`, the skill is only included when explicitly invoked via `/skill-name`.

```markdown
---
name: [skill-name]
description: [Short description of what this skill does and when to use it]
license: [optional license name or reference]
compatibility: [optional environment requirements]
metadata: [optional arbitrary key-value mapping]
disable-model-invocation: [optional true/false for manual invocation only]
---

# [Skill Name]
Detailed instructions for the agent.

## When to Use
- Use this skill when...
- This skill is helpful for...

## Instructions
- Step-by-step guidance for the agent
- Domain-specific conventions
- Best practices and patterns
- Use the ask questions tool if you need to clarify requirements with the user
```

**Ví dụ thực tế - parent-orchestrator Skill:**

```markdown
---
name: parent-orchestrator
description: Điều phối toàn bộ hệ thống Archon, phân phối tasks cho appropriate workers với appropriate skills. Use when user requests any task execution.
---
```
# Parent Orchestrator Skill
Skill điều phối toàn bộ hệ thống Archon, phân phối tasks cho appropriate workers với appropriate skills.

## When to Use
- Khi người dùng yêu cầu thực hiện bất kỳ task nào
- Khi cần điều phối multiple workers
- Khi cần ra quyết định về resource allocation

## Instructions
- **Mental Model:** Sử dụng OODA Loop (Observe-Orient-Decide-Act)
- **Observe:** Đọc `/.project_contexts/project_context_map.md` để hiểu trạng thái hiện tại
- **Orient:** Xác định task type và worker/skill phù hợp
- **Decide:** Ra quyết định về việc delegate cho worker nào
- **Act:** Thực thi delegation với context đầy đủ
- **Constraints:** Không trực tiếp viết code, luôn verify kết quả trước khi accept
- **Output Format:** Trả về JSON với decision, worker, skill, context, expected_output
- **Verification:** Kiểm tra worker được delegate đúng skill và context được truyền đầy đủ
- Sử dụng ask questions tool nếu cần clarify requirements với user

### 1.4 Optional Directories for Skills

Skills hỗ trợ các optional directories để tổ chức resources:

| Directory | Purpose |
|-----------|---------|
| `scripts/` | Executable code mà agents có thể chạy |
| `references/` | Additional documentation loaded on demand |
| `assets/` | Static resources như templates, images, data files |

**Example Structure:**
```
.cursor/
└── skills/
    └── my-skill/
        ├── SKILL.md
        ├── scripts/
        │   ├── deploy.sh
        │   └── validate.py
        ├── references/
        │   └── REFERENCE.md
        └── assets/
            └── config-template.json
```

**Best Practices:**
- Giữ SKILL.md focused và ngắn gọn
- Move detailed reference material vào separate files
- Scripts should be self-contained, include error handling
- Load resources progressively để giữ context usage efficient

### 1.5 Skill Loading Strategy

**Context-Aware Loading:**
- Skills được load on-demand khi relevant
- Không load tất cả skills cùng lúc (tốn token)
- Dựa trên trigger conditions để quyết định load

**Composable Skills:**
- Skills có thể combine hoặc chain together
- Ví dụ: delegation skill + review skill + report skill

**Durable Event Loop cho Skills:**

```
┌─────────────────────────────────────────┐
│         DURABLE EVENT LOOP              │
└───────────────┬─────────────────────────┘
                │
        ┌───────▼────────┐
        │  Start Goal    │
        └───────┬────────┘
                │
    ┌───────────▼────────────┐
    │ Ask LLM: Next Steps?  │◄──────┐
    └───────────┬────────────┘       │
                │                    │
        ┌───────▼────────┐           │
        │ Load Skill      │           │
        │ (if needed)     │           │
        └───────┬────────┘           │
                │                    │
        ┌───────▼────────┐           │
        │ Execute Task    │           │
        └───────┬────────┘           │
                │                    │
        ┌───────▼────────┐           │
        │ Update Context │───────────┘
        └───────┬────────┘
                │
        ┌───────▼────────┐
        │ Goal Reached?  │───No──┐
        └───────┬────────┘       │
               │Yes              │
               ▼                │
        ┌──────────────┐         │
        │   Return     │         │
        │   Results    │         │
        └──────────────┘         │
                                 │
                         ┌───────▼────────┐
                         │ Retry / Fallback │
                         └────────────────┘
```

---

### 1.6 Durable Prompt Pattern cho Skills

Sử dụng pattern này cho 90% development tasks:

```
ROLE → CONTEXT → TASK → CONSTRAINTS → FORMAT → ACCEPTANCE
```

**Áp dụng cho parent-orchestrator Skill:**

| Component | Content |
|-----------|---------|
| **ROLE** | Socratic Orchestrator - Điều phối viên hệ thống |
| **CONTEXT** | `/.project_contexts/project_context_map.md`, User request, Available workers/skills |
| **TASK** | Phân tích user request và điều phối cho appropriate worker với appropriate skill |
| **CONSTRAINTS** | Không trực tiếp code, Human-in-the-loop, Verify trước khi accept |
| **FORMAT** | JSON với decision, worker, skill, context, expected_output |
| **ACCEPTANCE** | Worker được delegate đúng, Context đầy đủ, Kết quả được verify |

---

### 1.7 Context Engineering cho Skills

**Core Principles:**

1. **Summarize, Don't Stream:** Collapse intermediate results để save tokens
2. **Layered Context:** Organize by priority và relevance
3. **Context Pruning:** Only load relevant portions, use summaries for large files
4. **Structured Note-Taking:** Write notes to persistent memory outside context
5. **Agentic Memory:** Regularly update và summarize state

**Context Pruning Strategy (Anti-Token-Overflow):**

1. **File Size Threshold:** Nếu file > 10KB, chỉ load summary section
2. **Active-First Loading:** Ưu tiên load active tasks thay vì toàn bộ backlog
3. **Progressive Loading:** Load basic context first, detailed context on-demand
4. **Summary Extraction:** Tự động extract key information từ large files

**Context Chunking:**
```
[GOAL] → What we're trying to achieve
[SKILLS] → Relevant domain knowledge
[TOOLS] → Available capabilities
[CONTEXT] → Current state, history
[REASONING] → Previous decisions made
```

**Áp dụng cho parent-orchestrator Skill:**

```python
# Pseudo-code cho context loading with pruning
def load_context_for_parent_orchestrator():
    context = {
        "GOAL": "Điều phối task cho appropriate worker",
        "SKILLS": [
            "parent-orchestrator",
            "tech-consultant",
            "po-product-owner",
            "pm-project-manager"
        ],
        "TOOLS": [
            "delegation",
            "review",
            "report"
        ],
        "CONTEXT": load_pruned_context(),
        "REASONING": {
            "previous_decisions": load_from_memory("decisions_log"),
            "learnings": load_from_memory("learnings_log")
        }
    }
    return context

def load_pruned_context():
    """Load context with pruning to prevent token overflow"""
    context = {}

    # Project state - only load summary if file is large
    project_map_path = "/.project_contexts/project_context_map.md"
    if get_file_size(project_map_path) > 10240:  # 10KB threshold
        context["project_state"] = extract_summary_section(project_map_path)
    else:
        context["project_state"] = read_file(project_map_path)

    # Current progress - always load (typically small)
    context["current_progress"] = read_file("/.project_contexts/management/current_progress.md")

    # Active tasks only - not entire backlog
    context["active_tasks"] = read_file("/.project_contexts/management/backlogs/active.md")

    return context

def extract_summary_section(file_path):
    """Extract only summary/key sections from large files"""
    content = read_file(file_path)
    # Extract sections like "Current Status", "Active Tasks", "Key Objectives"
    # Return only these sections to save tokens
    return extract_relevant_sections(content, ["Current Status", "Active Tasks", "Key Objectives"])

def get_file_size(file_path):
    """Get file size in bytes"""
    return os.path.getsize(file_path)
```

---

## Phần 2: Subagent (Worker) Design

### 2.1 Tổng quan về Subagents

**Định nghĩa:** Subagents là **specialized AI assistants** có thể delegate specific tasks trong development workflow. Mỗi subagent hoạt động trong isolated context window, handles specific types of work, và returns results về parent agent.

**Key Characteristics:**
- **Context Isolation:** Mỗi subagent có clean context window
- **Autonomous Operation:** Works independently mà không pollute main context
- **Specialized Expertise:** Configured cho specific tasks hoặc domains
- **Controlled Communication:** Returns structured results về parent agent
- **Execution Modes:** Có thể chạy foreground (blocking) hoặc background (non-blocking) thông qua field `is_background`

---

### 2.2 Loại Subagents (Workers)

Dựa trên usecase_requirement_spec.md và best practices:

#### 2.2.1 Planning Worker

**Vai trò:** Xử lý các tasks cần planning, analysis, và design

**Skills sử dụng:**
- po-product-owner (High-Level Skill)
- tech-consultant (High-Level Skill)
- pm-project-manager (High-Level Skill)

**Configuration:**
```yaml
---
name: planning-worker
description: >
  Use for planning, analysis, and design tasks. Handles requirement analysis,
  technical solution design, and project management planning.
  Uses high-level skills: po-product-owner, tech-consultant, pm-project-manager.
model: standard
readonly: false
is_background: false
---

When planning:
1. Analyze requirements using po-product-owner skill
2. Design solutions using tech-consultant skill
3. Create implementation plans using pm-project-manager skill

Return structured results with:
- Analysis findings
- Design decisions
- Implementation plans
```

**Use Cases:**
- UC-02: Tiếp nhận và phân tích yêu cầu
- UC-03: Thiết kế giải pháp kỹ thuật
- UC-04: Lập kế hoạch triển khai

**Collaboration Patterns:**

**PM-Tech Consultant Handshake:**
```
Planning Worker Internal Flow:
1. PO analyzes requirements → User Stories
2. Tech Consultant designs solution → Tech Specs, Architecture
3. PM breaks down into tasks → Implementation Plan
4. [CRITICAL] Tech Consultant reviews PM's task breakdown
   - Verify architectural integrity
   - Identify missing dependencies
   - Flag overly complex tasks
5. PM adjusts plan based on feedback
6. Return verified implementation plan
```

**Why Handshake Matters:**
- PM may lack technical depth for complex architectural decisions
- Prevents "dependency hell" from poor task decomposition
- Ensures implementation feasibility
- Reduces costly rework during execution phase

#### 2.2.2 Execute Worker

**Vai trò:** Xử lý các tasks cần coding, testing, và implementation

**Skills sử dụng:**
- coding (Technical Skill)
- code-analysis (Technical Skill)
- frontend-design (Technical Skill)
- test (Technical Skill)

**Configuration:**
```yaml
---
name: execute-worker
description: >
  Use for coding, testing, and implementation tasks. Handles writing code,
  running tests, and implementing features according to tech specs.
  Uses technical skills: coding, code-analysis, frontend-design, test.
model: standard
readonly: false
is_background: false
---

When executing:
1. Read implementation ticket
2. Read tech spec
3. Write code according to spec
4. Run tests
5. Report blockers immediately

Return structured results with:
- Code changes
- Test results
- Changelog entries
- Blockers (if any)
```

**Use Cases:**
- UC-05: Thực thi coding

#### 2.2.3 General Worker

**Vai trò:** Xử lý các tasks chung, report generation, và automation

**Skills sử dụng:**
- update-project (Technical Skill)
- report (Technical Skill)
- research (Technical Skill)

**Configuration:**
```yaml
---
name: system-maintainer
description: >
  Use for system maintenance tasks including deep research, comprehensive progress reporting,
  and executing project automation scripts.
  Trigger: Use when user asks for research, status reports, or project updates.
  Uses technical skills: update-project, report, research.
model: fast
readonly: false
is_background: true
---

When handling general tasks:
1. Execute automation scripts
2. Generate progress reports
3. Perform research tasks
4. Update project documentation

Return structured results with:
- Execution status
- Report data
- Research findings
```

**Use Cases:**
- UC-01: Khởi tạo dự án mới (cần skill update-project)
- UC-07: Báo cáo tiến độ (cần skill report)

---

### 2.3 Orchestration Patterns

Dựa trên subagent-settings-best-practices.md, áp dụng 4 patterns:

#### 2.3.1 The Conductor Pattern (LLM-Based Orchestration)

**Use When:**
- Workflow requires dynamic decision-making
- Next step không predetermined
- Tasks context-dependent và nuanced

**Áp dụng cho:** parent-orchestrator skill

**Example:**
```
User: "Tôi muốn tính năng Login bằng Google"
Parent Agent (Conductor):
1. Analyze task requirements
2. Identify required specialists (PO, Tech Consultant, PM)
3. Plan execution order
4. Delegate to specialists
5. Integrate results
6. Verify final output
```

#### 2.3.2 The Assembly Line Pattern (Sequential Workflow)

**Use When:**
- Order matters strictly
- Each step depends on previous output
- Clear dependencies exist

**Áp dụng cho:** UC-02 → UC-03 → UC-04 → UC-05 flow

**Example với Handshake Pattern:**
```
1. PO Skill analyzes requirements → User Stories, Acceptance Criteria
2. Tech Consultant designs solution → Tech Specs, ADRs, Architecture
3. PM creates implementation plan → Sprint Backlog, Task Breakdown, Dependencies
4. [HANDSHAKE] Tech Consultant verifies plan → Check architectural integrity, identify dependency issues
5. PM adjusts plan based on consultant feedback → Update task breakdown if needed
6. Execute Worker implements code → Code according to verified plan
```

**Handshake Benefits:**
- Prevent architectural violations from poor task breakdown
- Catch dependency hell early in planning phase
- Ensure PM plans are technically sound
- Reduce rework from implementation issues

#### 2.3.3 The Task Force Pattern (Parallel Execution)

**Use When:**
- Multiple independent tasks có thể run simultaneously
- Speed is crucial
- No dependencies giữa tasks

**Example:**
```
Parallel Execution:
├─ Planning Worker: Analyze API requirements
├─ Planning Worker: Design database schema
├─ Planning Worker: Plan UI components
└─ Execute Worker: Setup project structure
```

#### 2.3.4 The Refinement Cycle Pattern (Loop Orchestration)

**Use When:**
- Quality requires iterative improvement
- Feedback loops necessary
- Success criteria verifiable

**Áp dụng cho:** UC-06 Review & Acceptance

**Example:**
```
1. Execute Worker implements code
2. Execute Worker runs tests
3. Planning Worker reviews code
4. Loop until all tests pass
```

---

### 2.4 Context Isolation Strategy

**Mental Model:**
```
Parent Agent → Delegates Task → Subagent receives context
                                     ↓
                               [Isolated Context Window]
                                     ↓
                          Subagent works autonomously
                                     ↓
                               Returns structured result
                                     ↓
                          Parent Agent receives only final summary
```

**Implications:**
- Subagents không thể access previous conversation history
- Parent phải explicitly provide relevant context
- Intermediate debugging output stays isolated
- Results phải be structured cho handoff

**Best Practice cho Context Passing:**

```python
# Pseudo-code cho context passing
def delegate_to_worker(worker_type, skill_name, context):
    # Prepare context for subagent
    subagent_context = {
        "task": context["task"],
        "requirements": context["requirements"],
        "constraints": context.get("constraints", []),
        "expected_output": context.get("expected_output", {}),
        "relevant_files": context.get("relevant_files", []),
        "previous_decisions": context.get("previous_decisions", {})
    }
    
    # Delegate to worker
    result = worker.execute(skill_name, subagent_context)
    
    # Return only summary to parent
    return {
        "status": result["status"],
        "summary": result["summary"],
        "output": result["output"],
        "blockers": result.get("blockers", [])
    }
```

---

### 2.5 Model Selection Strategy

**Decision Framework:**

| Model Tier | Use Case | Characteristics |
|------------|----------|----------------|
| **Fast Models** | Repetitive searches, pattern matching, codebase exploration | 4-10x faster, lower cost, suitable cho parallel operations |
| **Standard Models** | Day-to-day coding, refactoring, debugging | Balanced speed/quality, good cho most tasks |
| **Premium Models** | Architectural decisions, complex reasoning, security reviews | Highest quality, larger context, higher cost |
| **Max Context Models** | Large codebase analysis, cross-file refactoring | Huge context windows (200k+ tokens), slower inference |

**Áp dụng cho Workers:**

```yaml
# Planning Worker
model: standard  # Cần reasoning depth

# Execute Worker
model: standard  # Cần code quality

# General Worker
model: fast  # Dùng cho parallel operations, report generation
```

---

### 2.6 Subagent Configuration Template

Dựa trên best practices và Cursor documentation, mỗi subagent phải có các fields sau:

**Configuration Fields:**
- **name** (optional): Unique identifier. Sử dụng lowercase letters và hyphens. Defaults to filename without extension.
- **description** (optional): Khi nào sử dụng subagent này. Agent đọc field này để quyết định delegation.
- **model** (optional): Model để sử dụng: fast, inherit, hoặc specific model ID. Defaults to inherit.
- **readonly** (optional): Nếu true, subagent chạy với restricted write permissions.
- **is_background** (optional): Nếu true, subagent chạy trong background mà không chờ completion.

```yaml
---
name: [worker-name]
description: >
  [Detailed description of what this subagent does and when to use it]
  [Trigger conditions and scope]
model: [fast|inherit|specific-model-id]
readonly: [true|false]
is_background: [true|false]
---

## When to Use
[List of trigger conditions]

## What It Does
[Scope and capabilities]

## What It Doesn't Do
[Boundaries and limitations]

## Configuration
[Specific settings]

## Examples
[Good and bad examples]

## Return Format
[Structured output format]
```

**Ví dụ thực tế - Planning Worker:**

```yaml
---
name: planning-worker
description: >
  Use for planning, analysis, and design tasks. Handles requirement analysis,
  technical solution design, and project management planning.
  Trigger: When user requests planning, analysis, or design work.
  Scope: Requirements analysis, technical design, implementation planning.
  Constraints: Does not write code, focuses on planning and design.
  Output: Structured plans, specs, and tickets.
model: standard
readonly: false
is_background: false
---

## When to Use
- User requests requirement analysis
- User requests technical solution design
- User requests implementation planning
- User requests architecture decisions

## What It Does
- Analyze requirements using po-product-owner skill
- Design solutions using tech-consultant skill
- Create plans using pm-project-manager skill
- Generate structured documentation

## What It Doesn't Do
- Write implementation code
- Execute terminal commands
- Modify source files directly

## Configuration
Skills: [po-product-owner, tech-consultant, pm-project-manager]
Context: /.project_contexts/
Output: Markdown documents, JSON tickets

## Examples

**Good:**
User: "Thiết kế giải pháp cho tính năng Login bằng Google"
Planning Worker:
1. Use po-product-owner to analyze requirements
2. Use tech-consultant to design solution
3. Use pm-project-manager to create plan
4. Return structured plan

**Bad:**
User: "Thiết kế giải pháp cho tính năng Login bằng Google"
Planning Worker: "Ok tôi sẽ code ngay" (Vi phạm: không phải responsibility của planning worker)

## Return Format
```json
{
  "status": "success|error",
  "skill_used": "skill-name",
  "output": {
    "documents": [...],
    "tickets": [...],
    "decisions": [...]
  },
  "summary": "..."
}
```

---

### 3.1 Tổng quan về Automation Scripts

**Mục tiêu:** Tự động hóa các tasks lặp lại, giảm manual work, đảm bảo consistency.

**Nguyên tắc:**
- CLI as Universal Interface (dùng cho cả humans và agents)
- Scripts phải be standalone (no external dependencies)
- Scripts phải có error handling
- Scripts phải log mọi actions

**Error Handling Strategy cho Scripts:**

1. **Dependency Check:** Scripts phải check và report missing dependencies
2. **Graceful Degradation:** Nếu dependency thiếu, đề xuất installation steps
3. **Structured Error Output:** Return JSON error format cho agent parsing
4. **Recovery Suggestions:** Agent phải analyze stderr và propose fixes

**Agent-Script Integration Pattern:**
```python
def execute_script_with_error_handling(script_path, args):
    """Execute script with comprehensive error handling"""
    try:
        result = subprocess.run(
            ["python", script_path] + args,
            capture_output=True,
            text=True,
            timeout=300  # 5 minute timeout
        )

        if result.returncode == 0:
            return {"status": "success", "output": result.stdout}
        else:
            # Parse error and suggest fixes
            error_analysis = analyze_script_error(result.stderr)
            return {
                "status": "error",
                "error": result.stderr,
                "suggested_fix": error_analysis["fix"],
                "user_action": error_analysis["action"]
            }

    except subprocess.TimeoutExpired:
        return {"status": "timeout", "suggested_fix": "Script took too long, consider optimizing or running in background"}
    except FileNotFoundError:
        return {"status": "missing_script", "suggested_fix": "Script file not found, check file path"}

def analyze_script_error(stderr):
    """Analyze script errors and suggest fixes"""
    if "ModuleNotFoundError" in stderr:
        module = extract_module_name(stderr)
        return {
            "fix": f"Missing Python module: {module}",
            "action": f"Run: pip install {module}"
        }
    elif "Permission denied" in stderr:
        return {
            "fix": "Permission denied",
            "action": "Check file permissions or run with appropriate privileges"
        }
    else:
        return {
            "fix": "Unknown error",
            "action": "Check script logs and fix manually"
        }
```

---



### 3.2 Script Structure Template

Dựa trên best practices, mỗi script phải có:

```python
"""
[Script Name]
[Purpose]
[Usage]
[Arguments]
[Output]
"""

import os
import sys
import logging
from typing import Dict, Any

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

def main():
    """Main execution function."""
    try:
        # Parse arguments
        args = parse_arguments()
        
        # Execute task
        result = execute_task(args)
        
        # Return result
        return result
        
    except Exception as e:
        logger.error(f"Error: {e}")
        sys.exit(1)

def parse_arguments() -> Dict[str, Any]:
    """Parse command line arguments."""
    # Implementation
    pass

def execute_task(args: Dict[str, Any]) -> Dict[str, Any]:
    """Execute the main task."""
    # Implementation
    pass

if __name__ == "__main__":
    main()
```

---

### 3.3 Danh sách Automation Scripts

#### 3.3.1 init_project.py

**Mục tiêu:** Khởi tạo cấu trúc dự án mới

**Pseudo-code:**

```python
"""
init_project.py
Purpose: Initialize project structure for Archon
Usage: python ~/.cursor/skills/initialization/scripts/init_project.py [--project-name NAME] [--goal GOAL]
Arguments:
  --project-name: Name of the project
  --goal: Core goal of the project (The One Thing)
Output: Project structure initialized
"""

import os
import sys
import logging
from datetime import datetime
from typing import Dict, Any

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Configuration
PROJECT_ROOT = "/.project_contexts"
DIRECTORIES = [
    f"{PROJECT_ROOT}/pm/user_stories",
    f"{PROJECT_ROOT}/pm/prds",
    f"{PROJECT_ROOT}/pm/acceptance_criteria",
    f"{PROJECT_ROOT}/arch/tech_specs",
    f"{PROJECT_ROOT}/arch/adrs",
    f"{PROJECT_ROOT}/arch/diagrams",
    f"{PROJECT_ROOT}/arch/reviews",
    f"{PROJECT_ROOT}/dev/change_logs",
    f"{PROJECT_ROOT}/dev/documentations",
    f"{PROJECT_ROOT}/dev/current_blockings",
    f"{PROJECT_ROOT}/dev/reviews",
    f"{PROJECT_ROOT}/shared/definitions",
    f"{PROJECT_ROOT}/management/backlogs",
    f"{PROJECT_ROOT}/management/roadmaps",
    f"{PROJECT_ROOT}/management/progress_reports",
]

COMMUNICATION_TEMPLATE = """---
description: Apply when agents + skill communicate with each other.
alwaysApply: False
---

# Communication Template

## Message Format
- Sender: [Agent/Skill name]
- Receiver: [Agent/Skill name]
- Message Type: [request|response|notification]
- Content: [Message content]

## Response Format
- Status: [success|error|in_progress]
- Data: [Response data]
- Next Steps: [What to do next]

## Error Handling
- If error occurs, log and return structured error
- If blocker encountered, report immediately
- If clarification needed, ask questions
"""

GITIGNORE_TEMPLATE = """# Dependencies
node_modules/
__pycache__/
*.pyc
*.pyo
*.pyd
.Python
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
*.egg-info/
.installed.cfg
*.egg
MANIFEST

# Environment variables
.env
.env.local
.env.development.local
.env.test.local
.env.production.local

# IDE
.vscode/
.idea/
*.swp
*.swo
*~

# OS
.DS_Store
.DS_Store?
._*
.Spotlight-V100
.Trashes
ehthumbs.db
Thumbs.db

# Logs
*.log
logs/
npm-debug.log*
yarn-debug.log*
yarn-error.log*

# Project Context - CRITICAL: Keep this ignored!
/.project_contexts/
"""

CURSORIGNORE_TEMPLATE = """# Allow AI to access project context files despite gitignore
# This overrides git's ignore rules for Cursor AI operations
!.project_contexts/

# Still ignore generated/sensitive content within project_contexts
.project_contexts/**/temp/
.project_contexts/**/cache/
# Still ignore generated/sensitive content within project_contexts
.project_contexts/**/temp/
.project_contexts/**/cache/
.project_contexts/**/*.log

# Allow access to agents and rules
!.cursor/agents/
!.cursor/rules/
!.cursor/skills/
"""

def main():
    """Main execution function."""
    try:
        args = parse_arguments()
        
        logger.info("Initializing project structure...")
        
        # Create directories
        create_directories()
        
        # Create templates
        create_templates(args)
        
        # Create communication rules
        create_communication_rules()
        
        # Create cursor directories
        create_cursor_directories()

        # Create git configuration
        create_gitignore()
        create_cursorignore()

        logger.info("Project initialization complete!")
        logger.info(f"Next step: Update {PROJECT_ROOT}/project_context_map.md")
        
        return {
            "status": "success",
            "project_root": PROJECT_ROOT,
            "directories_created": len(DIRECTORIES)
        }
        
    except Exception as e:
        logger.error(f"Error: {e}")
        sys.exit(1)

def parse_arguments() -> Dict[str, Any]:
    """Parse command line arguments."""
    import argparse
    
    parser = argparse.ArgumentParser(description='Initialize project structure')
    parser.add_argument('--project-name', type=str, help='Project name')
    parser.add_argument('--goal', type=str, help='Core goal of the project')
    
    return vars(parser.parse_args())

def create_directories():
    """Create all required directories."""
    for directory in DIRECTORIES:
        if not os.path.exists(directory):
            os.makedirs(directory)
            logger.info(f"Created directory: {directory}")
        else:
            logger.info(f"Directory exists: {directory}")

def create_templates(args: Dict[str, Any]):
    """Create template files."""
    current_date = datetime.now().strftime("%Y-%m-%d")
    
    # project_context_map.md
    project_context_map = f"""# Project Context Map
> Last Updated: {current_date}

## 1. Project Overview
- **Name:** {args.get('project_name', '[Project Name]')}
- **Stage:** INCEPTION
- **Current Goal:** {args.get('goal', '[The One Thing]')}

## 2. Directory Navigation

### PM Domain (Requirements & Logic)
| Path | Purpose | Key Files to Read |
| :--- | :--- | :--- |
| `/.project_contexts/pm/` | **Source of Truth** cho logic | `user_stories/`, `prds/` |
| `/.project_contexts/pm/products_requirements/` | Yêu cầu từ PO | `user_stories/`, `prds/` |
| `/.project_contexts/management/` | Trạng thái quản lý | `current_progress.md` (Đọc cái này đầu tiên!) |

### Arch Domain (Technical Architecture)
| Path | Purpose | Key Files to Read |
| :--- | :--- | :--- |
| `/.project_contexts/arch/` | **Source of Truth** cho kiến trúc | `tech_specs/`, `adrs/` |
| `/.project_contexts/arch/tech_specs/` | Technical Specs | Implementation Guides |
| `/.project_contexts/arch/adrs/` | Architecture Decisions | Decision Records |

### Dev Domain (Execution & Logs)
| Path | Purpose | Key Files to Read |
| :--- | :--- | :--- |
| `/.project_contexts/dev/` | Execution logs | `change_logs/` |
| `/.project_contexts/dev/change_logs/` | Nhật ký thay đổi | `daily_log.md` |
| `/.project_contexts/dev/current_blockings/` | Issues | Blocker list |

## 3. Quick Links (Critical Paths)
- **Implementation Ticket hiện tại:** `/.project_contexts/management/backlogs/active.md`
- **Blocker hiện tại:** `/.project_contexts/dev/current_blockings/`
"""
    
    with open(f"{PROJECT_ROOT}/project_context_map.md", "w", encoding="utf-8") as f:
        f.write(project_context_map)
    logger.info(f"Created file: {PROJECT_ROOT}/project_context_map.md")
    
    # current_progress.md
    current_progress = f"""# Current Project Status
**Status:** INCEPTION
**Last Updated:** {current_date}

## Key Objectives
- [ ] Define MVP Scope
- [ ] Create initial Architecture Spec
- [ ] Setup Development Environment

## Recent Updates
- Project structure initialized on {current_date}
"""
    
    with open(f"{PROJECT_ROOT}/management/current_progress.md", "w", encoding="utf-8") as f:
        f.write(current_progress)
    logger.info(f"Created file: {PROJECT_ROOT}/management/current_progress.md")
    
    # active.md
    active = """# Active Tasks
*No active tasks currently. Please pull from sprint_backlog.md*
"""
    
    with open(f"{PROJECT_ROOT}/management/backlogs/active.md", "w", encoding="utf-8") as f:
        f.write(active)
    logger.info(f"Created file: {PROJECT_ROOT}/management/backlogs/active.md")
    
    # sprint_backlog.md
    sprint_backlog = """# Sprint Backlog
- [ ] Setup basic repository (Git init)
- [ ] Configure CI/CD pipeline
- [ ] Create initial documentation
"""
    
    with open(f"{PROJECT_ROOT}/management/backlogs/sprint_backlog.md", "w", encoding="utf-8") as f:
        f.write(sprint_backlog)
    logger.info(f"Created file: {PROJECT_ROOT}/management/backlogs/sprint_backlog.md")

def create_communication_rules():
    """Create communication rules file."""
    os.makedirs(".cursor/rules", exist_ok=True)

    with open(".cursor/rules/communication_rules.mdc", "w", encoding="utf-8") as f:
        f.write(COMMUNICATION_TEMPLATE)
    with open(".cursor/rules/communication_rules.mdc", "w", encoding="utf-8") as f:
        f.write(COMMUNICATION_TEMPLATE)
    logger.info("Created file: .cursor/rules/communication_rules.mdc")

def create_cursor_directories():
    """Create .cursor specific directories."""
    cursor_dirs = [
        ".cursor/agents",
        ".cursor/skills"
    ]
    for directory in cursor_dirs:
        os.makedirs(directory, exist_ok=True)
        logger.info(f"Created directory: {directory}")

def create_gitignore():
    """Create .gitignore file to exclude project contexts from git."""
    try:
        with open(".gitignore", "w", encoding="utf-8") as f:
            f.write(GITIGNORE_TEMPLATE)
        logger.info("Created file: .gitignore")
    except Exception as e:
        logger.error(f"Failed to create .gitignore: {e}")

def create_cursorignore():
    """Create .cursorignore file to allow AI access to project contexts."""
    try:
        with open(".cursorignore", "w", encoding="utf-8") as f:
            f.write(CURSORIGNORE_TEMPLATE)
        logger.info("Created file: .cursorignore")
    except Exception as e:
        logger.error(f"Failed to create .cursorignore: {e}")

if __name__ == "__main__":
    main()
```

**Usage:**
```bash
# Initialize project
python ~/.cursor/skills/initialization/scripts/init_project.py --project-name "My App" --goal "Build MVP"

# Script will:
# 1. Create directory structure /.project_contexts/
# 2. Create template files
# 3. Create .cursor/rules/communication_rules.mdc
# 4. Create .gitignore to protect /.project_contexts/
# 5. Create .cursorignore to allow AI access to project contexts
# 6. Log all actions
```

**Security & AI Access:**
- **`.gitignore`**: Protects `/.project_contexts/` from accidental commits
- **`.cursorignore`**: Overrides gitignore for Cursor AI operations using `!.project_contexts/`
- **Dotfile Protection**: Cursor prevents AI from modifying .gitignore directly
- **Context Isolation**: Project contexts are gitignored but accessible to AI via cursorignore

---

#### 3.3.2 update_project.py

**Mục tiêu:** Update project structure and templates

**Pseudo-code:**

```python
"""
update_project.py
Purpose: Update project structure and templates
Usage: python ~/.cursor/skills/update-project/scripts/update_project.py [--action ACTION] [--target TARGET]
Arguments:
  --action: update_structure|update_templates|update_context_map
  --target: Target to update
Output: Project updated
"""

import os
import sys
import logging
from typing import Dict, Any

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

def main():
    """Main execution function."""
    try:
        args = parse_arguments()
        
        logger.info(f"Updating project: {args['action']}")
        
        # Execute action
        if args['action'] == 'update_structure':
            result = update_structure()
        elif args['action'] == 'update_templates':
            result = update_templates()
        elif args['action'] == 'update_context_map':
            result = update_context_map()
        else:
            raise ValueError(f"Unknown action: {args['action']}")
        
        logger.info("Project update complete!")
        return result
        
    except Exception as e:
        logger.error(f"Error: {e}")
        sys.exit(1)

def parse_arguments() -> Dict[str, Any]:
    """Parse command line arguments."""
    import argparse
    
    parser = argparse.ArgumentParser(description='Update project structure')
    parser.add_argument('--action', type=str, required=True,
                       choices=['update_structure', 'update_templates', 'update_context_map'])
    parser.add_argument('--target', type=str, help='Target to update')
    
    return vars(parser.parse_args())

def update_structure() -> Dict[str, Any]:
    """Update project structure."""
    # Implementation
    pass

def update_templates() -> Dict[str, Any]:
    """Update templates."""
    # Implementation
    pass

def update_context_map() -> Dict[str, Any]:
    """Update context map."""
    # Implementation
    pass

if __name__ == "__main__":
    main()
```

---

#### 3.3.3 generate_report.py

**Mục tiêu:** Generate progress report

**Pseudo-code:**

```python
"""
generate_report.py
Purpose: Generate progress report
Usage: python ~/.cursor/skills/report/scripts/generate_report.py [--format FORMAT]
Arguments:
  --format: markdown|json|html
Output: Progress report
"""

import os
import sys
import logging
from typing import Dict, Any

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

def main():
    """Main execution function."""
    try:
        args = parse_arguments()
        
        logger.info("Generating progress report...")
        
        # Read project state
        project_state = read_project_state()
        
        # Generate report
        report = generate_report(project_state, args['format'])
        
        # Save report
        save_report(report, args['format'])
        
        logger.info("Report generated!")
        return report
        
    except Exception as e:
        logger.error(f"Error: {e}")
        sys.exit(1)

def parse_arguments() -> Dict[str, Any]:
    """Parse command line arguments."""
    import argparse
    
    parser = argparse.ArgumentParser(description='Generate progress report')
    parser.add_argument('--format', type=str, default='markdown',
                       choices=['markdown', 'json', 'html'])
    
    return vars(parser.parse_args())

def read_project_state() -> Dict[str, Any]:
    """Read project state from files."""
    # Read project_context_map.md
    # Read current_progress.md
    # Read active.md
    # Read sprint_backlog.md
    pass

def generate_report(state: Dict[str, Any], format: str) -> str:
    """Generate report in specified format."""
    # Implementation
    pass

def save_report(report: str, format: str):
    """Save report to file."""
    # Implementation
    pass

if __name__ == "__main__":
    main()
```

---

### 3.4 Script Integration with Skills

**Integration Pattern:**

```python
# Pseudo-code cho skill update-project
def execute_update_project_skill():
    # Check if script exists
    if not os.path.exists("update_project.py"):
        raise FileNotFoundError("update_project.py not found")
    
    # Execute script
    result = subprocess.run(
        ["python", "update_project.py", "--action", "update_structure"],
        capture_output=True,
        text=True
    )
    
    # Check result
    if result.returncode != 0:
        raise RuntimeError(f"Script failed: {result.stderr}")
    
    # Return result
    return {
        "status": "success",
        "output": result.stdout
    }
```

---

## Phần 4: Integration & Orchestration

### 4.1 Complete Workflow Example

**Scenario:** User requests "Tôi muốn tính năng Login bằng Google"

**Flow:**

```
1. User Request
   ↓
2. Parent Agent (parent-orchestrator skill)
   - Observe: Read project_context_map.md
   - Orient: Task type = new feature
   - Decide: Delegate to Planning Worker with po-product-owner skill
   - Act: Delegate
   ↓
3. Planning Worker (po-product-owner skill)
   - Analyze requirements
   - Create user story
   - Define acceptance criteria
   - Return result to Parent Agent
   ↓
4. Parent Agent (parent-orchestrator skill)
   - Verify result
   - Decide: Delegate to Planning Worker with tech-consultant skill
   - Act: Delegate
   ↓
5. Planning Worker (tech-consultant skill)
   - Design technical solution
   - Create ADRs
   - Create tech specs
   - Return result to Parent Agent
   ↓
6. Parent Agent (parent-orchestrator skill)
   - Verify result
   - Decide: Delegate to Planning Worker with pm-project-manager skill
   - Act: Delegate
   ↓
7. Planning Worker (pm-project-manager skill)
   - Create implementation plan
   - Create tickets
   - Return result to Parent Agent
   ↓
8. Parent Agent (parent-orchestrator skill)
   - Verify result
   - Decide: Delegate to Execute Worker with coding skill
   - Act: Delegate
   ↓
9. Execute Worker (coding skill)
   - Implement code
   - Run tests
   - Write changelog
   - Return result to Parent Agent
   ↓
10. Parent Agent (parent-orchestrator skill)
    - Verify result
    - Present to user for review
    - User confirms commit
    - Close task
```

### 4.2 Error Handling & Fallback

**Error Handling Pattern:**

```python
# Pseudo-code cho error handling
def execute_with_fallback(worker, skill, context):
    try:
        # Execute primary task
        result = worker.execute(skill, context)
        
        # Verify result
        if not verify_result(result):
            raise ValueError("Result verification failed")
        
        return result
        
    except Exception as e:
        logger.error(f"Error: {e}")
        
        # Fallback strategy
        if is_recoverable(e):
            return retry_with_different_strategy(worker, skill, context)
        else:
            return report_error_to_user(e)
```

---

## Phần 5: Best Practices Summary

### 5.1 Skills Best Practices

1. **Quality Descriptions:** Spend time crafting clear descriptions. Agent uses this field to decide when to delegate.
2. **Progressive Loading:** Keep main SKILL.md focused. Move detailed reference material to separate files in references/.
3. **Executable Scripts:** Scripts should be self-contained, include error handling, and be written in any executable language.
4. **Manual vs Automatic:** Use `disable-model-invocation: true` for skills that should only be invoked explicitly via `/skill-name`.
5. **Version Control:** Store skills in repository for team sharing. Use `.cursor/skills/` for project-level skills.
6. **Resource Efficiency:** Load resources on demand, keep context usage efficient.

### 5.2 Subagent Best Practices

1. **Single Responsibility:** Mỗi subagent = One clear job
2. **Context Isolation:** Subagents không share memory
3. **Quality Descriptions:** Spend 70% time on descriptions
4. **Execution Mode Selection:** Use `is_background: false` cho sequential tasks, `is_background: true` cho parallel/long-running tasks
5. **Model Selection:** Choose right model cho task (fast cho parallel operations, standard cho complex reasoning, inherit để sử dụng model của parent)
6. **Permission Control:** Use `readonly: true` cho subagents chỉ cần read access, `readonly: false` cho subagents cần write/modify files
7. **Structured Output:** Always return structured results cho parent agent integration

### 5.3 Automation Script Best Practices

1. **CLI as Universal Interface:** Dùng cho cả humans và agents
2. **Standalone Scripts:** No external dependencies
3. **Error Handling:** Comprehensive error handling
4. **Logging:** Log mọi actions
5. **Structured Output:** Return structured results

---

## Phần 6: Implementation Roadmap

### Phase 1: Foundation (Tuần 1-2)
- [ ] Tạo cấu trúc thư mục skills/
- [ ] Tạo cấu trúc thư mục agents/
- [ ] Viết init_project.py với .gitignore và .cursorignore
- [ ] Tạo communication_rules.mdc
- [ ] Test git configuration và AI access protection
- [ ] Test initialization workflow

### Phase 2: High-Level Skills (Tuần 3-4)
- [ ] Viết parent-orchestrator skill
- [ ] Viết tech-consultant skill
- [ ] Viết po-product-owner skill
- [ ] Viết pm-project-manager skill
- [ ] Test skills

### Phase 3: Technical Skills (Tuần 5-6)
- [ ] Viết review skill
- [ ] Viết delegation skill
- [ ] Viết initialization skill
- [ ] Viết debug skill
- [ ] Viết report skill
- [ ] Viết research skill
- [ ] Test skills

### Phase 4: Workers (Tuần 7-8)
- [ ] Tạo Planning Worker
- [ ] Tạo Execute Worker
- [ ] Tạo General Worker
- [ ] Integrate with skills
- [ ] Test delegation

### Phase 5: Automation Scripts (Tuần 9-10)
- [ ] Viết update_project.py
- [ ] Viết generate_report.py
- [ ] Integrate with skills
- [ ] Test automation

### Phase 6: Integration (Tuần 11-12)
- [ ] Integrate parent-orchestrator with workers
- [ ] Test end-to-end workflows
- [ ] Document usage
- [ ] Deploy

---

**Phiên bản:** 1.5 (Added .gitignore and .cursorignore for project context protection and AI access)
**Ngày tạo:** 2026-01-29
**Ngày cập nhật:** 2026-01-29
**Tác giả:** System Design Document
**Trạng thái:** Enhanced init_project.py with git configuration templates for secure AI context management
