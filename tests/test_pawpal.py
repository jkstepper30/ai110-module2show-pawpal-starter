import pytest
from datetime import datetime, time, timedelta

from pawpal_system import Task, Pet, Owner, Scheduler


def test_task_completion_marks_completed():
	"""Task Completion: calling mark_complete() should set completed to True."""
	t = Task(id=1, title="Give treat")
	assert not t.completed
	t.mark_complete()
	assert t.completed is True


def test_adding_task_increases_pet_task_count():
	"""Task Addition: adding a task to a Pet increases that pet's tasks length."""
	owner = Owner(id=1, name="Buddy Owner")
	pet = owner.create_pet(name="Buddy")
	initial_count = len(pet.get_tasks())
	task = Task(id=2, title="Playtime")
	pet.add_task(task)
	assert len(pet.get_tasks()) == initial_count + 1


def _today_datetime(hour: int, minute: int = 0) -> datetime:
	today = datetime.now().date()
	return datetime.combine(today, time(hour=hour, minute=minute))


def test_sorting_correctness_returns_chronological_order():
	"""Sorting Correctness: verify tasks are returned in chronological order."""
	owner = Owner(id=10, name="Sorter")
	pet = owner.create_pet(name="Sorty")
	sched = Scheduler()
	sched.register_owner(owner)

	# create tasks and add them to the pet
	t1 = Task(id=101, title="Morning walk")
	t2 = Task(id=102, title="Noon check")
	t3 = Task(id=103, title="Evening meds")
	pet.add_task(t1)
	pet.add_task(t2)
	pet.add_task(t3)

	# schedule out-of-order
	sched.schedule_task(t2, _today_datetime(12, 30))
	sched.schedule_task(t3, _today_datetime(20, 0))
	sched.schedule_task(t1, _today_datetime(8, 0))

	sorted_tasks = sched.sort_by_time(owner_id=owner.id, by_full_datetime=True)
	sorted_ids = [t.id for t in sorted_tasks if t.due_date is not None]
	assert sorted_ids == [101, 102, 103]


def test_recurrence_logic_daily_creates_next_day_task():
	"""Recurrence Logic: marking a daily task complete creates a new task for the following day."""
	owner = Owner(id=20, name="Recurrer")
	pet = owner.create_pet(name="RecurPet")
	sched = Scheduler()
	sched.register_owner(owner)

	due = _today_datetime(9, 0)
	t = Task(id=201, title="Daily Meds", frequency="daily")
	pet.add_task(t)
	sched.schedule_task(t, due)

	new_task = sched.complete_task(t.id)

	# original is marked completed
	assert any(tt.id == 201 and tt.completed for tt in sched.all_tasks)
	# a new task was created for the next day
	assert new_task is not None
	assert new_task.due_date == due + timedelta(days=1)
	assert new_task.completed is False
	# new task attached to pet
	assert any(tt.id == new_task.id for tt in pet.get_tasks())


def test_conflict_detection_flags_duplicate_times():
	"""Conflict Detection: verify that the Scheduler flags duplicate times."""
	owner = Owner(id=30, name="Conflicter")
	pet = owner.create_pet(name="ConflictPet")
	sched = Scheduler()
	sched.register_owner(owner)

	when = _today_datetime(15, 0)
	a = Task(id=301, title="Task A")
	b = Task(id=302, title="Task B")
	pet.add_task(a)
	pet.add_task(b)

	warn1 = sched.schedule_task(a, when)
	warn2 = sched.schedule_task(b, when)

	assert warn1 is None
	assert warn2 is not None
	assert "conflict" in warn2.lower() or "conflicts" in warn2.lower()
