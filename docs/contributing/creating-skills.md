# Creating Skills

This guide explains how to create new skills for Archon's skills library. Skills are the core architectural pattern that makes Archon extensible and powerful.

## Understanding Skills

### What is a Skill?

A **Skill** is a domain-specific knowledge module that encapsulates:
- **Expertise**: Specialized knowledge in a domain
- **Best Practices**: Proven methods and patterns
- **Implementation Guidance**: Step-by-step instructions
- **Quality Assurance**: Validation and verification

### Skill Categories

Archon has three skill categories:

#### 1. High-Level Skills (4 total)
- **Purpose**: Strategic decision-making and coordination
- **Examples**: `agent-orchestrator`, `po-product-owner`, `tech-consultant`
- **Characteristics**: Complex reasoning, multiple perspectives, long-term planning

#### 2. Technical Skills (6 total)
- **Purpose**: Implementation and analysis
- **Examples**: `coding`, `debug`, `test`, `review`
- **Characteristics**: Specific technologies, code generation, quality assurance

#### 3. Support Skills (5 total)
- **Purpose**: Infrastructure and maintenance
- **Examples**: `report`, `research`, `update-project`
- **Characteristics**: Data processing, automation, project management

## Skill Structure

### Directory Structure

```
cursor/skills/your-skill-name/
├── SKILL.md              # Main skill definition
├── assets/               # Templates and resources (optional)
│   ├── template.md       # Output templates
│   └── examples/         # Example files
└── scripts/              # Automation scripts (optional)
    ├── script.py         # Python automation
    └── script.sh         # Shell automation
```

### SKILL.md Format

Every skill must have a `SKILL.md` file following this structure:

```markdown
# Skill Name

Brief description of what this skill does and when to use it.

## When to Use

- Condition 1 for using this skill
- Condition 2 for using this skill
- Specific scenarios and use cases

## Instructions

Detailed implementation guidance:

### Step 1: Preparation
Description and requirements for this step.

### Step 2: Analysis
How to analyze the situation.

### Step 3: Implementation
Step-by-step implementation instructions.

### Step 4: Validation
How to validate the results.

## Output Format

Expected output structure and format:

### Required Sections
- **Summary**: Brief overview of results
- **Details**: Comprehensive implementation details
- **Validation**: How results were verified

### Example Output
```markdown
## Summary
[Brief summary of work completed]

## Implementation Details
[Detailed description of what was done]

## Validation Results
[How the implementation was tested and verified]
```

## Examples

[Practical examples of skill usage]

## Constraints

Any limitations, requirements, or prerequisites:
- Required input format
- System requirements
- Limitations and edge cases
- Security considerations
```

## Creating a New Skill

### Step 1: Plan Your Skill

**Define the Skill Scope**:
- What problem does it solve?
- Who will use it? (developers, architects, managers)
- What category does it fit? (high-level, technical, support)

**Analyze Existing Skills**:
- Review similar skills in the same category
- Identify gaps your skill will fill
- Ensure no duplication of functionality

**Define Success Criteria**:
- What should the skill accomplish?
- How will success be measured?
- What quality standards apply?

### Step 2: Create Skill Directory

```bash
# Create skill directory
mkdir cursor/skills/your-skill-name

# Create main skill file
touch cursor/skills/your-skill-name/SKILL.md
```

### Step 3: Write Skill Definition

**Start with Clear Purpose**:
```markdown
# API Design Skill

Creates comprehensive API specifications and documentation following RESTful and GraphQL best practices.
```

**Define Usage Conditions**:
```markdown
## When to Use

- Designing new APIs for web services
- Documenting existing API endpoints
- Creating API specifications for development teams
- Reviewing API designs for best practices compliance
```

**Provide Detailed Instructions**:
```markdown
## Instructions

### 1. Requirements Analysis
- Identify API consumers and use cases
- Define resource models and relationships
- Determine authentication and authorization needs

### 2. Endpoint Design
- Design RESTful or GraphQL endpoint structure
- Define request/response formats
- Specify error handling patterns

### 3. Documentation Creation
- Write OpenAPI/Swagger specifications
- Create usage examples and tutorials
- Document authentication flows
```

### Step 4: Add Templates and Assets

**Create Output Templates**:
```markdown
# Store templates in assets/
cursor/skills/api-design/assets/
├── api-specification.md
├── endpoint-template.md
└── examples/
    ├── rest-api-example.md
    └── graphql-example.md
```

