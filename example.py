#!/usr/bin/env python3
"""
Example script demonstrating lexicographic optimization.

This shows how to define custom objective priorities for schedule optimization.
Each user can create their own script with different objective orderings.
"""

from satisfaculty import (
    InstructorScheduler,
    MinimizeClassesBefore,
    MinimizeClassesAfter,
    MaximizePreferredRooms,
)

scheduler = InstructorScheduler()
scheduler.load_rooms('input/rooms.csv')
scheduler.load_courses('input/courses.csv')
scheduler.load_time_slots('input/time_slots.csv')

objectives = [
    MinimizeClassesBefore('9:00'),
]

scheduler.lexicographic_optimize(objectives)
scheduler.save_schedule('output/schedule.csv')
scheduler.visualize_schedule('output/schedule_visual.png')
