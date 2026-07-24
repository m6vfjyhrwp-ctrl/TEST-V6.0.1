# Developer Guide

Serve the repository root over HTTPS or localhost. Keep release metadata in `release-identity.js` and `release-identity.json` synchronized. After any production-file edit, regenerate `integrity-manifest.json` and `BUILD_CHECKSUMS.txt`, run `python3 tools/validate_release.py`, and test offline updates. Never change marker IDs or `acbf-companion-m3` without a migration plan.
