# CyberShield Academy – Phase 1 System Planning Document

## 1) Project Context and Scope

**Project Name:** CyberShield Academy  
**Project Type:** Cybersecurity awareness and training web platform (portfolio project, intermediate honours level)  
**Primary Goal:** Teach beginners practical cybersecurity awareness through lessons, phishing simulations, password analysis, and quizzes.

### 1.1 Scope of Phase 1 (Planning)
This document defines the functional scope, non-functional constraints, core user journeys, module-level architecture, and database design baseline for development. It establishes a clear blueprint for implementation using Flask Blueprints (modular backend), PostgreSQL, and a modern cybersecurity-themed web UI.

### 1.2 In Scope
- User and admin authentication and authorization.
- Lessons delivery and completion tracking.
- Phishing detection simulation workflows.
- Password strength analyzer logic and feedback.
- Quiz management, delivery, timing, scoring, and result storage.
- User dashboards and admin reporting views.
- Activity tracking across key user actions.

### 1.3 Out of Scope (for this phase)
- Production cloud deployment setup.
- External SIEM/security tooling integrations.
- Multi-language/localization support.
- Native mobile applications.

---

## 2) Functional Requirements

> Requirement IDs are sequential and grouped by feature domain.

### 2.1 Authentication, Authorization, and Session Management
- **FR-01:** The system shall allow a regular user to register with email and password.
- **FR-02:** The system shall validate registration input (email format, password policy, required fields).
- **FR-03:** The system shall prevent duplicate registration for an existing email.
- **FR-04:** The system shall allow regular users to log in and log out securely.
- **FR-05:** The system shall maintain authenticated sessions and restrict protected routes to authenticated users only.
- **FR-06:** The system shall support password reset using either a security-question verification flow or an email-token flow.
- **FR-07:** The system shall store user passwords only as salted cryptographic hashes.
- **FR-08:** The system shall provide a separate registration workflow for admins.
- **FR-09:** The system shall provide a separate login workflow for admins.
- **FR-10:** The system shall enforce role-based access so admins and regular users access only their respective views.
- **FR-11:** The system shall record authentication-related activities (login, logout, reset request, reset completion) in activity history.

### 2.2 Fake Phishing Detector (Simulation)
- **FR-12:** The system shall display phishing email simulations retrieved from the database.
- **FR-13:** The system shall display phishing website simulations retrieved from the database.
- **FR-14:** The system shall display fake login-page simulations retrieved from the database.
- **FR-15:** The system shall prompt users to identify suspicious elements in each simulation.
- **FR-16:** The system shall evaluate user submissions using rule-based checks, including urgent/threatening language patterns.
- **FR-17:** The system shall evaluate suspicious/fake URL indicators in user-submitted analyses.
- **FR-18:** The system shall evaluate misspelled sender-name indicators.
- **FR-19:** The system shall provide immediate feedback indicating correct/incorrect or missed warning signs.
- **FR-20:** The system shall save simulation outcomes and user performance metrics to activity history.

### 2.3 Password Strength Analyzer
- **FR-21:** The system shall allow users to input a password into a secure client-side field for analysis.
- **FR-22:** The system shall evaluate minimum length (>= 8 characters).
- **FR-23:** The system shall evaluate uppercase-character presence.
- **FR-24:** The system shall evaluate lowercase-character presence.
- **FR-25:** The system shall evaluate numeric-character presence.
- **FR-26:** The system shall evaluate special-character presence.
- **FR-27:** The system shall display a real-time strength rating (Weak / Medium / Strong).
- **FR-28:** The system shall display a visual strength bar that updates dynamically.
- **FR-29:** The system shall provide actionable tips to improve the password score.

### 2.4 Security Quizzes
- **FR-30:** The system shall retrieve quiz metadata and questions from PostgreSQL.
- **FR-31:** The system shall support multiple-choice questions with exactly 4 options and 1 correct answer.
- **FR-32:** The system shall support timed quiz sessions with a countdown timer.
- **FR-33:** The system shall auto-submit or finalize a quiz when time expires.
- **FR-34:** The system shall calculate score percentage when a quiz is completed.
- **FR-35:** The system shall determine pass/fail status using a 70% pass mark.
- **FR-36:** The system shall display detailed quiz result feedback to the user.
- **FR-37:** The system shall save quiz results to the user profile/history.
- **FR-38:** The system shall allow admins to add, edit, and delete quiz questions.

### 2.5 User Dashboard
- **FR-39:** The system shall display each user’s overall progress percentage.
- **FR-40:** The system shall display quiz scores and quiz history.
- **FR-41:** The system shall display completed lessons.
- **FR-42:** The system shall display recent activity logs (e.g., logins, quizzes, simulations).
- **FR-43:** The system shall present progress metrics via visual cards and charts.

