# Observed Defects Review

## Human Summary

Top recurring issues:
1. Bad chunk splits remain the largest category, but the failures are now more specific: long-form dates are split from their year, source/title line breaks are flattened into confusing chunks, and cohesive phrases such as phrasal verbs, qualifier pairs, coordinated nouns, and noun-preposition phrases are still being separated.
2. Layout and visibility defects are a major user-facing blocker on mobile: long ghosted previous chunks can wrap into the active chunk area, and several reports note unexplained reduced font sizing.
3. Underdense chunks still appear where a verb, object, or connector is stranded instead of being grouped with the phrase that gives it meaning.
4. Proper-name and title handling still needs narrower protection, especially for two-word person names and occupational or institutional title phrases.
5. A smaller number of overlong chunks show that the chunker sometimes over-preserves subject/verb cohesion when the pieces would read cleanly as separate beats.

Priority for next refinement:
- Fix the ghost/active chunk layout and default font-size behavior first, because it can obscure the text even when chunking is otherwise acceptable.
- Then preserve source structure boundaries: headings, bylines, blank lines, and long-form dates should not be merged into neighboring prose.
- Then tighten phrase cohesion for phrasal verbs, qualifier pairs, coordinated forms, proper names, and two-word titles.
- Then rebalance underdense and overlong edge cases with focused regressions from this pass.

## Summary

- Total reports: 39
- Included reports: 39
- Reports with timing context: 39
- Reports without timing context: 0
- Reports by category:
  - bad_chunk_split: 17
  - layout_or_visibility_issue: 12
  - overlong_chunk: 2
  - proper_name_split: 1
  - title_name_split: 2
  - underdense_chunk: 5

---

<!-- Source: defect_20260710_144130_05e03c.md.gz -->

# Semantic RSVP Defect Report

Report ID: defect_20260710_144130_05e03c
Created at: 2026-07-10T14:41:30.087893Z

## Classification

Category: layout_or_visibility_issue
Severity: 2
Notes:
Ghosted chunk blocked from view

Preferred behavior:
Might be an edge case as this is the final chunk, but the ghosted chunk wrapped to the current's display area and was superimposed.

## Reader State

Current index: 118
Sentence index: 16
Playback speed: 1.5x
Adaptation enabled: true

Current chunk:
away.

## Timing Context

Base duration ms: 580
Effective duration ms: 387
Playback speed: 1.5x
Duration source: schedule
Current syntactic hint: normal
Current content word count: 1
Character length: 5
In quote: false
Quote boundary: none
In parenthetical: false
Parenthetical depth: 0
Navigation progress percent: 100
Navigation paragraph index: 3

## Navigability Context

Previous displayed chunk:
- Index: 117
- Text: the sentence has walked
- Duration ms: 640
- Progress percent: 99
- Paragraph index: 3

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
The reader should be allowed to hesitate, consider, and revise without feeling that the sentence has walked away.

Previous chunks:
- [115] "and revise" - 440ms base / 293ms effective - normal - 1 content word(s) - 10 chars - quote=false/none - parenthetical=false/0 - navigation=96%/p3
- [116] "without feeling that" - 640ms base / 427ms effective - dense - 2 content word(s) - 20 chars - quote=false/none - parenthetical=false/0 - navigation=98%/p3
- [117] "the sentence has walked" - 640ms base / 427ms effective - dense - 2 content word(s) - 23 chars - quote=false/none - parenthetical=false/0 - navigation=99%/p3

Next chunks:
- none

## Session Summary

Event count: 6
Rewind count: 0
Pause count: 0
Speed change count: 0
Adaptation count: 3
Completed: true
Elapsed session ms: 146994
Estimated remaining chunks: 0
Average effective duration ms: 352
Last adaptation reason: smooth_run
Last adaptation direction: faster

## Client

User agent:
Mozilla/5.0 (Android 16; Mobile; rv:152.0) Gecko/152.0 Firefox/152.0

Viewport:
384x678

Display:
Reader width px: 368
Chunk scroll width px: 340
Chunk client width px: 340
Chunk may overflow: false

---

<!-- Source: defect_20260710_144336_77fe8c.md.gz -->

# Semantic RSVP Defect Report

Report ID: defect_20260710_144336_77fe8c
Created at: 2026-07-10T14:43:36.035696Z

## Classification

Category: layout_or_visibility_issue
Severity: 2
Notes:
Ghosted chunk partly obscured

Preferred behavior:
Looks it's not a last chunk issue. Just happens when ghosted chunk wraps a line. Needs a bit more line space from current chunk

## Reader State

Current index: 44
Sentence index: 5
Playback speed: 1.15x
Adaptation enabled: false

Current chunk:
the pilot

## Timing Context

Base duration ms: 440
Effective duration ms: 383
Playback speed: 1.15x
Duration source: schedule
Current syntactic hint: normal
Current content word count: 1
Character length: 9
In quote: false
Quote boundary: none
In parenthetical: false
Parenthetical depth: 0
Navigation progress percent: 34
Navigation paragraph index: 1

## Navigability Context

Previous displayed chunk:
- Index: 43
- Text: members emphasized that
- Duration ms: 690
- Progress percent: 34
- Paragraph index: 1

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
Several board members emphasized that the pilot is not a fare increase.

Previous chunks:
- [41] "cutting service." - 820ms base / 713ms effective - dense - 2 content word(s) - 16 chars - quote=false/none - parenthetical=false/0 - navigation=32%/p0
- [42] "Several board" - 600ms base / 522ms effective - dense - 2 content word(s) - 13 chars - quote=false/none - parenthetical=false/0 - navigation=32%/p1
- [43] "members emphasized that" - 690ms base / 600ms effective - dense - 2 content word(s) - 23 chars - quote=false/none - parenthetical=false/0 - navigation=34%/p1

Next chunks:
- [45] "is not a fare" - 440ms base / 383ms effective - normal - 1 content word(s) - 13 chars - quote=false/none - parenthetical=false/0 - navigation=35%/p1
- [46] "increase." - 620ms base / 539ms effective - normal - 1 content word(s) - 9 chars - quote=false/none - parenthetical=false/0 - navigation=36%/p1
- [47] "They said" - 600ms base / 522ms effective - dense - 2 content word(s) - 9 chars - quote=false/none - parenthetical=false/0 - navigation=37%/p1

## Session Summary

Event count: 9
Rewind count: 4
Pause count: 1
Speed change count: 1
Adaptation count: 0
Completed: false
Elapsed session ms: 119361
Estimated remaining chunks: 76
Average effective duration ms: 485
Last adaptation reason: 
Last adaptation direction: 

## Client

User agent:
Mozilla/5.0 (Android 16; Mobile; rv:152.0) Gecko/152.0 Firefox/152.0

Viewport:
384x678

Display:
Reader width px: 368
Chunk scroll width px: 340
Chunk client width px: 340
Chunk may overflow: false

---

<!-- Source: defect_20260710_150356_654a84.md.gz -->

# Semantic RSVP Defect Report

Report ID: defect_20260710_150356_654a84
Created at: 2026-07-10T15:03:56.095165Z

## Classification

Category: overlong_chunk
Severity: 2
Notes:
Feels like this should be two chunks

Preferred behavior:
It's a good thought to keep subject with verb but in the future case I think it's ok to separate them 'the country' and 'wil navigate' each feel like full chunks already

## Reader State

Current index: 166
Sentence index: 12
Playback speed: 1x
Adaptation enabled: false

Current chunk:
the country will navigate

## Timing Context

Base duration ms: 640
Effective duration ms: 640
Playback speed: 1x
Duration source: schedule
Current syntactic hint: dense
Current content word count: 2
Character length: 25
In quote: false
Quote boundary: none
In parenthetical: false
Parenthetical depth: 0
Navigation progress percent: 74
Navigation paragraph index: 7

## Navigability Context

Previous displayed chunk:
- Index: 165
- Text: and how
- Duration ms: 400
- Progress percent: 73
- Paragraph index: 7

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
Without a strong central authority like the elder Ayatollah Khamenei, it has become even more unpredictable which faction will eventually gain the upper hand — and how the country will navigate its many crises.

Previous chunks:
- [163] "the upper" - 440ms base / 440ms effective - normal - 1 content word(s) - 9 chars - quote=false/none - parenthetical=false/0 - navigation=72%/p7
- [164] "hand—" - 400ms base / 400ms effective - normal - 1 content word(s) - 5 chars - quote=false/none - parenthetical=false/0 - navigation=73%/p7
- [165] "and how" - 400ms base / 400ms effective - normal - 1 content word(s) - 7 chars - quote=false/none - parenthetical=false/0 - navigation=73%/p7

Next chunks:
- [167] "its many crises." - 820ms base / 820ms effective - dense - 2 content word(s) - 16 chars - quote=false/none - parenthetical=false/0 - navigation=74%/p7
- [168] "The Funeral" - 440ms base / 440ms effective - normal - 1 content word(s) - 11 chars - quote=false/none - parenthetical=false/0 - navigation=75%/p8
- [169] "of Iran’s" - 440ms base / 440ms effective - normal - 1 content word(s) - 9 chars - quote=false/none - parenthetical=false/0 - navigation=75%/p8

## Session Summary

Event count: 23
Rewind count: 13
Pause count: 2
Speed change count: 0
Adaptation count: 0
Completed: false
Elapsed session ms: 313259
Estimated remaining chunks: 56
Average effective duration ms: 540
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

---

<!-- Source: defect_20260710_150615_e3250d.md.gz -->

# Semantic RSVP Defect Report

Report ID: defect_20260710_150615_e3250d
Created at: 2026-07-10T15:06:15.735716Z

## Classification

Category: layout_or_visibility_issue
Severity: 2
Notes:
Very jarring overlap of current ghost chunk

Preferred behavior:
This will keep happening when a line wrapping ghost chunk is followed by a very light chunk. We need to limit to ghost chunk to one line at the cost of its leading word to maintain on screen continuity

## Reader State

Current index: 172
Sentence index: 13
Playback speed: 1x
Adaptation enabled: false

Current chunk:
Iran’s

## Timing Context

Base duration ms: 400
Effective duration ms: 400
Playback speed: 1x
Duration source: schedule
Current syntactic hint: normal
Current content word count: 1
Character length: 6
In quote: false
Quote boundary: none
In parenthetical: false
Parenthetical depth: 0
Navigation progress percent: 77
Navigation paragraph index: 8

## Navigability Context

Previous displayed chunk:
- Index: 171
- Text: Ayatollah Ali Khamenei
- Duration ms: 750
- Progress percent: 76
- Paragraph index: 8

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
The Funeral of Iran’s Supreme Leader Ayatollah Ali Khamenei
Iran’s new leaders are commemorating Ayatollah Khamenei, who was killed on the first day of the U.S.-Israeli war against the country.

Previous chunks:
- [169] "of Iran’s" - 440ms base / 440ms effective - normal - 1 content word(s) - 9 chars - quote=false/none - parenthetical=false/0 - navigation=75%/p8
- [170] "Supreme Leader" - 660ms base / 660ms effective - dense - 2 content word(s) - 14 chars - quote=false/none - parenthetical=false/0 - navigation=76%/p8
- [171] "Ayatollah Ali Khamenei" - 750ms base / 750ms effective - dense - 3 content word(s) - 22 chars - quote=false/none - parenthetical=false/0 - navigation=76%/p8

Next chunks:
- [173] "new leaders" - 600ms base / 600ms effective - dense - 2 content word(s) - 11 chars - quote=false/none - parenthetical=false/0 - navigation=77%/p8
- [174] "are commemorating" - 440ms base / 440ms effective - normal - 1 content word(s) - 17 chars - quote=false/none - parenthetical=false/0 - navigation=77%/p8
- [175] "Ayatollah Khamenei," - 750ms base / 750ms effective - dense - 2 content word(s) - 19 chars - quote=false/none - parenthetical=false/0 - navigation=78%/p8

## Session Summary

Event count: 30
Rewind count: 17
Pause count: 3
Speed change count: 0
Adaptation count: 0
Completed: false
Elapsed session ms: 452924
Estimated remaining chunks: 50
Average effective duration ms: 540
Last adaptation reason: 
Last adaptation direction: 

## Client

User agent:
Mozilla/5.0 (Android 16; Mobile; rv:152.0) Gecko/152.0 Firefox/152.0

Viewport:
384x678

Display:
Reader width px: 368
Chunk scroll width px: 340
Chunk client width px: 340
Chunk may overflow: false

---

<!-- Source: defect_20260710_150800_c8f162.md.gz -->

# Semantic RSVP Defect Report

Report ID: defect_20260710_150800_c8f162
Created at: 2026-07-10T15:08:00.011108Z

## Classification

Category: bad_chunk_split
Severity: 2
Notes:
The year belongs with the date

Preferred behavior:
Date formats should ptobably occupy their own chunk in their long forms. Day month year is dense enough.

