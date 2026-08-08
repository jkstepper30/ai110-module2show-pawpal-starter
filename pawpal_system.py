from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, timedelta
from typing import List, Optional


@dataclass
class Task:
	"""Represents a care task for a pet."""

	id: int
	title: str
	description: Optional[str] = None
	frequency: Optional[str] = None  # e.g. "daily", "weekly"
	due_date: Optional[datetime] = None
	completed: bool = False
	pet_id: Optional[int] = None
	owner_id: Optional[int] = None

	def mark_complete(self) -> None:
		"""Mark the task as completed."""
		raise NotImplementedError

	def snooze(self, duration: timedelta) -> None:
		"""Postpone the due_date by the given duration."""
		raise NotImplementedError

	def is_overdue(self) -> bool:
		"""Return True if the task is past due and not completed."""
		raise NotImplementedError


@dataclass
class Pet:
	"""Represents a pet owned by an Owner."""

	id: int
	name: str
	species: Optional[str] = None
	breed: Optional[str] = None
	age: Optional[int] = None
	owner_id: Optional[int] = None
	tasks: List[Task] = field(default_factory=list)

	def add_task(self, task: Task) -> None:
		"""Attach a Task to this pet."""
		raise NotImplementedError

	def remove_task(self, task_id: int) -> None:
		"""Remove a task from this pet by id."""
		raise NotImplementedError

	def get_tasks(self) -> List[Task]:
		"""Return tasks assigned to this pet."""
		raise NotImplementedError


class Owner:
	"""Represents an owner of one or more pets."""

	def __init__(
		self,
		id: int,
		name: str,
		email: Optional[str] = None,
		phone: Optional[str] = None,
		pets: Optional[List[Pet]] = None,
	) -> None:
		self.id = id
		self.name = name
		self.email = email
		self.phone = phone
		self.pets: List[Pet] = pets or []

	def create_pet(self, name: str, species: Optional[str] = None, breed: Optional[str] = None, age: Optional[int] = None) -> Pet:
		"""Create and attach a new Pet to this owner."""
		raise NotImplementedError

	def remove_pet(self, pet_id: int) -> None:
		"""Remove a pet by id."""
		raise NotImplementedError

	def get_pets(self) -> List[Pet]:
		"""Return all pets owned by this owner."""
		raise NotImplementedError

	def notify(self, message: str) -> None:
		"""Send a notification to the owner (placeholder)."""
		raise NotImplementedError


class Scheduler:
	"""Responsible for scheduling and managing tasks across owners and pets."""

	def __init__(self) -> None:
		self.all_tasks: List[Task] = []

	def schedule_task(self, task: Task, when: datetime) -> None:
		"""Schedule a task at a specific datetime."""
		raise NotImplementedError

	def reschedule_task(self, task_id: int, when: datetime) -> None:
		"""Change the scheduled time for a task."""
		raise NotImplementedError

	def cancel_task(self, task_id: int) -> None:
		"""Cancel a scheduled task."""
		raise NotImplementedError

	def get_upcoming_tasks(self, owner_id: int, days: int = 7) -> List[Task]:
		"""Return tasks for an owner in the next `days` days."""
		raise NotImplementedError

	def send_reminders(self) -> None:
		"""Process tasks and send reminders to owners for upcoming/overdue tasks."""
		raise NotImplementedError