### 2.6 Admin Panel
- **FR-44:** The system shall provide a dedicated admin panel route set separate from user dashboard routes.
- **FR-45:** The system shall allow admins to view user accounts.
- **FR-46:** The system shall allow admins to deactivate user accounts.
- **FR-47:** The system shall allow admins to add, edit, and delete lessons.
- **FR-48:** The system shall allow admins to add, edit, and delete quiz questions.
- **FR-49:** The system shall allow admins to view reports summarizing user progress and quiz results.
- **FR-50:** The system shall prevent admins from accessing regular-user dashboard interfaces intended for learning workflows.

### 2.7 Lessons Module
- **FR-51:** The system shall support lesson categories: Introduction to Cybersecurity, Phishing Attacks, Password Security.
- **FR-52:** Each lesson shall include title, content, category, and difficulty level.
- **FR-53:** The system shall store lessons in the database and retrieve them by category.
- **FR-54:** The system shall allow users to mark a lesson as completed.
- **FR-55:** The system shall persist lesson completion status for each user.
- **FR-56:** The dashboard shall reflect lesson completion updates in progress calculations.

---

## 3) Non-Functional Requirements

### 3.1 Performance
- **NFR-01:** Standard page responses (dashboard, lesson list, quiz load) should complete within 2 seconds under normal local development load.
- **NFR-02:** Real-time password strength feedback should update within 200 ms after each keystroke.
- **NFR-03:** Database reads for lesson and quiz content should use indexed query fields to keep retrieval latency low.

### 3.2 Security
- **NFR-04:** All passwords must be stored as strong salted hashes using established password-hashing algorithms.
- **NFR-05:** Session identifiers must be protected with secure cookie settings (HttpOnly, Secure in HTTPS environments, SameSite).
- **NFR-06:** Role-based access control must be enforced server-side for all privileged routes.
- **NFR-07:** Input validation and output encoding must be applied to reduce SQL injection and XSS risks.
- **NFR-08:** Sensitive operations (login failures, resets, admin actions) should be logged for auditability.

### 3.3 Usability
- **NFR-09:** UI must be beginner-friendly with clear language, guided feedback, and clear action states.
- **NFR-10:** Core workflows (register, start lesson, take quiz, run simulation) should be reachable within 3 clicks from primary navigation.
- **NFR-11:** Error messages should be specific, non-technical where possible, and indicate next steps.

### 3.4 Maintainability
- **NFR-12:** Backend shall use modular Flask Blueprint architecture separating auth, quizzes, lessons, phishing, dashboard, and admin domains.
- **NFR-13:** Configuration and environment secrets must be externalized (e.g., environment variables) rather than hardcoded.
- **NFR-14:** Database schema changes should be managed via versioned migrations.
- **NFR-15:** Codebase should follow consistent naming, linting, and directory conventions to support future expansion.

### 3.5 Compatibility and Accessibility
- **NFR-16:** Frontend shall support modern browsers (Chrome, Firefox, Edge, Safari latest stable releases).
- **NFR-17:** Responsive layout must support desktop and tablet form factors cleanly.
- **NFR-18:** Color contrast in the dark neon theme should remain readable and accessible for educational content.

---

## 4) Use Cases

| Use Case ID | Actor | Action | Goal |
|---|---|---|---|
| UC-01 | Visitor | Register as regular user | Create learning account |
| UC-02 | Visitor | Register as admin | Create administrative account |
| UC-03 | User | Log in | Access learning modules and dashboard |
| UC-04 | Admin | Log in | Access admin panel |
| UC-05 | User | Reset password | Regain account access securely |
| UC-06 | User | Open lesson by category | Learn cybersecurity topic content |
| UC-07 | User | Mark lesson completed | Track progress and completion |
| UC-08 | User | Start phishing simulation | Practice identifying phishing signals |
| UC-09 | User | Submit phishing analysis | Receive rule-based feedback and save result |
| UC-10 | User | Use password analyzer | Improve password strength quality |
| UC-11 | User | Take timed quiz | Validate topic understanding |
| UC-12 | User | View quiz result | See score and pass/fail status |
| UC-13 | Admin | Manage lessons (CRUD) | Keep educational content updated |
| UC-14 | Admin | Manage quiz questions (CRUD) | Maintain assessment quality |
| UC-15 | Admin | View user reports | Monitor progress and performance trends |
| UC-16 | Admin | Deactivate user account | Enforce governance and moderation |

---

## 5) User Flows

