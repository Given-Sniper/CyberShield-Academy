# CyberShield Academy – Phase 2 System Design Document

## Overview
This Phase 2 document translates Phase 1 planning into an implementation-ready system design for a modular Flask + PostgreSQL web application. It defines the complete project structure, SQL schema, blueprint architecture, model mapping, security design, UI page map, and a Phase 3 readiness checklist.

---

## PART 1: Complete Folder Structure

```text
CyberShield-Academy/
├── .env
├── .env.example
├── .gitignore
├── README.md
├── requirements.txt
├── run.py
├── config.py
├── instance/
│   └── .gitkeep
├── migrations/
│   ├── README
│   ├── alembic.ini
│   ├── env.py
│   ├── script.py.mako
│   └── versions/
│       └── .gitkeep
├── app/
│   ├── __init__.py
│   ├── extensions.py
│   ├── models/
│   │   ├── __init__.py
│   │   ├── admin.py
│   │   ├── user.py
│   │   ├── lesson.py
│   │   ├── quiz.py
│   │   ├── quiz_question.py
│   │   ├── quiz_result.py
│   │   ├── phishing_example.py
│   │   ├── activity.py
│   │   └── user_lesson.py
│   ├── blueprints/
│   │   ├── main/
│   │   │   ├── __init__.py
│   │   │   ├── routes.py
│   │   │   └── forms.py
│   │   ├── auth/
│   │   │   ├── __init__.py
│   │   │   ├── routes.py
│   │   │   └── forms.py
│   │   ├── dashboard/
│   │   │   ├── __init__.py
│   │   │   ├── routes.py
│   │   │   └── forms.py
│   │   ├── lessons/
│   │   │   ├── __init__.py
│   │   │   ├── routes.py
│   │   │   └── forms.py
│   │   ├── quizzes/
│   │   │   ├── __init__.py
│   │   │   ├── routes.py
│   │   │   └── forms.py
│   │   ├── phishing/
│   │   │   ├── __init__.py
│   │   │   ├── routes.py
│   │   │   └── forms.py
│   │   └── admin/
│   │       ├── __init__.py
│   │       ├── routes.py
│   │       └── forms.py
│   ├── services/
│   │   ├── __init__.py
│   │   ├── auth_service.py
│   │   ├── dashboard_service.py
│   │   ├── quiz_service.py
│   │   ├── phishing_service.py
│   │   ├── lesson_service.py
│   │   └── reporting_service.py
│   ├── utils/
│   │   ├── __init__.py
│   │   ├── decorators.py
│   │   ├── constants.py
│   │   ├── validators.py
│   │   └── activity_logger.py
│   ├── templates/
│   │   ├── base.html
│   │   ├── includes/
│   │   │   ├── _navbar_public.html
│   │   │   ├── _navbar_user.html
│   │   │   ├── _navbar_admin.html
│   │   │   ├── _alerts.html
│   │   │   └── _footer.html
│   │   ├── errors/
│   │   │   ├── 403.html
│   │   │   ├── 404.html
│   │   │   └── 500.html
│   │   ├── main/
│   │   │   ├── index.html
│   │   │   ├── about.html
│   │   │   ├── contact.html
│   │   │   └── privacy.html
│   │   ├── auth/
│   │   │   ├── user_register.html
│   │   │   ├── user_login.html
│   │   │   ├── user_reset_request.html
│   │   │   ├── user_reset_security_question.html
│   │   │   ├── user_reset_token.html
│   │   │   ├── user_reset_password.html
│   │   │   ├── admin_register.html
│   │   │   └── admin_login.html
│   │   ├── dashboard/
│   │   │   ├── user_dashboard.html
│   │   │   ├── progress_details.html
│   │   │   └── activity_history.html
│   │   ├── lessons/
│   │   │   ├── lessons_list.html
│   │   │   ├── lesson_detail.html
│   │   │   └── lesson_complete_confirm.html
│   │   ├── quizzes/
│   │   │   ├── quiz_list.html
│   │   │   ├── quiz_start.html
│   │   │   ├── quiz_take.html
│   │   │   ├── quiz_submit_confirm.html
│   │   │   ├── quiz_result.html
│   │   │   └── quiz_history.html
│   │   ├── phishing/
│   │   │   ├── phishing_home.html
│   │   │   ├── phishing_example_view.html
│   │   │   ├── phishing_submit.html
│   │   │   ├── phishing_feedback.html
│   │   │   └── phishing_history.html
│   │   └── admin/
│   │       ├── admin_dashboard.html
│   │       ├── users_list.html
│   │       ├── user_detail.html
│   │       ├── user_deactivate_confirm.html
│   │       ├── lessons_manage.html
│   │       ├── lesson_form.html
│   │       ├── quizzes_manage.html
│   │       ├── quiz_form.html
│   │       ├── questions_manage.html
│   │       ├── question_form.html
│   │       ├── phishing_examples_manage.html
│   │       ├── phishing_example_form.html
│   │       ├── reports_overview.html
│   │       ├── reports_user_progress.html
│   │       └── reports_quiz_results.html
│   └── static/
│       ├── css/
│       │   ├── base.css
│       │   ├── theme_dark_neon.css
│       │   ├── auth.css
│       │   ├── dashboard.css
│       │   ├── lessons.css
│       │   ├── quizzes.css
│       │   ├── phishing.css
│       │   ├── admin.css
│       │   └── responsive.css
│       ├── js/
│       │   ├── main.js
│       │   ├── password_strength.js
│       │   ├── quiz_timer.js
│       │   ├── phishing_interactions.js
│       │   ├── dashboard_charts.js
│       │   └── admin_actions.js
│       └── images/
│           ├── logo.png
│           ├── hero-cyber-bg.jpg
│           ├── icons/
│           │   ├── icon-lessons.svg
│           │   ├── icon-quizzes.svg
│           │   ├── icon-phishing.svg
│           │   ├── icon-password.svg
│           │   └── icon-dashboard.svg
│           └── illustrations/
│               ├── phishing-mail-example.png
│               ├── phishing-site-example.png
│               └── secure-password-guide.png
└── tests/
    ├── __init__.py
    ├── conftest.py
    ├── test_auth_routes.py
    ├── test_lessons_routes.py
    ├── test_quizzes_routes.py
    ├── test_phishing_routes.py
    ├── test_admin_routes.py
    └── test_models.py
```