## Reader State

Current index: 182
Sentence index: 14
Playback speed: 1x
Adaptation enabled: false

Current chunk:
2026 Inherent

## Timing Context

Base duration ms: 600
Effective duration ms: 600
Playback speed: 1x
Duration source: schedule
Current syntactic hint: dense
Current content word count: 2
Character length: 13
In quote: false
Quote boundary: none
In parenthetical: false
Parenthetical depth: 0
Navigation progress percent: 81
Navigation paragraph index: 8

## Navigability Context

Previous displayed chunk:
- Index: 181
- Text: July 4,
- Duration ms: 560
- Progress percent: 81
- Paragraph index: 8

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
July 4, 2026
Inherent in the peace talks are fundamental questions about the fate of the country.

Previous chunks:
- [179] "war against" - 600ms base / 600ms effective - dense - 2 content word(s) - 11 chars - quote=false/none - parenthetical=false/0 - navigation=80%/p8
- [180] "the country." - 620ms base / 620ms effective - normal - 1 content word(s) - 12 chars - quote=false/none - parenthetical=false/0 - navigation=81%/p8
- [181] "July 4," - 560ms base / 560ms effective - dense - 2 content word(s) - 7 chars - quote=false/none - parenthetical=false/0 - navigation=81%/p8

Next chunks:
- [183] "in the peace talks" - 600ms base / 600ms effective - dense - 2 content word(s) - 18 chars - quote=false/none - parenthetical=false/0 - navigation=82%/p8
- [184] "are fundamental" - 440ms base / 440ms effective - normal - 1 content word(s) - 15 chars - quote=false/none - parenthetical=false/0 - navigation=82%/p8
- [185] "questions about" - 650ms base / 650ms effective - dense - 2 content word(s) - 15 chars - quote=false/none - parenthetical=false/0 - navigation=83%/p8

## Session Summary

Event count: 36
Rewind count: 20
Pause count: 4
Speed change count: 0
Adaptation count: 0
Completed: false
Elapsed session ms: 557202
Estimated remaining chunks: 40
Average effective duration ms: 540
Last adaptation reason: 
Last adaptation direction: 

## Client

User agent:
Mozilla/5.0 (Android 16; Mobile; rv:152.0) Gecko/152.0 Firefox/152.0

Viewport:
384x678

Display:
Reader width px: 368
Chunk scroll width px: 340
Chunk client width px: 340
Chunk may overflow: false

---

<!-- Source: defect_20260710_150919_3c26ba.md.gz -->

# Semantic RSVP Defect Report

Report ID: defect_20260710_150919_3c26ba
Created at: 2026-07-10T15:09:19.192082Z

## Classification

Category: bad_chunk_split
Severity: 2
Notes:
Too small

Preferred behavior:
We didn't need to reduce display to half width for the chunk. Adjusting to fit to width would avoid this issue.

## Reader State

Current index: 200
Sentence index: 15
Playback speed: 1x
Adaptation enabled: false

Current chunk:
a long-struggling

## Timing Context

Base duration ms: 440
Effective duration ms: 440
Playback speed: 1x
Duration source: schedule
Current syntactic hint: normal
Current content word count: 1
Character length: 17
In quote: false
Quote boundary: none
In parenthetical: false
Parenthetical depth: 0
Navigation progress percent: 91
Navigation paragraph index: 8

## Navigability Context

Previous displayed chunk:
- Index: 199
- Text: effort to rebuild
- Duration ms: 600
- Progress percent: 90
- Paragraph index: 8

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
Those include the future of Iran’s relationship with the United States; its willingness to compromise on its nuclear program in order to secure relief from sanctions; and its effort to rebuild a long-struggling economy, now battered by war, that had already led to deep popular discontent.

Previous chunks:
- [197] "from sanctions;" - 510ms base / 510ms effective - normal - 1 content word(s) - 15 chars - quote=false/none - parenthetical=false/0 - navigation=89%/p8
- [198] "and its" - 400ms base / 400ms effective - normal - 1 content word(s) - 7 chars - quote=false/none - parenthetical=false/0 - navigation=89%/p8
- [199] "effort to rebuild" - 600ms base / 600ms effective - dense - 2 content word(s) - 17 chars - quote=false/none - parenthetical=false/0 - navigation=90%/p8

Next chunks:
- [201] "economy," - 420ms base / 420ms effective - normal - 1 content word(s) - 8 chars - quote=false/none - parenthetical=false/0 - navigation=91%/p8
- [202] "now battered" - 600ms base / 600ms effective - dense - 2 content word(s) - 12 chars - quote=false/none - parenthetical=false/0 - navigation=91%/p8
- [203] "by war," - 400ms base / 400ms effective - normal - 1 content word(s) - 7 chars - quote=false/none - parenthetical=false/0 - navigation=92%/p8

## Session Summary

Event count: 43
Rewind count: 24
Pause count: 5
Speed change count: 0
Adaptation count: 0
Completed: false
Elapsed session ms: 636390
Estimated remaining chunks: 22
Average effective duration ms: 540
Last adaptation reason: 
Last adaptation direction: 

## Client

User agent:
Mozilla/5.0 (Android 16; Mobile; rv:152.0) Gecko/152.0 Firefox/152.0

Viewport:
384x678

Display:
Reader width px: 368
Chunk scroll width px: 340
Chunk client width px: 340
Chunk may overflow: false

---

<!-- Source: defect_20260710_151236_698f99.md.gz -->

# Semantic RSVP Defect Report

Report ID: defect_20260710_151236_698f99
Created at: 2026-07-10T15:12:36.929272Z

## Classification

Category: layout_or_visibility_issue
Severity: 2
Notes:
Smaller font is jarring

Preferred behavior:
There's plenty of room up top because the line wrapped, font could be bigger

## Reader State

Current index: 33
Sentence index: 4
Playback speed: 1x
Adaptation enabled: false

Current chunk:
has typically been defined

## Timing Context

Base duration ms: 690
Effective duration ms: 690
Playback speed: 1x
Duration source: schedule
Current syntactic hint: dense
Current content word count: 2
Character length: 26
In quote: false
Quote boundary: none
In parenthetical: false
Parenthetical depth: 0
Navigation progress percent: 24
Navigation paragraph index: 2

## Navigability Context

Previous displayed chunk:
- Index: 32
- Text: but that authority
- Duration ms: 440
- Progress percent: 23
- Paragraph index: 2

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
Under Iran’s Constitution, the position wields great power, but that authority has typically been defined more by the supreme leader himself and his followers’ zeal.

Previous chunks:
- [30] "wields great" - 600ms base / 600ms effective - dense - 2 content word(s) - 12 chars - quote=false/none - parenthetical=false/0 - navigation=22%/p2
- [31] "power," - 400ms base / 400ms effective - normal - 1 content word(s) - 6 chars - quote=false/none - parenthetical=false/0 - navigation=22%/p2
- [32] "but that authority" - 440ms base / 440ms effective - normal - 1 content word(s) - 18 chars - quote=false/none - parenthetical=false/0 - navigation=23%/p2

Next chunks:
- [34] "more by" - 400ms base / 400ms effective - normal - 1 content word(s) - 7 chars - quote=false/none - parenthetical=false/0 - navigation=25%/p2
- [35] "the supreme leader" - 600ms base / 600ms effective - dense - 2 content word(s) - 18 chars - quote=false/none - parenthetical=false/0 - navigation=26%/p2
- [36] "himself" - 400ms base / 400ms effective - normal - 1 content word(s) - 7 chars - quote=false/none - parenthetical=false/0 - navigation=26%/p2

## Session Summary

Event count: 12
Rewind count: 4
Pause count: 2
Speed change count: 0
Adaptation count: 0
Completed: false
Elapsed session ms: 118703
Estimated remaining chunks: 120
Average effective duration ms: 556
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

---

<!-- Source: defect_20260710_151513_26f5fc.md.gz -->

# Semantic RSVP Defect Report

Report ID: defect_20260710_151513_26f5fc
Created at: 2026-07-10T15:15:13.749469Z

## Classification

Category: layout_or_visibility_issue
Severity: 2
Notes:
This chunk is too small

Preferred behavior:
There's no line wrap but the font is smaller fitting only half the width. When this chunk is displayed as a ghost for the next chunk it is displayed correctly. Not sure why the size varies but it shouldn't between chunk and its ghost

## Reader State

Current index: 70
Sentence index: 7
Playback speed: 1x
Adaptation enabled: false

Current chunk:
while conservatives

## Timing Context

Base duration ms: 690
Effective duration ms: 690
Playback speed: 1x
Duration source: schedule
Current syntactic hint: dense
Current content word count: 2
Character length: 19
In quote: false
Quote boundary: none
In parenthetical: false
Parenthetical depth: 0
Navigation progress percent: 47
Navigation paragraph index: 3

## Navigability Context

Previous displayed chunk:
- Index: 69
- Text: minister’s office,
- Duration ms: 600
- Progress percent: 46
- Paragraph index: 3

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
During much of his tenure, for instance, leftists held the prime minister’s office, while conservatives held the presidency.

Previous chunks:
- [67] "leftists held" - 600ms base / 600ms effective - dense - 2 content word(s) - 13 chars - quote=false/none - parenthetical=false/0 - navigation=45%/p3
- [68] "the prime" - 440ms base / 440ms effective - normal - 1 content word(s) - 9 chars - quote=false/none - parenthetical=false/0 - navigation=46%/p3
- [69] "minister’s office," - 600ms base / 600ms effective - dense - 2 content word(s) - 18 chars - quote=false/none - parenthetical=false/0 - navigation=46%/p3

Next chunks:
- [71] "held" - 400ms base / 400ms effective - normal - 1 content word(s) - 4 chars - quote=false/none - parenthetical=false/0 - navigation=48%/p3
- [72] "the presidency." - 620ms base / 620ms effective - normal - 1 content word(s) - 15 chars - quote=false/none - parenthetical=false/0 - navigation=48%/p3
- [73] "His successor," - 650ms base / 650ms effective - dense - 2 content word(s) - 14 chars - quote=false/none - parenthetical=false/0 - navigation=49%/p4

## Session Summary

Event count: 21
Rewind count: 9
Pause count: 3
Speed change count: 0
Adaptation count: 0
Completed: false
Elapsed session ms: 275548
Estimated remaining chunks: 83
Average effective duration ms: 556
Last adaptation reason: 
Last adaptation direction: 

## Client

User agent:
Mozilla/5.0 (Android 16; Mobile; rv:152.0) Gecko/152.0 Firefox/152.0

Viewport:
384x678

Display:
Reader width px: 368
Chunk scroll width px: 340
Chunk client width px: 340
Chunk may overflow: false

---

<!-- Source: defect_20260710_151724_c77da3.md.gz -->

# Semantic RSVP Defect Report

Report ID: defect_20260710_151724_c77da3
Created at: 2026-07-10T15:17:24.443717Z

## Classification

Category: bad_chunk_split
Severity: 2
Notes:
Too long

Preferred behavior:
Behemoth is a rare enough word to warrant its own chunk. It's not dense semantically but it has more cognitive load because of rare activation.

## Reader State

Current index: 124
Sentence index: 13
Playback speed: 1x
Adaptation enabled: false

Current chunk:
behemoth that inserted

## Timing Context

Base duration ms: 640
Effective duration ms: 640
Playback speed: 1x
Duration source: schedule
Current syntactic hint: dense
Current content word count: 2
Character length: 22
In quote: false
Quote boundary: none
In parenthetical: false
Parenthetical depth: 0
Navigation progress percent: 82
Navigation paragraph index: 6

## Navigability Context

Previous displayed chunk:
- Index: 123
- Text: a bureaucratic
- Duration ms: 440
- Progress percent: 81
- Paragraph index: 6

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
By the time of his death, Ali Khamenei had built up his office into a bureaucratic behemoth that inserted itself across Iran’s government, enabling him to oversee the country’s military, intelligence, economy and foreign affairs.

Previous chunks:
- [121] "up his" - 560ms base / 560ms effective - dense - 2 content word(s) - 6 chars - quote=false/none - parenthetical=false/0 - navigation=80%/p6
- [122] "office into" - 600ms base / 600ms effective - dense - 2 content word(s) - 11 chars - quote=false/none - parenthetical=false/0 - navigation=80%/p6
- [123] "a bureaucratic" - 440ms base / 440ms effective - normal - 1 content word(s) - 14 chars - quote=false/none - parenthetical=false/0 - navigation=81%/p6

Next chunks:
- [125] "itself across" - 600ms base / 600ms effective - dense - 2 content word(s) - 13 chars - quote=false/none - parenthetical=false/0 - navigation=83%/p6
- [126] "Iran’s government," - 650ms base / 650ms effective - dense - 2 content word(s) - 18 chars - quote=false/none - parenthetical=false/0 - navigation=84%/p6
- [127] "enabling him" - 600ms base / 600ms effective - dense - 2 content word(s) - 12 chars - quote=false/none - parenthetical=false/0 - navigation=84%/p6

