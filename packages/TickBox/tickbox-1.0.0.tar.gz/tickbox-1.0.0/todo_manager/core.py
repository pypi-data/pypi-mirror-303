from datetime import datetime
from .data_handler import load_tasks, save_tasks, get_task_by_id
from rich.console import Console
from rich.table import Table


class TaskManager:
    def __init__(self):
        # Load tasks from storage
        self.tasks = load_tasks()
        self.next_id = self.get_next_id()

    def get_next_id(self):
        # Get the next available task ID (incremental)
        if self.tasks:
            return max(int(task['id']) for task in self.tasks) + 1
        return 1

    def add_task(self, description, due_date=None, priority='Medium', tags=None):
        tags = tags or []
        task = {
            'id': str(self.next_id),  # Incremental ID
            'description': description,
            'due_date': due_date,
            'priority': priority,
            'tags': tags,
            'completed': False,
            'created_at': datetime.now().isoformat(),
            'updated_at': datetime.now().isoformat()
        }
        self.tasks.append(task)
        self.next_id += 1
        self.save_tasks()
        print(f'Task added with ID: {task["id"]}')

    def list_tasks(self, filter_by_status=None, sort_by=None):
        console = Console()
        console.print("[bold yellow]Debug: Using rich to display tasks[/]")
        # Filtering tasks
        tasks = self.tasks
        if filter_by_status:
            tasks = [
                task for task in tasks if 
                (task['completed'] and filter_by_status == 'done') or 
                (not task['completed'] and filter_by_status == 'pending')
            ]

        # Sorting tasks
        if sort_by == 'due_date':
            tasks = sorted(tasks, key=lambda t: t['due_date'] or '9999-12-31')
        elif sort_by == 'priority':
            priority_map = {'High': 1, 'Medium': 2, 'Low': 3}
            tasks = sorted(tasks, key=lambda t: priority_map.get(t['priority'], 4))

        # Display tasks in a table
        table = Table(title="[bold magenta]To-Do List[/]")
        table.add_column("ID", style="cyan", no_wrap=True)
        table.add_column("Description", style="magenta")
        table.add_column("Due Date", style="green")
        table.add_column("Priority", style="yellow")
        table.add_column("Status", style="bold blue")

        if not tasks:
            console.print("[bold red]No tasks available.[/]")
            return

        for task in tasks:
            status = "[bold green]✓[/]" if task['completed'] else "[bold red]✗[/]"
            priority_color = {
                'High': '[bold red]High[/]',
                'Medium': '[bold yellow]Medium[/]',
                'Low': '[bold green]Low[/]'
            }.get(task['priority'], '[bold white]Unknown[/]')

            table.add_row(
                task['id'],
                task['description'],
                task.get('due_date', '[bold red]N/A[/]'),
                priority_color,
                status
            )

        console.print(table)

    def delete_task(self, task_id):
        # Remove the specified task
        self.tasks = [task for task in self.tasks if task['id'] != task_id]
        self.save_tasks()
        print(f"Task {task_id} deleted.")

    def mark_task_status(self, task_id, status):
        task = get_task_by_id(task_id, self.tasks)
        if task:
            task['completed'] = status
            task['updated_at'] = datetime.now().isoformat()
            self.save_tasks()
            status_text = 'done' if status else 'pending'
            print(f"Task {task_id} marked as {status_text}.")
        else:
            print(f"Task {task_id} not found.")

    def edit_task(self, task_id, description=None, due_date=None, priority=None, tags=None):
        task = get_task_by_id(task_id, self.tasks)
        if task:
            if description:
                task['description'] = description
            if due_date:
                task['due_date'] = due_date
            if priority:
                task['priority'] = priority
            if tags:
                task['tags'] = tags
            task['updated_at'] = datetime.now().isoformat()
            self.save_tasks()
            print(f"Task {task_id} updated.")
        else:
            print(f"Task {task_id} not found.")

    def save_tasks(self):
        # Save the current state of tasks
        save_tasks(self.tasks)