### `.env` placeholder variables
- `FLASK_ENV=development`
- `SECRET_KEY=`
- `DATABASE_URL=postgresql+psycopg2://<user>:<password>@localhost:5432/cybershield_academy`
- `SQLALCHEMY_TRACK_MODIFICATIONS=False`
- `WTF_CSRF_ENABLED=True`
- `SESSION_COOKIE_SECURE=False`
- `SESSION_COOKIE_HTTPONLY=True`
- `SESSION_COOKIE_SAMESITE=Lax`
- `MAIL_SERVER=`
- `MAIL_PORT=`
- `MAIL_USERNAME=`
- `MAIL_PASSWORD=`
- `MAIL_USE_TLS=True`
- `MAIL_USE_SSL=False`
- `PASSWORD_RESET_TOKEN_EXPIRES_MINUTES=30`

### `requirements.txt` placeholder packages
- Flask
- Flask-SQLAlchemy
- Flask-Migrate
- Flask-Login
- Flask-WTF
- WTForms
- email-validator
- psycopg2-binary
- python-dotenv
- Werkzeug
- itsdangerous
- Flask-Mail
- gunicorn
- pytest
- pytest-flask

---

## PART 2: Complete Database Schema (PostgreSQL SQL)

```sql
-- 1) admins
COMMENT ON SCHEMA public IS 'Default schema for CyberShield Academy';

CREATE TABLE admins (
    id BIGSERIAL PRIMARY KEY,
    email VARCHAR(255) NOT NULL UNIQUE,
    password_hash VARCHAR(255) NOT NULL,
    full_name VARCHAR(120),
    is_active BOOLEAN NOT NULL DEFAULT TRUE,
    created_at TIMESTAMP NOT NULL DEFAULT NOW(),
    updated_at TIMESTAMP NOT NULL DEFAULT NOW(),
    last_login_at TIMESTAMP
);
COMMENT ON TABLE admins IS 'Stores administrator accounts with separate authentication from regular users.';

CREATE INDEX idx_admins_created_at ON admins (created_at);

-- 2) users
CREATE TABLE users (
    id BIGSERIAL PRIMARY KEY,
    email VARCHAR(255) NOT NULL UNIQUE,
    password_hash VARCHAR(255) NOT NULL,
    full_name VARCHAR(120),
    security_question VARCHAR(255),
    security_answer_hash VARCHAR(255),
    is_active BOOLEAN NOT NULL DEFAULT TRUE,
    created_at TIMESTAMP NOT NULL DEFAULT NOW(),
    updated_at TIMESTAMP NOT NULL DEFAULT NOW(),
    last_login_at TIMESTAMP
);
COMMENT ON TABLE users IS 'Stores regular learner accounts, credentials, and status metadata.';

CREATE INDEX idx_users_created_at ON users (created_at);

-- 3) lessons
CREATE TABLE lessons (
    id BIGSERIAL PRIMARY KEY,
    title VARCHAR(200) NOT NULL,
    content TEXT NOT NULL,
    category VARCHAR(80) NOT NULL,
    difficulty_level VARCHAR(30) NOT NULL,
    created_by_admin_id BIGINT,
    is_published BOOLEAN NOT NULL DEFAULT TRUE,
    created_at TIMESTAMP NOT NULL DEFAULT NOW(),
    updated_at TIMESTAMP NOT NULL DEFAULT NOW(),
    CONSTRAINT fk_lessons_created_by_admin
        FOREIGN KEY (created_by_admin_id)
        REFERENCES admins (id)
        ON DELETE SET NULL
);
COMMENT ON TABLE lessons IS 'Stores educational cybersecurity lessons grouped by category and difficulty.';

CREATE INDEX idx_lessons_created_at ON lessons (created_at);
CREATE INDEX idx_lessons_category ON lessons (category);

-- 4) quizzes
CREATE TABLE quizzes (
    id BIGSERIAL PRIMARY KEY,
    title VARCHAR(200) NOT NULL,
    description TEXT,
    category VARCHAR(80) NOT NULL,
    time_limit_seconds INTEGER NOT NULL,
    pass_mark_percent INTEGER NOT NULL DEFAULT 70,
    is_active BOOLEAN NOT NULL DEFAULT TRUE,
    created_by_admin_id BIGINT,
    created_at TIMESTAMP NOT NULL DEFAULT NOW(),
    updated_at TIMESTAMP NOT NULL DEFAULT NOW(),
    CONSTRAINT fk_quizzes_created_by_admin
        FOREIGN KEY (created_by_admin_id)
        REFERENCES admins (id)
        ON DELETE SET NULL
);
COMMENT ON TABLE quizzes IS 'Stores quiz definitions, timing rules, and pass thresholds.';

CREATE INDEX idx_quizzes_created_at ON quizzes (created_at);
CREATE INDEX idx_quizzes_category ON quizzes (category);

-- 5) quiz_questions
CREATE TABLE quiz_questions (
    id BIGSERIAL PRIMARY KEY,
    quiz_id BIGINT NOT NULL,
    question_text TEXT NOT NULL,
    option_a VARCHAR(255) NOT NULL,
    option_b VARCHAR(255) NOT NULL,
    option_c VARCHAR(255) NOT NULL,
    option_d VARCHAR(255) NOT NULL,
    correct_option CHAR(1) NOT NULL CHECK (correct_option IN ('A','B','C','D')),
    explanation TEXT,
    order_index INTEGER NOT NULL DEFAULT 1,
    created_at TIMESTAMP NOT NULL DEFAULT NOW(),
    updated_at TIMESTAMP NOT NULL DEFAULT NOW(),
    CONSTRAINT fk_quiz_questions_quiz
        FOREIGN KEY (quiz_id)
        REFERENCES quizzes (id)
        ON DELETE CASCADE
);
COMMENT ON TABLE quiz_questions IS 'Stores multiple-choice questions for each quiz with one correct option.';

CREATE INDEX idx_quiz_questions_quiz_id ON quiz_questions (quiz_id);
CREATE INDEX idx_quiz_questions_created_at ON quiz_questions (created_at);

-- 6) quiz_results
CREATE TABLE quiz_results (
    id BIGSERIAL PRIMARY KEY,
    user_id BIGINT NOT NULL,
    quiz_id BIGINT NOT NULL,
    score_percent NUMERIC(5,2) NOT NULL,
    correct_answers INTEGER NOT NULL,
    total_questions INTEGER NOT NULL,
    passed BOOLEAN NOT NULL,
    started_at TIMESTAMP NOT NULL,
    submitted_at TIMESTAMP NOT NULL,
    duration_seconds INTEGER NOT NULL,
    CONSTRAINT fk_quiz_results_user
        FOREIGN KEY (user_id)
        REFERENCES users (id)
        ON DELETE CASCADE,
    CONSTRAINT fk_quiz_results_quiz
        FOREIGN KEY (quiz_id)
        REFERENCES quizzes (id)
        ON DELETE CASCADE
);
COMMENT ON TABLE quiz_results IS 'Stores each user quiz attempt result including score, duration, and pass status.';

CREATE INDEX idx_quiz_results_user_id ON quiz_results (user_id);
CREATE INDEX idx_quiz_results_quiz_id ON quiz_results (quiz_id);
CREATE INDEX idx_quiz_results_submitted_at ON quiz_results (submitted_at);

-- 7) phishing_examples
CREATE TABLE phishing_examples (
    id BIGSERIAL PRIMARY KEY,
    example_type VARCHAR(30) NOT NULL CHECK (example_type IN ('email','website','login_page')),
    title VARCHAR(200) NOT NULL,
    content TEXT NOT NULL,
    sender_display_name VARCHAR(120),
    sender_email VARCHAR(255),
    target_url VARCHAR(500),
    has_urgent_language BOOLEAN NOT NULL DEFAULT FALSE,
    has_suspicious_url BOOLEAN NOT NULL DEFAULT FALSE,
    has_misspelling BOOLEAN NOT NULL DEFAULT FALSE,
    difficulty_level VARCHAR(30) NOT NULL DEFAULT 'Beginner',
    is_active BOOLEAN NOT NULL DEFAULT TRUE,
    created_by_admin_id BIGINT,
    created_at TIMESTAMP NOT NULL DEFAULT NOW(),
    updated_at TIMESTAMP NOT NULL DEFAULT NOW(),
    CONSTRAINT fk_phishing_examples_admin
        FOREIGN KEY (created_by_admin_id)
        REFERENCES admins (id)
        ON DELETE SET NULL
);
COMMENT ON TABLE phishing_examples IS 'Stores fake phishing scenarios used for simulation-based user training.';

CREATE INDEX idx_phishing_examples_created_at ON phishing_examples (created_at);
CREATE INDEX idx_phishing_examples_type ON phishing_examples (example_type);

-- 8) activities
CREATE TABLE activities (
    id BIGSERIAL PRIMARY KEY,
    user_id BIGINT,
    admin_id BIGINT,
    activity_type VARCHAR(80) NOT NULL,
    activity_details JSONB,
    reference_type VARCHAR(80),
    reference_id BIGINT,
    created_at TIMESTAMP NOT NULL DEFAULT NOW(),
    CONSTRAINT fk_activities_user
        FOREIGN KEY (user_id)
        REFERENCES users (id)
        ON DELETE CASCADE,
    CONSTRAINT fk_activities_admin
        FOREIGN KEY (admin_id)
        REFERENCES admins (id)
        ON DELETE SET NULL,
    CONSTRAINT chk_activities_actor_present
        CHECK (user_id IS NOT NULL OR admin_id IS NOT NULL)
);
COMMENT ON TABLE activities IS 'Stores auditable platform events for users and admins across all major actions.';

CREATE INDEX idx_activities_user_id ON activities (user_id);
CREATE INDEX idx_activities_admin_id ON activities (admin_id);
CREATE INDEX idx_activities_activity_type ON activities (activity_type);
CREATE INDEX idx_activities_created_at ON activities (created_at);

-- 9) user_lessons
CREATE TABLE user_lessons (
    id BIGSERIAL PRIMARY KEY,
    user_id BIGINT NOT NULL,
    lesson_id BIGINT NOT NULL,
    completed_at TIMESTAMP NOT NULL DEFAULT NOW(),
    CONSTRAINT fk_user_lessons_user
        FOREIGN KEY (user_id)
        REFERENCES users (id)
        ON DELETE CASCADE,
    CONSTRAINT fk_user_lessons_lesson
        FOREIGN KEY (lesson_id)
        REFERENCES lessons (id)
        ON DELETE CASCADE,
    CONSTRAINT uq_user_lessons_unique_completion UNIQUE (user_id, lesson_id)
);
COMMENT ON TABLE user_lessons IS 'Join table tracking lesson completion per user.';

CREATE INDEX idx_user_lessons_user_id ON user_lessons (user_id);
CREATE INDEX idx_user_lessons_lesson_id ON user_lessons (lesson_id);
CREATE INDEX idx_user_lessons_completed_at ON user_lessons (completed_at);
```

