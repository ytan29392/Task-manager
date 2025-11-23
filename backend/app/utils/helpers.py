def calculate_task_progress(subtasks):
    """
    Progress = (completed subtasks / total subtasks) * 100
    """
    if not subtasks or len(subtasks) == 0:
        return 0
    
    completed = len([s for s in subtasks if s.status == "Done"])
    total = len(subtasks)

    return round((completed / total) * 100, 2)


def count_statuses(subtasks):
    summary = {
        "todo": 0,
        "in_progress": 0,
        "done": 0,
        "overdue": 0
    }
    for s in subtasks:
        if s.status == "To Do":
            summary["todo"] += 1
        elif s.status == "In Progress":
            summary["in_progress"] += 1
        elif s.status == "Done":
            summary["done"] += 1
        elif s.status == "Overdue":
            summary["overdue"] += 1

    return summary