## Session Summary

Event count: 31
Rewind count: 13
Pause count: 5
Speed change count: 0
Adaptation count: 0
Completed: false
Elapsed session ms: 406230
Estimated remaining chunks: 29
Average effective duration ms: 556
Last adaptation reason: 
Last adaptation direction: 

## Client

User agent:
Mozilla/5.0 (Android 16; Mobile; rv:152.0) Gecko/152.0 Firefox/152.0

Viewport:
384x678

Display:
Reader width px: 368
Chunk scroll width px: 340
Chunk client width px: 340
Chunk may overflow: false

---

<!-- Source: defect_20260710_151837_42552d.md.gz -->

# Semantic RSVP Defect Report

Report ID: defect_20260710_151837_42552d
Created at: 2026-07-10T15:18:37.823796Z

## Classification

Category: proper_name_split
Severity: 2
Notes:
Ray Takeyh is one thing

Preferred behavior:
Don't split proper names

## Reader State

Current index: 7
Sentence index: 0
Playback speed: 1x
Adaptation enabled: false

Current chunk:
Takeyh,

## Timing Context

Base duration ms: 400
Effective duration ms: 400
Playback speed: 1x
Duration source: schedule
Current syntactic hint: normal
Current content word count: 1
Character length: 7
In quote: false
Quote boundary: none
In parenthetical: false
Parenthetical depth: 0
Navigation progress percent: 5
Navigation paragraph index: 0

## Navigability Context

Previous displayed chunk:
- Index: 6
- Text: said Ray
- Duration ms: 560
- Progress percent: 4
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
The divisions that do exist do not appear to have hampered the government in a significant way, said Ray Takeyh, a senior fellow at the Council on Foreign Relations.

Previous chunks:
- [4] "the government" - 440ms base / 440ms effective - normal - 1 content word(s) - 14 chars - quote=false/none - parenthetical=false/0 - navigation=3%/p0
- [5] "in a significant way," - 690ms base / 690ms effective - dense - 2 content word(s) - 21 chars - quote=false/none - parenthetical=false/0 - navigation=4%/p0
- [6] "said Ray" - 560ms base / 560ms effective - dense - 2 content word(s) - 8 chars - quote=false/none - parenthetical=false/0 - navigation=4%/p0

Next chunks:
- [8] "a senior" - 400ms base / 400ms effective - normal - 1 content word(s) - 8 chars - quote=false/none - parenthetical=false/0 - navigation=5%/p0
- [9] "fellow at" - 440ms base / 440ms effective - normal - 1 content word(s) - 9 chars - quote=false/none - parenthetical=false/0 - navigation=5%/p0
- [10] "the Council" - 440ms base / 440ms effective - normal - 1 content word(s) - 11 chars - quote=false/none - parenthetical=false/0 - navigation=6%/p0

## Session Summary

Event count: 40
Rewind count: 16
Pause count: 6
Speed change count: 0
Adaptation count: 0
Completed: true
Elapsed session ms: 479601
Estimated remaining chunks: 146
Average effective duration ms: 556
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

---

<!-- Source: defect_20260710_151937_e5e23a.md.gz -->

# Semantic RSVP Defect Report

Report ID: defect_20260710_151937_e5e23a
Created at: 2026-07-10T15:19:37.747073Z

## Classification

Category: title_name_split
Severity: 2
Notes:
A senior fellow is one thing

Preferred behavior:
This 2 word title shouldn't be split

## Reader State

Current index: 9
Sentence index: 0
Playback speed: 1x
Adaptation enabled: false

Current chunk:
fellow at

## Timing Context

Base duration ms: 440
Effective duration ms: 440
Playback speed: 1x
Duration source: schedule
Current syntactic hint: normal
Current content word count: 1
Character length: 9
In quote: false
Quote boundary: none
In parenthetical: false
Parenthetical depth: 0
Navigation progress percent: 5
Navigation paragraph index: 0

## Navigability Context

Previous displayed chunk:
- Index: 8
- Text: a senior
- Duration ms: 400
- Progress percent: 5
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
The divisions that do exist do not appear to have hampered the government in a significant way, said Ray Takeyh, a senior fellow at the Council on Foreign Relations.

Previous chunks:
- [6] "said Ray" - 560ms base / 560ms effective - dense - 2 content word(s) - 8 chars - quote=false/none - parenthetical=false/0 - navigation=4%/p0
- [7] "Takeyh," - 400ms base / 400ms effective - normal - 1 content word(s) - 7 chars - quote=false/none - parenthetical=false/0 - navigation=5%/p0
- [8] "a senior" - 400ms base / 400ms effective - normal - 1 content word(s) - 8 chars - quote=false/none - parenthetical=false/0 - navigation=5%/p0

Next chunks:
- [10] "the Council" - 440ms base / 440ms effective - normal - 1 content word(s) - 11 chars - quote=false/none - parenthetical=false/0 - navigation=6%/p0
- [11] "on Foreign Relations." - 970ms base / 970ms effective - dense - 2 content word(s) - 21 chars - quote=false/none - parenthetical=false/0 - navigation=7%/p0
- [12] "People should have different" - 750ms base / 750ms effective - dense - 2 content word(s) - 28 chars - quote=false/none - parenthetical=false/0 - navigation=8%/p1

## Session Summary

Event count: 46
Rewind count: 19
Pause count: 7
Speed change count: 0
Adaptation count: 0
Completed: true
Elapsed session ms: 539542
Estimated remaining chunks: 144
Average effective duration ms: 556
Last adaptation reason: 
Last adaptation direction: 

## Client

User agent:
Mozilla/5.0 (Android 16; Mobile; rv:152.0) Gecko/152.0 Firefox/152.0

Viewport:
384x678

Display:
Reader width px: 368
Chunk scroll width px: 340
Chunk client width px: 340
Chunk may overflow: false

---

<!-- Source: defect_20260710_152115_468227.md.gz -->

# Semantic RSVP Defect Report

Report ID: defect_20260710_152115_468227
Created at: 2026-07-10T15:21:15.835850Z

## Classification

Category: title_name_split
Severity: 2
Notes:
The prime minister is one thing

Preferred behavior:
Don't split two word titles, should have split this after the possessive s instead

## Reader State

Current index: 69
Sentence index: 7
Playback speed: 1x
Adaptation enabled: false

Current chunk:
minister’s office,

## Timing Context

Base duration ms: 600
Effective duration ms: 600
Playback speed: 1x
Duration source: schedule
Current syntactic hint: dense
Current content word count: 2
Character length: 18
In quote: false
Quote boundary: none
In parenthetical: false
Parenthetical depth: 0
Navigation progress percent: 46
Navigation paragraph index: 3

## Navigability Context

Previous displayed chunk:
- Index: 68
- Text: the prime
- Duration ms: 440
- Progress percent: 46
- Paragraph index: 3

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
During much of his tenure, for instance, leftists held the prime minister’s office, while conservatives held the presidency.

Previous chunks:
- [66] "for instance," - 440ms base / 440ms effective - normal - 1 content word(s) - 13 chars - quote=false/none - parenthetical=false/0 - navigation=45%/p3
- [67] "leftists held" - 600ms base / 600ms effective - dense - 2 content word(s) - 13 chars - quote=false/none - parenthetical=false/0 - navigation=45%/p3
- [68] "the prime" - 440ms base / 440ms effective - normal - 1 content word(s) - 9 chars - quote=false/none - parenthetical=false/0 - navigation=46%/p3

Next chunks:
- [70] "while conservatives" - 690ms base / 690ms effective - dense - 2 content word(s) - 19 chars - quote=false/none - parenthetical=false/0 - navigation=47%/p3
- [71] "held" - 400ms base / 400ms effective - normal - 1 content word(s) - 4 chars - quote=false/none - parenthetical=false/0 - navigation=48%/p3
- [72] "the presidency." - 620ms base / 620ms effective - normal - 1 content word(s) - 15 chars - quote=false/none - parenthetical=false/0 - navigation=48%/p3

## Session Summary

Event count: 50
Rewind count: 20
Pause count: 8
Speed change count: 0
Adaptation count: 0
Completed: true
Elapsed session ms: 637637
Estimated remaining chunks: 84
Average effective duration ms: 556
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

---

<!-- Source: defect_20260710_152356_e53c11.md.gz -->

# Semantic RSVP Defect Report

Report ID: defect_20260710_152356_e53c11
Created at: 2026-07-10T15:23:56.892210Z

## Classification

Category: layout_or_visibility_issue
Severity: 2
Notes:
Unexpected small chunk

Preferred behavior:
Smaller font for no apparent reason, this time the ghost got smaller too, but again, no obvious reason for the downscaling.

## Reader State

Current index: 76
Sentence index: 8
Playback speed: 1x
Adaptation enabled: false

Current chunk:
underestimated.

## Timing Context

Base duration ms: 620
Effective duration ms: 620
Playback speed: 1x
Duration source: schedule
Current syntactic hint: normal
Current content word count: 1
Character length: 15
In quote: false
Quote boundary: none
In parenthetical: false
Parenthetical depth: 0
Navigation progress percent: 51
Navigation paragraph index: 4

## Navigability Context

Previous displayed chunk:
- Index: 75
- Text: was initially
- Duration ms: 440
- Progress percent: 50
- Paragraph index: 4

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
His successor, Ali Khamenei, was initially underestimated.

Previous chunks:
- [73] "His successor," - 650ms base / 650ms effective - dense - 2 content word(s) - 14 chars - quote=false/none - parenthetical=false/0 - navigation=49%/p4
- [74] "Ali Khamenei," - 660ms base / 660ms effective - dense - 2 content word(s) - 13 chars - quote=false/none - parenthetical=false/0 - navigation=50%/p4
- [75] "was initially" - 440ms base / 440ms effective - normal - 1 content word(s) - 13 chars - quote=false/none - parenthetical=false/0 - navigation=50%/p4

Next chunks:
- [77] "He had far" - 600ms base / 600ms effective - dense - 2 content word(s) - 10 chars - quote=false/none - parenthetical=false/0 - navigation=52%/p4
- [78] "less impressive" - 650ms base / 650ms effective - dense - 2 content word(s) - 15 chars - quote=false/none - parenthetical=false/0 - navigation=52%/p4
- [79] "religious credentials," - 750ms base / 750ms effective - dense - 2 content word(s) - 22 chars - quote=false/none - parenthetical=false/0 - navigation=53%/p4

## Session Summary

Event count: 66
Rewind count: 29
Pause count: 10
Speed change count: 0
Adaptation count: 0
Completed: true
Elapsed session ms: 798684
Estimated remaining chunks: 77
Average effective duration ms: 556
Last adaptation reason: 
Last adaptation direction: 

## Client

User agent:
Mozilla/5.0 (Android 16; Mobile; rv:152.0) Gecko/152.0 Firefox/152.0

Viewport:
384x678

Display:
Reader width px: 368
Chunk scroll width px: 340
Chunk client width px: 340
Chunk may overflow: false

---

<!-- Source: defect_20260710_152538_4b838c.md.gz -->

# Semantic RSVP Defect Report

Report ID: defect_20260710_152538_4b838c
Created at: 2026-07-10T15:25:38.384569Z

## Classification

Category: layout_or_visibility_issue
Severity: 2
Notes:
Far less impressive is one thing

Preferred behavior:
Don't split qualifier/quantifier pairs (wr should have a rule for this already). Stuff lime too much, far less, quite a few, these are all atomic units

## Reader State

Current index: 78
Sentence index: 9
Playback speed: 1x
Adaptation enabled: false

Current chunk:
less impressive

## Timing Context

Base duration ms: 650
Effective duration ms: 650
Playback speed: 1x
Duration source: schedule
Current syntactic hint: dense
Current content word count: 2
Character length: 15
In quote: false
Quote boundary: none
In parenthetical: false
Parenthetical depth: 0
Navigation progress percent: 52
Navigation paragraph index: 4

## Navigability Context

Previous displayed chunk:
- Index: 77
- Text: He had far
- Duration ms: 600
- Progress percent: 52
- Paragraph index: 4

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
He had far less impressive religious credentials, and was believed to be less powerful than the president at the time, Ali Akbar Hashemi Rafsanjani.

Previous chunks:
- [75] "was initially" - 440ms base / 440ms effective - normal - 1 content word(s) - 13 chars - quote=false/none - parenthetical=false/0 - navigation=50%/p4
- [76] "underestimated." - 620ms base / 620ms effective - normal - 1 content word(s) - 15 chars - quote=false/none - parenthetical=false/0 - navigation=51%/p4
- [77] "He had far" - 600ms base / 600ms effective - dense - 2 content word(s) - 10 chars - quote=false/none - parenthetical=false/0 - navigation=52%/p4