### 5.1 Flow A — New User Registers and Completes a Lesson
1. User opens landing page and selects **Register**.
2. User submits email, password, and required profile details.
3. System validates input and creates account with hashed password.
4. System starts user session and redirects to user dashboard.
5. User opens **Lessons** from navigation.
6. User selects category (e.g., Introduction to Cybersecurity).
7. User opens a lesson and reads content.
8. User clicks **Mark as Complete**.
9. System stores completion record and logs activity.
10. Dashboard updates progress indicators and completed-lesson list.

### 5.2 Flow B — User Takes a Quiz
1. Authenticated user opens **Quizzes** section.
2. User selects an available quiz.
3. System loads quiz metadata and starts countdown timer.
4. User answers multiple-choice questions (4 options each).
5. User submits before time ends (or system auto-submits at timeout).
6. System calculates score and pass/fail status (>=70% = pass).
7. Result page displays score, status, and optional learning feedback.
8. System stores quiz result and logs activity for dashboard/reporting.

### 5.3 Flow C — User Performs a Phishing Simulation
1. User opens **Phishing Detector** module.
2. System presents a simulation type (email, website, or fake login page).
3. User inspects content and marks suspicious indicators.
4. User submits identified warning signs.
5. Rule engine evaluates against defined phishing cues (urgency, URL anomalies, sender spelling).
6. System returns immediate explanatory feedback.
7. System stores performance outcome and activity history entry.
8. Dashboard reflects simulation completion/progress.

### 5.4 Flow D — Admin Logs In and Adds a Lesson
1. Admin opens admin login page.
2. Admin authenticates using admin credentials.
3. System validates role and redirects to admin panel.
4. Admin navigates to **Lessons Management**.
5. Admin selects **Add Lesson**.
6. Admin enters title, content, category, difficulty level.
7. System validates fields and saves lesson in database.
8. System confirms success and logs admin activity.
9. New lesson becomes available to users in lesson catalog.

---

## 6) System Modules / Components

### 6.1 Presentation Layer (Frontend UI)
Provides all user-facing pages using HTML, CSS, and JavaScript. It renders dark/neon themed interfaces, interactive forms, quiz timers, password strength visuals, and dashboard cards/charts. It communicates with Flask routes to fetch and submit learning data.

### 6.2 Authentication Module (Auth Blueprint)
Handles registration, login, logout, session lifecycle, password resets, and credential validation. Enforces account separation between users and admins and applies secure password hashing and verification.

### 6.3 Authorization & Access Control Module
Centralizes role checks and route guards for user-only and admin-only pages. Prevents unauthorized access to protected endpoints and ensures strict separation of user dashboard vs. admin panel.

### 6.4 Lessons Module (Lessons Blueprint)
Manages lesson retrieval, categorization, display, and completion marking. Supports three predefined categories and persists completion records that feed progress calculations.

### 6.5 Quiz Engine Module (Quizzes Blueprint)
Loads quiz definitions/questions, manages timed attempts, validates submitted answers, and computes scores/pass-fail outcomes. Stores attempt-level results and exposes them to both user dashboards and admin reports.

### 6.6 Phishing Simulation Module (Phishing Blueprint)
Delivers pre-written phishing examples (email/site/login) and captures user threat-identification inputs. Applies rule-based detection checks and returns immediate educational feedback while recording outcomes.

### 6.7 Password Analyzer Module
Performs real-time password policy checks and strength classification. Updates visual indicators and tips instantly on the frontend while following consistent security guidance.

### 6.8 User Dashboard Module (Dashboard Blueprint)
Aggregates lesson completion, quiz performance, simulation activities, and recent account events. Displays progress cards and chart data to motivate and guide continued learning.

### 6.9 Admin Panel Module (Admin Blueprint)
Provides administrative interfaces to manage users, lessons, and quiz questions. Includes reporting views for monitoring user progress, quiz outcomes, and platform engagement.

### 6.10 Activity Logging Module
Records important user and admin events (authentication, quiz attempts, simulation submissions, lesson completions, account actions). Serves as the base data source for history feeds, analytics, and audits.

### 6.11 Data Access Layer / ORM Integration
Encapsulates model definitions and database operations for PostgreSQL. Keeps business logic organized and reusable across modules while supporting migrations and relational integrity.

### 6.12 Reporting & Analytics Module
Builds summary metrics for admin consumption (completion rates, average scores, pass rates, active users). Exposes structured report data for tables/cards/charts in the admin interface.

---

## 7) Database Design Plan (PostgreSQL)

> The schema below covers required tables and key relationships for Phase 1.

