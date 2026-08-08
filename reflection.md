# PawPal+ Project Reflection

## 1. System Design

User should be able to:
- add a pet
- schedule a walk
- track pet care tasks


* Classes I chose and their responsibilities:
  •	Task: models a single care item (title, optional description, schedule, completion state) and should encapsulate behavior for completing, snoozing, and overdue checks.
  
•	Pet: models an owned animal and is responsible for owning/organizing its Task objects (add/remove/query).

•	Owner: models the human owner and is responsible for creating/removing pets, returning their pets, and receiving notifications.

•	Scheduler: global coordinator for scheduling, rescheduling, cancelling, querying, and sending reminders for tasks across owners/pets.


**b. Design changes**

Summary of Changes made: 
•	Implemented Task methods to handle completion, snoozing, and overdue detection so tasks can be used in workflows and unit-tested.

•	mark_complete: Needed to support recurring tasks and to advance a task to its next occurrence when completed. This prevents lost or duplicate occurrences and models real-world recurring care (e.g., daily medication).

•	snooze: Adds safe postponement behavior with validation (cannot snooze completed tasks or tasks with no due date, and duration must be positive). Prevents accidental regressions of due_date.

•	is_overdue: Provides a reliable way to determine if a pending task is past due. Uses the due_date time-zone when present to avoid incorrect comparisons across tz-aware datetimes.

---

## 2. Scheduling Logic and Tradeoffs

**a. Constraints and priorities**

- What constraints does your scheduler consider (for example: time, priority, preferences)?
- How did you decide which constraints mattered most?

**b. Tradeoffs**

- Describe one tradeoff your scheduler makes.
- Why is that tradeoff reasonable for this scenario?

---

## 3. AI Collaboration

**a. How you used AI**

- How did you use AI tools during this project (for example: design brainstorming, debugging, refactoring)?
- What kinds of prompts or questions were most helpful?

**b. Judgment and verification**

- Describe one moment where you did not accept an AI suggestion as-is.
- How did you evaluate or verify what the AI suggested?

---

## 4. Testing and Verification

**a. What you tested**

- What behaviors did you test?
- Why were these tests important?

**b. Confidence**

- How confident are you that your scheduler works correctly?
- What edge cases would you test next if you had more time?

---

## 5. Reflection

**a. What went well**

- What part of this project are you most satisfied with?

**b. What you would improve**

- If you had another iteration, what would you improve or redesign?

**c. Key takeaway**

- What is one important thing you learned about designing systems or working with AI on this project?
