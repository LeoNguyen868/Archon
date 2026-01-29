# Use Cases & Requirement Specification
## Hệ thống AI Agent (Archon)

---

## Phần 1: Use Cases (Trường hợp sử dụng)

### UC-01: Khởi tạo dự án mới (Project Initialization)

**Mô tả:** Người dùng yêu cầu khởi tạo cấu trúc dự án mới với đầy đủ thư mục và template.

**Actors:** 
- Người dùng (PO/Owner)
- Parent Agent (sử dụng skill **agent-orchestrator**)

**Preconditions:** 
- Không có cấu trúc `/.project_contexts/` tồn tại
- Người dùng có quyền tạo file/thư mục

**Main Flow:**
1. Người dùng gửi yêu cầu: "Khởi tạo dự án [Tên dự án]"
2. Parent Agent kích hoạt skill **agent-orchestrator**
3. Parent-orchestrator skill gọi action `initialize-project.md`
4. Parent-orchestrator skill chạy script `init_project.py`:
   ```python
   # Pseudo-code logic cho init_project.py
   def initialize_project_structure():
       # 1. Tạo cấu trúc thư mục /.project_contexts/
       create_directory("/.project_contexts/pm/")
       create_directory("/.project_contexts/arch/")
       create_directory("/.project_contexts/dev/")
       create_directory("/.project_contexts/shared/")
       
       # 2. Tạo file template
       create_template("project_context_map.md")
       create_template("current_progress.md")
       create_template("implementation_ticket.md")
       
       # 3. Tạo communication rules
       create_file(".cursor/rules/communication_rules.mdc", COMMUNICATION_TEMPLATE)
   ```
5. Script tạo cấu trúc thư mục:
   - `/.project_contexts/pm/` - Product Owner domain
   - `/.project_contexts/arch/` - Technical Architecture domain
   - `/.project_contexts/dev/` - Development domain
   - `/.project_contexts/shared/` - Shared artifacts
6. Script tạo file template:
   - `project_context_map.md` - Bản đồ ngữ cảnh dự án
   - `current_progress.md` - Trạng thái hiện tại
   - Các template cho backlog, changelog
7. Script tạo file `.cursor/rules/communication_rules.mdc` với template giao tiếp
8. Parent Agent yêu cầu người dùng cung cấp:
   - Tên dự án
   - Mục tiêu cốt lõi (The One Thing)
9. Parent Agent cập nhật `project_context_map.md` (manual)
10. Parent Agent báo cáo hoàn thành

**Ghi chú:** Logic chi tiết của UC-01 được đặc tả trong skill **agent-orchestrator** (action `initialize-project.md` và script `init_project.py`).

**Postconditions:**
- Cấu trúc thư mục đầy đủ được tạo
- `project_context_map.md` chứa thông tin cơ bản
- Dự án ở trạng thái INCEPTION

**Alternative Flows:**
- Nếu thư mục đã tồn tại: Script báo cáo và bỏ qua các file đã có
- Nếu người dùng không đủ quyền: Script báo lỗi và yêu cầu cấp quyền

---

### UC-02: Tiếp nhận và phân tích yêu cầu (Requirement Analysis)

**Mô tả:** Người dùng đưa ra yêu cầu tính năng mới, Parent Agent điều phối để phân tích và tạo User Story.

**Actors:**
- Người dùng (PO)
- Parent Agent
- Planning Worker (sử dụng skill **po-product-owner**)

**Preconditions:**
- Dự án đã được khởi tạo
- `/.project_contexts/pm/` tồn tại

**Main Flow:**
1. Người dùng mô tả yêu cầu tính năng
2. Người dùng tương tác với Parent Agent
3. Parent Agent kích hoạt skill **agent-orchestrator**
4. Parent-orchestrator skill điều phối: gọi Planning Worker với skill **po-product-owner**
5. Planning Worker (với PO Skill) áp dụng phương pháp Socratic:
   - Hỏi "Is that true?" - Xác thực giả định
   - Hỏi "What is the real problem?" - Xác định vấn đề gốc
   - Hỏi "What if?" - Khám phá các phương án
