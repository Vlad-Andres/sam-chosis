# Align First Four Scenes With Script Spec

## Why
The current Ren’Py project implements most of Scene 1 and Scene 2, but the script extends through Scene 4 with branching, hallucination effects, and transitions that are not yet represented end-to-end.

## What Changes
- Bring the game flow in sync with the provided script through Scene 4 (Bedroom → Kitchen → Sidewalk/Park → Supermarket), including choices and flags.
- Add consistent “thought” presentation for **player thoughts** distinct from spoken dialogue.
- Add placeholder visuals for new backgrounds/scene inserts (no external images), and safe audio hooks (no required audio files).
- Add meds-dependent presentation rules (visual tone + audio ambience rules) that can be driven by a single flag.
- Refactor the story into clear labels per scene to make it easy to extend later (Scene 5+).

## Impact
- Affected specs: narrative flow, choices/branching, transitions/effects, placeholder assets, audio hooks.
- Affected code: [script.rpy](file:///Users/vladandres/Public/UU%20(doing)/GHIS/renpy-8.5.2-sdk/schizo/game/script.rpy), [images.rpy](file:///Users/vladandres/Public/UU%20(doing)/GHIS/renpy-8.5.2-sdk/schizo/game/images.rpy), [animations.rpy](file:///Users/vladandres/Public/UU%20(doing)/GHIS/renpy-8.5.2-sdk/schizo/game/animations.rpy), [screens.rpy](file:///Users/vladandres/Public/UU%20(doing)/GHIS/renpy-8.5.2-sdk/schizo/game/screens.rpy)

## Current State (Gap Summary)
- Implemented:
  - Disclaimer splashscreen.
  - Scene 1 (Bedroom) with wake-up beats + inconsequential mirror choice.
  - Scene 2 (Kitchen) with “Michael loud music” hallucination sequence, breakfast choice (eggs vs cereal), and meds choice stored in `flag["meds"]`.
  - Placeholder images for bedroom/kitchen/phone/breakfast closeups.
  - Minimal main menu (Play/Preferences/Quit).
- Missing / inconsistent with script:
  - Scene 3 (Sidewalk/Park) and Scene 4 (Supermarket) not implemented.
  - Meds-dependent “tone” effects (desaturated/blur vs vibrant/unreal) not implemented beyond setting the flag.
  - Charlie “reality check” mechanic for the Mystery Person not implemented.
  - Panic/heartbeat pulsing effect sequence in the supermarket aisle not implemented.
  - Audio cues exist but are not standardized as a project convention (filenames, channels, stop rules per scene).
  - Thought formatting (**…**) is currently displayed as regular narration; needs a distinct style.

## ADDED Requirements

### Requirement: Scene Labels And Flow
The system SHALL provide a linear playable flow from disclaimer through Scene 4, with labeled entry points for each scene.

#### Scenario: Player starts game and reaches Scene 4
- **WHEN** the player selects Play from the main menu
- **THEN** the disclaimer is shown once per launch (skippable by click/confirm)
- **AND THEN** the story proceeds through Scene 1 → Scene 2 → Scene 3 → Scene 4 without returning early
- **AND THEN** the script reaches the “— END —” marker for this draft and returns/ends cleanly

### Requirement: Thought Presentation
The system SHALL render “Sam’s thoughts” in a distinct style from spoken dialogue.

#### Scenario: Thought line is displayed
- **WHEN** the script displays a **thought** line
- **THEN** it appears visually distinct (e.g., italicized text and/or different text box styling)
- **AND** it is not attributed as spoken dialogue by any character name

### Requirement: Choices And Flags
The system SHALL store and use the following state for branching:
- `flag["meds"]`: boolean set by the meds choice in Scene 2.
- `flag["breakfast"]`: enum string `"eggs"` or `"cereal"` set by the breakfast choice.

#### Scenario: Meds choice affects later scenes
- **WHEN** `flag["meds"]` is True
- **THEN** later scenes use the “meds tone” (desaturated/soft/slow mood)
- **WHEN** `flag["meds"]` is False
- **THEN** later scenes use the “no meds tone” (vivid/saturated/uncanny-but-not-horror mood)

### Requirement: Placeholder Visuals (No External Images)
The system SHALL define placeholder displayables for every background/insert required by Scenes 1–4 so the game never crashes due to missing images.

#### Scenario: Scene background is shown
- **WHEN** the scene transitions to a background described in the script
- **THEN** a placeholder background is used if no real image exists

### Requirement: Safe Audio Hooks
The system SHALL attempt to play audio cues only if the referenced file exists, so missing audio does not error.

#### Scenario: Audio file is missing
- **WHEN** the script triggers an audio cue whose file is not present
- **THEN** the game continues with no error

### Requirement: Scene 3 (Sidewalk/Park) Content
The system SHALL implement Scene 3 per the script with meds-dependent branches and the Charlie “reality check” sequence.

#### Scenario: Scene 3 completes and reaches the supermarket
- **WHEN** Scene 3 begins after leaving the apartment
- **THEN** the player sees sidewalk ambience and a short “flowers/park” beat
- **AND** the script shows a “time passes” beat (e.g., “10 minutes later” title card)
- **AND** the Mystery Person asks for help and is revealed as a hallucination via Charlie not approaching
- **AND** the player continues to the supermarket

### Requirement: Scene 4 (Supermarket) Content
The system SHALL implement Scene 4 per the script including the panic sequence and Grandpa interaction.

#### Scenario: Panic and reality snapback
- **WHEN** the player enters the crowded aisle
- **THEN** panic builds (heartbeat/pulsing effect) and culminates in a hallucination where the aisle “stares”
- **AND** Charlie grounds the player
- **AND** the scene snaps back to normal aisle activity
- **AND** Grandpa asks if Sam is okay and Sam responds

## MODIFIED Requirements

### Requirement: Scene 2 Alignment
Scene 2 SHALL match the script beats and timing:
- Loud music audible on entering kitchen.
- Breakfast choice shows a top-down “close-up” insert and returns to the kitchen.
- Door banging sequence includes Sam’s spoken lines.
- Phone check reveals Michael is away.
- Loud music stops only after that realization beat (not before).

## REMOVED Requirements
None.