### 7.1 `users`
| Column | Type | Constraints | Description |
|---|---|---|---|
| id | BIGSERIAL | PK | Unique user ID |
| email | VARCHAR(255) | UNIQUE, NOT NULL | Login identity |
| password_hash | VARCHAR(255) | NOT NULL | Hashed password |
| full_name | VARCHAR(120) | NULL | Display name |
| security_question | VARCHAR(255) | NULL | Optional reset question |
| security_answer_hash | VARCHAR(255) | NULL | Hashed answer |
| is_active | BOOLEAN | NOT NULL DEFAULT TRUE | Account status |
| created_at | TIMESTAMP | NOT NULL DEFAULT NOW() | Registration time |
| updated_at | TIMESTAMP | NOT NULL DEFAULT NOW() | Last profile update |
| last_login_at | TIMESTAMP | NULL | Last successful login |

### 7.2 `admins`
| Column | Type | Constraints | Description |
|---|---|---|---|
| id | BIGSERIAL | PK | Unique admin ID |
| email | VARCHAR(255) | UNIQUE, NOT NULL | Admin login identity |
| password_hash | VARCHAR(255) | NOT NULL | Hashed password |
| full_name | VARCHAR(120) | NULL | Admin display name |
| is_active | BOOLEAN | NOT NULL DEFAULT TRUE | Admin account status |
| created_at | TIMESTAMP | NOT NULL DEFAULT NOW() | Admin registration time |
| updated_at | TIMESTAMP | NOT NULL DEFAULT NOW() | Last profile update |
| last_login_at | TIMESTAMP | NULL | Last successful login |

### 7.3 `lessons`
| Column | Type | Constraints | Description |
|---|---|---|---|
| id | BIGSERIAL | PK | Unique lesson ID |
| title | VARCHAR(200) | NOT NULL | Lesson title |
| content | TEXT | NOT NULL | Lesson body |
| category | VARCHAR(80) | NOT NULL | Intro / Phishing / Password |
| difficulty_level | VARCHAR(30) | NOT NULL | Beginner/Intermediate/etc. |
| created_by_admin_id | BIGINT | FK -> admins.id, NULL | Authoring admin |
| is_published | BOOLEAN | NOT NULL DEFAULT TRUE | Publish status |
| created_at | TIMESTAMP | NOT NULL DEFAULT NOW() | Created timestamp |
| updated_at | TIMESTAMP | NOT NULL DEFAULT NOW() | Updated timestamp |

### 7.4 `quizzes`
| Column | Type | Constraints | Description |
|---|---|---|---|
| id | BIGSERIAL | PK | Unique quiz ID |
| title | VARCHAR(200) | NOT NULL | Quiz title |
| description | TEXT | NULL | Quiz guidance |
| category | VARCHAR(80) | NOT NULL | Topic category |
| time_limit_seconds | INTEGER | NOT NULL | Countdown duration |
| pass_mark_percent | INTEGER | NOT NULL DEFAULT 70 | Pass threshold |
| is_active | BOOLEAN | NOT NULL DEFAULT TRUE | Quiz visibility |
| created_by_admin_id | BIGINT | FK -> admins.id, NULL | Authoring admin |
| created_at | TIMESTAMP | NOT NULL DEFAULT NOW() | Created timestamp |
| updated_at | TIMESTAMP | NOT NULL DEFAULT NOW() | Updated timestamp |

### 7.5 `quiz_questions`
| Column | Type | Constraints | Description |
|---|---|---|---|
| id | BIGSERIAL | PK | Unique question ID |
| quiz_id | BIGINT | FK -> quizzes.id, NOT NULL | Parent quiz |
| question_text | TEXT | NOT NULL | Question prompt |
| option_a | VARCHAR(255) | NOT NULL | Choice A |
| option_b | VARCHAR(255) | NOT NULL | Choice B |
| option_c | VARCHAR(255) | NOT NULL | Choice C |
| option_d | VARCHAR(255) | NOT NULL | Choice D |
| correct_option | CHAR(1) | NOT NULL | A/B/C/D |
| explanation | TEXT | NULL | Feedback rationale |
| order_index | INTEGER | NOT NULL DEFAULT 1 | Display order |
| created_at | TIMESTAMP | NOT NULL DEFAULT NOW() | Created timestamp |
| updated_at | TIMESTAMP | NOT NULL DEFAULT NOW() | Updated timestamp |