6. PO Skill ghi nhận User Story vào `/.project_contexts/pm/user_stories/`
7. PO Skill xác định Acceptance Criteria
8. PO Skill cập nhật `/.project_contexts/pm/prds/`
9. Planning Worker báo cáo kết quả về Parent Agent
10. Parent Agent trình bày kết quả cho người dùng xác nhận

**Postconditions:**
- User Story được tạo và lưu
- Acceptance Criteria rõ ràng
- Người dùng xác nhận yêu cầu

**Alternative Flows:**
- Nếu yêu cầu mơ hồ: PO Skill tiếp tục hỏi cho đến khi rõ
- Nếu yêu cầu không khả thi: PO Skill đề xuất phương án thay thế

**Ghi chú:** User tương tác với Parent Agent -> Parent Agent gọi skill agent-orchestrator -> agent-orchestrator điều phối Planning Worker với skill po-product-owner.

---

### UC-03: Thiết kế giải pháp kỹ thuật (Technical Solution Design)

**Mô tả:** Tech Consultant phân tích yêu cầu và tạo Tech Spec với ADRs.

**Actors:**
- Parent Agent
- Planning Worker (sử dụng skill **tech-consultant**)

**Preconditions:**
- User Story đã được xác nhận
- `/.project_contexts/arch/` tồn tại

**Main Flow:**
1. Parent Agent kích hoạt skill **agent-orchestrator**
2. Parent-orchestrator skill điều phối: gọi Planning Worker với skill **tech-consultant**
3. Planning Worker (với Tech Consultant Skill) đọc User Story từ `/.project_contexts/pm/user_stories/`
4. Tech Consultant phân tích tính khả thi:
   - Đánh giá trade-offs (Pros/Cons)
   - Áp dụng nguyên lý KISS & YAGNI
   - Xem xét Security First
   - Có thể yêu cầu tài liệu technical bên ngoài cho công nghệ đặc thù/chuyên biệt hóa
5. Tech Consultant tạo Tech Spec vào `/.project_contexts/arch/tech_specs/`:
   - Cấu trúc dữ liệu
   - API contracts
   - Architecture decisions
6. Tech Consultant tạo ADR vào `/.project_contexts/arch/adrs/` nếu cần:
   - Context
   - Decision
   - Consequences
7. Tech Consultant tạo diagrams vào `/.project_contexts/arch/diagrams/` (C4 model)
8. Planning Worker báo cáo hoàn thành về Parent Agent

**Postconditions:**
- Tech Spec được tạo
- ADRs được ghi nhận
- Diagrams được vẽ
- Dev có đủ thông tin để implement

**Alternative Flows:**
- Nếu yêu cầu không khả thi: Tech Consultant từ chối và đề xuất giải pháp
- Nếu thiếu thông tin: Tech Consultant yêu cầu thêm context

**Ghi chú:** Parent Agent gọi skill agent-orchestrator -> agent-orchestrator điều phối Planning Worker với skill tech-consultant.

---

### UC-04: Lập kế hoạch triển khai (Implementation Planning)

**Mô tả:** PM Skill chia nhỏ Tech Spec thành tasks và tạo backlog.

**Actors:**
- Parent Agent
- Planning Worker (sử dụng skill **pm-project-manager**)

**Preconditions:**
- Tech Spec đã được tạo
- `/.project_contexts/management/` tồn tại

**Main Flow:**
1. Parent Agent kích hoạt skill **agent-orchestrator**
2. Parent-orchestrator skill điều phối: gọi Planning Worker với skill **pm-project-manager**
3. Planning Worker (với PM Skill) đọc Tech Spec từ `/.project_contexts/arch/tech_specs/`
4. PM Skill chia nhỏ thành tasks:
   - Xác định dependencies
   - Ước lượng effort
   - Sắp xếp thứ tự ưu tiên
5. PM Skill tạo tasks vào `/.project_contexts/management/backlogs/sprint_backlog.md`
6. PM Skill tạo Implementation Ticket cho task đầu tiên vào `/.project_contexts/management/backlogs/active.md`
7. PM Skill cập nhật `/.project_contexts/management/roadmaps/`
8. Planning Worker báo cáo kế hoạch về Parent Agent