Next chunks:
- [79] "religious credentials," - 750ms base / 750ms effective - dense - 2 content word(s) - 22 chars - quote=false/none - parenthetical=false/0 - navigation=53%/p4
- [80] "and was believed" - 440ms base / 440ms effective - normal - 1 content word(s) - 16 chars - quote=false/none - parenthetical=false/0 - navigation=54%/p4
- [81] "to be less powerful" - 640ms base / 640ms effective - dense - 2 content word(s) - 19 chars - quote=false/none - parenthetical=false/0 - navigation=55%/p4

## Session Summary

Event count: 71
Rewind count: 31
Pause count: 11
Speed change count: 0
Adaptation count: 0
Completed: true
Elapsed session ms: 900199
Estimated remaining chunks: 75
Average effective duration ms: 556
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

---

<!-- Source: defect_20260710_152545_68cfb8.md.gz -->

# Semantic RSVP Defect Report

Report ID: defect_20260710_152545_68cfb8
Created at: 2026-07-10T15:25:45.682721Z

## Classification

Category: bad_chunk_split
Severity: 2
Notes:
Far less impressive is one thing

Preferred behavior:
Don't split qualifier/quantifier pairs (wr should have a rule for this already). Stuff lime too much, far less, quite a few, these are all atomic units

## Reader State

Current index: 78
Sentence index: 9
Playback speed: 1x
Adaptation enabled: false

Current chunk:
less impressive

## Timing Context

Base duration ms: 650
Effective duration ms: 650
Playback speed: 1x
Duration source: schedule
Current syntactic hint: dense
Current content word count: 2
Character length: 15
In quote: false
Quote boundary: none
In parenthetical: false
Parenthetical depth: 0
Navigation progress percent: 52
Navigation paragraph index: 4

## Navigability Context

Previous displayed chunk:
- Index: 77
- Text: He had far
- Duration ms: 600
- Progress percent: 52
- Paragraph index: 4

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
He had far less impressive religious credentials, and was believed to be less powerful than the president at the time, Ali Akbar Hashemi Rafsanjani.

Previous chunks:
- [75] "was initially" - 440ms base / 440ms effective - normal - 1 content word(s) - 13 chars - quote=false/none - parenthetical=false/0 - navigation=50%/p4
- [76] "underestimated." - 620ms base / 620ms effective - normal - 1 content word(s) - 15 chars - quote=false/none - parenthetical=false/0 - navigation=51%/p4
- [77] "He had far" - 600ms base / 600ms effective - dense - 2 content word(s) - 10 chars - quote=false/none - parenthetical=false/0 - navigation=52%/p4

Next chunks:
- [79] "religious credentials," - 750ms base / 750ms effective - dense - 2 content word(s) - 22 chars - quote=false/none - parenthetical=false/0 - navigation=53%/p4
- [80] "and was believed" - 440ms base / 440ms effective - normal - 1 content word(s) - 16 chars - quote=false/none - parenthetical=false/0 - navigation=54%/p4
- [81] "to be less powerful" - 640ms base / 640ms effective - dense - 2 content word(s) - 19 chars - quote=false/none - parenthetical=false/0 - navigation=55%/p4

## Session Summary

Event count: 72
Rewind count: 31
Pause count: 11
Speed change count: 0
Adaptation count: 0
Completed: true
Elapsed session ms: 907481
Estimated remaining chunks: 75
Average effective duration ms: 556
Last adaptation reason: 
Last adaptation direction: 

## Client

User agent:
Mozilla/5.0 (Android 16; Mobile; rv:152.0) Gecko/152.0 Firefox/152.0

Viewport:
384x678

Display:
Reader width px: 368
Chunk scroll width px: 340
Chunk client width px: 340
Chunk may overflow: false

---

<!-- Source: defect_20260710_152904_5f2a48.md.gz -->

# Semantic RSVP Defect Report

Report ID: defect_20260710_152904_5f2a48
Created at: 2026-07-10T15:29:04.255194Z

## Classification

Category: bad_chunk_split
Severity: 3
Notes:
The meaning changed because of the awkward split

Preferred behavior:
Verb + quantifier does not equal verb + qualifier + d.obj. In this case instead of increasing his democratness it sounds like he's evolving to become more, which leaves the lone d.obj with last stop at semantic oblivion

## Reader State

Current index: 100
Sentence index: 10
Playback speed: 1x
Adaptation enabled: false

Current chunk:
democratic.

## Timing Context

Base duration ms: 620
Effective duration ms: 620
Playback speed: 1x
Duration source: schedule
Current syntactic hint: normal
Current content word count: 1
Character length: 11
In quote: false
Quote boundary: none
In parenthetical: false
Parenthetical depth: 0
Navigation progress percent: 67
Navigation paragraph index: 5

## Navigability Context

Previous displayed chunk:
- Index: 99
- Text: to become more
- Duration ms: 600
- Progress percent: 66
- Paragraph index: 5

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
Over time, he revealed his ambition and agenda, as he drew close to Iran’s security services and proved willing to repress even loyal factions that wanted Iran’s system to become more democratic.

Previous chunks:
- [97] "factions that wanted" - 640ms base / 640ms effective - dense - 2 content word(s) - 20 chars - quote=false/none - parenthetical=false/0 - navigation=65%/p5
- [98] "Iran’s system" - 600ms base / 600ms effective - dense - 2 content word(s) - 13 chars - quote=false/none - parenthetical=false/0 - navigation=66%/p5
- [99] "to become more" - 600ms base / 600ms effective - dense - 2 content word(s) - 14 chars - quote=false/none - parenthetical=false/0 - navigation=66%/p5

Next chunks:
- [101] "That was most" - 440ms base / 440ms effective - normal - 1 content word(s) - 13 chars - quote=false/none - parenthetical=false/0 - navigation=67%/p5
- [102] "evident when" - 600ms base / 600ms effective - dense - 2 content word(s) - 12 chars - quote=false/none - parenthetical=false/0 - navigation=68%/p5
- [103] "he crushed" - 600ms base / 600ms effective - dense - 2 content word(s) - 10 chars - quote=false/none - parenthetical=false/0 - navigation=69%/p5

## Session Summary

Event count: 79
Rewind count: 35
Pause count: 12
Speed change count: 0
Adaptation count: 0
Completed: true
Elapsed session ms: 1106068
Estimated remaining chunks: 53
Average effective duration ms: 556
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

---

<!-- Source: defect_20260710_153207_75b6dd.md.gz -->

# Semantic RSVP Defect Report

Report ID: defect_20260710_153207_75b6dd
Created at: 2026-07-10T15:32:07.888744Z

## Classification

Category: underdense_chunk
Severity: 2
Notes:
Too short

Preferred behavior:
A compound subject like this should be chunked together before introducing the verb. In this case 'the men who led' 'the movement' 'were loyal to' 'the Islamic Revolution.' 

## Reader State

Current index: 109
Sentence index: 12
Playback speed: 1x
Adaptation enabled: false

Current chunk:
led

## Timing Context

Base duration ms: 400
Effective duration ms: 400
Playback speed: 1x
Duration source: schedule
Current syntactic hint: normal
Current content word count: 1
Character length: 3
In quote: false
Quote boundary: none
In parenthetical: false
Parenthetical depth: 0
Navigation progress percent: 71
Navigation paragraph index: 5

## Navigability Context

Previous displayed chunk:
- Index: 108
- Text: men who
- Duration ms: 560
- Progress percent: 71
- Paragraph index: 5

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
Although the two men who led the movement were loyal to the Islamic Revolution, they demanded that Ayatollah Khamenei address serious allegations of election fraud.

Previous chunks:
- [106] "Although" - 400ms base / 400ms effective - normal - 1 content word(s) - 8 chars - quote=false/none - parenthetical=false/0 - navigation=70%/p5
- [107] "the two" - 400ms base / 400ms effective - normal - 1 content word(s) - 7 chars - quote=false/none - parenthetical=false/0 - navigation=70%/p5
- [108] "men who" - 560ms base / 560ms effective - dense - 2 content word(s) - 7 chars - quote=false/none - parenthetical=false/0 - navigation=71%/p5

Next chunks:
- [110] "the movement were loyal" - 640ms base / 640ms effective - dense - 2 content word(s) - 23 chars - quote=false/none - parenthetical=false/0 - navigation=72%/p5
- [111] "to the Islamic Revolution," - 750ms base / 750ms effective - dense - 2 content word(s) - 26 chars - quote=false/none - parenthetical=false/0 - navigation=73%/p5
- [112] "they demanded that" - 600ms base / 600ms effective - dense - 2 content word(s) - 18 chars - quote=false/none - parenthetical=false/0 - navigation=74%/p5

## Session Summary

Event count: 91
Rewind count: 41
Pause count: 13
Speed change count: 0
Adaptation count: 0
Completed: true
Elapsed session ms: 1289706
Estimated remaining chunks: 44
Average effective duration ms: 556
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

---

<!-- Source: defect_20260710_153416_b4d23d.md.gz -->

# Semantic RSVP Defect Report

Report ID: defect_20260710_153416_b4d23d
Created at: 2026-07-10T15:34:16.975255Z

## Classification

Category: bad_chunk_split
Severity: 2
Notes:
Built up is one thing

Preferred behavior:
Don't separate auxiliary words from their idiomatic verbs. Build up, reach out, get on, take off. These can never be split unless there's a word between them.

## Reader State

Current index: 121
Sentence index: 13
Playback speed: 1x
Adaptation enabled: false

Current chunk:
up his

## Timing Context

Base duration ms: 560
Effective duration ms: 560
Playback speed: 1x
Duration source: schedule
Current syntactic hint: dense
Current content word count: 2
Character length: 6
In quote: false
Quote boundary: none
In parenthetical: false
Parenthetical depth: 0
Navigation progress percent: 80
Navigation paragraph index: 6

## Navigability Context

Previous displayed chunk:
- Index: 120
- Text: had built
- Duration ms: 440
- Progress percent: 79
- Paragraph index: 6

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
By the time of his death, Ali Khamenei had built up his office into a bureaucratic behemoth that inserted itself across Iran’s government, enabling him to oversee the country’s military, intelligence, economy and foreign affairs.

Previous chunks:
- [118] "of his death," - 600ms base / 600ms effective - dense - 2 content word(s) - 13 chars - quote=false/none - parenthetical=false/0 - navigation=78%/p6
- [119] "Ali Khamenei" - 660ms base / 660ms effective - dense - 2 content word(s) - 12 chars - quote=false/none - parenthetical=false/0 - navigation=79%/p6
- [120] "had built" - 440ms base / 440ms effective - normal - 1 content word(s) - 9 chars - quote=false/none - parenthetical=false/0 - navigation=79%/p6

Next chunks:
- [122] "office into" - 600ms base / 600ms effective - dense - 2 content word(s) - 11 chars - quote=false/none - parenthetical=false/0 - navigation=80%/p6
- [123] "a bureaucratic" - 440ms base / 440ms effective - normal - 1 content word(s) - 14 chars - quote=false/none - parenthetical=false/0 - navigation=81%/p6
- [124] "behemoth that inserted" - 640ms base / 640ms effective - dense - 2 content word(s) - 22 chars - quote=false/none - parenthetical=false/0 - navigation=82%/p6

## Session Summary

Event count: 97
Rewind count: 44
Pause count: 14
Speed change count: 0
Adaptation count: 0
Completed: true
Elapsed session ms: 1418799
Estimated remaining chunks: 32
Average effective duration ms: 556
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

---

<!-- Source: defect_20260710_153853_fd3041.md.gz -->

# Semantic RSVP Defect Report

Report ID: defect_20260710_153853_fd3041
Created at: 2026-07-10T15:38:53.471593Z

## Classification

Category: overlong_chunk
Severity: 2
Notes:
Too long

Preferred behavior:
Quasi-governmental is dense enough on its own, no need to ctowd it

## Reader State

Current index: 28
Sentence index: 1
Playback speed: 1x
Adaptation enabled: false

Current chunk:
quasi-governmental business

## Timing Context

Base duration ms: 750
Effective duration ms: 750
Playback speed: 1x
Duration source: schedule
Current syntactic hint: dense
Current content word count: 2
Character length: 27
In quote: false
Quote boundary: none
In parenthetical: false
Parenthetical depth: 0
Navigation progress percent: 40
Navigation paragraph index: 0

## Navigability Context

Previous displayed chunk:
- Index: 27
- Text: several wealthy
- Duration ms: 600
- Progress percent: 38
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
In addition to inheriting his father’s bureaucracy, he also has official control over several wealthy quasi-governmental business conglomerates.

