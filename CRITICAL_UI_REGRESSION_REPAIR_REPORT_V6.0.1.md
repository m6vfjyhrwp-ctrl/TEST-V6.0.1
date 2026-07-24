# Critical UI Regression Repair Report

The More Map Actions menu lived inside a clipped map stacking context and depended on a generated `click` after touch processing. The repair positions the menu in the fixed viewport layer, opens it on `pointerup`, suppresses the duplicate synthetic click, delays outside-dismiss handling, raises its stacking level, and adds Escape/arrow-key handling, focus restoration, `aria-expanded`, and responsive repositioning. The original five actions and order are preserved.