**Postconditions:**
- Sprint Backlog được tạo
- Active Task được xác định
- Roadmap được cập nhật

**Alternative Flows:**
- Nếu task quá lớn: PM Skill chia nhỏ thêm
- Nếu dependencies chưa rõ: PM Skill yêu cầu Tech Consultant làm rõ

**Ghi chú:** Parent Agent gọi skill agent-orchestrator -> agent-orchestrator điều phối Planning Worker với skill pm-project-manager.

---

### UC-05: Thực thi coding (Code Execution)

**Mô tả:** Execute Worker nhận task và implement code.

**Actors:**
- Parent Agent
- Execute Worker (sử dụng các technical skills: coding, code-analysis, frontend-design)

**Preconditions:**
- Active Task tồn tại trong `/.project_contexts/management/backlogs/active.md`
- Tech Spec đã được tạo

**Main Flow:**
1. Parent Agent kích hoạt skill **agent-orchestrator**
2. Parent-orchestrator skill điều phối: gọi Execute Worker với technical skills tương ứng
3. Execute Worker đọc Implementation Ticket từ `/.project_contexts/management/backlogs/active.md`
4. Execute Worker đọc Tech Spec từ `/.project_contexts/arch/tech_specs/`
5. Execute Worker thực hiện coding:
   - Viết code theo spec
   - Chạy unit tests
   - Áp dụng best practices
6. Execute Worker chạy tests
7. Execute Worker ghi changelog vào `/.project_contexts/dev/change_logs/`
8. Execute Worker báo cáo hoàn thành về Parent Agent

**Postconditions:**
- Code được implement
- Tests pass
- Changelog được ghi
- Task báo cáo hoàn thành

**Alternative Flows:**
- Nếu gặp blocker: Execute Worker báo cáo ngay cho Parent Agent
- Nếu tests fail: Execute Worker debug và sửa

**Ghi chú:** Parent Agent gọi skill agent-orchestrator -> agent-orchestrator điều phối Execute Worker với technical skills.

---

### UC-06: Review và nghiệm thu (Review & Acceptance)

**Mô tả:** Parent Agent review kết quả và người dùng xác nhận.

**Actors:**
- Người dùng
- Parent Agent
- Tech Consultant (nếu cần)

**Preconditions:**
- Execute Worker báo cáo hoàn thành
- Test cases passed
- Người dùng confirm code đã được commit

**Main Flow:**
1. Execute Worker báo cáo hoàn thành
2. Parent Agent kích hoạt skill **agent-orchestrator**
3. Parent-orchestrator skill điều phối review:
   - Gọi Planning Worker với skill **pm-project-manager** để review
   - Gọi Planning Worker với skill **tech-consultant** nếu cần review kỹ thuật
4. Reviewer áp dụng "Trust but Verify":
   - Đọc changelog
   - Kiểm tra code output
   - Verify với requirements
5. Reviewer báo cáo kết quả về Parent Agent
6. Parent Agent trình bày kết quả cho người dùng
7. Người dùng review
8. Nếu đạt: Người dùng xác nhận, Parent Agent đóng task
9. Nếu không đạt: Parent Agent yêu cầu sửa đổi

**Postconditions:**
- Task được đánh dấu Done
- Progress được cập nhật
- Hoặc task được gửi lại để sửa

**Alternative Flows:**
- Nếu cần review kỹ thuật: Parent Agent kích hoạt Tech Consultant
- Nếu có bug: Tạo task mới vào backlog

**Ghi chú:** Review (PM), Test (Dev). Parent Agent điều phối review process.

---

### UC-07: Báo cáo tiến độ (Progress Reporting)

**Mô tả:** Người dùng yêu cầu báo cáo trạng thái dự án.

**Actors:**
- Người dùng
- Parent Agent
- General Worker (sử dụng skill **report**)

**Preconditions:**
- Dự án đã được khởi tạo

