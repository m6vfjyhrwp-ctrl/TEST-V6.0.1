# Production Audit Findings — v4.0.3

## Fixed

1. `--safe-left` and `--safe-right` were referenced but not defined, which could invalidate responsive safe-area declarations.
2. The desktop `min-height: 520px` on the map shell could force overflow on short iPhones despite dynamic viewport sizing.
3. Compact toolbar targets dropped below the intended practical mobile size at narrow widths.
4. Version strings and diagnostics still identified v4.0.2.
5. The service worker treated numerous historical reports as required install assets, unnecessarily increasing the chance that one missing documentation file would block installation.
6. The release archive contained an unnecessary parent directory; the final package is flattened.

## Verified and preserved

- The large main-map Next Objective banner is absent from `index.html`.
- Next Objective logic remains available in the route drawer and location details.
- Existing `ResizeObserver`-based map resizing remains active.
- Marker IDs, record order, map artwork, branding files, storage key, schema, and database version remain unchanged.

## Documented, not changed

- Geographic alignment of all markers against the replacement artwork requires manual visual testing.
- Broad architectural refactoring and historical-document pruning were intentionally avoided during stabilization.
