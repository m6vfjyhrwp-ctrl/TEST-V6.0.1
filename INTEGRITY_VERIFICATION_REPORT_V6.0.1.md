# Integrity Verification Report

Critical static assets are hashed with SHA-256 in `integrity-manifest.json`. At runtime, supported browsers fetch same-origin files and compare Web Crypto digests. Results are Official Release, Integrity Check Failed, or Integrity Not Verified. Verification failure never erases or blocks user data.
