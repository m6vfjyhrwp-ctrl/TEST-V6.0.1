# MASTER IMPLEMENTATION PROMPT — Animus Companion v3.4.1 Mobile Polish

Treat the attached latest working Animus Companion project ZIP as the authoritative production codebase. Do not rebuild the application, replace its architecture, discard its database, alter saved marker IDs, or remove existing map, route, progress, filtering, Island Explorer, Nearest Objective, detail-sheet, backup, calibration, branding, or offline systems.

Implement one carefully integrated mobile usability update and return a fully working, upload-ready GitHub Pages/PWABuilder ZIP with all deployable files located at the ZIP root.

## Required corrections

1. **Three-second confirmation messages**
   - All temporary toast/confirmation messages, including route-built notices, completion notices, favorite notices, saves, and similar feedback, must disappear automatically after exactly three seconds.
   - Tapping a toast should dismiss it immediately.
   - Undo buttons must remain functional and must not accidentally trigger the toast background dismissal before the undo operation runs.
   - Repeated actions must reset the timer cleanly, with only one visible toast and no stacked or lingering notifications.

2. **iPhone toolbar accessibility and safe-area correction**
   - Ensure every map command remains reachable on all supported iPhone widths, including narrow screens and Display Zoom.
   - Prevent the map title and toolbar from appearing under the iOS status bar, Dynamic Island, clock, signal, Wi-Fi, or battery indicators, especially in standalone and fullscreen PWA modes.
   - Respect `env(safe-area-inset-top)` and all other safe-area insets.
   - Never allow toolbar buttons to be clipped offscreen.
   - Use compact touch-friendly buttons, title truncation, and a smooth horizontal action scroller when necessary rather than hiding functions.
   - Preserve clear accessibility labels and minimum practical touch targets.

## Recommended production refinements

- Keep temporary messages within the visible viewport and cap their width on small phones.
- Allow immediate tap-to-dismiss while preserving screen-reader `role="status"` behavior.
- Ensure route summaries, detail sheets, map controls, and bottom navigation do not cover one another.
- Verify portrait and landscape behavior at 320, 375, 390, 393, 414, and 430 CSS-pixel widths.
- Verify normal Safari, Add-to-Home-Screen standalone mode, and app fullscreen mode.
- Preserve all localStorage data and maintain backward compatibility with prior saves.
- Increment the application and service-worker cache version so updated assets replace older cached files.
- Do not change the approved map artwork, branding, database, routes, or marker calibration unless required to fix a proven defect.

## Acceptance criteria

- Selecting or routing objectives produces a notification that disappears after three seconds without further interaction.
- Every top map action can be reached and activated on a narrow iPhone.
- No title or command is hidden behind the status bar or Dynamic Island.
- Existing saves, progress, notes, favorites, routes, filters, screenshots, and backups continue working.
- The service worker installs the new build rather than serving stale interface assets.
- The final ZIP is upload-ready with `index.html`, manifest, service worker, scripts, styles, map, icons, and documentation at its root.