---

## PART 3: Flask Blueprint Architecture

### A) Application Factory Pattern
Use `create_app(config_class=DevelopmentConfig)` in `app/__init__.py`.

**Factory initialization sequence:**
1. Create Flask app instance.
2. Load config object from `config.py`.
3. Initialize extensions from `app/extensions.py`:
   - `db = SQLAlchemy()`
   - `migrate = Migrate()`
   - `login_manager = LoginManager()`
   - `csrf = CSRFProtect()`
   - `mail = Mail()`
4. Register model imports (if required by migration/autoload pattern).
5. Register blueprints with URL prefixes.
6. Configure login manager callbacks:
   - user loader for regular users/admins.
   - unauthorized redirect behavior.
7. Register error handlers (403/404/500).
8. Return configured app.

**Pattern skeleton (design-level):**
- `def create_app(config_class):`
  - `app = Flask(__name__, instance_relative_config=True)`
  - `app.config.from_object(config_class)`
  - `init_extensions(app)`
  - `register_blueprints(app)`
  - `register_error_handlers(app)`
  - `return app`

### B) Blueprint Definitions

| Blueprint | URL Prefix | Route | Method(s) | Purpose |
|---|---|---|---|---|
| `main_bp` | `/` | `/` | GET | Public landing page |
| `main_bp` | `/` | `/about` | GET | Platform overview |
| `main_bp` | `/` | `/contact` | GET/POST | Contact form/info page |
| `main_bp` | `/` | `/privacy` | GET | Privacy policy |
| `auth_bp` | `/auth` | `/register` | GET/POST | User registration |
| `auth_bp` | `/auth` | `/login` | GET/POST | User login |
| `auth_bp` | `/auth` | `/logout` | POST | User logout |
| `auth_bp` | `/auth` | `/reset/request` | GET/POST | Start reset flow |
| `auth_bp` | `/auth` | `/reset/security-question` | GET/POST | Security question verification |
| `auth_bp` | `/auth` | `/reset/token/<token>` | GET/POST | Token verification/reset entry |
| `auth_bp` | `/auth` | `/reset/password` | GET/POST | Set new password |
| `auth_bp` | `/auth` | `/admin/register` | GET/POST | Admin registration |
| `auth_bp` | `/auth` | `/admin/login` | GET/POST | Admin login |
| `auth_bp` | `/auth` | `/admin/logout` | POST | Admin logout |
| `dashboard_bp` | `/dashboard` | `/` | GET | User dashboard summary |
| `dashboard_bp` | `/dashboard` | `/progress` | GET | Detailed progress analytics |
| `dashboard_bp` | `/dashboard` | `/activity` | GET | User activity history |
| `lessons_bp` | `/lessons` | `/` | GET | Lessons list by category |
| `lessons_bp` | `/lessons` | `/<int:lesson_id>` | GET | Lesson detail view |
| `lessons_bp` | `/lessons` | `/<int:lesson_id>/complete` | POST | Mark lesson complete |
| `quizzes_bp` | `/quizzes` | `/` | GET | Quiz catalog |
| `quizzes_bp` | `/quizzes` | `/<int:quiz_id>/start` | GET/POST | Start quiz attempt |
| `quizzes_bp` | `/quizzes` | `/<int:quiz_id>/take` | GET | Quiz question interface |
| `quizzes_bp` | `/quizzes` | `/<int:quiz_id>/submit` | POST | Submit answers |
| `quizzes_bp` | `/quizzes` | `/results/<int:result_id>` | GET | Quiz result page |
| `quizzes_bp` | `/quizzes` | `/history` | GET | User quiz attempt history |
| `phishing_bp` | `/phishing` | `/` | GET | Phishing module home |
| `phishing_bp` | `/phishing` | `/example/<int:example_id>` | GET | Show simulation sample |
| `phishing_bp` | `/phishing` | `/example/<int:example_id>/submit` | POST | Submit suspicious findings |
| `phishing_bp` | `/phishing` | `/feedback/<int:activity_id>` | GET | Show simulation feedback |
| `phishing_bp` | `/phishing` | `/history` | GET | User simulation history |
| `admin_bp` | `/admin` | `/` | GET | Admin dashboard |
| `admin_bp` | `/admin` | `/users` | GET | Manage/view users |
| `admin_bp` | `/admin` | `/users/<int:user_id>` | GET | User detail |
| `admin_bp` | `/admin` | `/users/<int:user_id>/deactivate` | POST | Deactivate user |
| `admin_bp` | `/admin` | `/lessons` | GET | Manage lessons list |
| `admin_bp` | `/admin` | `/lessons/new` | GET/POST | Add lesson |
| `admin_bp` | `/admin` | `/lessons/<int:lesson_id>/edit` | GET/POST | Edit lesson |
| `admin_bp` | `/admin` | `/lessons/<int:lesson_id>/delete` | POST | Delete lesson |
| `admin_bp` | `/admin` | `/quizzes` | GET | Manage quizzes |
| `admin_bp` | `/admin` | `/quizzes/new` | GET/POST | Create quiz |
| `admin_bp` | `/admin` | `/quizzes/<int:quiz_id>/edit` | GET/POST | Edit quiz metadata |
| `admin_bp` | `/admin` | `/quizzes/<int:quiz_id>/delete` | POST | Delete quiz |
| `admin_bp` | `/admin` | `/quizzes/<int:quiz_id>/questions` | GET | Manage quiz questions |
| `admin_bp` | `/admin` | `/quizzes/<int:quiz_id>/questions/new` | GET/POST | Add question |
| `admin_bp` | `/admin` | `/questions/<int:question_id>/edit` | GET/POST | Edit question |
| `admin_bp` | `/admin` | `/questions/<int:question_id>/delete` | POST | Delete question |
| `admin_bp` | `/admin` | `/phishing-examples` | GET | Manage phishing examples |
| `admin_bp` | `/admin` | `/phishing-examples/new` | GET/POST | Add phishing example |
| `admin_bp` | `/admin` | `/phishing-examples/<int:example_id>/edit` | GET/POST | Edit phishing example |
| `admin_bp` | `/admin` | `/phishing-examples/<int:example_id>/delete` | POST | Delete phishing example |
| `admin_bp` | `/admin` | `/reports` | GET | Reports overview |
| `admin_bp` | `/admin` | `/reports/user-progress` | GET | User progress report |
| `admin_bp` | `/admin` | `/reports/quiz-results` | GET | Quiz outcomes report |

