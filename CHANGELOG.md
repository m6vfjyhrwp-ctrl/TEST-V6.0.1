# Changelog

## 5.1.1 — Canonical Database Evidence Audit

- Preserved all 104 production records and IDs.
- Added source-registry URLs and evidence-audit documentation.
- Documented published baseline discrepancies without overstating completeness.
- Refreshed deployment cache/version metadata.

## 5.1.0 — Canonical Database Completion, Verification & Certification

- Reconciled all existing supported categories against a documented external-reference baseline.
- Preserved all 104 marker IDs, map positions, categories, storage key, and save compatibility.
- Added source registry and normalized traceability metadata.
- Updated database version to 9 and runtime version to 5.1.0.
- Added complete certification and audit documentation.
- Added no speculative records.

## 5.0.0 — Final Completion Edition

- Preserved the complete v4.0.6 runtime and save-compatible architecture.
- Synchronized production version references to 5.0.0.
- Corrected database coverage metadata to the actual 104 records.
- Added `sourceBasis` and `lastReviewedVersion` traceability metadata to all 104 location records.
- Preserved all marker IDs, ordering, coordinates, calibration, and existing verification labels.
- Added database, content, calibration, gameplay, performance, accessibility, PWA, testing, and release-certification reports.
- No existing production file was removed.

# Changelog

## 4.0.6 — Release Candidate Certification
- Completed a conservative dependency and production audit.
- Synchronized runtime, manifest, diagnostics, documentation, and service-worker versions.
- Reduced the service worker installation-critical precache list to runtime essentials; optional documentation remains available online and may be cached on demand.
- Preserved the `acbf-companion-m3` storage key, user-data schema 3, database version 8, 104 records, and all marker IDs.
- Retained historical documentation because safe deletion could not be conclusively demonstrated.
- Packaged deployable files directly at ZIP root.
- No gameplay features, branding, map artwork, calibration, database records, or save formats were changed.

## 4.0.3 — Production Cleanup (2026-07-24)

- Preserved the expanded map layout with no Next Objective banner on the main map page.
- Added missing left/right safe-area variables used by the responsive toolbar and menus.
- Removed the desktop map minimum-height constraint on mobile to prevent short-iPhone overflow.
- Restored approximately 44 × 44 CSS-pixel mobile toolbar targets.
- Synchronized visible, runtime, diagnostics, VERSION.json, and service-worker cache versions.
- Reduced the required service-worker precache list to production assets and current stable documentation, lowering update-install failure risk.
- Preserved marker IDs, database records, calibration, routes, localStorage key, and user-data schema.

## 4.0.1 — Updated Caribbean Base Map
- Replaced only the interactive map background artwork with the supplied clean map image.
- Preserved the production filename `caribbean-map.jpg`, map engine, marker IDs, database records, routes, calibration data, branding, and `acbf-companion-m3` saved-data key.
- Center-cropped the supplied 1466×1073 source to the existing map aspect ratio, then exported at the original 1944×1665 canvas to avoid CSS stretching or coordinate-transform changes.
- Incremented the service-worker cache identifier so installed PWAs request the updated map.
- No gameplay records or verification states were changed.

## 4.0.0 — Captain’s Edition
- Added local Fleet Manager with vessel class, power, cargo, repairs, profit, and notes.
- Expanded Jackdaw view with next-upgrade recommendations.
- Added offline searchable and bookmarkable encyclopedia.
- Added 100% completion planner with scope, sorting, local milestones, and route generation.
- Added manual drag reorder and per-stop removal to Route Planner 2.0.
- Added optional Animus visual mode and marker-size settings.
- Added compressed local screenshot storage with quota checks.
- Added recent-search management and storage diagnostics.
- Preserved database IDs, map calibration, branding, storage key, and user-data schema.


## 4.0.2 — Stability Audit and Expanded Map
- Removed the Map-page Next Objective banner and returned its vertical space to the map.
- Preserved Next Objective access in Route Planner and location details.
- Added viewport resize observation.
- Corrected app-version and database-metadata inconsistencies.
- Improved service-worker install/fallback behavior.
- Restored browser page zoom accessibility outside the map.

## 6.0.1 — 2026-07-24
- Restored the mobile More Map Actions menu and its five original commands.
- Added centralized release identity and visible integrity status.
- Added runtime SHA-256 verification, safer imports, CSP hardening, and scoped offline caching.
- Added repository security templates, validation workflow, signing guidance, and production reports.
- Preserved all production database records, IDs, categories, storage keys, and user schema.
