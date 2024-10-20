import click
from .core import TaskManager

task_manager = TaskManager()

@click.group()
def cli():
    """To-Do List Manager"""
    pass

@cli.command()
@click.argument('description')
@click.option('--due_date', help='Due date in YYYY-MM-DD format')
@click.option('--priority', default='Medium', help='Task priority (Low, Medium, High)')
@click.option('--tags', help='Comma-separated tags for the task')
def add(description, due_date, priority, tags):
    """Add a new task"""
    tag_list = tags.split(',') if tags else []
    task_manager.add_task(description, due_date, priority, tag_list)

@cli.command()
@click.option('--status', help='Filter tasks by status (pending, done)')
@click.option('--sort', help='Sort tasks by due_date or priority')
def list(status, sort):
    """List all tasks"""
    print("Debug: 'list' command invoked")  # Add this line
    task_manager.list_tasks(filter_by_status=status, sort_by=sort)

@cli.command()
@click.argument('task_id')
def done(task_id):
    """Mark a task as done"""
    task_manager.mark_task_status(task_id, True)

@cli.command()
@click.argument('task_id')
def pending(task_id):
    """Mark a task as pending"""
    task_manager.mark_task_status(task_id, False)

@cli.command()
@click.argument('task_id')
def delete(task_id):
    """Delete a task"""
    task_manager.delete_task(task_id)

@cli.command()
@click.argument('task_id')
@click.option('--description', help='New task description')
@click.option('--due_date', help='New due date in YYYY-MM-DD format')
@click.option('--priority', help='New priority (Low, Medium, High)')
@click.option('--tags', help='Comma-separated tags for the task')
def edit(task_id, description, due_date, priority, tags):
    """Edit an existing task"""
    tag_list = tags.split(',') if tags else None
    task_manager.edit_task(task_id, description, due_date, priority, tag_list)



@cli.command()
def select_task():
    """Select a task interactively for editing, deleting, or marking as done."""
    tasks = task_manager.tasks
    if not tasks:
        print("No tasks available.")
        return

    # Display the list of tasks for selection
    click.echo("Available Tasks:")
    for task in tasks:
        status = "✓" if task['completed'] else "✗"
        click.echo(f"[{task['id']}] {task['description']} (Due: {task.get('due_date', 'N/A')}, Status: {status})")

    # Prompt user to select a task by ID
    task_id = click.prompt("Enter the task ID", type=str)

    # Perform actions based on the user's choice
    action = click.prompt("Choose an action (edit, delete, mark done, mark pending)", type=str)

    if action.lower() == "edit":
        description = click.prompt("New description (leave empty to keep current)", default="")
        due_date = click.prompt("New due date (leave empty to keep current)", default="")
        priority = click.prompt("New priority (leave empty to keep current)", default="")
        tags = click.prompt("New tags (comma-separated, leave empty to keep current)", default="")
        task_manager.edit_task(task_id, description if description else None,
                               due_date if due_date else None,
                               priority if priority else None,
                               tags.split(',') if tags else None)

    elif action.lower() == "delete":
        task_manager.delete_task(task_id)

    elif action.lower() == "mark done":
        task_manager.mark_task_status(task_id, True)

    elif action.lower() == "mark pending":
        task_manager.mark_task_status(task_id, False)

    else:
        print("Invalid action. Please try again.")


def main():
    cli()

if __name__ == "__main__":
    main()
