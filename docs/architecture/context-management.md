# Context Management System

Archon's **Context Management System** maintains the single source of truth for project state. This document explains how context is structured, accessed, and maintained throughout the system.

## Overview

The context management system serves as Archon's "memory" and coordination mechanism:

- **Single Source of Truth**: All project knowledge in `.project_contexts/`
- **Domain Separation**: Organized by concern and responsibility
- **Context Pruning**: Performance optimization for large projects
- **Git Integration**: Selective access and version control

## Directory Structure

### Root Structure

```
.project_contexts/
├── project_context_map.md      # Navigation and overview
├── pm/                         # Product Owner domain
├── arch/                       # Architecture domain
├── dev/                        # Development domain
├── management/                 # Project management
└── shared/                     # Cross-domain artifacts
```

### Domain Breakdown

#### PM Domain (`pm/`)

**Purpose**: What the system should do (requirements and business logic)

```
pm/
├── user_stories/              # User story definitions
├── prds/                      # Product requirement documents
├── acceptance_criteria/       # Acceptance criteria
└── feature_requests/          # Incoming feature requests
```

#### Architecture Domain (`arch/`)

**Purpose**: How the system works (technical design and decisions)

```
arch/
├── tech_specs/                # Technical specifications
├── adrs/                      # Architecture decision records
├── diagrams/                  # System and component diagrams
└── reviews/                   # Architecture reviews
```

#### Development Domain (`dev/`)

**Purpose**: Implementation details and current work

```
dev/
├── change_logs/               # Change documentation
├── documentations/            # Implementation docs
├── current_blockings/         # Current impediments
└── reviews/                   # Code reviews and feedback
```

#### Management Domain (`management/`)

**Purpose**: Project coordination and tracking

```
management/
├── backlogs/                  # Task and sprint backlogs
├── roadmaps/                  # Product and release roadmaps
└── progress_reports/          # Status and progress reports
```

#### Shared Domain (`shared/`)

**Purpose**: Cross-domain artifacts and definitions

```
shared/
├── definitions/               # Common definitions and glossary
├── templates/                 # Reusable templates
└── assets/                    # Shared resources
```

## Key Files

### Project Context Map

**File**: `project_context_map.md`

**Purpose**: Navigation map and project overview

**Contents**:
```markdown
# Project Context Map

## Current Status
[Current project phase and status]

## Active Domains
- PM: [Current user stories and requirements]
- Arch: [Active technical decisions and designs]
- Dev: [Current implementation work]
- Management: [Active tasks and planning]

## Key Artifacts
- [Links to important documents]
- [Current specifications]
- [Active backlogs]

## Navigation
[Links to domain entry points]
```

### Current Progress

**File**: `management/current_progress.md`

**Purpose**: Immediate status for quick context loading

**Contents**:
```markdown
# Current Progress

## Active Tasks
- [Current implementation tickets]
- [In-progress work items]

## Blockers
- [Current impediments]
- [Dependencies waiting]

## Next Actions
- [Immediate next steps]
- [Upcoming priorities]
```

### Active Implementation Ticket

**File**: `management/backlogs/active.md`

**Purpose**: Current task being worked on

**Format**:
```markdown
# Active Implementation Ticket: [TICKET-ID]

**Status:** [IN_PROGRESS|REVIEW|PENDING]

**Assignee:** [worker-type]

**Created:** [date]

## Context
[Task background and requirements]

## Requirements
- [ ] Requirement 1
- [ ] Requirement 2

## Technical Notes
[Implementation details and constraints]

## Acceptance Criteria
- [ ] Criteria 1
- [ ] Criteria 2

## Plan
1. Step 1
2. Step 2
3. Step 3
```

## Context Access Patterns

### Read Access Strategies

#### 1. File Size Threshold

```javascript
function loadContext(file) {
  if (file.size > 10 * 1024 * 1024) { // 10MB
    return loadSummaryOnly(file);
  }
  return loadFullContent(file);
}
```