**Main Flow:**
1. Người dùng yêu cầu: "Báo cáo tiến độ"
2. Parent Agent kích hoạt skill **agent-orchestrator**
3. Parent-orchestrator skill điều phối: gọi General Worker với skill **report**
4. General Worker (với Report Skill) đọc `/.project_contexts/project_context_map.md`
5. General Worker đọc `/.project_contexts/management/progress_reports/`
6. General Worker đọc `/.project_contexts/management/backlogs/`
7. General Worker tổng hợp:
   - Trạng thái hiện tại
   - Tasks đang làm
   - Blockers
   - Milestones
8. General Worker báo cáo về Parent Agent
9. Parent Agent trình bày báo cáo cho người dùng

**Postconditions:**
- Người dùng có cái nhìn tổng quan
- Quyết định tiếp theo được xác định

**Ghi chú:** Parent Agent gọi skill agent-orchestrator -> agent-orchestrator điều phối General Worker với skill report.

---

## Phần 2: Requirement Specification (Đặc tả yêu cầu)

### 2.1 Functional Requirements (Yêu cầu chức năng)

#### FR-01: Quản lý cấu trúc dự án
- **Skill agent-orchestrator** cần quản lý việc này bằng các script tự động (Python)
- Parent Agent (với skill agent-orchestrator) có thể gọi General Worker với skill **update-project** khi người dùng yêu cầu
- Skill **update-project** (biến thành skill.md) thực hiện:
  - Tạo cấu trúc thư mục
  - Tạo file template (Markdown)
- Manual cập nhật `project_context_map.md` (do người dùng hoặc Parent Agent thực hiện)

#### FR-02: Phân tích yêu cầu
- PO Skill phải áp dụng phương pháp Socratic
- PO Skill phải tạo User Story với format chuẩn
- PO Skill phải xác định Acceptance Criteria rõ ràng
- PO Skill phải lưu tài liệu vào `/.project_contexts/pm/`

#### FR-03: Thiết kế kỹ thuật
- Tech Consultant (là một skill) phải tạo Tech Spec chi tiết
- Tech Consultant phải tạo ADR cho quyết định lớn
- Tech Consultant phải vẽ diagrams theo C4 model
- Tech Consultant phải áp dụng Security First
- Tech Consultant có thể yêu cầu tài liệu technical bên ngoài cho công nghệ đặc thù/chuyên biệt hóa

#### FR-04: Quản lý tiến độ
- PM Skill phải chia nhỏ tasks
- PM Skill phải tạo Sprint Backlog
- PM Skill phải tạo Implementation Ticket
- PM Skill phải quản lý dependencies

#### FR-05: Thực thi code
- Execute Worker phải implement theo Tech Spec
- Execute Worker phải chạy tests
- Execute Worker phải ghi changelog
- Execute Worker phải báo cáo blocker ngay

#### FR-06: Review & Nghiệm thu
- Parent Agent (với skill agent-orchestrator) cần phải quản lý việc cập nhật của FR-01
- Parent Agent phải verify kết quả
- Parent Agent phải yêu cầu người dùng xác nhận
- Parent Agent phải kích hoạt Tech Consultant khi cần
- Parent Agent phải đóng task khi đạt

#### FR-07: Báo cáo
- Công việc của Parent Agent (với skill agent-orchestrator)
- Parent Agent có thể gọi General Worker với skill **report** khi người dùng yêu cầu (tương tự FR-01)
- Hệ thống phải tổng hợp progress
- Hệ thống phải hiển thị blockers
- Hệ thống phải track milestones

---

### 2.2 Non-Functional Requirements (Yêu cầu phi chức năng)

#### NFR-01: Performance
- Thời gian khởi tạo dự án < 5 giây
- Thời gian phân tích yêu cầu < 10 giây
- Thời gian tạo Tech Spec < 30 giây

#### NFR-02: Reliability
- Việc của Parent Agent (với skill agent-orchestrator) - vẫn là skill-centric
- Hệ thống phải ghi log mọi hành động
- Hệ thống phải detect lỗi sớm
- Hệ thống phải có rollback capability

