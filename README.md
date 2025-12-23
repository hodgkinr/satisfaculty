# Satisfaculty

A course scheduling optimization tool using integer linear programming.

## Installation

```bash
python3 -m venv venv
source venv/bin/activate
pip install -e .
```

## Usage

```python
from satisfaculty import InstructorScheduler, MinimizeClassesBefore

scheduler = InstructorScheduler()
scheduler.load_rooms('example/rooms.csv')
scheduler.load_courses('example/courses.csv')
scheduler.load_time_slots(`example/time_slots.csv')

objectives = [MinimizeClassesBefore("9:00")]
scheduler.lexicographic_optimize(objectives)
scheduler.visualize_schedule()
```

This will output a complete schedule:

![Example schedule output](docs/schedule_visual.png)

## Documentation

- [Objectives Guide](docs/OBJECTIVES_GUIDE.md)