Previous chunks:
- [25] "has official" - 440ms base / 440ms effective - normal - 1 content word(s) - 12 chars - quote=false/none - parenthetical=false/0 - navigation=35%/p0
- [26] "control over" - 600ms base / 600ms effective - dense - 2 content word(s) - 12 chars - quote=false/none - parenthetical=false/0 - navigation=36%/p0
- [27] "several wealthy" - 600ms base / 600ms effective - dense - 2 content word(s) - 15 chars - quote=false/none - parenthetical=false/0 - navigation=38%/p0

Next chunks:
- [29] "conglomerates." - 620ms base / 620ms effective - normal - 1 content word(s) - 14 chars - quote=false/none - parenthetical=false/0 - navigation=42%/p0
- [30] "I don’t" - 560ms base / 560ms effective - dense - 2 content word(s) - 7 chars - quote=false/none - parenthetical=false/0 - navigation=43%/p1
- [31] "think" - 400ms base / 400ms effective - normal - 1 content word(s) - 5 chars - quote=false/none - parenthetical=false/0 - navigation=43%/p1

## Session Summary

Event count: 22
Rewind count: 6
Pause count: 5
Speed change count: 0
Adaptation count: 0
Completed: false
Elapsed session ms: 216816
Estimated remaining chunks: 42
Average effective duration ms: 549
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

---

<!-- Source: defect_20260710_154142_1e822a.md.gz -->

# Semantic RSVP Defect Report

Report ID: defect_20260710_154142_1e822a
Created at: 2026-07-10T15:41:42.237589Z

## Classification

Category: bad_chunk_split
Severity: 2
Notes:
Business conglomerates is one thing

Preferred behavior:
Don't split identifying adjectives from their immediate nouns 'pretty girl' 'first born' 'great depression' 'abundant supplies. Although in this case the two words actually mean one thing

## Reader State

Current index: 29
Sentence index: 1
Playback speed: 1x
Adaptation enabled: false

Current chunk:
conglomerates.

## Timing Context

Base duration ms: 620
Effective duration ms: 620
Playback speed: 1x
Duration source: schedule
Current syntactic hint: normal
Current content word count: 1
Character length: 14
In quote: false
Quote boundary: none
In parenthetical: false
Parenthetical depth: 0
Navigation progress percent: 42
Navigation paragraph index: 0

## Navigability Context

Previous displayed chunk:
- Index: 28
- Text: quasi-governmental business
- Duration ms: 750
- Progress percent: 40
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
In addition to inheriting his father’s bureaucracy, he also has official control over several wealthy quasi-governmental business conglomerates.

Previous chunks:
- [26] "control over" - 600ms base / 600ms effective - dense - 2 content word(s) - 12 chars - quote=false/none - parenthetical=false/0 - navigation=36%/p0
- [27] "several wealthy" - 600ms base / 600ms effective - dense - 2 content word(s) - 15 chars - quote=false/none - parenthetical=false/0 - navigation=38%/p0
- [28] "quasi-governmental business" - 750ms base / 750ms effective - dense - 2 content word(s) - 27 chars - quote=false/none - parenthetical=false/0 - navigation=40%/p0

Next chunks:
- [30] "I don’t" - 560ms base / 560ms effective - dense - 2 content word(s) - 7 chars - quote=false/none - parenthetical=false/0 - navigation=43%/p1
- [31] "think" - 400ms base / 400ms effective - normal - 1 content word(s) - 5 chars - quote=false/none - parenthetical=false/0 - navigation=43%/p1
- [32] "the supreme leader" - 600ms base / 600ms effective - dense - 2 content word(s) - 18 chars - quote=false/none - parenthetical=false/0 - navigation=45%/p1

## Session Summary

Event count: 26
Rewind count: 7
Pause count: 6
Speed change count: 0
Adaptation count: 0
Completed: false
Elapsed session ms: 385611
Estimated remaining chunks: 41
Average effective duration ms: 549
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

---

<!-- Source: defect_20260710_154244_8b68e7.md.gz -->

# Semantic RSVP Defect Report

Report ID: defect_20260710_154244_8b68e7
Created at: 2026-07-10T15:42:44.741686Z

## Classification

Category: underdense_chunk
Severity: 2
Notes:
Too short

Preferred behavior:
Should have been 'I don't think'

## Reader State

Current index: 31
Sentence index: 2
Playback speed: 1x
Adaptation enabled: false

Current chunk:
think

## Timing Context

Base duration ms: 400
Effective duration ms: 400
Playback speed: 1x
Duration source: schedule
Current syntactic hint: normal
Current content word count: 1
Character length: 5
In quote: false
Quote boundary: none
In parenthetical: false
Parenthetical depth: 0
Navigation progress percent: 43
Navigation paragraph index: 1

## Navigability Context

Previous displayed chunk:
- Index: 30
- Text: I don’t
- Duration ms: 560
- Progress percent: 43
- Paragraph index: 1

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
“I don’t think the supreme leader can be neutralized,” Mr. Takeyh said.

Previous chunks:
- [28] "quasi-governmental business" - 750ms base / 750ms effective - dense - 2 content word(s) - 27 chars - quote=false/none - parenthetical=false/0 - navigation=40%/p0
- [29] "conglomerates." - 620ms base / 620ms effective - normal - 1 content word(s) - 14 chars - quote=false/none - parenthetical=false/0 - navigation=42%/p0
- [30] "I don’t" - 560ms base / 560ms effective - dense - 2 content word(s) - 7 chars - quote=false/none - parenthetical=false/0 - navigation=43%/p1

Next chunks:
- [32] "the supreme leader" - 600ms base / 600ms effective - dense - 2 content word(s) - 18 chars - quote=false/none - parenthetical=false/0 - navigation=45%/p1
- [33] "can be neutralized," - 480ms base / 480ms effective - normal - 1 content word(s) - 19 chars - quote=false/none - parenthetical=false/0 - navigation=47%/p1
- [34] "Mr. Takeyh" - 600ms base / 600ms effective - dense - 2 content word(s) - 10 chars - quote=false/none - parenthetical=false/0 - navigation=48%/p1

## Session Summary

Event count: 32
Rewind count: 10
Pause count: 7
Speed change count: 0
Adaptation count: 0
Completed: false
Elapsed session ms: 448123
Estimated remaining chunks: 39
Average effective duration ms: 549
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

---

<!-- Source: defect_20260710_154343_306d93.md.gz -->

# Semantic RSVP Defect Report

Report ID: defect_20260710_154343_306d93
Created at: 2026-07-10T15:43:43.446854Z

## Classification

Category: underdense_chunk
Severity: 2
Notes:
Too short

Preferred behavior:
Should have been 'Mr. Takeyh said.'

## Reader State

Current index: 35
Sentence index: 2
Playback speed: 1x
Adaptation enabled: false

Current chunk:
said.

## Timing Context

Base duration ms: 580
Effective duration ms: 580
Playback speed: 1x
Duration source: schedule
Current syntactic hint: normal
Current content word count: 1
Character length: 5
In quote: false
Quote boundary: none
In parenthetical: false
Parenthetical depth: 0
Navigation progress percent: 49
Navigation paragraph index: 1

## Navigability Context

Previous displayed chunk:
- Index: 34
- Text: Mr. Takeyh
- Duration ms: 600
- Progress percent: 48
- Paragraph index: 1

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
“I don’t think the supreme leader can be neutralized,” Mr. Takeyh said.

Previous chunks:
- [32] "the supreme leader" - 600ms base / 600ms effective - dense - 2 content word(s) - 18 chars - quote=false/none - parenthetical=false/0 - navigation=45%/p1
- [33] "can be neutralized," - 480ms base / 480ms effective - normal - 1 content word(s) - 19 chars - quote=false/none - parenthetical=false/0 - navigation=47%/p1
- [34] "Mr. Takeyh" - 600ms base / 600ms effective - dense - 2 content word(s) - 10 chars - quote=false/none - parenthetical=false/0 - navigation=48%/p1

Next chunks:
- [36] "There’s so much" - 600ms base / 600ms effective - dense - 2 content word(s) - 15 chars - quote=false/none - parenthetical=false/0 - navigation=51%/p1
- [37] "institutional power" - 690ms base / 690ms effective - dense - 2 content word(s) - 19 chars - quote=false/none - parenthetical=false/0 - navigation=53%/p1
- [38] "and so much money" - 600ms base / 600ms effective - dense - 2 content word(s) - 17 chars - quote=false/none - parenthetical=false/0 - navigation=54%/p1

## Session Summary

Event count: 37
Rewind count: 12
Pause count: 8
Speed change count: 0
Adaptation count: 0
Completed: false
Elapsed session ms: 506819
Estimated remaining chunks: 35
Average effective duration ms: 549
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

---

<!-- Source: defect_20260710_154430_68d809.md.gz -->

# Semantic RSVP Defect Report

Report ID: defect_20260710_154430_68d809
Created at: 2026-07-10T15:44:30.041085Z

## Classification

Category: layout_or_visibility_issue
Severity: 2
Notes:
Suddenly small

Preferred behavior:
For no apparent reason the font size was reduced.

## Reader State

Current index: 37
Sentence index: 3
Playback speed: 1x
Adaptation enabled: false

Current chunk:
institutional power

## Timing Context

Base duration ms: 690
Effective duration ms: 690
Playback speed: 1x
Duration source: schedule
Current syntactic hint: dense
Current content word count: 2
Character length: 19
In quote: false
Quote boundary: none
In parenthetical: false
Parenthetical depth: 0
Navigation progress percent: 53
Navigation paragraph index: 1

## Navigability Context

Previous displayed chunk:
- Index: 36
- Text: There’s so much
- Duration ms: 600
- Progress percent: 51
- Paragraph index: 1

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
“There’s so much institutional power and so much money that if the supreme leader is functional, then I think that institutional power cannot be negated by alternative centers.”

Previous chunks:
- [34] "Mr. Takeyh" - 600ms base / 600ms effective - dense - 2 content word(s) - 10 chars - quote=false/none - parenthetical=false/0 - navigation=48%/p1
- [35] "said." - 580ms base / 580ms effective - normal - 1 content word(s) - 5 chars - quote=false/none - parenthetical=false/0 - navigation=49%/p1
- [36] "There’s so much" - 600ms base / 600ms effective - dense - 2 content word(s) - 15 chars - quote=false/none - parenthetical=false/0 - navigation=51%/p1

Next chunks:
- [38] "and so much money" - 600ms base / 600ms effective - dense - 2 content word(s) - 17 chars - quote=false/none - parenthetical=false/0 - navigation=54%/p1
- [39] "that if the" - 340ms base / 340ms effective - light - 0 content word(s) - 11 chars - quote=false/none - parenthetical=false/0 - navigation=56%/p1
- [40] "supreme leader" - 600ms base / 600ms effective - dense - 2 content word(s) - 14 chars - quote=false/none - parenthetical=false/0 - navigation=57%/p1

## Session Summary

Event count: 43
Rewind count: 15
Pause count: 9
Speed change count: 0
Adaptation count: 0
Completed: false
Elapsed session ms: 553445
Estimated remaining chunks: 33
Average effective duration ms: 549
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

---

<!-- Source: defect_20260710_154536_9a2fef.md.gz -->

# Semantic RSVP Defect Report

Report ID: defect_20260710_154536_9a2fef
Created at: 2026-07-10T15:45:36.517885Z

## Classification

Category: underdense_chunk
Severity: 2
Notes:
Too short, loses meaning

Preferred behavior:
Should have been 'overlooks the fact'

## Reader State

Current index: 50
Sentence index: 4
Playback speed: 1x
Adaptation enabled: false

Current chunk:
overlooks

## Timing Context

Base duration ms: 440
Effective duration ms: 440
Playback speed: 1x
Duration source: schedule
Current syntactic hint: normal
Current content word count: 1
Character length: 9
In quote: false
Quote boundary: none
In parenthetical: false
Parenthetical depth: 0
Navigation progress percent: 72
Navigation paragraph index: 2

## Navigability Context

Previous displayed chunk:
- Index: 49
- Text: with his father
- Duration ms: 600
- Progress percent: 71
- Paragraph index: 2

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
To some, the comparison with his father overlooks the fact that Mojtaba Khamenei is taking up the position with distinct disadvantages, including that he hasn’t yet been able to assert himself publicly.

Previous chunks:
- [47] "To some," - 400ms base / 400ms effective - normal - 1 content word(s) - 8 chars - quote=false/none - parenthetical=false/0 - navigation=67%/p2
- [48] "the comparison" - 440ms base / 440ms effective - normal - 1 content word(s) - 14 chars - quote=false/none - parenthetical=false/0 - navigation=69%/p2
- [49] "with his father" - 600ms base / 600ms effective - dense - 2 content word(s) - 15 chars - quote=false/none - parenthetical=false/0 - navigation=71%/p2

Next chunks:
- [51] "the fact that Mojtaba" - 640ms base / 640ms effective - dense - 2 content word(s) - 21 chars - quote=false/none - parenthetical=false/0 - navigation=74%/p2
- [52] "Khamenei is taking" - 600ms base / 600ms effective - dense - 2 content word(s) - 18 chars - quote=false/none - parenthetical=false/0 - navigation=76%/p2
- [53] "up" - 400ms base / 400ms effective - normal - 1 content word(s) - 2 chars - quote=false/none - parenthetical=false/0 - navigation=76%/p2