#### NFR-03: Usability
- Giao tiếp phải ngắn gọn, súc tích
- Hệ thống phải hỏi khi thiếu context
- Hệ thống phải trình bày rõ ràng

#### NFR-04: Maintainability
- Code phải clean và documented
- Structure phải scalable
- Templates phải reusable

#### NFR-05: Security
- Không bao giờ expose sensitive data
- Áp dụng principle of least privilege
- Verify trước khi execute

#### NFR-06: Scalability
- Hỗ trợ thêm skill mới dễ dàng
- Hỗ trợ thêm worker mới dễ dàng
- Hỗ trợ dự án lớn

**Phân loại Skills:**

1. **High-Level Skills** (cần phải specialized, general, mental models, system thinking, rules, critical thinking):
   - agent-orchestrator skill
   - tech-consultant skill
   - po-product-owner skill
   - pm-project-manager skill

2. **Technical Skills** (cần phải chuyên biệt hóa, modular):
   - review skill
   - delegation skill
   - initialization skill
   - debug skill
   - report skill
   - research skill

3. **General Skills** (có thể shared):
   - Các skill chung dùng cho nhiều tác vụ

---

### 2.3 Data Requirements (Yêu cầu dữ liệu)

#### DR-01: Cấu trúc thư mục
```
/.project_contexts/                  # Thư mục ngữ cảnh dự án (được initialized bằng script trong thư mục dự án)
├── pm/                              # PO Domain - WHAT & WHY
│   ├── user_stories/               # User Stories
│   ├── prds/                       # Product Requirements
│   └── acceptance_criteria/        # Điều kiện nghiệm thu
│
├── arch/                            # Tech Consultant Domain - HOW (High-level)
│   ├── tech_specs/                 # Implementation Guides
│   ├── adrs/                       # Architecture Decisions
│   ├── diagrams/                   # Data flow, System design
│   └── reviews/                    # Tech reviews
│
├── dev/                             # Execute Worker Domain - HOW (Low-level)
│   ├── change_logs/                # Daily technical updates
│   ├── documentations/             # Technical Specs
│   ├── current_blockings/          # Issues
│   └── reviews/                    # Code reviews
│
└── shared/                          # Cross-team artifacts
    ├── definitions/                # Terminology
    ├── team_roles.md               # Roles
    └── processes.md                 # Processes
```

**Lưu ý:** `/.project_contexts/` không phải `project_files/`. Thư mục này sẽ được initialized bằng script trong thư mục dự án.

#### DR-02: File Templates
- `project_context_map.md` - Bản đồ ngữ cảnh
- `implementation_ticket.md` - Ticket giao việc
- `adr.md` - Architecture Decision Record
- `status_report.md` - Báo cáo trạng thái

#### DR-03: Data Formats
- Tất cả tài liệu phải là Markdown
- Changelog phải có format chuẩn
- ADR phải theo template

---

### 2.4 Interface Requirements (Yêu cầu giao tiếp)

#### IR-01: Giao tiếp với Người dùng
- Sử dụng phương pháp Socratic
- Hỏi "Is that true?", "What is the real problem?", "What if?"
- Không trả lời trực tiếp, đặt câu hỏi gợi mở
- Ngắn gọn, súc tích (quy tắc 80/20)

#### IR-02: Giao tiếp giữa Agents
- Sử dụng format báo cáo chuẩn
- Gửi kết quả qua file
- Ghi log mọi hành động
- Verify trước khi accept

#### IR-03: Giao tiếp với Terminal
- Hệ thống phải có khả năng chạy script
- Hệ thống phải có khả năng tạo file
- Hệ thống phải có khả năng đọc file
- Hệ thống phải có khả năng debug

---

### 2.5 Integration Requirements (Yêu cầu tích hợp)

#### ITR-01: Tích hợp với Cursor IDE
- Phải hoạt động trong môi trường Cursor
- Phải sử dụng shared skills
- Phải tương thích với agents hiện có

#### ITR-02: Tích hợp với Git
- **Lưu ý:** Không định hình skill hay agent nào có quyền commit ngoài người dùng
- Hệ thống phải hỗ trợ git operations
- Hệ thống phải tạo commit messages
- Hệ thống phải support branches
- Chỉ người dùng mới có quyền thực hiện commit

