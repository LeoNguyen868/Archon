# OODA Loop Implementation

The **OODA Loop** (Observe, Orient, Decide, Act) is the cognitive framework that drives all decision-making in Archon. This document explains how OODA is implemented across the system.

## OODA Loop Overview

The OODA Loop was developed by military strategist John Boyd as a decision-making framework. It consists of four iterative phases:

```
Observe → Orient → Decide → Act → Observe...
```

Each cycle processes information faster than the opponent/adversary, creating a competitive advantage.

## Implementation in Archon

### Primary Implementation

**Location**: `cursor/skills/agent-orchestrator/SKILL.md`

**Scope**: Used by the Agent Orchestrator for all major decisions

### Secondary Implementations

OODA principles are applied throughout the system:

- **Workers**: Each worker applies OODA for task execution
- **Skills**: Individual skills implement mini-OODA loops
- **Context Management**: Context pruning follows OODA principles

## Detailed Phase Implementation

### 1. Observe Phase

**Purpose**: Gather information about current state and requirements

**Implementation in Archon**:

#### Data Sources
- User request analysis
- Project context files (`.project_contexts/`)
- Current progress status
- Historical execution data

#### Context Pruning Strategy
```javascript
// File size threshold
if (file.size > 10KB) {
  loadSummarySectionsOnly(file);
}

// Active-first loading
prioritizeActiveTasks(context);

// Progressive loading
loadBasicContextFirst();
loadDetailsOnDemand();
```

#### Observation Points
- `.project_contexts/project_context_map.md` (single source of truth)
- `.project_contexts/management/current_progress.md` (immediate status)
- `.project_contexts/management/backlogs/active.md` (current task)

### 2. Orient Phase

**Purpose**: Analyze information and classify the request

**Implementation in Archon**:

#### Request Classification
```javascript
function classifyRequest(request) {
  if (isNewFeature(request)) return "Planning/Analysis";
  if (isImplementation(request)) return "Execution/Coding";
  if (isReporting(request)) return "General/Reporting";
  return "Complex/Multi-phase";
}
```

#### Worker Mapping
```javascript
const workerMapping = {
  "Planning/Analysis": "planning-worker",
  "Execution/Coding": "execute-worker",
  "General/Reporting": "general-worker"
};
```

#### Skill Selection
- **Planning**: PO, Tech Consultant, PM skills
- **Execution**: Coding, Testing, Debugging skills
- **General**: Report, Research, Update skills

#### Context Chunking
```
[GOAL] → What we're trying to achieve
[SKILLS] → Relevant domain knowledge
[TOOLS] → Available capabilities
[CONTEXT] → Current state and history
[REASONING] → Previous decisions made
```

### 3. Decide Phase

**Purpose**: Select the optimal course of action

**Implementation in Archon**:

#### Decision Matrix
```javascript
const decisionMatrix = {
  "New Feature": {
    worker: "planning-worker",
    skill: "po-product-owner",
    pattern: "conductor"
  },
  "Architecture": {
    worker: "planning-worker",
    skill: "tech-consultant",
    pattern: "assembly-line"
  },
  "Implementation": {
    worker: "execute-worker",
    skill: "coding",
    pattern: "refinement-cycle"
  }
};
```

#### Orchestration Pattern Selection

**Conductor Pattern** (LLM-Based):
- Dynamic decision-making
- Context-dependent tasks
- Complex coordination

**Assembly Line Pattern** (Sequential):
- Strict order dependencies
- Handshake verification
- Predictable workflows

**Task Force Pattern** (Parallel):
- Independent tasks
- Speed critical
- Resource optimization

**Refinement Cycle Pattern** (Iterative):
- Feedback loops
- Quality improvement
- Iterative development

#### Context Passing Strategy
```javascript
function constructContext(worker, task) {
  return {
    targetSkill: selectedSkill,
    inputContext: userRequest + relevantContext,
    outputTemplate: skillSpecificTemplate,
    constraints: safetyAndQualityConstraints
  };
}
```

### 4. Act Phase

**Purpose**: Execute the decision and monitor results

**Implementation in Archon**:

#### Task Delegation
```javascript
function delegateTask(worker, context) {
  // Create isolated context window
  const isolatedContext = createIsolationBoundary();

  // Delegate to worker
  const result = worker.execute(context);

  // Monitor execution
  monitorProgress(worker);

  return result;
}
```

