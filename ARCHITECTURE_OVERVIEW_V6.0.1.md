# Architecture Overview

The application remains a static offline-first PWA. `database.js` contains immutable built-in records; `app.js` maintains user state in local storage; `engine.js` controls map gestures; `service-worker.js` manages same-origin application caching. `release-identity.js` centralizes build metadata and `integrity.js` verifies critical assets against `integrity-manifest.json`.
