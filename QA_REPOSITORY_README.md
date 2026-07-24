# Animus Companion QA Repository

This package is the dedicated **QA/test deployment** for Animus Companion v6.0.1. It is not the public production release.

## Deploy

1. Create a new GitHub repository, preferably private while testing.
2. Upload every file and folder from this ZIP to the repository root.
3. In **Settings → Pages**, deploy from the `main` branch and root folder.
4. Open the generated HTTPS Pages URL on iPhone Safari.
5. Add the QA site to the Home Screen and run `IPHONE_QA_CHECKLIST.md`.

The gold **QA** button opens the on-device diagnostics panel. It captures JavaScript errors, promise rejections, release identity, integrity status, service-worker state, cache inventory, local-storage size, viewport details, and the More Map Actions state. Use **Export Report** after reproducing a problem.

Append `?qa=0` to disable the QA overlay temporarily.

## Repository workflow

- Development repository: active coding and experiments.
- This QA repository: browser, iPhone, PWA, accessibility, and regression testing.
- Production repository: only validated release packages.

Do not promote this package directly to production. Promote the corresponding production build after the QA checklist passes.