### C) Models Architecture

| Model File | Model Name | Table | Relationships | Suggested Helper Methods |
|---|---|---|---|---|
| `models/admin.py` | `Admin` | `admins` | 1-to-many with `lessons`, `quizzes`, `phishing_examples`, `activities` | `set_password()`, `check_password()`, `is_active_admin()` |
| `models/user.py` | `User` | `users` | 1-to-many with `quiz_results`, `activities`; many-to-many with `lessons` via `user_lessons` | `set_password()`, `check_password()`, `calculate_progress_percent()` |
| `models/lesson.py` | `Lesson` | `lessons` | many-to-1 `admins`; many-to-many `users` via `user_lessons` | `is_completed_by(user_id)` |
| `models/quiz.py` | `Quiz` | `quizzes` | many-to-1 `admins`; 1-to-many `quiz_questions`, `quiz_results` | `total_questions()`, `pass_mark()` |
| `models/quiz_question.py` | `QuizQuestion` | `quiz_questions` | many-to-1 `quizzes` | `is_correct(option)` |
| `models/quiz_result.py` | `QuizResult` | `quiz_results` | many-to-1 `users`; many-to-1 `quizzes` | `calculate_passed()`, `duration_display()` |
| `models/phishing_example.py` | `PhishingExample` | `phishing_examples` | many-to-1 `admins` | `evaluate_submission(payload)` |
| `models/activity.py` | `Activity` | `activities` | many-to-1 `users`; many-to-1 `admins` | `log_event()`, `to_feed_item()` |
| `models/user_lesson.py` | `UserLesson` | `user_lessons` | many-to-1 `users`; many-to-1 `lessons` | `mark_complete(user_id, lesson_id)` |

