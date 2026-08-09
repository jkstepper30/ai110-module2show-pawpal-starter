# PawPal+ (Module 2 Project)

You are building **PawPal+**, a Streamlit app that helps a pet owner plan care tasks for their pet.

## Scenario

A busy pet owner needs help staying consistent with pet care. They want an assistant that can:

- Track pet care tasks (walks, feeding, meds, enrichment, grooming, etc.)
- Consider constraints (time available, priority, owner preferences)
- Produce a daily plan and explain why it chose that plan

Your job is to design the system first (UML), then implement the logic in Python, then connect it to the Streamlit UI.

## What you will build

Your final app should:

- Let a user enter basic owner + pet info
- Let a user add/edit tasks (duration + priority at minimum)
- Generate a daily schedule/plan based on constraints and priorities
- Display the plan clearly (and ideally explain the reasoning)
- Include tests for the most important scheduling behaviors

## Getting started

### Setup

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

### Suggested workflow

1. Read the scenario carefully and identify requirements and edge cases.
2. Draft a UML diagram (classes, attributes, methods, relationships).
3. Convert UML into Python class stubs (no logic yet).
4. Implement scheduling logic in small increments.
5. Add tests to verify key behaviors.
6. Connect your logic to the Streamlit UI in `app.py`.
7. Refine UML so it matches what you actually built.

## 🖥️ Sample Output

Paste a sample of your app's CLI or Streamlit output here so a reader can see what a generated plan looks like:

```
Today's Schedule
------------------
Time     Pet          Task                         Description                              Status
------------------------------------------------------------------------------------------------
08:00    Fido         Morning walk                 30 minute walk around the block          ⚠
12:30    Mittens      Litter box clean             Scoop and refresh litter                 ⚠
20:00    Fido         Evening meds                 Give prescribed medication

```

## 🧪 Testing PawPal+

```bash
# Run the full test suite:
pytest

# Run with coverage:
pytest --cov

#Run tests
python -m pytest

The test suite verifies core scheduler behavior: task lifecycle (completion and daily recurrence), pet-task associations, chronological sorting of scheduled tasks, and detection of scheduling conflicts.

```

Sample test output:

```
plugins: anyio-4.10.0
collected 5 items

tests\test_pawpal.py .....                                                                                                                                           [100%]

============================================================================ 5 passed in 0.05s ============================================================================
```

## 📐 Smarter Scheduling

> Fill in once you've implemented scheduling logic.


| Feature | Method(s) | Notes |
|---------|-----------|-------|
| Task sorting | `Scheduler.sort_by_time()`, `Scheduler.sort_by_priority()`, `Scheduler.sort_by_duration()` | e.g., by priority, duration; stable multi-key ordering (priority → duration → start time). |
| Filtering | `Scheduler.filter_by_pet(pet_id)`, `Scheduler.filter_by_completion_status(completed=False)`, `Scheduler.skip_if_time_insufficient(available_time)` | e.g., skip tasks if time runs out; filters applied before scheduling to skip or deprioritize tasks. |
| Conflict handling | `Scheduler.find_conflicts()`, `Scheduler.mark_conflicts()`, `Scheduler.resolve_conflicts(strategy='shift'|'skip'|'alert')` | e.g., overlapping time slots; detects overlaps and resolves by shifting, skipping, or alerting. |
| Recurring tasks | `Recurrence.expand(task)`, `Scheduler.apply_recurring_rule(task, rule)` | e.g., daily vs. weekly; expands recurrence rules into concrete instances and supports exceptions/end dates. 
## 📸 Demo Walkthrough

Describe your app in numbered steps so a reader can follow along without watching a video:

1.	Create an Owner.
•	Action: call Owner(id, name, ...).
•	What to look for: owner object created to hold pets and receive notifications.
2.	Add one or more Pets.
•	Action: owner.create_pet(name, species, ...).
•	What to look for: pet ids auto-generated and owner_id set on each Pet.
3.	Create Tasks and attach them to pets.
•	Action: Task(...); pet.add_task(task).
•	What to look for: task.pet_id and task.owner_id populated; duplicate task ids are replaced.
4.	Schedule a Task for a specific datetime.
•	Action: sched.schedule_task(task, when).
•	What to look for: task.due_date set; schedule_task returns a warning string only if there’s a conflict.
5.	Intentionally create a conflict to show a warning.
•	Action: schedule two different tasks at the exact same datetime.
•	What to look for: schedule_task returns a human-readable conflict warning (non-blocking).
6.	View “Today’s Schedule.”
•	Action: filter sched.all_tasks for due_date.date() == today and sort by due_date.
•	What to look for: tasks printed chronologically (sorting by time).
7.	Snooze or reschedule a Task.
•	Action: task.snooze(timedelta(...)) or sched.reschedule_task(task_id, new_when).
•	What to look for: due_date moves forward; reschedule returns conflict warning if applicable.
8.	Mark a recurring Task complete to advance it.
•	Action: task.mark_complete() on a task with frequency and due_date.
•	What to look for: due_date advanced to next occurrence and task reopened for the next cycle.
9.	Check overdue detection and status.
•	Action: call task.is_overdue() for tasks with past due_date.
•	What to look for: True if past due and not completed; comparisons preserve tzinfo when present.
10.	Remove tasks or pets
•	Action: pet.remove_task(task_id) or owner.remove_pet(pet_id).
•	What to look for: item removed if present; no error if id not found.
**Screenshot or video** *(optional)*: <!-- Insert a screenshot or link to a demo video here -->
