import auditor

from event_manager.events import bookmark

auditor.subscribe(bookmark.BookmarkBuildJobsViewedEvent)
auditor.subscribe(bookmark.BookmarkJobsViewedEvent)
auditor.subscribe(bookmark.BookmarkExperimentsViewedEvent)
auditor.subscribe(bookmark.BookmarkExperimentGroupsViewedEvent)
auditor.subscribe(bookmark.BookmarkProjectsViewedEvent)