### D) Configuration Structure (`config.py`)

**Classes:**
- `BaseConfig`: shared defaults.
- `DevelopmentConfig(BaseConfig)`: local dev configuration.
- (Optional next phases: `TestingConfig`, `ProductionConfig`).

**DevelopmentConfig settings and purpose:**
- `SECRET_KEY`: session signing and CSRF token signing.
- `SQLALCHEMY_DATABASE_URI`: PostgreSQL connection URL.
- `SQLALCHEMY_TRACK_MODIFICATIONS`: disable overhead event system.
- `WTF_CSRF_ENABLED`: enable CSRF protection globally.
- `SESSION_COOKIE_HTTPONLY`: prevent JS access to session cookie.
- `SESSION_COOKIE_SECURE`: secure-only in HTTPS environments.
- `SESSION_COOKIE_SAMESITE`: CSRF mitigation on cross-site requests.
- `REMEMBER_COOKIE_HTTPONLY`, `REMEMBER_COOKIE_SECURE`: Flask-Login remember-cookie hardening.
- `MAIL_SERVER`, `MAIL_PORT`, `MAIL_USERNAME`, `MAIL_PASSWORD`: password reset email transport.
- `MAIL_USE_TLS`, `MAIL_USE_SSL`: email channel security.
- `PASSWORD_RESET_TOKEN_EXPIRES_MINUTES`: reset token TTL.
- `PERMANENT_SESSION_LIFETIME`: session expiration policy.

