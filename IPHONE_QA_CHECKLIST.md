# iPhone and Installed-PWA QA Checklist

Record iPhone model, iOS version, Safari version, test date, and QA build ID.

## Safari

- [ ] Fresh load over HTTPS
- [ ] No blank screen or startup error
- [ ] Map renders and pans with one finger
- [ ] Pinch zoom works without page zoom conflict
- [ ] More Map Actions opens with one tap
- [ ] Exactly five actions appear
- [ ] Filters opens and closes
- [ ] Animus Scan runs
- [ ] Route Planner opens and builds/clears a route
- [ ] Full-Screen Map enters and exits
- [ ] Nearest Objective responds
- [ ] Menu still works after each action
- [ ] Search, marker details, favorites, notes, and progress work
- [ ] Import rejects malformed JSON and accepts a known-good backup
- [ ] Export produces a usable backup

## Installed PWA

- [ ] Add to Home Screen succeeds with correct icon/name
- [ ] Standalone launch succeeds
- [ ] Close and relaunch preserves data
- [ ] Airplane-mode launch succeeds after one online load
- [ ] Map and core controls work offline
- [ ] Service-worker update does not mix old/new UI
- [ ] More Map Actions works after offline reload

## Accessibility

- [ ] VoiceOver identifies More Map Actions and reports expanded/collapsed state
- [ ] Menu items are announced in order
- [ ] Focus returns to the ••• button after closing
- [ ] Text remains usable at larger text sizes
- [ ] Reduced Motion setting is respected
- [ ] Touch targets are comfortably tappable

## Diagnostics

After any failure, open **QA**, tap **Refresh**, reproduce the issue, then tap **Export Report**. Attach the JSON report and a screenshot to the bug report.