## Session Summary

Event count: 50
Rewind count: 19
Pause count: 10
Speed change count: 0
Adaptation count: 0
Completed: false
Elapsed session ms: 619905
Estimated remaining chunks: 20
Average effective duration ms: 549
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

---

<!-- Source: defect_20260710_154826_15fab7.md.gz -->

# Semantic RSVP Defect Report

Report ID: defect_20260710_154826_15fab7
Created at: 2026-07-10T15:48:26.872237Z

## Classification

Category: bad_chunk_split
Severity: 2
Notes:
Lost track at this stop

Preferred behavior:
Should have been 'wields great power'

## Reader State

Current index: 31
Sentence index: 4
Playback speed: 1x
Adaptation enabled: false

Current chunk:
power,

## Timing Context

Base duration ms: 400
Effective duration ms: 400
Playback speed: 1x
Duration source: schedule
Current syntactic hint: normal
Current content word count: 1
Character length: 6
In quote: false
Quote boundary: none
In parenthetical: false
Parenthetical depth: 0
Navigation progress percent: 22
Navigation paragraph index: 2

## Navigability Context

Previous displayed chunk:
- Index: 30
- Text: wields great
- Duration ms: 600
- Progress percent: 22
- Paragraph index: 2

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
Under Iran’s Constitution, the position wields great power, but that authority has typically been defined more by the supreme leader himself and his followers’ zeal.

Previous chunks:
- [28] "Under Iran’s Constitution," - 750ms base / 750ms effective - dense - 2 content word(s) - 26 chars - quote=false/none - parenthetical=false/0 - navigation=21%/p2
- [29] "the position" - 440ms base / 440ms effective - normal - 1 content word(s) - 12 chars - quote=false/none - parenthetical=false/0 - navigation=21%/p2
- [30] "wields great" - 600ms base / 600ms effective - dense - 2 content word(s) - 12 chars - quote=false/none - parenthetical=false/0 - navigation=22%/p2

Next chunks:
- [32] "but that authority" - 440ms base / 440ms effective - normal - 1 content word(s) - 18 chars - quote=false/none - parenthetical=false/0 - navigation=23%/p2
- [33] "has typically been defined" - 690ms base / 690ms effective - dense - 2 content word(s) - 26 chars - quote=false/none - parenthetical=false/0 - navigation=24%/p2
- [34] "more by" - 400ms base / 400ms effective - normal - 1 content word(s) - 7 chars - quote=false/none - parenthetical=false/0 - navigation=25%/p2

## Session Summary

Event count: 17
Rewind count: 7
Pause count: 3
Speed change count: 0
Adaptation count: 0
Completed: false
Elapsed session ms: 107882
Estimated remaining chunks: 122
Average effective duration ms: 556
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

---

<!-- Source: defect_20260710_155031_9303d4.md.gz -->

# Semantic RSVP Defect Report

Report ID: defect_20260710_155031_9303d4
Created at: 2026-07-10T15:50:31.695228Z

## Classification

Category: underdense_chunk
Severity: 2
Notes:
Too short

Preferred behavior:
A rare case where the verb should be chunked alone: 'enjoyed' 'enormous authority'

## Reader State

Current index: 44
Sentence index: 5
Playback speed: 1x
Adaptation enabled: false

Current chunk:
authority,

## Timing Context

Base duration ms: 460
Effective duration ms: 460
Playback speed: 1x
Duration source: schedule
Current syntactic hint: normal
Current content word count: 1
Character length: 10
In quote: false
Quote boundary: none
In parenthetical: false
Parenthetical depth: 0
Navigation progress percent: 31
Navigation paragraph index: 3

## Navigability Context

Previous displayed chunk:
- Index: 43
- Text: enjoyed enormous
- Duration ms: 600
- Progress percent: 30
- Paragraph index: 3

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
The first to hold the position, Ayatollah Khomeini, enjoyed enormous authority, largely from the force of his charisma, his religious credentials and the fact that he had led the movement that unseated Iran’s monarchy.

Previous chunks:
- [41] "the position," - 440ms base / 440ms effective - normal - 1 content word(s) - 13 chars - quote=false/none - parenthetical=false/0 - navigation=29%/p3
- [42] "Ayatollah Khomeini," - 750ms base / 750ms effective - dense - 2 content word(s) - 19 chars - quote=false/none - parenthetical=false/0 - navigation=29%/p3
- [43] "enjoyed enormous" - 600ms base / 600ms effective - dense - 2 content word(s) - 16 chars - quote=false/none - parenthetical=false/0 - navigation=30%/p3

Next chunks:
- [45] "largely from" - 440ms base / 440ms effective - normal - 1 content word(s) - 12 chars - quote=false/none - parenthetical=false/0 - navigation=31%/p3
- [46] "the force" - 440ms base / 440ms effective - normal - 1 content word(s) - 9 chars - quote=false/none - parenthetical=false/0 - navigation=32%/p3
- [47] "of his charisma," - 600ms base / 600ms effective - dense - 2 content word(s) - 16 chars - quote=false/none - parenthetical=false/0 - navigation=33%/p3

## Session Summary

Event count: 25
Rewind count: 9
Pause count: 4
Speed change count: 0
Adaptation count: 0
Completed: false
Elapsed session ms: 232727
Estimated remaining chunks: 109
Average effective duration ms: 556
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

---

<!-- Source: defect_20260710_155126_977d13.md.gz -->

# Semantic RSVP Defect Report

Report ID: defect_20260710_155126_977d13
Created at: 2026-07-10T15:51:26.016933Z

## Classification

Category: layout_or_visibility_issue
Severity: 2
Notes:
Why so small

Preferred behavior:
No evident reason the font size was reduced here

## Reader State

Current index: 57
Sentence index: 6
Playback speed: 1x
Adaptation enabled: false

Current chunk:
decision-making,

## Timing Context

Base duration ms: 440
Effective duration ms: 440
Playback speed: 1x
Duration source: schedule
Current syntactic hint: normal
Current content word count: 1
Character length: 16
In quote: false
Quote boundary: none
In parenthetical: false
Parenthetical depth: 0
Navigation progress percent: 40
Navigation paragraph index: 3

## Navigability Context

Previous displayed chunk:
- Index: 56
- Text: in on day-to- day
- Duration ms: 600
- Progress percent: 39
- Paragraph index: 3

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
He also avoided weighing in on day-to-day decision-making, and tended to seek balance between Iran’s left and right wings.

Previous chunks:
- [54] "He also" - 560ms base / 560ms effective - dense - 2 content word(s) - 7 chars - quote=false/none - parenthetical=false/0 - navigation=37%/p3
- [55] "avoided weighing" - 600ms base / 600ms effective - dense - 2 content word(s) - 16 chars - quote=false/none - parenthetical=false/0 - navigation=38%/p3
- [56] "in on day-to- day" - 600ms base / 600ms effective - dense - 2 content word(s) - 17 chars - quote=false/none - parenthetical=false/0 - navigation=39%/p3

Next chunks:
- [58] "and tended" - 440ms base / 440ms effective - normal - 1 content word(s) - 10 chars - quote=false/none - parenthetical=false/0 - navigation=40%/p3
- [59] "to seek balance" - 600ms base / 600ms effective - dense - 2 content word(s) - 15 chars - quote=false/none - parenthetical=false/0 - navigation=41%/p3
- [60] "between Iran’s" - 600ms base / 600ms effective - dense - 2 content word(s) - 14 chars - quote=false/none - parenthetical=false/0 - navigation=42%/p3

## Session Summary

Event count: 33
Rewind count: 12
Pause count: 6
Speed change count: 0
Adaptation count: 0
Completed: false
Elapsed session ms: 287049
Estimated remaining chunks: 96
Average effective duration ms: 556
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

---

<!-- Source: defect_20260710_155329_24cccc.md.gz -->

# Semantic RSVP Defect Report

Report ID: defect_20260710_155329_24cccc
Created at: 2026-07-10T15:53:29.214114Z

## Classification

Category: bad_chunk_split
Severity: 2
Notes:
Left and right wings is one thing

Preferred behavior:
This is a form that should be maintained both in singular and this expanded form 'the left wing' 'the right wing' 'the left and right wings'

## Reader State

Current index: 62
Sentence index: 6
Playback speed: 1x
Adaptation enabled: false

Current chunk:
and right

## Timing Context

Base duration ms: 440
Effective duration ms: 440
Playback speed: 1x
Duration source: schedule
Current syntactic hint: normal
Current content word count: 1
Character length: 9
In quote: false
Quote boundary: none
In parenthetical: false
Parenthetical depth: 0
Navigation progress percent: 42
Navigation paragraph index: 3

## Navigability Context

Previous displayed chunk:
- Index: 61
- Text: left
- Duration ms: 400
- Progress percent: 42
- Paragraph index: 3

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
He also avoided weighing in on day-to-day decision-making, and tended to seek balance between Iran’s left and right wings.

Previous chunks:
- [59] "to seek balance" - 600ms base / 600ms effective - dense - 2 content word(s) - 15 chars - quote=false/none - parenthetical=false/0 - navigation=41%/p3
- [60] "between Iran’s" - 600ms base / 600ms effective - dense - 2 content word(s) - 14 chars - quote=false/none - parenthetical=false/0 - navigation=42%/p3
- [61] "left" - 400ms base / 400ms effective - normal - 1 content word(s) - 4 chars - quote=false/none - parenthetical=false/0 - navigation=42%/p3

Next chunks:
- [63] "wings." - 580ms base / 580ms effective - normal - 1 content word(s) - 6 chars - quote=false/none - parenthetical=false/0 - navigation=43%/p3
- [64] "During much" - 440ms base / 440ms effective - normal - 1 content word(s) - 11 chars - quote=false/none - parenthetical=false/0 - navigation=43%/p3
- [65] "of his tenure," - 600ms base / 600ms effective - dense - 2 content word(s) - 14 chars - quote=false/none - parenthetical=false/0 - navigation=44%/p3

## Session Summary

Event count: 38
Rewind count: 14
Pause count: 7
Speed change count: 0
Adaptation count: 0
Completed: false
Elapsed session ms: 410212
Estimated remaining chunks: 91
Average effective duration ms: 556
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

---

<!-- Source: defect_20260710_155434_8c0ff2.md.gz -->

# Semantic RSVP Defect Report

Report ID: defect_20260710_155434_8c0ff2
Created at: 2026-07-10T15:54:34.025554Z

## Classification

Category: layout_or_visibility_issue
Severity: 2
Notes:
So small

Preferred behavior:
No evident reason for the font size reduction

## Reader State

Current index: 76
Sentence index: 8
Playback speed: 1x
Adaptation enabled: false

Current chunk:
underestimated.

## Timing Context

Base duration ms: 620
Effective duration ms: 620
Playback speed: 1x
Duration source: schedule
Current syntactic hint: normal
Current content word count: 1
Character length: 15
In quote: false
Quote boundary: none
In parenthetical: false
Parenthetical depth: 0
Navigation progress percent: 51
Navigation paragraph index: 4

## Navigability Context

Previous displayed chunk:
- Index: 75
- Text: was initially
- Duration ms: 440
- Progress percent: 50
- Paragraph index: 4

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
His successor, Ali Khamenei, was initially underestimated.

Previous chunks:
- [73] "His successor," - 650ms base / 650ms effective - dense - 2 content word(s) - 14 chars - quote=false/none - parenthetical=false/0 - navigation=49%/p4
- [74] "Ali Khamenei," - 660ms base / 660ms effective - dense - 2 content word(s) - 13 chars - quote=false/none - parenthetical=false/0 - navigation=50%/p4
- [75] "was initially" - 440ms base / 440ms effective - normal - 1 content word(s) - 13 chars - quote=false/none - parenthetical=false/0 - navigation=50%/p4

Next chunks:
- [77] "He had far" - 600ms base / 600ms effective - dense - 2 content word(s) - 10 chars - quote=false/none - parenthetical=false/0 - navigation=52%/p4
- [78] "less impressive" - 650ms base / 650ms effective - dense - 2 content word(s) - 15 chars - quote=false/none - parenthetical=false/0 - navigation=52%/p4
- [79] "religious credentials," - 750ms base / 750ms effective - dense - 2 content word(s) - 22 chars - quote=false/none - parenthetical=false/0 - navigation=53%/p4

## Session Summary

Event count: 60
Rewind count: 26
Pause count: 9
Speed change count: 0
Adaptation count: 0
Completed: false
Elapsed session ms: 475018
Estimated remaining chunks: 77
Average effective duration ms: 556
Last adaptation reason: 
Last adaptation direction: 

## Client