**Environment variables read from `.env`:**
- `FLASK_ENV`
- `SECRET_KEY`
- `DATABASE_URL`
- `SQLALCHEMY_TRACK_MODIFICATIONS`
- `WTF_CSRF_ENABLED`
- `SESSION_COOKIE_SECURE`
- `SESSION_COOKIE_HTTPONLY`
- `SESSION_COOKIE_SAMESITE`
- `MAIL_SERVER`
- `MAIL_PORT`
- `MAIL_USERNAME`
- `MAIL_PASSWORD`
- `MAIL_USE_TLS`
- `MAIL_USE_SSL`
- `PASSWORD_RESET_TOKEN_EXPIRES_MINUTES`

### E) Security Architecture

1. **Password hashing**
   - Library: `Werkzeug.security`.
   - Functions: `generate_password_hash()` and `check_password_hash()`.
   - Design: Hash passwords at registration/reset; verify only via hash comparison during login.

2. **Session management (Flask-Login)**
   - `LoginManager` initialized in app factory.
   - `@login_required` protects authenticated routes.
   - Separate user/admin session guards via custom decorators and role checks.
   - Session cookie hardening via config flags.

3. **Role separation (user vs admin)**
   - Add explicit role context in session or login manager identity handling.
   - `admin_required` decorator checks admin-authenticated identity before `/admin/*` access.
   - `user_required` decorator prevents admins from entering regular user dashboards/modules.

