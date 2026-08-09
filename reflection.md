# PawPal+ Project Reflection

## 1. System Design

User should be able to:
- add a pet
- schedule a walk
- track pet care tasks

 Classes I chose and their responsibilities:
 
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

Tradeoff: lightweight conflict detection only compares exact equality of task.due_date (i.e., two tasks conflict if their due_date datetimes are identical). This keeps the data model (single due_date per task) and checks very simple and fast, but it will not detect real-world overlaps when tasks have durations or flexible windows (for example, a 1-hour grooming at 10:00 will not be flagged as conflicting with a 10:30 vaccination). To detect those overlaps you must extend Task to include start/end or duration and replace the equality check with an interval-overlap test (interval tree or O(n log n) sweep), which increases model complexity and runtime/space cost for large schedules.

Why this is reasonable: the current Task model intentionally tracks a single due_date and no duration, so exact-match detection is a cheap and predictable heuristic that suits lightweight reminder workflows and small datasets. Detecting real interval overlaps requires extending Task with start/end or duration fields and using interval-overlap algorithms (interval trees or sweep algorithms), which increases implementation complexity and runtime/space cost. Keep the simpler approach until the application needs true interval scheduling.

---

## 3. AI Collaboration

**a. How you used AI**

I use the AI tools during this project for design brainstorming, debugging and overall understand what the app was supposed to do and how I can make any adjustments. 

**b. Judgment and verification**

•	The AI suggested replacing an explicit null/validation check with a one-line helper that returned a default object. I rejected it because it hid an important validation path and could mask upstream errors.

---

## 4. Testing and Verification

**a. What you tested**

Behaviors tested:
•	Correctness of return values for normal inputs and edge cases (null/empty/invalid).
•	Error handling and propagation (exceptions vs. silent defaults).
•	Integration with callers: that downstream code still receives expected values and error signals.

Why these tests were important:
•	To ensure functional correctness and avoid regressions.
•	To preserve observable error handling and debugging information.
•	To prevent introducing subtle bugs (hidden defaults, state changes) that unit tests or review would otherwise miss.

**b. Confidence**

I am confident that my scheduler works correctly.

Some edge cases I would test next would be: 

Input variability
•	null/undefined and partially populated objects (missing fields)
•	wrong types (strings instead of numbers, arrays instead of objects)

Resource and performance limits
•	low-memory conditions, large allocations, GC pressure
•	throughput/latency under load and backpressure behavior


---

## 5. Reflection

**a. What went well**

I am most satisfied with the process of working on the app and being able to understand everything.

**b. What you would improve**

- If I had another iteration, I would include more Ai features and make it more detailed and most likely implement RAG with it. 

**c. Key takeaway**

One key takeaway I had was to keep a human-in-the-loop by designing clear contracts and automated tests so AI suggestions are always validated before merging.