User agent:
Mozilla/5.0 (Android 16; Mobile; rv:152.0) Gecko/152.0 Firefox/152.0

Viewport:
384x678

Display:
Reader width px: 368
Chunk scroll width px: 340
Chunk client width px: 340
Chunk may overflow: false

---

<!-- Source: defect_20260710_155622_eab9c3.md.gz -->

# Semantic RSVP Defect Report

Report ID: defect_20260710_155622_eab9c3
Created at: 2026-07-10T15:56:22.526307Z

## Classification

Category: bad_chunk_split
Severity: 2
Notes:
Drew close is one action

Preferred behavior:
'As he drew close' 'to iran's' 'security services' is the only sensible split here.

## Reader State

Current index: 92
Sentence index: 10
Playback speed: 1x
Adaptation enabled: false

Current chunk:
close to Iran’s

## Timing Context

Base duration ms: 600
Effective duration ms: 600
Playback speed: 1x
Duration source: schedule
Current syntactic hint: dense
Current content word count: 2
Character length: 15
In quote: false
Quote boundary: none
In parenthetical: false
Parenthetical depth: 0
Navigation progress percent: 61
Navigation paragraph index: 5

## Navigability Context

Previous displayed chunk:
- Index: 91
- Text: as he drew
- Duration ms: 600
- Progress percent: 61
- Paragraph index: 5

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
Over time, he revealed his ambition and agenda, as he drew close to Iran’s security services and proved willing to repress even loyal factions that wanted Iran’s system to become more democratic.

Previous chunks:
- [89] "his ambition" - 600ms base / 600ms effective - dense - 2 content word(s) - 12 chars - quote=false/none - parenthetical=false/0 - navigation=60%/p5
- [90] "and agenda," - 440ms base / 440ms effective - normal - 1 content word(s) - 11 chars - quote=false/none - parenthetical=false/0 - navigation=60%/p5
- [91] "as he drew" - 600ms base / 600ms effective - dense - 2 content word(s) - 10 chars - quote=false/none - parenthetical=false/0 - navigation=61%/p5

Next chunks:
- [93] "security services" - 600ms base / 600ms effective - dense - 2 content word(s) - 17 chars - quote=false/none - parenthetical=false/0 - navigation=62%/p5
- [94] "and proved" - 440ms base / 440ms effective - normal - 1 content word(s) - 10 chars - quote=false/none - parenthetical=false/0 - navigation=63%/p5
- [95] "willing to repress" - 600ms base / 600ms effective - dense - 2 content word(s) - 18 chars - quote=false/none - parenthetical=false/0 - navigation=63%/p5

## Session Summary

Event count: 69
Rewind count: 30
Pause count: 11
Speed change count: 0
Adaptation count: 0
Completed: false
Elapsed session ms: 583581
Estimated remaining chunks: 61
Average effective duration ms: 556
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

---

<!-- Source: defect_20260710_155916_59b4eb.md.gz -->

# Semantic RSVP Defect Report

Report ID: defect_20260710_155916_59b4eb
Created at: 2026-07-10T15:59:16.145084Z

## Classification

Category: bad_chunk_split
Severity: 2
Notes:
Can't split that

Preferred behavior:
'The end of war' 'without' 'the end of power' is the ideal split here.

## Reader State

Current index: 1
Sentence index: 0
Playback speed: 1x
Adaptation enabled: false

Current chunk:
of War Without

## Timing Context

Base duration ms: 660
Effective duration ms: 660
Playback speed: 1x
Duration source: schedule
Current syntactic hint: dense
Current content word count: 2
Character length: 14
In quote: false
Quote boundary: none
In parenthetical: false
Parenthetical depth: 0
Navigation progress percent: 0
Navigation paragraph index: 0

## Navigability Context

Previous displayed chunk:
- Index: 0
- Text: The End
- Duration ms: 400
- Progress percent: 0
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
The End of War Without the End of Power
Toward a Global Security System Built on Economic Deterrence
Alex
Apr 02, 2026

There is a persistent mistake in how we imagine peace.

Previous chunks:
- [0] "The End" - 400ms base / 400ms effective - normal - 1 content word(s) - 7 chars - quote=false/none - parenthetical=false/0 - navigation=0%/p0

Next chunks:
- [2] "the End" - 400ms base / 400ms effective - normal - 1 content word(s) - 7 chars - quote=false/none - parenthetical=false/0 - navigation=0%/p0
- [3] "of Power Toward" - 660ms base / 660ms effective - dense - 2 content word(s) - 15 chars - quote=false/none - parenthetical=false/0 - navigation=0%/p0
- [4] "a Global" - 400ms base / 400ms effective - normal - 1 content word(s) - 8 chars - quote=false/none - parenthetical=false/0 - navigation=0%/p0

## Session Summary

Event count: 9
Rewind count: 5
Pause count: 1
Speed change count: 0
Adaptation count: 0
Completed: false
Elapsed session ms: 88892
Estimated remaining chunks: 851
Average effective duration ms: 581
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

---

<!-- Source: defect_20260710_160144_c6e929.md.gz -->

# Semantic RSVP Defect Report

Report ID: defect_20260710_160144_c6e929
Created at: 2026-07-10T16:01:44.657424Z

## Classification

Category: bad_chunk_split
Severity: 2
Notes:
Huh?

Preferred behavior:
This is a line and heading break in the original text but for some reason we didn't split properly:  'the end of power' ' toward a global' 'security system'

## Reader State

Current index: 3
Sentence index: 0
Playback speed: 1x
Adaptation enabled: false

Current chunk:
of Power Toward

## Timing Context

Base duration ms: 660
Effective duration ms: 660
Playback speed: 1x
Duration source: schedule
Current syntactic hint: dense
Current content word count: 2
Character length: 15
In quote: false
Quote boundary: none
In parenthetical: false
Parenthetical depth: 0
Navigation progress percent: 0
Navigation paragraph index: 0

## Navigability Context

Previous displayed chunk:
- Index: 2
- Text: the End
- Duration ms: 400
- Progress percent: 0
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
The End of War Without the End of Power
Toward a Global Security System Built on Economic Deterrence
Alex
Apr 02, 2026

There is a persistent mistake in how we imagine peace.

Previous chunks:
- [0] "The End" - 400ms base / 400ms effective - normal - 1 content word(s) - 7 chars - quote=false/none - parenthetical=false/0 - navigation=0%/p0
- [1] "of War Without" - 660ms base / 660ms effective - dense - 2 content word(s) - 14 chars - quote=false/none - parenthetical=false/0 - navigation=0%/p0
- [2] "the End" - 400ms base / 400ms effective - normal - 1 content word(s) - 7 chars - quote=false/none - parenthetical=false/0 - navigation=0%/p0

Next chunks:
- [4] "a Global" - 400ms base / 400ms effective - normal - 1 content word(s) - 8 chars - quote=false/none - parenthetical=false/0 - navigation=0%/p0
- [5] "Security System" - 660ms base / 660ms effective - dense - 2 content word(s) - 15 chars - quote=false/none - parenthetical=false/0 - navigation=0%/p0
- [6] "Built on Economic" - 660ms base / 660ms effective - dense - 2 content word(s) - 17 chars - quote=false/none - parenthetical=false/0 - navigation=0%/p0

## Session Summary

Event count: 17
Rewind count: 10
Pause count: 2
Speed change count: 0
Adaptation count: 0
Completed: false
Elapsed session ms: 237406
Estimated remaining chunks: 849
Average effective duration ms: 581
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

---

<!-- Source: defect_20260710_160305_646c57.md.gz -->

# Semantic RSVP Defect Report

Report ID: defect_20260710_160305_646c57
Created at: 2026-07-10T16:03:05.900477Z

## Classification

Category: bad_chunk_split
Severity: 2
Notes:
Who is Deterrence Alex?

Preferred behavior:
Line split not respected causing confusion. 'Built on' 'economic deterrence' 'Alex'

## Reader State

Current index: 7
Sentence index: 0
Playback speed: 1x
Adaptation enabled: false

Current chunk:
Deterrence Alex

## Timing Context

Base duration ms: 710
Effective duration ms: 710
Playback speed: 1x
Duration source: schedule
Current syntactic hint: dense
Current content word count: 2
Character length: 15
In quote: false
Quote boundary: none
In parenthetical: false
Parenthetical depth: 0
Navigation progress percent: 0
Navigation paragraph index: 0

## Navigability Context

Previous displayed chunk:
- Index: 6
- Text: Built on Economic
- Duration ms: 660
- Progress percent: 0
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
The End of War Without the End of Power
Toward a Global Security System Built on Economic Deterrence
Alex
Apr 02, 2026

There is a persistent mistake in how we imagine peace.

Previous chunks:
- [4] "a Global" - 400ms base / 400ms effective - normal - 1 content word(s) - 8 chars - quote=false/none - parenthetical=false/0 - navigation=0%/p0
- [5] "Security System" - 660ms base / 660ms effective - dense - 2 content word(s) - 15 chars - quote=false/none - parenthetical=false/0 - navigation=0%/p0
- [6] "Built on Economic" - 660ms base / 660ms effective - dense - 2 content word(s) - 17 chars - quote=false/none - parenthetical=false/0 - navigation=0%/p0

Next chunks:
- [8] "Apr 02," - 560ms base / 560ms effective - dense - 2 content word(s) - 7 chars - quote=false/none - parenthetical=false/0 - navigation=0%/p0
- [9] "2026 There" - 600ms base / 600ms effective - dense - 2 content word(s) - 10 chars - quote=false/none - parenthetical=false/0 - navigation=0%/p0
- [10] "is a persistent" - 440ms base / 440ms effective - normal - 1 content word(s) - 15 chars - quote=false/none - parenthetical=false/0 - navigation=1%/p1

## Session Summary

Event count: 23
Rewind count: 13
Pause count: 3
Speed change count: 0
Adaptation count: 0
Completed: false
Elapsed session ms: 318628
Estimated remaining chunks: 845
Average effective duration ms: 581
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

---

<!-- Source: defect_20260710_160447_d3cdb9.md.gz -->

# Semantic RSVP Defect Report

Report ID: defect_20260710_160447_d3cdb9
Created at: 2026-07-10T16:04:47.886435Z

## Classification

Category: bad_chunk_split
Severity: 2
Notes:
Don't split the year from the day

Preferred behavior:
Wr've encountered this before. Need to preserve long form dates in a single dedicated chunks. 'Apr 02, 2026'

## Reader State

Current index: 9
Sentence index: 0
Playback speed: 1x
Adaptation enabled: false

Current chunk:
2026 There

## Timing Context

Base duration ms: 600
Effective duration ms: 600
Playback speed: 1x
Duration source: schedule
Current syntactic hint: dense
Current content word count: 2
Character length: 10
In quote: false
Quote boundary: none
In parenthetical: false
Parenthetical depth: 0
Navigation progress percent: 0
Navigation paragraph index: 0

## Navigability Context

Previous displayed chunk:
- Index: 8
- Text: Apr 02,
- Duration ms: 560
- Progress percent: 0
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
The End of War Without the End of Power
Toward a Global Security System Built on Economic Deterrence
Alex
Apr 02, 2026

There is a persistent mistake in how we imagine peace.

Previous chunks:
- [6] "Built on Economic" - 660ms base / 660ms effective - dense - 2 content word(s) - 17 chars - quote=false/none - parenthetical=false/0 - navigation=0%/p0
- [7] "Deterrence Alex" - 710ms base / 710ms effective - dense - 2 content word(s) - 15 chars - quote=false/none - parenthetical=false/0 - navigation=0%/p0
- [8] "Apr 02," - 560ms base / 560ms effective - dense - 2 content word(s) - 7 chars - quote=false/none - parenthetical=false/0 - navigation=0%/p0

Next chunks:
- [10] "is a persistent" - 440ms base / 440ms effective - normal - 1 content word(s) - 15 chars - quote=false/none - parenthetical=false/0 - navigation=1%/p1
- [11] "mistake in how" - 600ms base / 600ms effective - dense - 2 content word(s) - 14 chars - quote=false/none - parenthetical=false/0 - navigation=1%/p1
- [12] "we imagine" - 600ms base / 600ms effective - dense - 2 content word(s) - 10 chars - quote=false/none - parenthetical=false/0 - navigation=1%/p1

## Session Summary

Event count: 28
Rewind count: 15
Pause count: 4
Speed change count: 0
Adaptation count: 0
Completed: false
Elapsed session ms: 420642
Estimated remaining chunks: 843
Average effective duration ms: 581
Last adaptation reason: 
Last adaptation direction: 

## Client

User agent:
Mozilla/5.0 (Android 16; Mobile; rv:152.0) Gecko/152.0 Firefox/152.0

Viewport:
384x1085

Display:
Reader width px: 360
Chunk scroll width px: 332
Chunk client width px: 332
Chunk may overflow: false

---