4. **CSRF protection**
   - Library: `Flask-WTF` (`CSRFProtect`).
   - All state-changing forms (POST/PUT/DELETE) include CSRF token.

5. **Input validation**
   - Library: `WTForms` + validators (`DataRequired`, `Email`, `Length`, `Regexp`, `AnyOf`).
   - Server-side validation mandatory for all forms.
   - Client-side validation used only as UX enhancement, not a trust boundary.

---

## PART 4: UI Page Map

| Page Name | Template Path | Blueprint | Displays | User Actions |
|---|---|---|---|---|
| Landing Page | `templates/main/index.html` | `main_bp` | Platform intro, CTA buttons | Navigate to register/login/about |
| About Page | `templates/main/about.html` | `main_bp` | Mission, learning approach | Return home, go to auth pages |
| Contact Page | `templates/main/contact.html` | `main_bp` | Contact form/info | Submit contact request |
| Privacy Page | `templates/main/privacy.html` | `main_bp` | Data/privacy notice | Read policies |
| User Register | `templates/auth/user_register.html` | `auth_bp` | User signup form | Create user account |
| User Login | `templates/auth/user_login.html` | `auth_bp` | User login form | Login as user |
| Reset Request | `templates/auth/user_reset_request.html` | `auth_bp` | Reset method selector | Start reset flow |
| Reset Security Question | `templates/auth/user_reset_security_question.html` | `auth_bp` | Security question prompt | Verify identity |
| Reset Token | `templates/auth/user_reset_token.html` | `auth_bp` | Token validation input | Validate token |
| Reset Password | `templates/auth/user_reset_password.html` | `auth_bp` | New password form | Save new password |
| Admin Register | `templates/auth/admin_register.html` | `auth_bp` | Admin signup form | Create admin account |
| Admin Login | `templates/auth/admin_login.html` | `auth_bp` | Admin login form | Login as admin |
| User Dashboard | `templates/dashboard/user_dashboard.html` | `dashboard_bp` | Progress cards, scores, recent activity | Go to lessons/quizzes/phishing |
| Progress Details | `templates/dashboard/progress_details.html` | `dashboard_bp` | Completion metrics/charts | Filter progress views |
| Activity History | `templates/dashboard/activity_history.html` | `dashboard_bp` | Timeline/table of events | Inspect past activity |
| Lessons List | `templates/lessons/lessons_list.html` | `lessons_bp` | Lessons grouped by category | Open lesson |
| Lesson Detail | `templates/lessons/lesson_detail.html` | `lessons_bp` | Lesson title/content/meta | Mark completed |
| Lesson Completion Confirm | `templates/lessons/lesson_complete_confirm.html` | `lessons_bp` | Completion confirmation | Return to dashboard/next lesson |
| Quiz List | `templates/quizzes/quiz_list.html` | `quizzes_bp` | Available quizzes | Start selected quiz |
| Quiz Start | `templates/quizzes/quiz_start.html` | `quizzes_bp` | Instructions, time limit | Begin attempt |
| Quiz Take | `templates/quizzes/quiz_take.html` | `quizzes_bp` | Questions + options + timer | Select answers, submit |
| Quiz Submit Confirm | `templates/quizzes/quiz_submit_confirm.html` | `quizzes_bp` | Submission confirmation | Confirm final submit |
| Quiz Result | `templates/quizzes/quiz_result.html` | `quizzes_bp` | Score, pass/fail, feedback | Retry another quiz |
| Quiz History | `templates/quizzes/quiz_history.html` | `quizzes_bp` | Past attempts table | View detailed result |
| Phishing Home | `templates/phishing/phishing_home.html` | `phishing_bp` | Simulation intro/types | Start simulation |
| Phishing Example View | `templates/phishing/phishing_example_view.html` | `phishing_bp` | Example content/email/site/login page | Identify suspicious elements |
| Phishing Submit | `templates/phishing/phishing_submit.html` | `phishing_bp` | Submission form/checklist | Submit findings |
| Phishing Feedback | `templates/phishing/phishing_feedback.html` | `phishing_bp` | Correct indicators + explanation | Continue to next simulation |
| Phishing History | `templates/phishing/phishing_history.html` | `phishing_bp` | Past simulation outcomes | Review learning history |
| Admin Dashboard | `templates/admin/admin_dashboard.html` | `admin_bp` | Admin KPIs and shortcuts | Navigate to management pages |
| Users List | `templates/admin/users_list.html` | `admin_bp` | User accounts table | View/deactivate account |
| User Detail | `templates/admin/user_detail.html` | `admin_bp` | User profile and activity summary | Deactivate/reactivate (future) |
| User Deactivate Confirm | `templates/admin/user_deactivate_confirm.html` | `admin_bp` | Confirmation dialogue | Confirm deactivation |
| Lessons Manage | `templates/admin/lessons_manage.html` | `admin_bp` | Lessons CRUD list | Add/edit/delete lesson |
| Lesson Form | `templates/admin/lesson_form.html` | `admin_bp` | Lesson create/edit form | Save lesson |
| Quizzes Manage | `templates/admin/quizzes_manage.html` | `admin_bp` | Quizzes CRUD list | Add/edit/delete quiz |
| Quiz Form | `templates/admin/quiz_form.html` | `admin_bp` | Quiz create/edit form | Save quiz metadata |
| Questions Manage | `templates/admin/questions_manage.html` | `admin_bp` | Question list for selected quiz | Add/edit/delete question |
| Question Form | `templates/admin/question_form.html` | `admin_bp` | Question create/edit form | Save question |
| Phishing Examples Manage | `templates/admin/phishing_examples_manage.html` | `admin_bp` | Simulation examples list | Add/edit/delete examples |
| Phishing Example Form | `templates/admin/phishing_example_form.html` | `admin_bp` | Example create/edit form | Save example |
| Reports Overview | `templates/admin/reports_overview.html` | `admin_bp` | Report navigation and high-level stats | Open detailed reports |
| User Progress Report | `templates/admin/reports_user_progress.html` | `admin_bp` | Progress by user/course metrics | Filter/export (future) |
| Quiz Results Report | `templates/admin/reports_quiz_results.html` | `admin_bp` | Quiz performance analytics | Filter by category/quiz |
| 403 Error | `templates/errors/403.html` | Global | Unauthorized access message | Return to safe route |
| 404 Error | `templates/errors/404.html` | Global | Not found message | Navigate back/home |
| 500 Error | `templates/errors/500.html` | Global | Server error fallback | Retry or go home |