**Template Example** (`assets/api-specification.md`):
```markdown
# API Specification: {API_NAME}

## Overview
- **Purpose**: {API_PURPOSE}
- **Version**: {VERSION}
- **Base URL**: {BASE_URL}

## Authentication
{AUTHENTICATION_DETAILS}

## Endpoints

### {ENDPOINT_NAME}
- **Method**: {HTTP_METHOD}
- **Path**: {ENDPOINT_PATH}
- **Description**: {DESCRIPTION}

**Request Body**:
```json
{REQUEST_SCHEMA}
```

**Response**:
```json
{RESPONSE_SCHEMA}
```

**Error Responses**:
{ERROR_RESPONSES}
```

### Step 5: Add Simple Automation Scripts (Optional - Use Sparingly)

**Guideline**: Prefer LLM-driven instructions over complex scripts. Only use scripts for:
- Simple, deterministic operations
- Well-defined data transformations
- File system operations that don't require complex logic

**Python Scripts for Deterministic Operations**:
```python
# cursor/skills/api-design/scripts/generate_openapi.py
import json
import yaml

def generate_openapi_spec(api_definition):
    """Generate OpenAPI specification from API definition"""
    spec = {
        "openapi": "3.0.1",
        "info": {
            "title": api_definition["name"],
            "version": api_definition["version"]
        },
        "paths": generate_paths(api_definition["endpoints"])
    }
    return yaml.dump(spec)
```

**Shell Scripts for File Operations**:
```bash
# cursor/skills/api-design/scripts/setup_api_docs.sh
#!/bin/bash

# Create API documentation structure
mkdir -p docs/api
mkdir -p docs/api/examples

# Generate initial files
touch docs/api/README.md
touch docs/api/changelog.md
```

### Step 6: Test Your Skill

**Manual Testing**:
1. Use the skill in Cursor IDE
2. Verify output format matches specifications
3. Test with different input scenarios
4. Validate against real-world use cases

**Integration Testing**:
1. Test skill with different workers
2. Verify context integration
3. Check template rendering
4. Validate LLM instruction execution (if scripts are used)

### Step 7: Document and Share

**Update Skill Documentation**:
- Add comprehensive examples
- Document edge cases and limitations
- Provide troubleshooting guidance

**Create Usage Examples**:
```markdown
## Examples

### Basic API Design
```
/api-design create user management API with CRUD operations
```

### Advanced API with Authentication
```
/api-design design e-commerce API with OAuth2 authentication and payment integration
```
```

## Skill Development Best Practices

### Clarity and Precision

**Clear Instructions**:
- Use step-by-step format
- Include specific actions and decisions
- Provide clear success criteria

**Precise Language**:
- Avoid ambiguous terms
- Define technical terms
- Use consistent terminology

### Comprehensive Coverage

**Handle Edge Cases**:
```markdown
## Constraints

- Requires existing database schema for data APIs
- Limited support for real-time WebSocket APIs
- Does not generate client SDKs (use separate skill)
```

**Provide Alternatives**:
```markdown
## Alternative Approaches

For simple APIs: Use basic REST conventions
For complex systems: Consider GraphQL federation
For legacy systems: Focus on wrapper APIs
```

### Quality Assurance

**Validation Steps**:
```markdown
### 4. Validation
- Verify endpoint naming conventions
- Check error response consistency
- Validate request/response schemas
- Test API documentation rendering
```

**Error Handling**:
```markdown
## Error Scenarios

- **Missing Requirements**: Request additional information
- **Conflicting Constraints**: Present trade-off options
- **Invalid Input**: Provide clear error messages and corrections
```

### Performance Considerations

**Efficient Processing**:
- Break complex tasks into steps
- Use progressive disclosure
- Implement early validation

**Resource Management**:
- Clean up temporary files
- Handle large inputs gracefully
- Provide progress indicators for long operations

## Advanced Skill Patterns

### Composite Skills

**Skills that Use Other Skills**:
```markdown
## Instructions

### 1. Initial Analysis
Use research skill to gather requirements:
```
/research analyze competitor API designs
```

### 2. Design Creation
Apply API design principles...

### 3. Documentation
Use report skill to generate docs:
```
/report create API documentation
```
```

### Template-Driven Skills

**Heavy Template Usage**:
```markdown
## Output Format

Use the following template structure:

```markdown
# {API_NAME} API Documentation

## Authentication
{authentication_details}

