# Tasks
- [x] Task 1: Audit current implementation vs script and decide the label structure.
  - [x] Confirm which beats of Scene 1 and Scene 2 already match the script and list mismatches to adjust.
  - [x] Decide label boundaries (`scene_1_bedroom`, `scene_2_kitchen`, `scene_3_walk`, `scene_4_supermarket`) and a single linear “start” flow.

- [x] Task 2: Standardize narration types (thoughts vs spoken dialogue) and characters.
  - [x] Define/choose a “thought” presentation for **Sam’s thoughts** (distinct from spoken dialogue).
  - [x] Ensure spoken lines use named Characters (Sam, Mystery Person, Grandpa). Keep Michael offscreen unless needed.

- [x] Task 3: Make Scene 2 fully conform to the script timing.
  - [x] Ensure loud music starts on kitchen entry and stops only after phone realization.
  - [x] Store breakfast choice into `flag["breakfast"]`.
  - [x] Keep breakfast insert scenes (eggs/cereal closeups) and return to kitchen.

- [x] Task 4: Add placeholder assets for all new Scene 3 and Scene 4 visuals.
  - [x] Add placeholder backgrounds/inserts: sidewalk, park/flowers, supermarket entrance, breakfast aisle/crowded aisle, “10 minutes later” card (if implemented as an image/screen).
  - [x] Ensure every scene statement references a defined image to avoid crashes.

- [x] Task 5: Implement Scene 3 (Sidewalk/Park) including meds branches and Charlie “reality check”.
  - [x] Implement the walk + flowers beat.
  - [x] Implement meds-dependent branch text (meds: disinterest; no meds: vivid enjoyment + “flowers look off”).
  - [x] Implement “10 minutes later” beat.
  - [x] Implement Mystery Person interaction and hallucination reveal via Charlie not approaching.

- [x] Task 6: Implement Scene 4 (Supermarket) including panic sequence, grounding, and Grandpa interaction.
  - [x] Add ambient sound hooks (crowd chatter, store music, scanner beeps, kid “doggy”).
  - [x] Implement crowded aisle beat and escalating panic (heartbeat + pulsing screen effect).
  - [x] Implement hallucination “everyone staring” freeze beat, then snap-back to normal.
  - [x] Implement Grandpa dialogue and end marker.

- [x] Task 7: Implement meds-dependent presentation rules for Scene 3+ (minimal first pass).
  - [x] Meds True: desaturated/softened look and calmer/slower ambience hooks.
  - [x] Meds False: more saturated/vivid look and more prominent ambience hooks.
  - [x] Keep the implementation compatible with placeholders (no required image/audio files).

- [ ] Task 8: Validation
  - [ ] Run Ren’Py lint.
  - [ ] Smoke test: Play through Scene 1 → Scene 4 on both breakfast branches and both meds branches without errors.

- [ ] Task 9: Fix local validation blocker and complete spec validation.
  - [ ] Restore a working Ren’Py CLI/runtime so `renpy.sh` can run without the missing `librenpython.dylib` error.
  - [ ] Re-run Ren’Py lint for the project.
  - [ ] Smoke test all breakfast and meds branches after the runtime issue is fixed.

# Task Dependencies
- Task 3 depends on Task 1 and Task 2
- Task 5 depends on Task 2 and Task 4
- Task 6 depends on Task 2 and Task 4
- Task 7 depends on Task 5 (and may partially be done alongside Task 5)
- Task 8 depends on Tasks 3–7
- Task 9 depends on Task 8
