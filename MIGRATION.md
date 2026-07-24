# v4.0 migration
The build retains localStorage key `acbf-companion-m3` and user-data schema 3. New fields are optional and merged into existing saves: `fleet`, `encyclopediaBookmarks`, `settings.animusMode`, and existing v3 settings. No existing location state, route, note, favorite, screenshot, log, calibration, or map view is cleared.


## v4.0.2
No saved-data migration is required. The storage key remains `acbf-companion-m3`, user-data version remains 3, and all changes are UI/runtime-only.


## v4.0.3

No user-data migration is required. The storage key remains `acbf-companion-m3`, the user-data schema remains 3, and the database version remains 8. All changes are presentation, packaging, diagnostics, and cache metadata changes.