### 7.6 `quiz_results`
| Column | Type | Constraints | Description |
|---|---|---|---|
| id | BIGSERIAL | PK | Unique result ID |
| user_id | BIGINT | FK -> users.id, NOT NULL | User who attempted |
| quiz_id | BIGINT | FK -> quizzes.id, NOT NULL | Attempted quiz |
| score_percent | NUMERIC(5,2) | NOT NULL | Final percentage |
| correct_answers | INTEGER | NOT NULL | Count correct |
| total_questions | INTEGER | NOT NULL | Count attempted |
| passed | BOOLEAN | NOT NULL | Pass/fail flag |
| started_at | TIMESTAMP | NOT NULL | Attempt start |
| submitted_at | TIMESTAMP | NOT NULL | Attempt submit |
| duration_seconds | INTEGER | NOT NULL | Attempt duration |

### 7.7 `phishing_examples`
| Column | Type | Constraints | Description |
|---|---|---|---|
| id | BIGSERIAL | PK | Unique simulation ID |
| example_type | VARCHAR(30) | NOT NULL | email / website / login_page |
| title | VARCHAR(200) | NOT NULL | Example label |
| content | TEXT | NOT NULL | Example body/markup text |
| sender_display_name | VARCHAR(120) | NULL | For email simulations |
| sender_email | VARCHAR(255) | NULL | Sender address |
| target_url | VARCHAR(500) | NULL | URL to evaluate |
| has_urgent_language | BOOLEAN | NOT NULL DEFAULT FALSE | Rule signal |
| has_suspicious_url | BOOLEAN | NOT NULL DEFAULT FALSE | Rule signal |
| has_misspelling | BOOLEAN | NOT NULL DEFAULT FALSE | Rule signal |
| difficulty_level | VARCHAR(30) | NOT NULL DEFAULT 'Beginner' | Scenario complexity |
| is_active | BOOLEAN | NOT NULL DEFAULT TRUE | Availability |
| created_by_admin_id | BIGINT | FK -> admins.id, NULL | Authoring admin |
| created_at | TIMESTAMP | NOT NULL DEFAULT NOW() | Created timestamp |
| updated_at | TIMESTAMP | NOT NULL DEFAULT NOW() | Updated timestamp |

### 7.8 `activities`
| Column | Type | Constraints | Description |
|---|---|---|---|
| id | BIGSERIAL | PK | Unique activity ID |
| user_id | BIGINT | FK -> users.id, NULL | Related user (if user action) |
| admin_id | BIGINT | FK -> admins.id, NULL | Related admin (if admin action) |
| activity_type | VARCHAR(80) | NOT NULL | login, quiz_completed, lesson_completed, etc. |
| activity_details | JSONB | NULL | Structured event metadata |
| reference_type | VARCHAR(80) | NULL | quizzes, lessons, phishing_examples |
| reference_id | BIGINT | NULL | Related entity record ID |
| created_at | TIMESTAMP | NOT NULL DEFAULT NOW() | Event timestamp |

---

## 8) Relationship Summary

- `quizzes (1) -> (M) quiz_questions`
- `users (1) -> (M) quiz_results`
- `quizzes (1) -> (M) quiz_results`
- `users (1) -> (M) activities`
- `admins (1) -> (M) activities`
- `admins (1) -> (M) lessons` *(created_by_admin_id)*
- `admins (1) -> (M) quizzes` *(created_by_admin_id)*
- `admins (1) -> (M) phishing_examples` *(created_by_admin_id)*

> Recommended additional join table for implementation phase: `user_lessons(user_id, lesson_id, completed_at)` for many-to-many lesson completion tracking.

---

## 9) UI/UX Direction (Theme Specification)

### 9.1 Visual Language
- Dark base palette (near-black backgrounds) to evoke a cybersecurity operations feel.
- Neon blue and green accents for interactive states, highlights, and progress indicators.
- Terminal-inspired typography accents and subtle grid/glow effects for identity.

### 9.2 Component Style Guidelines
- Dashboard cards with security-themed icons for progress, quizzes, and simulations.
- High-contrast buttons with clear hover/focus states for accessibility.
- Clean spacing and readable text blocks to maintain an educational, not purely decorative, experience.

### 9.3 Interaction Principles
- Immediate feedback for user actions (form validation, quiz submission, simulation scoring).
- Lightweight micro-interactions (animated progress bars, state transitions) to keep engagement high.
- Consistent iconography and color semantics (green=good, amber=warning, red=risk) for intuitive learning.

---

## 10) Phase 1 Deliverables Checklist

- Functional requirements baseline approved.
- Non-functional requirements baseline approved.
- Core use cases documented.
- User flows documented for critical paths.
- Module architecture documented.
- Initial PostgreSQL schema plan documented.
- UI/UX direction documented.

This Phase 1 planning document is the authoritative guide for Phase 2 (system design + implementation breakdown), Phase 3 (development), and Phase 4 (testing and refinement).
