# Production Audit Findings — v4.0.2

## Fixed

1. **Map-page space loss:** the large Next Objective banner consumed substantial mobile viewport height. It was removed from the DOM and its space now belongs to the flex-growing map viewport.
2. **Next Objective dependency on removed DOM:** the renderer previously required `nextObjectiveCard` and dynamically created `openNextObjective`/`skipNextObjective` controls. The state logic was separated from the removed banner. Access now exists in Route Planner and each location detail sheet.
3. **Resize synchronization:** map layers could retain stale dimensions after a layout-height change. A `ResizeObserver` now requests the existing resize path through `requestAnimationFrame`.
4. **Version mismatch:** `VERSION.json` reported 4.0.1 while `app.js`, the page title, and visible version button still reported 4.0.0. All production-facing version references now report 4.0.2.
5. **Database metadata mismatch:** the runtime database version was 8 while a later assignment set `ACBF_DATABASE_META.version` to 7. The metadata now consistently reports 8.
6. **Accessibility zoom restriction:** the viewport meta tag disabled page zoom globally. The restriction was removed; map gestures remain isolated through the map surface's existing touch-action handling.
7. **Service-worker partial installation risk:** `Promise.allSettled` allowed installation to succeed with missing required assets. Installation now requires the complete core set.
8. **Incorrect non-navigation fallback:** failed image/static requests could receive `index.html`. Navigation fallback is now limited to navigation requests; failed static assets no longer receive HTML.
9. **Diagnostics cache mismatch:** diagnostics displayed the older v4.0.0 cache name. It now matches the v4.0.2 service-worker cache.

## Verified without change

- Storage key remains `acbf-companion-m3`.
- User-data schema remains version 3.
- Database version remains 8.
- All 104 database marker IDs are unique and preserved.
- Current base-map artwork and branding assets are unchanged.
- No duplicate static HTML IDs were found.
- All statically referenced local HTML and service-worker core assets exist.

## Documented but not changed

- Existing marker-to-map alignment requires in-game visual verification because the base artwork was replaced in an earlier patch.
- Dynamic DOM IDs reported by a simple static reference scan are intentionally created at runtime and are not missing production elements.
- Large-scale refactoring and database expansion were outside this maintenance patch.
