import notifier

from event_manager.events import notebook

# notifier.subscribe_event(notebook.NotebookNewStatusEvent)
notifier.subscribe_event(notebook.NotebookStartedEvent)
notifier.subscribe_event(notebook.NotebookFailedEvent)
notifier.subscribe_event(notebook.NotebookSucceededEvent)