#### Result Integration
```javascript
function integrateResult(result, originalContext) {
  // Verify result against expectations
  validateResult(result);

  // Update project context
  updateProjectContext(result);

  // Check for follow-up actions
  identifyNextSteps(result);

  return integratedResult;
}
```

#### Verification Mechanisms
- **Human-in-the-Loop**: Critical decisions require approval
- **Automated Checks**: Result validation against templates
- **Socratic Questioning**: "Is that true?" verification
- **Context Consistency**: Ensure context integrity

## OODA in Practice

### Example: Feature Development

```
User Request: "Add user authentication"

1. OBSERVE:
   - Read current codebase
   - Check existing auth components
   - Analyze requirements

2. ORIENT:
   - Classify as "New Feature"
   - Identify security requirements
   - Map to planning domain

3. DECIDE:
   - Select planning-worker + PO skill
   - Choose assembly line pattern
   - Prepare context with templates

4. ACT:
   - Delegate to planning worker
   - Monitor user story creation
   - Integrate results
   - Trigger next phase (design)
```

### Example: Bug Fix

```
User Request: "Login form not working"

1. OBSERVE:
   - Check error logs
   - Analyze current code
   - Identify symptoms

2. ORIENT:
   - Classify as "Debugging"
   - Map to execute domain
   - Prepare debug context

3. DECIDE:
   - Select execute-worker + debug skill
   - Choose refinement cycle
   - Include error context

4. ACT:
   - Delegate debugging task
   - Monitor analysis
   - Verify fix implementation
   - Update documentation
```

## OODA Integration Points

### Skills Level

Each skill implements a mini-OODA loop:

```
Skill Execution:
├── Observe: Analyze input and context
├── Orient: Understand requirements
├── Decide: Select implementation approach
├── Act: Generate output and verify
```

### Worker Level

Workers apply OODA for task management:

```
Worker Operation:
├── Observe: Task requirements and constraints
├── Orient: Available skills and resources
├── Decide: Execution strategy and sequencing
├── Act: Skill delegation and result integration
```

### System Level

Agent Orchestrator runs the master OODA loop:

```
System Coordination:
├── Observe: User requests and system state
├── Orient: Request classification and context
├── Decide: Worker/skill selection and patterns
├── Act: Task delegation and result synthesis
```

## Performance Optimization

### Speed Optimization

- **Context Pruning**: Reduce observation time
- **Parallel Execution**: Multiple act phases simultaneously
- **Caching**: Reuse orientation results
- **Progressive Loading**: Fast initial observations

### Quality Optimization

- **Verification Loops**: Multiple act-decide cycles
- **Socratic Checks**: Quality gates at each phase
- **Template Enforcement**: Consistent output formats
- **Context Integrity**: Data consistency validation

## Error Handling

### OODA Error Recovery

**Observe Errors**:
- Context file missing → Initialize project
- File access denied → Check permissions
- Data corruption → Restore from backups

**Orient Errors**:
- Unclear requirements → Request clarification
- Unknown domain → Escalate to human
- Missing context → Gather additional information

**Decide Errors**:
- No suitable worker → Create custom worker
- Skill unavailable → Load alternative skill
- Pattern mismatch → Switch orchestration pattern

**Act Errors**:
- Worker failure → Retry with different worker
- Result invalid → Re-execute with corrections
- Timeout → Break into smaller tasks

## Monitoring and Analytics

### OODA Metrics

- **Cycle Time**: Time per OODA loop iteration
- **Decision Accuracy**: Correct worker/skill selection rate
- **Success Rate**: Task completion without errors
- **User Satisfaction**: Human-in-the-loop feedback

### Continuous Improvement

- **Pattern Learning**: Identify successful patterns
- **Context Optimization**: Improve pruning strategies
- **Skill Enhancement**: Update skills based on usage
- **Worker Tuning**: Adjust worker configurations

## Future Enhancements

### Advanced OODA Features

- **Predictive Orientation**: Machine learning for better classification
- **Adaptive Patterns**: Dynamic pattern selection based on history
- **Multi-loop Coordination**: Parallel OODA loops for complex tasks
- **Context Prediction**: Anticipate required context

### Integration Improvements

- **External Data Sources**: Incorporate external APIs in observe phase
- **Cross-system Coordination**: OODA loops across multiple systems
- **Real-time Adaptation**: Adjust loops based on real-time feedback
- **Collaborative OODA**: Multiple agents in shared OODA processes

The OODA Loop provides the cognitive framework that makes Archon more than just a collection of tools — it creates an intelligent, adaptive system that learns and improves with each interaction.