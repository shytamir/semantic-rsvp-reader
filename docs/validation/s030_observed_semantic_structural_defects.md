# Observed Defects Review

## Human Summary

- Only two evaluations to perform:
	- Possible exception for always justified rule for extra long words like antidisestablishmentarianism
	  Probable closure rule tightening for the new parser chunks
- Only one actionable UI issue:
    - CSS fix for structural fixtures not to clash with ghost chunk render

## Summary

- Total reports: 4
- Included reports: 4
- Reports with timing context: 4
- Reports without timing context: 0
- Reports by category:
  - layout_or_visibility_issue: 1
  - orphan_function_word: 1
  - parenthetical_state_confusion: 1
  - quote_state_confusion: 1

---

<!-- Source: defect_20260711_190700_73306e.md.gz -->

# Semantic RSVP Defect Report

Report ID: defect_20260711_190700_73306e
Created at: 2026-07-11T19:07:00.888547Z

## Classification

Category: layout_or_visibility_issue
Severity: 2
Notes:
Changed font size and anchor to justify the long word.

Preferred behavior:
Evaluate edge case for a rule for words above a long threshold

## Reader State

Current index: 3
Sentence index: 0
Playback speed: 1x
Adaptation enabled: true

Current chunk:
antidisestablishmentarianism.

## Timing Context

Base duration ms: 660
Effective duration ms: 660
Playback speed: 1x
Duration source: schedule
Current syntactic hint: normal
Current content word count: 1
Character length: 29
In quote: false
Quote boundary: none
In parenthetical: false
Parenthetical depth: 0
Navigation progress percent: 100
Navigation paragraph index: 0

## Structural Context

- Active H1: 
- Active H2: 
- Active label: 
- Active path: none
- Is header chunk: false
- Header level: unknown

## Navigability Context

Previous displayed chunk:
- Index: 2
- Text: beside
- Duration ms: 400
- Progress percent: 61
- Paragraph index: 0

Breakpoints:
- Count: 0
- Current is breakpoint: false
- Previous breakpoint: unknown
- Next breakpoint: unknown
- Indices: none

## Drift Recovery Context

- Active: false
- Pending: false
- Target breakpoint: unknown
- Lead-in index: unknown
- Delay ms: 500
- Direction: 

Original sentence:
The reader saw complementary explanations beside antidisestablishmentarianism.

Previous chunks:
- [0] "The reader" - 440ms base / 440ms effective - normal - 1 content word(s) - 10 chars - quote=false/none - parenthetical=false/0 - navigation=12%/p0
- [1] "saw complementary explanations" - 840ms base / 840ms effective - dense - 3 content word(s) - 30 chars - quote=false/none - parenthetical=false/0 - navigation=52%/p0
- [2] "beside" - 400ms base / 400ms effective - normal - 1 content word(s) - 6 chars - quote=false/none - parenthetical=false/0 - navigation=61%/p0

Next chunks:
- none

## Session Summary

Event count: 3
Rewind count: 0
Pause count: 0
Speed change count: 0
Adaptation count: 0
Completed: true
Elapsed session ms: 95022
Estimated remaining chunks: 0
Average effective duration ms: 585
Last adaptation reason: 
Last adaptation direction: 

## Client

User agent:
Mozilla/5.0 (Android 16; Mobile; rv:152.0) Gecko/152.0 Firefox/152.0

Viewport:
384x742

Display:
Reader width px: 368
Chunk scroll width px: 340
Chunk client width px: 340
Chunk may overflow: false
Layout context:
- Previous chunk visible: true
- Previous chunk text length: 6
- Active chunk text length: 29
- Viewport: 384x742

---

<!-- Source: defect_20260711_190819_8e1b8e.md.gz -->

# Semantic RSVP Defect Report

Report ID: defect_20260711_190819_8e1b8e
Created at: 2026-07-11T19:08:19.903210Z

## Classification

Category: quote_state_confusion
Severity: 2
Notes:
The end quote was pushed forward to start a non quoted chunk

Preferred behavior:
Evaluate closure chunking rules.

## Reader State

Current index: 2
Sentence index: 0
Playback speed: 1x
Adaptation enabled: true

Current chunk:
” and closed the file.

## Timing Context

Base duration ms: 980
Effective duration ms: 980
Playback speed: 1x
Duration source: schedule
Current syntactic hint: dense
Current content word count: 2
Character length: 22
In quote: true
Quote boundary: close
In parenthetical: false
Parenthetical depth: 0
Navigation progress percent: 100
Navigation paragraph index: 0

## Structural Context

- Active H1: 
- Active H2: 
- Active label: 
- Active path: none
- Is header chunk: false
- Header level: unknown