#### ITR-03: Tích hợp với Testing
- Hệ thống phải chạy unit tests
- Hệ thống phải chạy integration tests
- Hệ thống phải report test results

---

### 2.6 Security Requirements (Yêu cầu bảo mật)

#### SR-01: Access Control
- Parent Agent: Đọc/ghi tất cả
- PO Skill: Đọc/ghi `./pm/`
- Tech Consultant: Đọc/ghi `./arch/`, đọc `./pm/`
- PM Skill: Đọc/ghi `./management/`, đọc `./pm/`, `./arch/`
- Execute Worker: Đọc `./pm/`, `./arch/`, ghi `./dev/`

#### SR-02: Validation
- Verify trước khi execute
- Check permissions trước khi write
- Validate input trước khi process

#### SR-03: Audit
- Log mọi hành động
- Track ai làm gì khi nào
- Maintain history

---

### 2.7 Workflow Requirements (Yêu cầu quy trình)

#### WR-01: Inception Phase
1. Khởi tạo dự án
2. Định nghĩa scope
3. Xác định mục tiêu cốt lõi

#### WR-02: Planning Phase
1. Phân tích yêu cầu (PO)
2. Thiết kế giải pháp (Tech Consultant)
3. Lập kế hoạch (PM)

#### WR-03: Execution Phase
1. Giao việc (PM)
2. Implement code (Dev)
3. Review (PM), Test (Dev)

#### WR-04: Review Phase
1. Verify kết quả
2. Người dùng accept
3. Đóng task

---

## Phần 3: Acceptance Criteria (Tiêu chí nghiệm thu)

### AC-01: Khởi tạo dự án
- [ ] Cấu trúc thư mục đầy đủ được tạo
- [ ] File template được tạo
- [ ] `project_context_map.md` được cập nhật
- [ ] Script chạy < 5 giây

### AC-02: Phân tích yêu cầu
- [ ] User Story được tạo
- [ ] Acceptance Criteria rõ ràng
- [ ] Người dùng xác nhận
- [ ] Tài liệu được lưu đúng vị trí

### AC-03: Thiết kế kỹ thuật
- [ ] Tech Spec chi tiết
- [ ] ADRs được tạo
- [ ] Diagrams được vẽ
- [ ] Dev có đủ thông tin

### AC-04: Lập kế hoạch
- [ ] Tasks được chia nhỏ
- [ ] Sprint Backlog được tạo
- [ ] Implementation Ticket rõ ràng
- [ ] Dependencies được xác định

### AC-05: Thực thi
- [ ] Code implement theo spec
- [ ] Tests pass
- [ ] Changelog được ghi
- [ ] Blocker được báo cáo

### AC-06: Review
- [ ] Kết quả được verify
- [ ] Người dùng accept
- [ ] Task được đóng
- [ ] Progress được cập nhật

---

## Phần 4: Technical Constraints (Ràng buộc kỹ thuật)

### TC-01: Environment
- Phải chạy trong Cursor IDE
- Phải hỗ trợ Linux
- Phải có Python 3.8+

### TC-02: Dependencies
- Không có external dependencies
- Sử dụng built-in libraries
- Scripts phải standalone

### TC-03: Performance
- Context window optimization
- Lazy loading thông tin
- Token efficiency

---

## Phần 5: Success Metrics (Thước đo thành công)

### SM-01: Efficiency
- Thời gian từ yêu cầu đến code < 1 giờ
- Số lần iteration < 3
- Token usage tối ưu

### SM-02: Quality
- Code coverage > 80%
- Bug rate giảm 50%
- Review time giảm 70%

### SM-03: Usability
- Người dùng hài lòng > 90%
- Số câu hỏi cần giảm 60%
- Learning curve < 1 tuần

---

## Phần 6: Future Enhancements (Nâng cấp tương lai)

### FE-01: QA Agent
- Tạo QA Agent cho automated testing
- Tạo test cases từ requirements
- Run regression tests