---

## PART 5: Phase 3 Readiness Checklist

### 1) Python/Flask environment setup
- [ ] Install Python 3.11+ and pip.
- [ ] Create virtual environment: `python -m venv .venv`.
- [ ] Activate virtual environment.
- [ ] Install dependencies from `requirements.txt`.
- [ ] Verify Flask CLI availability and import health.

### 2) PostgreSQL database setup
- [ ] Install PostgreSQL locally.
- [ ] Create database user/role (e.g., `cyber_admin`) with password.
- [ ] Create database `cybershield_academy` owned by that role.
- [ ] Grant required privileges on database/schema.
- [ ] Validate connectivity with psql using `DATABASE_URL`.

### 3) `.env` configuration setup
- [ ] Create `.env` from `.env.example`.
- [ ] Set `SECRET_KEY` (random, long, unique).
- [ ] Set `DATABASE_URL` with local PostgreSQL credentials.
- [ ] Set cookie/security flags for development.
- [ ] Set mail settings for token-based reset testing.
- [ ] Confirm app loads all variables at startup.

### 4) Required package validation
- [ ] Flask
- [ ] Flask-SQLAlchemy
- [ ] Flask-Migrate
- [ ] Flask-Login
- [ ] Flask-WTF
- [ ] WTForms
- [ ] email-validator
- [ ] psycopg2-binary
- [ ] python-dotenv
- [ ] Werkzeug
- [ ] itsdangerous
- [ ] Flask-Mail
- [ ] gunicorn
- [ ] pytest / pytest-flask

### 5) Folder creation order (recommended)
1. [ ] Root files (`run.py`, `config.py`, `.env.example`, `requirements.txt`).
2. [ ] `app/` package and `extensions.py`.
3. [ ] `app/models/` files.
4. [ ] `app/blueprints/` module folders with `__init__.py`, `routes.py`, `forms.py`.
5. [ ] `templates/` structure by blueprint.
6. [ ] `static/` (`css`, `js`, `images`).
7. [ ] `migrations/` scaffold via Flask-Migrate.
8. [ ] `tests/` baseline suite.

### 6) Database migration readiness
- [ ] `flask db init` executed (if migrations folder not yet initialized).
- [ ] Initial models mapped to all 9 tables.
- [ ] `flask db migrate -m "initial schema"` generated.
- [ ] `flask db upgrade` applied successfully.
- [ ] Schema validated against Phase 2 SQL design.

### 7) Security readiness gates before coding business logic
- [ ] Password hashing standard selected and documented.
- [ ] Role-based decorators designed (`login_required`, `admin_required`, `user_required`).
- [ ] CSRF enabled globally.
- [ ] Form validation rules defined for all input points.
- [ ] Activity logging strategy defined for audit trails.

---

## Final Note
This Phase 2 System Design Document is intended to be the direct execution blueprint for Phase 3 development. It provides the exact structure, schema, routing contracts, and security posture needed for implementation without introducing business logic code at this stage.