## Navigability Context

Previous displayed chunk:
- Index: 1
- Text: should not split the core claim,
- Duration ms: 880
- Progress percent: 70
- Paragraph index: 0

Breakpoints:
- Count: 0
- Current is breakpoint: false
- Previous breakpoint: unknown
- Next breakpoint: unknown
- Indices: none

## Drift Recovery Context

- Active: false
- Pending: false
- Target breakpoint: unknown
- Lead-in index: unknown
- Delay ms: 500
- Direction: 

Original sentence:
The chair said, “We should not split the core claim,” and closed the file.

Previous chunks:
- [0] "The chair said, “We" - 780ms base / 780ms effective - dense - 3 content word(s) - 19 chars - quote=true/open - parenthetical=false/0 - navigation=25%/p0
- [1] "should not split the core claim," - 880ms base / 880ms effective - dense - 3 content word(s) - 32 chars - quote=true/none - parenthetical=false/0 - navigation=70%/p0

Next chunks:
- none

## Session Summary

Event count: 3
Rewind count: 0
Pause count: 0
Speed change count: 0
Adaptation count: 0
Completed: true
Elapsed session ms: 67664
Estimated remaining chunks: 0
Average effective duration ms: 880
Last adaptation reason: 
Last adaptation direction: 

## Client

User agent:
Mozilla/5.0 (Android 16; Mobile; rv:152.0) Gecko/152.0 Firefox/152.0

Viewport:
384x742

Display:
Reader width px: 368
Chunk scroll width px: 340
Chunk client width px: 340
Chunk may overflow: false
Layout context:
- Previous chunk visible: true
- Previous chunk text length: 32
- Active chunk text length: 22
- Viewport: 384x742

---

<!-- Source: defect_20260711_191007_f42b7e.md.gz -->

# Semantic RSVP Defect Report

Report ID: defect_20260711_191007_f42b7e
Created at: 2026-07-11T19:10:07.821949Z

## Classification

Category: parenthetical_state_confusion
Severity: 2
Notes:
The start parentheses got tacked to the tail of the previous chunk, causing it's not yet quoted text to be flagged as quoted

Preferred behavior:
Evaluate necessity for closure chunking rule

## Reader State

Current index: 1
Sentence index: 0
Playback speed: 0.85x
Adaptation enabled: true

Current chunk:
kept the phrase together (

## Timing Context

Base duration ms: 780
Effective duration ms: 918
Playback speed: 0.85x
Duration source: schedule
Current syntactic hint: dense
Current content word count: 3
Character length: 26
In quote: false
Quote boundary: none
In parenthetical: true
Parenthetical depth: 1
Navigation progress percent: 44
Navigation paragraph index: 0

## Structural Context

- Active H1: 
- Active H2: 
- Active label: 
- Active path: none
- Is header chunk: false
- Header level: unknown

## Navigability Context

Previous displayed chunk:
- Index: 0
- Text: The system
- Duration ms: 440
- Progress percent: 11
- Paragraph index: 0

Breakpoints:
- Count: 0
- Current is breakpoint: false
- Previous breakpoint: unknown
- Next breakpoint: unknown
- Indices: none

## Drift Recovery Context

- Active: false
- Pending: false
- Target breakpoint: unknown
- Lead-in index: unknown
- Delay ms: 500
- Direction: 

Original sentence:
The system kept the phrase together (even when the aside was brief) before resuming.

Previous chunks:
- [0] "The system" - 440ms base / 518ms effective - normal - 1 content word(s) - 10 chars - quote=false/none - parenthetical=false/0 - navigation=11%/p0

Next chunks:
- [2] "even when the aside was brief)" - 880ms base / 1035ms effective - dense - 4 content word(s) - 30 chars - quote=false/none - parenthetical=true/0 - navigation=79%/p0
- [3] "before resuming." - 840ms base / 988ms effective - dense - 2 content word(s) - 16 chars - quote=false/none - parenthetical=false/0 - navigation=100%/p0

## Session Summary

Event count: 6
Rewind count: 2
Pause count: 0
Speed change count: 0
Adaptation count: 1
Completed: true
Elapsed session ms: 96649
Estimated remaining chunks: 2
Average effective duration ms: 865
Last adaptation reason: rewinds
Last adaptation direction: slower

## Client

User agent:
Mozilla/5.0 (Android 16; Mobile; rv:152.0) Gecko/152.0 Firefox/152.0

Viewport:
384x742

Display:
Reader width px: 368
Chunk scroll width px: 340
Chunk client width px: 340
Chunk may overflow: false
Layout context:
- Previous chunk visible: true
- Previous chunk text length: 10
- Active chunk text length: 26
- Viewport: 384x742
