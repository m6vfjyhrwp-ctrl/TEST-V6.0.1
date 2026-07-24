# Animus Companion v4.0.1 Base Map Replacement

## Scope
This patch changes only the production base-map artwork and the minimum version/cache documentation required to deliver it.

## Asset replacement
- Production path retained: `caribbean-map.jpg`
- Previous production image: 1944 × 1665 JPEG
- Supplied replacement source: 1466 × 1073 JPEG
- Source crop: centered horizontally to approximately 1253 × 1073 so its aspect ratio matches the original production canvas.
- Output: 1944 × 1665 progressive JPEG, quality 92, without stretching, rotation, mirroring, interface borders, controls, or overlays.

## Calibration strategy
The production filename and image canvas dimensions remain unchanged. Therefore, the existing normalized map coordinate transform and all stored marker coordinates remain untouched. No marker IDs or database relationships were changed.

The supplied artwork is a newly rendered visual map and does not reproduce the previous geography pixel-for-pixel. Maintaining the old canvas prevents technical transform breakage, but it cannot guarantee visual alignment of every marker with the new landmasses. Manual anchor verification is still required before claiming exact marker placement.

## Saved data
- Storage key remains `acbf-companion-m3`.
- User-data version remains 3.
- Database version remains 8.
- No localStorage migration or reset is performed.

## Rollback reference
`caribbean-map-v4.0.0-reference.jpg` is included as a non-pre-cached rollback reference. It is not loaded by the application.