<!-- Source: defect_20260710_160645_0b31d3.md.gz -->

# Semantic RSVP Defect Report

Report ID: defect_20260710_160645_0b31d3
Created at: 2026-07-10T16:06:45.225214Z

## Classification

Category: bad_chunk_split
Severity: 2
Notes:
Awkward split

Preferred behavior:
Should have been 'we assume peace' 'must arrive' 'dramatically' to preserve cohesion

## Reader State

Current index: 15
Sentence index: 1
Playback speed: 1x
Adaptation enabled: true

Current chunk:
peace must arrive

## Timing Context

Base duration ms: 600
Effective duration ms: 600
Playback speed: 1x
Duration source: schedule
Current syntactic hint: dense
Current content word count: 2
Character length: 17
In quote: false
Quote boundary: none
In parenthetical: false
Parenthetical depth: 0
Navigation progress percent: 1
Navigation paragraph index: 2

## Navigability Context

Previous displayed chunk:
- Index: 14
- Text: We assume
- Duration ms: 600
- Progress percent: 1
- Paragraph index: 2

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
We assume peace must arrive dramatically — through moral awakening, political unity, or the sudden disappearance of rivalry among nations.

Previous chunks:
- [12] "we imagine" - 600ms base / 600ms effective - dense - 2 content word(s) - 10 chars - quote=false/none - parenthetical=false/0 - navigation=1%/p1
- [13] "peace." - 580ms base / 580ms effective - normal - 1 content word(s) - 6 chars - quote=false/none - parenthetical=false/0 - navigation=1%/p1
- [14] "We assume" - 600ms base / 600ms effective - dense - 2 content word(s) - 9 chars - quote=false/none - parenthetical=false/0 - navigation=1%/p2

Next chunks:
- [16] "dramatically— through moral" - 750ms base / 750ms effective - dense - 2 content word(s) - 27 chars - quote=false/none - parenthetical=false/0 - navigation=1%/p2
- [17] "awakening," - 460ms base / 460ms effective - normal - 1 content word(s) - 10 chars - quote=false/none - parenthetical=false/0 - navigation=1%/p2
- [18] "political unity," - 650ms base / 650ms effective - dense - 2 content word(s) - 16 chars - quote=false/none - parenthetical=false/0 - navigation=1%/p2

## Session Summary

Event count: 9
Rewind count: 4
Pause count: 1
Speed change count: 0
Adaptation count: 2
Completed: false
Elapsed session ms: 84141
Estimated remaining chunks: 837
Average effective duration ms: 581
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

---

<!-- Source: defect_20260710_161122_883a14.md.gz -->

# Semantic RSVP Defect Report

Report ID: defect_20260710_161122_883a14
Created at: 2026-07-10T16:11:22.751233Z

## Classification

Category: bad_chunk_split
Severity: 3
Notes:
You meant the least rational option?

Preferred behavior:
Separating the qualifier from the adjective again. 'the least rational' 'option available' would have perserved meaning better

## Reader State

Current index: 48
Sentence index: 6
Playback speed: 0.85x
Adaptation enabled: true

Current chunk:
rational option

## Timing Context

Base duration ms: 600
Effective duration ms: 706
Playback speed: 0.85x
Duration source: schedule
Current syntactic hint: dense
Current content word count: 2
Character length: 15
In quote: false
Quote boundary: none
In parenthetical: false
Parenthetical depth: 0
Navigation progress percent: 5
Navigation paragraph index: 3

## Navigability Context

Previous displayed chunk:
- Index: 47
- Text: the least
- Duration ms: 440
- Progress percent: 5
- Paragraph index: 3

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
It has required only the redesign of incentives so that violence becomes the least rational option available.

Previous chunks:
- [45] "that violence" - 440ms base / 518ms effective - normal - 1 content word(s) - 13 chars - quote=false/none - parenthetical=false/0 - navigation=4%/p3
- [46] "becomes" - 400ms base / 471ms effective - normal - 1 content word(s) - 7 chars - quote=false/none - parenthetical=false/0 - navigation=4%/p3
- [47] "the least" - 440ms base / 518ms effective - normal - 1 content word(s) - 9 chars - quote=false/none - parenthetical=false/0 - navigation=5%/p3

Next chunks:
- [49] "available." - 620ms base / 729ms effective - normal - 1 content word(s) - 10 chars - quote=false/none - parenthetical=false/0 - navigation=5%/p3
- [50] "The modern" - 440ms base / 518ms effective - normal - 1 content word(s) - 10 chars - quote=false/none - parenthetical=false/0 - navigation=5%/p4
- [51] "international system" - 690ms base / 812ms effective - dense - 2 content word(s) - 20 chars - quote=false/none - parenthetical=false/0 - navigation=5%/p4

## Session Summary

Event count: 24
Rewind count: 9
Pause count: 3
Speed change count: 0
Adaptation count: 7
Completed: false
Elapsed session ms: 361684
Estimated remaining chunks: 804
Average effective duration ms: 683
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

---

<!-- Source: defect_20260710_161303_9e58d7.md.gz -->

# Semantic RSVP Defect Report

Report ID: defect_20260710_161303_9e58d7
Created at: 2026-07-10T16:13:03.006183Z

## Classification

Category: layout_or_visibility_issue
Severity: 2
Notes:
Lost the word in the orevious text

Preferred behavior:
Another instance of long ghost chunk overstepping unto a short current chunk. Visually it's a mess

## Reader State

Current index: 60
Sentence index: 9
Playback speed: 0.75x
Adaptation enabled: true

Current chunk:
Still,

## Timing Context

Base duration ms: 300
Effective duration ms: 400
Playback speed: 0.75x
Duration source: schedule
Current syntactic hint: light
Current content word count: 0
Character length: 6
In quote: false
Quote boundary: none
In parenthetical: false
Parenthetical depth: 0
Navigation progress percent: 6
Navigation paragraph index: 4

## Navigability Context

Previous displayed chunk:
- Index: 59
- Text: uncomfortable to observe.
- Duration ms: 970
- Progress percent: 6
- Paragraph index: 4

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
Still, they point toward a possibility that would have seemed implausible even a century ago: a world in which military force is not outlawed by moral consensus, but rendered strategically obsolete by automatic economic and diplomatic consequences.

Previous chunks:
- [57] "inconsistent," - 460ms base / 613ms effective - normal - 1 content word(s) - 13 chars - quote=false/none - parenthetical=false/0 - navigation=6%/p4
- [58] "and often" - 440ms base / 587ms effective - normal - 1 content word(s) - 9 chars - quote=false/none - parenthetical=false/0 - navigation=6%/p4
- [59] "uncomfortable to observe." - 970ms base / 1293ms effective - dense - 2 content word(s) - 25 chars - quote=false/none - parenthetical=false/0 - navigation=6%/p4

Next chunks:
- [61] "they point" - 600ms base / 800ms effective - dense - 2 content word(s) - 10 chars - quote=false/none - parenthetical=false/0 - navigation=6%/p4
- [62] "toward" - 400ms base / 533ms effective - normal - 1 content word(s) - 6 chars - quote=false/none - parenthetical=false/0 - navigation=6%/p4
- [63] "a possibility that" - 440ms base / 587ms effective - normal - 1 content word(s) - 18 chars - quote=false/none - parenthetical=false/0 - navigation=6%/p4

## Session Summary

Event count: 35
Rewind count: 14
Pause count: 4
Speed change count: 0
Adaptation count: 10
Completed: false
Elapsed session ms: 448119
Estimated remaining chunks: 792
Average effective duration ms: 774
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

---

<!-- Source: defect_20260710_161501_d5198e.md.gz -->

# Semantic RSVP Defect Report

Report ID: defect_20260710_161501_d5198e
Created at: 2026-07-10T16:15:01.522078Z

## Classification

Category: bad_chunk_split
Severity: 2
Notes:
Awkward split

Preferred behavior:
'The primary language' 'of international credibility'

## Reader State

Current index: 139
Sentence index: 18
Playback speed: 1x
Adaptation enabled: false

Current chunk:
language of international

## Timing Context

Base duration ms: 750
Effective duration ms: 750
Playback speed: 1x
Duration source: schedule
Current syntactic hint: dense
Current content word count: 2
Character length: 25
In quote: false
Quote boundary: none
In parenthetical: false
Parenthetical depth: 0
Navigation progress percent: 15
Navigation paragraph index: 8

## Navigability Context

Previous displayed chunk:
- Index: 138
- Text: the primary
- Duration ms: 440
- Progress percent: 15
- Paragraph index: 8

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
Power projection remains the primary language of international credibility.

Previous chunks:
- [136] "Power projection" - 650ms base / 650ms effective - dense - 2 content word(s) - 16 chars - quote=false/none - parenthetical=false/0 - navigation=14%/p8
- [137] "remains" - 400ms base / 400ms effective - normal - 1 content word(s) - 7 chars - quote=false/none - parenthetical=false/0 - navigation=15%/p8
- [138] "the primary" - 440ms base / 440ms effective - normal - 1 content word(s) - 11 chars - quote=false/none - parenthetical=false/0 - navigation=15%/p8

Next chunks:
- [140] "credibility." - 620ms base / 620ms effective - normal - 1 content word(s) - 12 chars - quote=false/none - parenthetical=false/0 - navigation=15%/p8
- [141] "The result is" - 440ms base / 440ms effective - normal - 1 content word(s) - 13 chars - quote=false/none - parenthetical=false/0 - navigation=15%/p9
- [142] "a system" - 400ms base / 400ms effective - normal - 1 content word(s) - 8 chars - quote=false/none - parenthetical=false/0 - navigation=15%/p9

## Session Summary

Event count: 53
Rewind count: 18
Pause count: 6
Speed change count: 3
Adaptation count: 15
Completed: false
Elapsed session ms: 566628
Estimated remaining chunks: 713
Average effective duration ms: 581
Last adaptation reason: smooth_run
Last adaptation direction: faster

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

---

<!-- Source: defect_20260710_161616_07cd8f.md.gz -->

# Semantic RSVP Defect Report

Report ID: defect_20260710_161616_07cd8f
Created at: 2026-07-10T16:16:16.783829Z

## Classification

Category: layout_or_visibility_issue
Severity: 2
Notes:
Tiny text

Preferred behavior:
Not sure why we keep randomly making a chunk at a reduced size. We need a better rule for default size.

## Reader State

Current index: 169
Sentence index: 24
Playback speed: 1x
Adaptation enabled: false

Current chunk:
intelligence,

## Timing Context

Base duration ms: 460
Effective duration ms: 460
Playback speed: 1x
Duration source: schedule
Current syntactic hint: normal
Current content word count: 1
Character length: 13
In quote: false
Quote boundary: none
In parenthetical: false
Parenthetical depth: 0
Navigation progress percent: 18
Navigation paragraph index: 15

## Navigability Context

Previous displayed chunk:
- Index: 168
- Text: governance of artificial
- Duration ms: 750
- Progress percent: 18
- Paragraph index: 15

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
Meanwhile, humanity faces risks that do not respect borders: climate instability, bioengineering hazards, governance of artificial intelligence, fragile global supply chains, and tightly coupled infrastructure systems. These challenges demand coordination at a scale the current security architecture struggles to produce.

Previous chunks:
- [166] "climate instability," - 690ms base / 690ms effective - dense - 2 content word(s) - 20 chars - quote=false/none - parenthetical=false/0 - navigation=18%/p15
- [167] "bioengineering hazards," - 690ms base / 690ms effective - dense - 2 content word(s) - 23 chars - quote=false/none - parenthetical=false/0 - navigation=18%/p15
- [168] "governance of artificial" - 750ms base / 750ms effective - dense - 2 content word(s) - 24 chars - quote=false/none - parenthetical=false/0 - navigation=18%/p15

Next chunks:
- [170] "fragile global" - 600ms base / 600ms effective - dense - 2 content word(s) - 14 chars - quote=false/none - parenthetical=false/0 - navigation=18%/p15
- [171] "supply chains," - 600ms base / 600ms effective - dense - 2 content word(s) - 14 chars - quote=false/none - parenthetical=false/0 - navigation=19%/p15
- [172] "and tightly" - 440ms base / 440ms effective - normal - 1 content word(s) - 11 chars - quote=false/none - parenthetical=false/0 - navigation=19%/p15

## Session Summary

Event count: 58
Rewind count: 20
Pause count: 7
Speed change count: 3
Adaptation count: 15
Completed: false
Elapsed session ms: 641912
Estimated remaining chunks: 683
Average effective duration ms: 581
Last adaptation reason: smooth_run
Last adaptation direction: faster

## Client

User agent:
Mozilla/5.0 (Android 16; Mobile; rv:152.0) Gecko/152.0 Firefox/152.0

Viewport:
384x678

Display:
Reader width px: 368
Chunk scroll width px: 340
Chunk client width px: 340
Chunk may overflow: false