## Endpoints
{endpoint_details}

## Examples
{usage_examples}
```
```

### LLM-Driven Skills (Recommended)

**Intelligence-First Approach**:
```markdown
## Instructions

### 1. Context Analysis
Analyze the current situation by reading relevant files and understanding requirements:
- Read project context and current state
- Identify stakeholders and their needs
- Assess constraints and opportunities

### 2. Strategic Planning
Develop approach based on analysis:
- Determine optimal strategy for the task
- Consider multiple alternatives and trade-offs
- Plan execution steps with clear milestones

### 3. Intelligent Execution
Execute with adaptability:
- Apply business logic and best practices
- Handle edge cases intelligently
- Maintain context awareness throughout

### 4. Quality Assurance
Validate results:
- Check against requirements and constraints
- Ensure consistency with existing patterns
- Verify stakeholder satisfaction
```

**Advantages of LLM-Driven Skills**:
- **Adaptability**: Handle unexpected situations and requirements
- **Context Awareness**: Understand project semantics and business impact
- **Error Recovery**: Intelligent handling of edge cases and failures
- **Self-Documentation**: Transparent reasoning and decision processes

### Script-Heavy Skills (Use Only for Deterministic Operations)

**Complex Automation**:
```markdown
## Instructions

### 1. Data Collection
Run analysis script:
```bash
python scripts/analyze_requirements.py
```

### 2. Processing
Execute main logic:
```bash
python scripts/generate_api.py
```

### 3. Validation
Run tests:
```bash
python scripts/validate_api.py
```
```

## Skill Maintenance

### Versioning

**Skill Evolution**:
- Increment version numbers for significant changes
- Document breaking changes
- Maintain backward compatibility when possible

### Updates

**Regular Maintenance**:
- Update examples with new patterns
- Incorporate user feedback
- Add new use cases and edge cases

### Deprecation

**Planned Removal**:
- Mark deprecated skills clearly
- Provide migration guides
- Maintain deprecated versions for compatibility

## Examples of Existing Skills

### Coding Skill Analysis

**Structure**: Simple, focused instructions
**Templates**: Code generation templates
**Validation**: Compilation and testing guidance

### Tech Consultant Skill Analysis

**Structure**: Complex decision framework
**Templates**: ADR and tech spec templates
**Process**: Trade-off analysis and documentation

### Debug Skill Analysis

**Structure**: Systematic investigation process
**Tools**: Logging, testing, analysis techniques
**Output**: Root cause and fix recommendations

## Testing and Validation

### Skill Testing Checklist

- [ ] Instructions are clear and actionable
- [ ] Output format is well-defined
- [ ] Templates render correctly
- [ ] Scripts execute without errors
- [ ] Examples work as documented
- [ ] Edge cases are handled
- [ ] Performance is acceptable
- [ ] Integration with workers works

### User Acceptance Testing

**Beta Testing**:
- Test with real development scenarios
- Gather feedback from multiple users
- Iterate based on usage patterns

**Production Validation**:
- Monitor skill usage in production
- Track success rates and error patterns
- Continuously improve based on data

## Contributing Your Skill

### Submission Process

1. **Test Thoroughly**: Ensure skill works reliably
2. **Document Completely**: Provide comprehensive documentation
3. **Create Examples**: Include practical usage examples
4. **Write Tests**: Include test cases and validation

### Review Process

1. **Peer Review**: Other contributors review the skill
2. **Integration Testing**: Test with existing workers
3. **Documentation Review**: Ensure docs are complete
4. **Approval**: Core team approves for inclusion

### Maintenance Commitment

**Ongoing Responsibility**:
- Monitor skill usage and feedback
- Fix bugs and issues promptly
- Update for new patterns and best practices
- Provide user support

## Skill Ecosystem

### Skill Dependencies

**Inter-Skill Relationships**:
- Some skills build on others (coding → test → review)
- Skills can reference each other
- Avoid circular dependencies

### Skill Discovery

**Finding Skills**:
- Browse `cursor/skills/` directory
- Check skill categories and descriptions
- Review usage examples and documentation

### Skill Composition

**Building Complex Solutions**:
- Combine multiple skills for comprehensive solutions
- Use agent orchestrator for complex workflows
- Create skill chains for sequential processing

Creating skills is both an art and a science. Focus on clarity, comprehensiveness, and practical value. Well-designed skills extend Archon's capabilities and improve the development experience for all users.