**Purpose**: Performance optimization for large files

**Implementation**: Load only section headers and key summaries

#### 2. Active-First Loading

```javascript
function loadProjectContext() {
  // Load critical files first
  const critical = [
    'management/current_progress.md',
    'management/backlogs/active.md',
    'project_context_map.md'
  ];

  // Then load domain-specific context
  const domains = loadRelevantDomains();
}
```

**Purpose**: Prioritize current work context

**Benefits**: Faster initial context loading

#### 3. Progressive Loading

```javascript
async function loadContextProgressively() {
  // Phase 1: Basic project info
  const basic = await loadBasicInfo();

  // Phase 2: Current work context
  const current = await loadCurrentWork();

  // Phase 3: Detailed context (on demand)
  const detailed = await loadDetailedContext();
}
```

**Purpose**: Fast initial response with progressive detail

### Write Access Patterns

#### Atomic Updates

```javascript
function updateContext(file, changes) {
  // Create backup
  backupFile(file);

  // Apply changes atomically
  applyChanges(file, changes);

  // Update context map
  updateProjectContextMap(file);

  // Validate integrity
  validateContextIntegrity();
}
```

#### Domain Isolation

```javascript
function updateDomainContext(domain, updates) {
  // Isolate domain-specific changes
  const domainPath = `.project_contexts/${domain}/`;

  // Apply updates within domain
  updateFiles(domainPath, updates);

  // Update cross-domain references
  updateSharedReferences(domain);
}
```

## Context Pruning Strategies

### Chunking Strategy

Context is organized into chunks for efficient access:

```
[GOAL] → What we're trying to achieve
[SKILLS] → Relevant domain knowledge
[TOOLS] → Available capabilities
[CONTEXT] → Current state and history
[REASONING] → Previous decisions made
```

### Relevance Filtering

```javascript
function filterRelevantContext(query, context) {
  // Keyword matching
  const keywordMatches = matchKeywords(query, context);

  // Domain relevance
  const domainRelevance = calculateDomainRelevance(query, context);

  // Recency weighting
  const recencyScore = calculateRecencyScore(context);

  return combineScores(keywordMatches, domainRelevance, recencyScore);
}
```

### Size Management

```javascript
function manageContextSize() {
  // Archive old contexts
  archiveObsoleteContexts();

  // Compress large files
  compressLargeFiles();

  // Clean temporary data
  removeTemporaryFiles();
}
```

## Git Integration

### Selective Access

**Git Configuration**:
```gitignore
# Ignore all project contexts
.project_contexts/

# But allow AI access via .cursorignore
!.project_contexts/
```

**Benefits**:
- Prevents accidental commits of sensitive data
- Allows AI access through `.cursorignore` override
- Maintains clean git history

### Version Control Strategy

```javascript
function versionControlContext() {
  // Track context changes
  trackContextChanges();

  // Create snapshots for major decisions
  createContextSnapshots();

  // Backup before destructive operations
  backupBeforeChanges();
}
```

## Security and Privacy

### Access Control

- **Read Permissions**: Workers can read relevant context
- **Write Permissions**: Controlled write access based on worker type
- **Isolation**: Workers operate in isolated context windows

### Sensitive Data Handling

```javascript
function sanitizeContext(context) {
  // Remove sensitive information
  removeSecrets(context);

  // Anonymize personal data
  anonymizePersonalData(context);

  // Validate safe content
  validateSafeContent(context);
}
```

### Audit Trail

```javascript
function auditContextAccess() {
  // Log all context accesses
  logAccess(operation, user, file, timestamp);

  // Track changes
  logChanges(file, oldContent, newContent);

  // Monitor anomalies
  detectAnomalousAccess();
}
```

## Performance Optimization

### Caching Strategy

```javascript
class ContextCache {
  // Cache frequently accessed files
  cache = new Map();

  // Cache domain summaries
  domainSummaries = new Map();

  // Implement LRU eviction
  evictLeastRecentlyUsed();
}
```