### FE-02: Security Agent
- Tạo Security Agent cho vulnerability scanning
- Review code cho security issues
- Suggest security improvements

### FE-03: Documentation Agent
- Tạo Documentation Agent
- Auto-generate API docs
- Maintain README files

### FE-04: CI/CD Integration
- Tự động deploy
- Tự động run tests
- Tự động generate reports

---

## Phần 7: Risk Assessment (Đánh giá rủi ro)

### R-01: Hallucination
- **Mô tả:** AI tạo ra thông tin sai
- **Giảm thiểu:** Verify trước khi accept
- **Mitigation:** Human-in-the-loop

### R-02: Context Overflow
- **Mô tả:** Token limit exceeded
- **Giảm thiểu:** Lazy loading, project_context_map
- **Mitigation:** Chunking, summarization

### R-03: Permission Issues
- **Mô tả:** Không thể write file
- **Giảm thiểu:** Check permissions trước
- **Mitigation:** Error handling, retry

### R-04: Integration Failures
- **Mô tả:** Script không chạy
- **Giảm thiểu:** Test scripts trước
- **Mitigation:** Fallback mechanisms

---

## Phần 8: Implementation Roadmap (Lộ trình triển khai)

### Phase 1: Foundation (Tuần 1-2)
- [ ] Tạo cấu trúc thư mục
- [ ] Viết init_project.py
- [ ] Tạo templates
- [ ] Test initialization

### Phase 2: Core Skills (Tuần 3-4)
- [ ] Viết PO Skill
- [ ] Viết Tech Consultant Skill
- [ ] Viết PM Skill
- [ ] Test skills

### Phase 3: Workers (Tuần 5-6)
- [ ] Tạo Planning Worker
- [ ] Tạo Execute Worker
- [ ] Integrate with skills
- [ ] Test delegation

### Phase 4: Orchestrator (Tuần 7-8)
- [ ] Viết Parent Agent prompt
- [ ] Implement OODA loop
- [ ] Test end-to-end
- [ ] Refine interactions

### Phase 5: Integration (Tuần 9-10)
- [ ] Integrate with Cursor
- [ ] Test real scenarios
- [ ] Document usage
- [ ] Deploy

---

## Phần 9: Glossary (Thuật ngữ)

| Thuật ngữ | Định nghĩa |
|-----------|------------|
| **Parent Agent** | Agent điều phối chính, giao tiếp với người dùng |
| **Skill** | Bộ kiến thức chuyên môn cho agent |
| **Worker** | Agent thực thi tác vụ cụ thể |
| **PO** | Product Owner - Người sở hữu sản phẩm |
| **PM** | Project Manager - Quản lý dự án |
| **ADR** | Architecture Decision Record - Ghi nhận quyết định kiến trúc |
| **OODA Loop** | Observe-Orient-Decide-Act - Vòng lặp ra quyết định |
| **Socratic Method** | Phương pháp hỏi đáp Socrates |
| **Lazy Loading** | Tải thông tin khi cần thiết |
| **Context Window** | Giới hạn token của AI |
| **The One Thing** | Điều quan trọng nhất |
| **First Principles** | Nguyên lý đầu tiên |
| **80/20 Rule** | Nguyên lý Pareto |
| **KISS** | Keep It Simple, Stupid |
| **YAGNI** | You Aren't Gonna Need It |
| **C4 Model** | Context-Container-Component-Code - Mô hình kiến trúc 4 tầng |

---

## Phần 10: References (Tài liệu tham khảo)

### Books
- Team Topologies - Matthew Skelton & Manuel Pais
- Shape Up - Ryan Singer
- The Checklist Manifesto - Atul Gawande
- Domain-Driven Design - Eric Evans

### Mental Models
- Gall's Law
- Second-Order Thinking
- Inversion
- ReAct Pattern
- Reflexion

### Frameworks
- Agile/Scrum
- Test-Driven Development
- Human-in-the-Loop
- Radical Truth

---

**Phiên bản:** 1.0  
**Ngày tạo:** 2026-01-29  
**Tác giả:** System Design Document  
**Trạng thái:** Draft
