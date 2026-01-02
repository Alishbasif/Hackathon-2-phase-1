# Tasks: Phase 1 - Todo Application

**Input**: Design documents from `specs/001-phase-1-todo-spec/`
**Prerequisites**: plan.md, spec.md, data-model.md

---

## Phase 1: Setup (Shared Infrastructure)

- [X] T001 Create project structure: `src/` and `tests/` directories.
- [X] T002 [P] Create empty Python files: `src/models.py`, `src/app.py`, `src/main.py`.
- [X] T003 [P] Create empty test file: `tests/test_app.py`.
- [X] T004 Configure `pytest` in a `pyproject.toml` file.

---

## Phase 2: Foundational (Blocking Prerequisites)

- [X] T005 [US1] Generate code for the `Task` data class in `src/models.py` based on `data-model.md`.
- [X] T006 [US1] Generate code for a test case in `tests/test_app.py` to verify the creation of a `Task` object.
- [X] T007 [US1] Generate code for the basic application structure in `src/app.py`, including the in-memory task list.
- [X] T008 [US1] Generate code for a test case in `tests/test_app.py` to verify the initial state of the application.

---

## Phase 3: User Story 1 - Add a new task

**Goal**: Allow a user to add a new task to the list.
**Independent Test**: A new task can be added and it appears in the task list.

### Tests for User Story 1
- [X] T009 [US1] Generate code for a test case in `tests/test_app.py` for successfully adding a task.
- [X] T010 [US1] Generate code for a test case in `tests/test_app.py` for adding a task with an empty description, expecting an error.

### Code Generation for User Story 1
- [X] T011 [US1] Generate code for the `add_task` function in `src/app.py`.
- [X] T012 [US1] Generate code for the user input handling for adding a task in `src/main.py`.

---

## Phase 4: User Story 2 - View all tasks

**Goal**: Allow a user to see all the tasks.
**Independent Test**: All added tasks are displayed correctly.

### Tests for User Story 2
- [X] T013 [US2] Generate code for a test case in `tests/test_app.py` for viewing multiple tasks.
- [X] T014 [US2] Generate code for a test case in `tests/test_app.py` for viewing an empty list of tasks.

### Code Generation for User Story 2
- [X] T015 [US2] Generate code for the `get_all_tasks` function in `src/app.py`.
- [X] T016 [US2] Generate code for the task display logic in `src/main.py`.

---

## Phase 5: User Story 3 - Update a task

**Goal**: Allow a user to update an existing task's description.
**Independent Test**: A task's description can be changed and is reflected in the task list.

### Tests for User Story 3
- [X] T017 [US3] Generate code for a test case in `tests/test_app.py` for successfully updating a task.
- [X] T018 [US3] Generate code for a test case in `tests/test_app.py` for updating a non-existent task, expecting an error.

### Code Generation for User Story 3
- [X] T019 [US3] Generate code for the `update_task` function in `src/app.py`.
- [X] T020 [US3] Generate code for the user input handling for updating a task in `src/main.py`.

---

## Phase 6: User Story 4 - Mark a task as complete

**Goal**: Allow a user to mark a task as completed.
**Independent Test**: A task's status can be changed to complete.

### Tests for User Story 4
- [X] T021 [US4] Generate code for a test case in `tests/test_app.py` for marking a task as complete.
- [X] T022 [US4] Generate code for a test case in `tests/test_app.py` for marking a non-existent task, expecting an error.

### Code Generation for User Story 4
- [X] T023 [US4] Generate code for the `mark_task_complete` function in `src/app.py`.
- [X] T024 [US4] Generate code for the user input handling for marking a task as complete in `src/main.py`.

---

## Phase 7: User Story 5 - Delete a task

**Goal**: Allow a user to delete a task.
**Independent Test**: A task can be removed from the list.

### Tests for User Story 5
- [X] T025 [US5] Generate code for a test case in `tests/test_app.py` for successfully deleting a task.
- [X] T026 [US5] Generate code for a test case in `tests/test_app.py` for deleting a non-existent task, expecting an error.

### Code Generation for User Story 5
- [X] T027 [US5] Generate code for the `delete_task` function in `src/app.py`.
- [X] T028 [US5] Generate code for the user input handling for deleting a task in `src/main.py`.

---

## Phase 8: Polish & Cross-Cutting Concerns

- [X] T029 Generate code for the main application loop and user menu in `src/main.py`.
- [X] T030 Generate code for robust error handling for user input (e.g., non-numeric IDs for update/delete actions) in `src/main.py`.
- [X] T031 Perform a final review of all generated code to ensure it aligns with the specification and constitution.
- [X] T032 Run all tests in `tests/test_app.py` and ensure they pass.

---

## Dependencies & Execution Order

- **Phase 1 (Setup)** must be completed first.
- **Phase 2 (Foundational)** depends on Phase 1.
- **User Story Phases (3-7)** depend on Phase 2. They can be implemented in any order but are presented here by priority.
- **Phase 8 (Polish)** depends on all user story phases being complete.