### Indexing

```javascript
function buildContextIndex() {
  // Index all context files
  const index = createFullTextIndex();

  // Index metadata
  indexMetadata();

  // Build domain relationships
  buildDomainRelationships();
}
```

### Lazy Loading

```javascript
function lazyLoadContext(filePath) {
  return new Promise((resolve) => {
    // Load on first access
    if (!loaded[filePath]) {
      loadFile(filePath).then(content => {
        loaded[filePath] = content;
        resolve(content);
      });
    } else {
      resolve(loaded[filePath]);
    }
  });
}
```

## Automation Scripts

### Context Initialization

**Script**: `cursor/skills/initialization/scripts/init_project.py`

**Functionality**:
- Creates directory structure
- Copies templates from skill assets
- Initializes context map
- Sets up `.cursorignore`

### Context Updates

**LLM-Driven Skill**: `cursor/skills/update-project/`

**Capabilities**:
- Analyzes current project structure requirements
- Creates missing directories following established patterns
- Updates context files with current information
- Synchronizes templates to appropriate locations
- Validates all changes and provides status reports

### Report Generation

**LLM-Driven Skill**: `cursor/skills/report/`

**Capabilities**:
- Reads and synthesizes information from multiple context sources
- Applies business logic to assess project health and status
- Generates comprehensive reports with actionable insights
- Adapts content and format based on audience and purpose
- Focuses on key decisions and next steps using 80/20 rule
- Creates visualizations

## Monitoring and Maintenance

### Health Checks

```javascript
function performHealthCheck() {
  // Check directory structure
  validateDirectoryStructure();

  // Validate context files
  validateContextFiles();

  // Check permissions
  validatePermissions();

  // Verify integrity
  checkIntegrity();
}
```

### Cleanup Operations

```javascript
function cleanupContext() {
  // Remove obsolete files
  removeObsoleteFiles();

  // Compress old logs
  compressOldLogs();

  // Optimize storage
  optimizeStorage();

  // Update indexes
  rebuildIndexes();
}
```

### Backup and Recovery

```javascript
function backupContext() {
  // Create timestamped backup
  createBackupSnapshot();

  // Store offsite if configured
  storeOffsiteBackup();

  // Test recovery procedures
  testRecoveryProcess();
}
```

## Integration with Workers

### Context Passing

Workers receive context through structured interfaces:

```javascript
function prepareWorkerContext(worker, task) {
  return {
    task: task,
    relevantContext: getRelevantContext(task),
    templates: getSkillTemplates(worker.skill),
    constraints: getWorkerConstraints(worker),
    outputFormat: getExpectedOutputFormat(task)
  };
}
```

### Result Integration

Worker results are integrated back into context:

```javascript
function integrateWorkerResult(result, context) {
  // Store result in appropriate domain
  storeInDomain(result);

  // Update context map
  updateContextMap(result);

  // Trigger dependent updates
  triggerUpdates(result);
}
```

## Best Practices

### Context Organization

1. **Use Domain Separation**: Store information in appropriate domains
2. **Maintain Context Map**: Keep navigation current
3. **Regular Cleanup**: Remove obsolete information
4. **Version Control**: Track important changes

### Performance

1. **Implement Pruning**: Use size thresholds and relevance filtering
2. **Cache Strategically**: Cache frequently accessed content
3. **Lazy Loading**: Load content on demand
4. **Monitor Usage**: Track access patterns for optimization

### Security

1. **Access Control**: Implement proper permissions
2. **Data Sanitization**: Remove sensitive information
3. **Audit Logging**: Track all access and changes
4. **Regular Backups**: Maintain secure backups

### Maintenance

1. **Health Monitoring**: Regular integrity checks
2. **Automated Cleanup**: Scheduled maintenance tasks
3. **Documentation**: Keep context documentation current
4. **Training**: Ensure team understands context usage

The context management system is the nervous system of Archon, enabling intelligent coordination while maintaining performance, security, and reliability.