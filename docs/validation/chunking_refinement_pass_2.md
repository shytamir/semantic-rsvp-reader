# Observed Defects Review
## Review Summary

Top recurring issues:
1. Proper names and named entities are split across chunks, including repeated entities like Air Force One.
2. Honorifics and titles are separated from surnames or names.
3. Definite articles are often separated from the noun phrase they introduce.
4. Several chunks begin or end with weak function words, especially pronouns and prepositions.
5. Quote/parenthetical state indicators appear [stable / unstable], with the following defects if any.

Priority for next refinement:
- Preserve compact proper names and repeated named entities when within mobile constraints.
- Keep honorific/title + surname/name units together.
- Improve definite article + noun phrase grouping.
- Penalize or avoid weak-boundary chunks where possible.
- Keep quote/parenthetical state fixes separate from chunking unless the defect involves boundary parsing.

## Summary

- Total reports: 44
- Included reports: 44
- Reports with timing context: 44
- Reports without timing context: 0
- Reports by category:
  - honorific_name_split: 5
  - orphan_function_word: 3
  - parenthetical_state_confusion: 1
  - proper_name_split: 30
  - quote_state_confusion: 1
  - title_name_split: 4

---

<!-- Source: defect_20260710_042113_c64e3d.md.gz -->

# Semantic RSVP Defect Report

Report ID: defect_20260710_042113_c64e3d
Created at: 2026-07-10T04:21:13.621780Z

## Classification

Category: proper_name_split
Severity: 2
Notes:
This One is from Air Force One

Preferred behavior:
Avoid splitting proper names

## Reader State

Current index: 29
Sentence index: 1
Playback speed: 1x
Adaptation enabled: false

Current chunk:
One.

## Timing Context

Base duration ms: 580
Effective duration ms: 580
Playback speed: 1x
Duration source: schedule
Current syntactic hint: normal
Current content word count: 1
Character length: 4
In quote: false
Quote boundary: none
In parenthetical: false
Parenthetical depth: 0
Navigation progress percent: 7
Navigation paragraph index: 1

Original sentence:
But in a statement it made when it announced that the donated jet was ready to transport the president, it acknowledged that the temporary plane did not have all the equipment usually found on an Air Force One.

Previous chunks:
- [26] "the equipment" - 440ms base / 440ms effective - normal - 1 content word(s) - 13 chars - quote=false/none - parenthetical=false/0 - navigation=6%/p1
- [27] "usually found on" - 600ms base / 600ms effective - dense - 2 content word(s) - 16 chars - quote=false/none - parenthetical=false/0 - navigation=7%/p1
- [28] "an Air Force" - 660ms base / 660ms effective - dense - 2 content word(s) - 12 chars - quote=false/none - parenthetical=false/0 - navigation=7%/p1

Next chunks:
- [30] "No risk" - 560ms base / 560ms effective - dense - 2 content word(s) - 7 chars - quote=false/none - parenthetical=false/0 - navigation=7%/p2
- [31] "was taken in security," - 640ms base / 640ms effective - dense - 2 content word(s) - 22 chars - quote=false/none - parenthetical=false/0 - navigation=8%/p2
- [32] "safety" - 400ms base / 400ms effective - normal - 1 content word(s) - 6 chars - quote=false/none - parenthetical=false/0 - navigation=8%/p2

## Session Summary

Event count: 21
Rewind count: 11
Pause count: 2
Speed change count: 2
Adaptation count: 2
Completed: false
Elapsed session ms: 111766
Estimated remaining chunks: 400
Average effective duration ms: 560
Last adaptation reason: rewinds
Last adaptation direction: slower

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

<!-- Source: defect_20260710_042207_16c019.md.gz -->

# Semantic RSVP Defect Report

Report ID: defect_20260710_042207_16c019
Created at: 2026-07-10T04:22:07.794538Z

## Classification

Category: proper_name_split
Severity: 2
Notes:
This is the Force from Air Force

Preferred behavior:
Don't split proper names.

## Reader State

Current index: 36
Sentence index: 2
Playback speed: 1x
Adaptation enabled: false

Current chunk:
Force said in

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
Navigation progress percent: 9
Navigation paragraph index: 2

Original sentence:
“No risk was taken in security, safety or mission communications,” the Air Force said in a statement on June 19.

Previous chunks:
- [33] "or mission" - 440ms base / 440ms effective - normal - 1 content word(s) - 10 chars - quote=false/none - parenthetical=false/0 - navigation=8%/p2
- [34] "communications," - 460ms base / 460ms effective - normal - 1 content word(s) - 15 chars - quote=false/none - parenthetical=false/0 - navigation=8%/p2
- [35] "the Air" - 400ms base / 400ms effective - normal - 1 content word(s) - 7 chars - quote=false/none - parenthetical=false/0 - navigation=8%/p2

Next chunks:
- [37] "a statement on June" - 690ms base / 690ms effective - dense - 2 content word(s) - 19 chars - quote=false/none - parenthetical=false/0 - navigation=9%/p2
- [38] "19." - 580ms base / 580ms effective - normal - 1 content word(s) - 3 chars - quote=false/none - parenthetical=false/0 - navigation=9%/p2
- [39] "But the collective" - 440ms base / 440ms effective - normal - 1 content word(s) - 18 chars - quote=false/none - parenthetical=false/0 - navigation=9%/p2

## Session Summary

Event count: 25
Rewind count: 12
Pause count: 3
Speed change count: 2
Adaptation count: 2
Completed: false
Elapsed session ms: 165970
Estimated remaining chunks: 393
Average effective duration ms: 560
Last adaptation reason: rewinds
Last adaptation direction: slower

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

<!-- Source: defect_20260710_042300_43ddcf.md.gz -->

# Semantic RSVP Defect Report

Report ID: defect_20260710_042300_43ddcf
Created at: 2026-07-10T04:23:00.015967Z

## Classification

Category: proper_name_split
Severity: 2
Notes:
Again, the Force from Air Force 

Preferred behavior:
Don't split proper names

## Reader State

Current index: 49
Sentence index: 4
Playback speed: 1x
Adaptation enabled: false

Current chunk:
Force

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
Navigation progress percent: 12
Navigation paragraph index: 3

Original sentence:
The Air Force would not say what it meant by “less commonly used mission sets.”

Previous chunks:
- [46] "to support the next" - 640ms base / 640ms effective - dense - 2 content word(s) - 19 chars - quote=false/none - parenthetical=false/0 - navigation=11%/p2
- [47] "40 years." - 820ms base / 820ms effective - dense - 2 content word(s) - 9 chars - quote=false/none - parenthetical=false/0 - navigation=11%/p2
- [48] "The Air" - 400ms base / 400ms effective - normal - 1 content word(s) - 7 chars - quote=false/none - parenthetical=false/0 - navigation=11%/p3

Next chunks:
- [50] "would not say" - 440ms base / 440ms effective - normal - 1 content word(s) - 13 chars - quote=false/none - parenthetical=false/0 - navigation=12%/p3
- [51] "what it meant" - 600ms base / 600ms effective - dense - 2 content word(s) - 13 chars - quote=false/none - parenthetical=false/0 - navigation=12%/p3
- [52] "by“ less" - 400ms base / 400ms effective - normal - 1 content word(s) - 8 chars - quote=true/open - parenthetical=false/0 - navigation=12%/p3

## Session Summary

Event count: 30
Rewind count: 14
Pause count: 4
Speed change count: 2
Adaptation count: 2
Completed: false
Elapsed session ms: 218160
Estimated remaining chunks: 380
Average effective duration ms: 560
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

<!-- Source: defect_20260710_042916_514e3d.md.gz -->

# Semantic RSVP Defect Report

Report ID: defect_20260710_042916_514e3d
Created at: 2026-07-10T04:29:16.920864Z

## Classification

Category: quote_state_confusion
Severity: 2
Notes:
This bad quotes mark insertion causes the rest of the sample into in quotes state

Preferred behavior:
Twofold correction: protect against failure mode by treating quote markers as start-finish markers for the state regardless of if they're end or start quotes. And teach our chunker how to properly use quotes so we stop getting them in inverse order.

## Reader State

Current index: 52
Sentence index: 4
Playback speed: 1x
Adaptation enabled: false

Current chunk:
by“ less

## Timing Context

Base duration ms: 400
Effective duration ms: 400
Playback speed: 1x
Duration source: schedule
Current syntactic hint: normal
Current content word count: 1
Character length: 8
In quote: true
Quote boundary: open
In parenthetical: false
Parenthetical depth: 0
Navigation progress percent: 12
Navigation paragraph index: 3

Original sentence:
The Air Force would not say what it meant by “less commonly used mission sets.”

Previous chunks:
- [49] "Force" - 400ms base / 400ms effective - normal - 1 content word(s) - 5 chars - quote=false/none - parenthetical=false/0 - navigation=12%/p3
- [50] "would not say" - 440ms base / 440ms effective - normal - 1 content word(s) - 13 chars - quote=false/none - parenthetical=false/0 - navigation=12%/p3
- [51] "what it meant" - 600ms base / 600ms effective - dense - 2 content word(s) - 13 chars - quote=false/none - parenthetical=false/0 - navigation=12%/p3

Next chunks:
- [53] "commonly used" - 600ms base / 600ms effective - dense - 2 content word(s) - 13 chars - quote=true/none - parenthetical=false/0 - navigation=12%/p3
- [54] "mission sets." - 820ms base / 820ms effective - dense - 2 content word(s) - 13 chars - quote=true/none - parenthetical=false/0 - navigation=13%/p3
- [55] "However," - 400ms base / 400ms effective - normal - 1 content word(s) - 8 chars - quote=true/none - parenthetical=false/0 - navigation=13%/p4

## Session Summary

Event count: 40
Rewind count: 20
Pause count: 5
Speed change count: 2
Adaptation count: 2
Completed: false
Elapsed session ms: 595080
Estimated remaining chunks: 377
Average effective duration ms: 560
Last adaptation reason: rewinds
Last adaptation direction: slower

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

<!-- Source: defect_20260710_043032_14c3e1.md.gz -->

# Semantic RSVP Defect Report

Report ID: defect_20260710_043032_14c3e1
Created at: 2026-07-10T04:30:32.531884Z

## Classification

Category: title_name_split
Severity: 2
Notes:
President Trump is one unit

Preferred behavior:
Don't split title and name

## Reader State

Current index: 73
Sentence index: 6
Playback speed: 1x
Adaptation enabled: false

Current chunk:
Trump,

## Timing Context

Base duration ms: 400
Effective duration ms: 400
Playback speed: 1x
Duration source: schedule
Current syntactic hint: normal
Current content word count: 1
Character length: 6
In quote: true
Quote boundary: none
In parenthetical: false
Parenthetical depth: 0
Navigation progress percent: 17
Navigation paragraph index: 5

Original sentence:
Image
President Trump, wearing a dark suit and yellow tie, stands in a plane before people holding cameras and recording gear.

Previous chunks:
- [70] "the previous" - 440ms base / 440ms effective - normal - 1 content word(s) - 12 chars - quote=true/none - parenthetical=false/0 - navigation=16%/p4
- [71] "model." - 580ms base / 580ms effective - normal - 1 content word(s) - 6 chars - quote=true/none - parenthetical=false/0 - navigation=17%/p4
- [72] "Image President" - 710ms base / 710ms effective - dense - 2 content word(s) - 15 chars - quote=true/none - parenthetical=false/0 - navigation=17%/p0

Next chunks:
- [74] "wearing a dark" - 600ms base / 600ms effective - dense - 2 content word(s) - 14 chars - quote=true/none - parenthetical=false/0 - navigation=17%/p5
- [75] "suit" - 400ms base / 400ms effective - normal - 1 content word(s) - 4 chars - quote=true/none - parenthetical=false/0 - navigation=17%/p5
- [76] "and yellow" - 440ms base / 440ms effective - normal - 1 content word(s) - 10 chars - quote=true/none - parenthetical=false/0 - navigation=18%/p5

## Session Summary

Event count: 48
Rewind count: 22
Pause count: 7
Speed change count: 2
Adaptation count: 2
Completed: false
Elapsed session ms: 670706
Estimated remaining chunks: 356
Average effective duration ms: 560
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

<!-- Source: defect_20260710_043117_57f86f.md.gz -->

# Semantic RSVP Defect Report

Report ID: defect_20260710_043117_57f86f
Created at: 2026-07-10T04:31:17.741976Z

## Classification

Category: proper_name_split
Severity: 2
Notes:
Air Force One is one unit

Preferred behavior:
Don't split proper names

## Reader State

Current index: 88
Sentence index: 7
Playback speed: 1x
Adaptation enabled: false

Current chunk:
One after

## Timing Context

Base duration ms: 600
Effective duration ms: 600
Playback speed: 1x
Duration source: schedule
Current syntactic hint: dense
Current content word count: 2
Character length: 9
In quote: true
Quote boundary: none
In parenthetical: false
Parenthetical depth: 0
Navigation progress percent: 20
Navigation paragraph index: 5

Original sentence:
President Trump talked to reporters aboard the new Air Force One after departing Mildenhall Air Force Base in England on Wednesday.Credit...Doug Mills/The New York Times
Two former Air Force officials, who had both been involved in the effort to replace the older Air Force One planes, said they were surprised to see Mr. Trump fly on the new jet overseas, where there are greater security risks.

Previous chunks:
- [85] "talked to reporters" - 690ms base / 690ms effective - dense - 2 content word(s) - 19 chars - quote=true/none - parenthetical=false/0 - navigation=19%/p5
- [86] "aboard the new" - 600ms base / 600ms effective - dense - 2 content word(s) - 14 chars - quote=true/none - parenthetical=false/0 - navigation=20%/p5
- [87] "Air Force" - 660ms base / 660ms effective - dense - 2 content word(s) - 9 chars - quote=true/none - parenthetical=false/0 - navigation=20%/p5

Next chunks:
- [89] "departing Mildenhall" - 750ms base / 750ms effective - dense - 2 content word(s) - 20 chars - quote=true/none - parenthetical=false/0 - navigation=20%/p5
- [90] "Air Force" - 660ms base / 660ms effective - dense - 2 content word(s) - 9 chars - quote=true/none - parenthetical=false/0 - navigation=20%/p5
- [91] "Base in England" - 660ms base / 660ms effective - dense - 2 content word(s) - 15 chars - quote=true/none - parenthetical=false/0 - navigation=21%/p5

## Session Summary

Event count: 51
Rewind count: 22
Pause count: 8
Speed change count: 2
Adaptation count: 2
Completed: false
Elapsed session ms: 715929
Estimated remaining chunks: 341
Average effective duration ms: 560
Last adaptation reason: rewinds
Last adaptation direction: slower

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

<!-- Source: defect_20260710_043226_73ccac.md.gz -->

# Semantic RSVP Defect Report

Report ID: defect_20260710_043226_73ccac
Created at: 2026-07-10T04:32:26.176062Z

## Classification

Category: proper_name_split
Severity: 2
Notes:
They are air force officials, not force officials

Preferred behavior:
Don't split proper names

## Reader State

Current index: 98
Sentence index: 7
Playback speed: 1x
Adaptation enabled: false

Current chunk:
Force officials,

## Timing Context

Base duration ms: 650
Effective duration ms: 650
Playback speed: 1x
Duration source: schedule
Current syntactic hint: dense
Current content word count: 2
Character length: 16
In quote: true
Quote boundary: none
In parenthetical: false
Parenthetical depth: 0
Navigation progress percent: 22
Navigation paragraph index: 5

Original sentence:
President Trump talked to reporters aboard the new Air Force One after departing Mildenhall Air Force Base in England on Wednesday.Credit...Doug Mills/The New York Times
Two former Air Force officials, who had both been involved in the effort to replace the older Air Force One planes, said they were surprised to see Mr. Trump fly on the new jet overseas, where there are greater security risks.

Previous chunks:
- [95] "New York" - 620ms base / 620ms effective - dense - 2 content word(s) - 8 chars - quote=true/none - parenthetical=false/0 - navigation=21%/p5
- [96] "Times Two" - 660ms base / 660ms effective - dense - 2 content word(s) - 9 chars - quote=true/none - parenthetical=false/0 - navigation=22%/p5
- [97] "former Air" - 600ms base / 600ms effective - dense - 2 content word(s) - 10 chars - quote=true/none - parenthetical=false/0 - navigation=22%/p5

Next chunks:
- [99] "who had both" - 600ms base / 600ms effective - dense - 2 content word(s) - 12 chars - quote=true/none - parenthetical=false/0 - navigation=22%/p5
- [100] "been involved in" - 440ms base / 440ms effective - normal - 1 content word(s) - 16 chars - quote=true/none - parenthetical=false/0 - navigation=23%/p5
- [101] "the effort" - 440ms base / 440ms effective - normal - 1 content word(s) - 10 chars - quote=true/none - parenthetical=false/0 - navigation=23%/p5

## Session Summary

Event count: 57
Rewind count: 23
Pause count: 10
Speed change count: 2
Adaptation count: 2
Completed: false
Elapsed session ms: 784376
Estimated remaining chunks: 331
Average effective duration ms: 560
Last adaptation reason: rewinds
Last adaptation direction: slower

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

<!-- Source: defect_20260710_043300_c2c928.md.gz -->

# Semantic RSVP Defect Report

Report ID: defect_20260710_043300_c2c928
Created at: 2026-07-10T04:33:00.663770Z

## Classification

Category: proper_name_split
Severity: 2
Notes:
Again

Preferred behavior:
AirForceOne Repetition

## Reader State

Current index: 104
Sentence index: 7
Playback speed: 1x
Adaptation enabled: false

Current chunk:
One planes,

## Timing Context

Base duration ms: 600
Effective duration ms: 600
Playback speed: 1x
Duration source: schedule
Current syntactic hint: dense
Current content word count: 2
Character length: 11
In quote: true
Quote boundary: none
In parenthetical: false
Parenthetical depth: 0
Navigation progress percent: 23
Navigation paragraph index: 5

Original sentence:
President Trump talked to reporters aboard the new Air Force One after departing Mildenhall Air Force Base in England on Wednesday.Credit...Doug Mills/The New York Times
Two former Air Force officials, who had both been involved in the effort to replace the older Air Force One planes, said they were surprised to see Mr. Trump fly on the new jet overseas, where there are greater security risks.

Previous chunks:
- [101] "the effort" - 440ms base / 440ms effective - normal - 1 content word(s) - 10 chars - quote=true/none - parenthetical=false/0 - navigation=23%/p5
- [102] "to replace the older" - 640ms base / 640ms effective - dense - 2 content word(s) - 20 chars - quote=true/none - parenthetical=false/0 - navigation=23%/p5
- [103] "Air Force" - 660ms base / 660ms effective - dense - 2 content word(s) - 9 chars - quote=true/none - parenthetical=false/0 - navigation=23%/p5

Next chunks:
- [105] "said they" - 600ms base / 600ms effective - dense - 2 content word(s) - 9 chars - quote=true/none - parenthetical=false/0 - navigation=24%/p5
- [106] "were surprised to see" - 690ms base / 690ms effective - dense - 2 content word(s) - 21 chars - quote=true/none - parenthetical=false/0 - navigation=24%/p5
- [107] "Mr." - 580ms base / 580ms effective - normal - 1 content word(s) - 3 chars - quote=true/none - parenthetical=false/0 - navigation=24%/p5

## Session Summary

Event count: 61
Rewind count: 24
Pause count: 11
Speed change count: 2
Adaptation count: 2
Completed: false
Elapsed session ms: 818859
Estimated remaining chunks: 325
Average effective duration ms: 560
Last adaptation reason: rewinds
Last adaptation direction: slower

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

<!-- Source: defect_20260710_043340_f1145f.md.gz -->

# Semantic RSVP Defect Report

Report ID: defect_20260710_043340_f1145f
Created at: 2026-07-10T04:33:40.397200Z

## Classification

Category: honorific_name_split
Severity: 2
Notes:
Mr. Trump is one unit

Preferred behavior:
Don't sllit honorific and name

## Reader State

Current index: 108
Sentence index: 7
Playback speed: 1x
Adaptation enabled: false

Current chunk:
Trump fly on

## Timing Context

Base duration ms: 600
Effective duration ms: 600
Playback speed: 1x
Duration source: schedule
Current syntactic hint: dense
Current content word count: 2
Character length: 12
In quote: true
Quote boundary: none
In parenthetical: false
Parenthetical depth: 0
Navigation progress percent: 24
Navigation paragraph index: 5

Original sentence:
President Trump talked to reporters aboard the new Air Force One after departing Mildenhall Air Force Base in England on Wednesday.Credit...Doug Mills/The New York Times
Two former Air Force officials, who had both been involved in the effort to replace the older Air Force One planes, said they were surprised to see Mr. Trump fly on the new jet overseas, where there are greater security risks.

Previous chunks:
- [105] "said they" - 600ms base / 600ms effective - dense - 2 content word(s) - 9 chars - quote=true/none - parenthetical=false/0 - navigation=24%/p5
- [106] "were surprised to see" - 690ms base / 690ms effective - dense - 2 content word(s) - 21 chars - quote=true/none - parenthetical=false/0 - navigation=24%/p5
- [107] "Mr." - 580ms base / 580ms effective - normal - 1 content word(s) - 3 chars - quote=true/none - parenthetical=false/0 - navigation=24%/p5

Next chunks:
- [109] "the new" - 400ms base / 400ms effective - normal - 1 content word(s) - 7 chars - quote=true/none - parenthetical=false/0 - navigation=24%/p5
- [110] "jet overseas," - 600ms base / 600ms effective - dense - 2 content word(s) - 13 chars - quote=true/none - parenthetical=false/0 - navigation=25%/p5
- [111] "where there" - 600ms base / 600ms effective - dense - 2 content word(s) - 11 chars - quote=true/none - parenthetical=false/0 - navigation=25%/p5

## Session Summary

Event count: 64
Rewind count: 24
Pause count: 12
Speed change count: 2
Adaptation count: 2
Completed: false
Elapsed session ms: 858599
Estimated remaining chunks: 321
Average effective duration ms: 560
Last adaptation reason: rewinds
Last adaptation direction: slower

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

<!-- Source: defect_20260710_043425_18340d.md.gz -->

# Semantic RSVP Defect Report

Report ID: defect_20260710_043425_18340d
Created at: 2026-07-10T04:34:25.200087Z

## Classification

Category: honorific_name_split
Severity: 2
Notes:
Again, Mr. Trump is one thing.

Preferred behavior:
Repeat, don't split honorific from name

## Reader State

Current index: 116
Sentence index: 8
Playback speed: 1x
Adaptation enabled: false

Current chunk:
Trump attended a

## Timing Context

Base duration ms: 600
Effective duration ms: 600
Playback speed: 1x
Duration source: schedule
Current syntactic hint: dense
Current content word count: 2
Character length: 16
In quote: true
Quote boundary: none
In parenthetical: false
Parenthetical depth: 0
Navigation progress percent: 26
Navigation paragraph index: 5

Original sentence:
Turkey, where Mr. Trump attended a NATO summit, borders Iran, which the United States pummeled with renewed strikes this week.

Previous chunks:
- [113] "security risks." - 820ms base / 820ms effective - dense - 2 content word(s) - 15 chars - quote=true/none - parenthetical=false/0 - navigation=25%/p5
- [114] "Turkey," - 400ms base / 400ms effective - normal - 1 content word(s) - 7 chars - quote=true/none - parenthetical=false/0 - navigation=25%/p5
- [115] "where Mr." - 820ms base / 820ms effective - dense - 2 content word(s) - 9 chars - quote=true/none - parenthetical=false/0 - navigation=26%/p5

Next chunks:
- [117] "NATO summit," - 600ms base / 600ms effective - dense - 2 content word(s) - 12 chars - quote=true/none - parenthetical=false/0 - navigation=26%/p5
- [118] "borders Iran," - 600ms base / 600ms effective - dense - 2 content word(s) - 13 chars - quote=true/none - parenthetical=false/0 - navigation=26%/p5
- [119] "which the United" - 600ms base / 600ms effective - dense - 2 content word(s) - 16 chars - quote=true/none - parenthetical=false/0 - navigation=27%/p5

## Session Summary

Event count: 67
Rewind count: 24
Pause count: 13
Speed change count: 2
Adaptation count: 2
Completed: false
Elapsed session ms: 903402
Estimated remaining chunks: 313
Average effective duration ms: 560
Last adaptation reason: rewinds
Last adaptation direction: slower

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

<!-- Source: defect_20260710_043544_ab057e.md.gz -->

# Semantic RSVP Defect Report

Report ID: defect_20260710_043544_ab057e
Created at: 2026-07-10T04:35:44.176338Z

## Classification

Category: proper_name_split
Severity: 2
Notes:
Never split the US

Preferred behavior:
Don't split proper names like 'the United States'

## Reader State

Current index: 120
Sentence index: 8
Playback speed: 1x
Adaptation enabled: false

Current chunk:
States pummeled with

## Timing Context

Base duration ms: 640
Effective duration ms: 640
Playback speed: 1x
Duration source: schedule
Current syntactic hint: dense
Current content word count: 2
Character length: 20
In quote: true
Quote boundary: none
In parenthetical: false
Parenthetical depth: 0
Navigation progress percent: 27
Navigation paragraph index: 5

Original sentence:
Turkey, where Mr. Trump attended a NATO summit, borders Iran, which the United States pummeled with renewed strikes this week.

Previous chunks:
- [117] "NATO summit," - 600ms base / 600ms effective - dense - 2 content word(s) - 12 chars - quote=true/none - parenthetical=false/0 - navigation=26%/p5
- [118] "borders Iran," - 600ms base / 600ms effective - dense - 2 content word(s) - 13 chars - quote=true/none - parenthetical=false/0 - navigation=26%/p5
- [119] "which the United" - 600ms base / 600ms effective - dense - 2 content word(s) - 16 chars - quote=true/none - parenthetical=false/0 - navigation=27%/p5

Next chunks:
- [121] "renewed strikes this" - 640ms base / 640ms effective - dense - 2 content word(s) - 20 chars - quote=true/none - parenthetical=false/0 - navigation=27%/p5
- [122] "week." - 580ms base / 580ms effective - normal - 1 content word(s) - 5 chars - quote=true/none - parenthetical=false/0 - navigation=27%/p5
- [123] "The former" - 440ms base / 440ms effective - normal - 1 content word(s) - 10 chars - quote=true/none - parenthetical=false/0 - navigation=28%/p6

## Session Summary

Event count: 71
Rewind count: 25
Pause count: 14
Speed change count: 2
Adaptation count: 2
Completed: false
Elapsed session ms: 982367
Estimated remaining chunks: 309
Average effective duration ms: 560
Last adaptation reason: rewinds
Last adaptation direction: slower

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

<!-- Source: defect_20260710_043712_7f08ad.md.gz -->

# Semantic RSVP Defect Report

Report ID: defect_20260710_043712_7f08ad
Created at: 2026-07-10T04:37:12.267897Z

## Classification

Category: orphan_function_word
Severity: 2
Notes:
The 't' from don't ran away to this new chunk

Preferred behavior:
Contraction suffixes shouldn't be split

## Reader State

Current index: 143
Sentence index: 10
Playback speed: 1x
Adaptation enabled: false

Current chunk:
t permit

## Timing Context

Base duration ms: 560
Effective duration ms: 560
Playback speed: 1x
Duration source: schedule
Current syntactic hint: dense
Current content word count: 2
Character length: 8
In quote: true
Quote boundary: none
In parenthetical: false
Parenthetical depth: 0
Navigation progress percent: 32
Navigation paragraph index: 7

Original sentence:
“Time didn’t permit all the normal Air Force One modifications, so some mix of security, communications and support is missing,” said Frank Kendall, the former Air Force secretary who was in charge of the department as it tried to push Boeing to accelerate its long-delayed contract to deliver two new Air Force One planes.

Previous chunks:
- [140] "a fully equipped" - 600ms base / 600ms effective - dense - 2 content word(s) - 16 chars - quote=true/none - parenthetical=false/0 - navigation=32%/p6
- [141] "presidential aircraft." - 910ms base / 910ms effective - dense - 2 content word(s) - 22 chars - quote=true/none - parenthetical=false/0 - navigation=32%/p6
- [142] "Time didn’" - 600ms base / 600ms effective - dense - 2 content word(s) - 10 chars - quote=true/none - parenthetical=false/0 - navigation=32%/p7

Next chunks:
- [144] "all the normal" - 600ms base / 600ms effective - dense - 2 content word(s) - 14 chars - quote=true/none - parenthetical=false/0 - navigation=33%/p7
- [145] "Air Force" - 660ms base / 660ms effective - dense - 2 content word(s) - 9 chars - quote=true/none - parenthetical=false/0 - navigation=33%/p7
- [146] "One modifications," - 650ms base / 650ms effective - dense - 2 content word(s) - 18 chars - quote=true/none - parenthetical=false/0 - navigation=33%/p7

## Session Summary

Event count: 75
Rewind count: 26
Pause count: 15
Speed change count: 2
Adaptation count: 2
Completed: false
Elapsed session ms: 1070480
Estimated remaining chunks: 286
Average effective duration ms: 560
Last adaptation reason: rewinds
Last adaptation direction: slower

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

<!-- Source: defect_20260710_043754_9e8ee3.md.gz -->

# Semantic RSVP Defect Report

Report ID: defect_20260710_043754_9e8ee3
Created at: 2026-07-10T04:37:54.155829Z

## Classification

Category: proper_name_split
Severity: 2
Notes:
AirForceOne Repeat

Preferred behavior:
AirForceOne Repeat

## Reader State

Current index: 146
Sentence index: 10
Playback speed: 1x
Adaptation enabled: false

Current chunk:
One modifications,

## Timing Context

Base duration ms: 650
Effective duration ms: 650
Playback speed: 1x
Duration source: schedule
Current syntactic hint: dense
Current content word count: 2
Character length: 18
In quote: true
Quote boundary: none
In parenthetical: false
Parenthetical depth: 0
Navigation progress percent: 33
Navigation paragraph index: 7

Original sentence:
“Time didn’t permit all the normal Air Force One modifications, so some mix of security, communications and support is missing,” said Frank Kendall, the former Air Force secretary who was in charge of the department as it tried to push Boeing to accelerate its long-delayed contract to deliver two new Air Force One planes.

Previous chunks:
- [143] "t permit" - 560ms base / 560ms effective - dense - 2 content word(s) - 8 chars - quote=true/none - parenthetical=false/0 - navigation=32%/p7
- [144] "all the normal" - 600ms base / 600ms effective - dense - 2 content word(s) - 14 chars - quote=true/none - parenthetical=false/0 - navigation=33%/p7
- [145] "Air Force" - 660ms base / 660ms effective - dense - 2 content word(s) - 9 chars - quote=true/none - parenthetical=false/0 - navigation=33%/p7

Next chunks:
- [147] "so some" - 560ms base / 560ms effective - dense - 2 content word(s) - 7 chars - quote=true/none - parenthetical=false/0 - navigation=33%/p7
- [148] "mix of security," - 600ms base / 600ms effective - dense - 2 content word(s) - 16 chars - quote=true/none - parenthetical=false/0 - navigation=34%/p7
- [149] "communications" - 440ms base / 440ms effective - normal - 1 content word(s) - 14 chars - quote=true/none - parenthetical=false/0 - navigation=34%/p7

## Session Summary

Event count: 79
Rewind count: 27
Pause count: 16
Speed change count: 2
Adaptation count: 2
Completed: false
Elapsed session ms: 1112347
Estimated remaining chunks: 283
Average effective duration ms: 560
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

<!-- Source: defect_20260710_043852_d3e40a.md.gz -->

# Semantic RSVP Defect Report

Report ID: defect_20260710_043852_d3e40a
Created at: 2026-07-10T04:38:52.476669Z

## Classification

Category: proper_name_split
Severity: 2
Notes:
Frank Kendall is his name

Preferred behavior:
Keep first-last name word lairs chunked together

## Reader State

Current index: 152
Sentence index: 10
Playback speed: 1x
Adaptation enabled: false

Current chunk:
Kendall,

## Timing Context

Base duration ms: 420
Effective duration ms: 420
Playback speed: 1x
Duration source: schedule
Current syntactic hint: normal
Current content word count: 1
Character length: 8
In quote: true
Quote boundary: none
In parenthetical: false
Parenthetical depth: 0
Navigation progress percent: 35
Navigation paragraph index: 7

Original sentence:
“Time didn’t permit all the normal Air Force One modifications, so some mix of security, communications and support is missing,” said Frank Kendall, the former Air Force secretary who was in charge of the department as it tried to push Boeing to accelerate its long-delayed contract to deliver two new Air Force One planes.

Previous chunks:
- [149] "communications" - 440ms base / 440ms effective - normal - 1 content word(s) - 14 chars - quote=true/none - parenthetical=false/0 - navigation=34%/p7
- [150] "and support is missing," - 640ms base / 640ms effective - dense - 2 content word(s) - 23 chars - quote=true/none - parenthetical=false/0 - navigation=34%/p7
- [151] "said Frank" - 600ms base / 600ms effective - dense - 2 content word(s) - 10 chars - quote=true/none - parenthetical=false/0 - navigation=34%/p7

Next chunks:
- [153] "the former" - 440ms base / 440ms effective - normal - 1 content word(s) - 10 chars - quote=true/none - parenthetical=false/0 - navigation=35%/p7
- [154] "Air Force" - 660ms base / 660ms effective - dense - 2 content word(s) - 9 chars - quote=true/none - parenthetical=false/0 - navigation=35%/p7
- [155] "secretary who" - 650ms base / 650ms effective - dense - 2 content word(s) - 13 chars - quote=true/none - parenthetical=false/0 - navigation=35%/p7

## Session Summary

Event count: 83
Rewind count: 28
Pause count: 17
Speed change count: 2
Adaptation count: 2
Completed: false
Elapsed session ms: 1170696
Estimated remaining chunks: 277
Average effective duration ms: 560
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

<!-- Source: defect_20260710_043946_08b4f0.md.gz -->

# Semantic RSVP Defect Report

Report ID: defect_20260710_043946_08b4f0
Created at: 2026-07-10T04:39:46.060023Z

## Classification

Category: honorific_name_split
Severity: 2
Notes:
Mr. Kendall is one thing

Preferred behavior:
Don't split honorific from name

## Reader State

Current index: 172
Sentence index: 11
Playback speed: 1x
Adaptation enabled: false

Current chunk:
Kendall said.

## Timing Context

Base duration ms: 820
Effective duration ms: 820
Playback speed: 1x
Duration source: schedule
Current syntactic hint: dense
Current content word count: 2
Character length: 13
In quote: true
Quote boundary: none
In parenthetical: false
Parenthetical depth: 0
Navigation progress percent: 39
Navigation paragraph index: 8

Original sentence:
“With the Iran situation, this could be of concern,” Mr. Kendall said.

Previous chunks:
- [169] "this could be" - 340ms base / 340ms effective - light - 0 content word(s) - 13 chars - quote=true/none - parenthetical=false/0 - navigation=38%/p8
- [170] "of concern," - 440ms base / 440ms effective - normal - 1 content word(s) - 11 chars - quote=true/none - parenthetical=false/0 - navigation=38%/p8
- [171] "Mr." - 580ms base / 580ms effective - normal - 1 content word(s) - 3 chars - quote=true/none - parenthetical=false/0 - navigation=38%/p8

Next chunks:
- [173] "Frankly," - 420ms base / 420ms effective - normal - 1 content word(s) - 8 chars - quote=true/none - parenthetical=false/0 - navigation=39%/p8
- [174] "I’ m" - 560ms base / 560ms effective - dense - 2 content word(s) - 4 chars - quote=true/none - parenthetical=false/0 - navigation=39%/p8
- [175] "surprised to see" - 650ms base / 650ms effective - dense - 2 content word(s) - 16 chars - quote=true/none - parenthetical=false/0 - navigation=39%/p8

## Session Summary

Event count: 86
Rewind count: 28
Pause count: 18
Speed change count: 2
Adaptation count: 2
Completed: false
Elapsed session ms: 1224253
Estimated remaining chunks: 257
Average effective duration ms: 560
Last adaptation reason: rewinds
Last adaptation direction: slower

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

<!-- Source: defect_20260710_044218_a4cf77.md.gz -->

# Semantic RSVP Defect Report

Report ID: defect_20260710_044218_a4cf77
Created at: 2026-07-10T04:42:18.784405Z

## Classification

Category: proper_name_split
Severity: 2
Notes:
Andrew P. Hunter is one thing

Preferred behavior:
Don't split first-initial.-last triplets of people's names.

## Reader State

Current index: 179
Sentence index: 12
Playback speed: 1x
Adaptation enabled: false

Current chunk:
P.

## Timing Context

Base duration ms: 580
Effective duration ms: 580
Playback speed: 1x
Duration source: schedule
Current syntactic hint: normal
Current content word count: 1
Character length: 2
In quote: false
Quote boundary: none
In parenthetical: false
Parenthetical depth: 0
Navigation progress percent: 40
Navigation paragraph index: 9

Original sentence:
“Frankly, I’m surprised to see this plane used outside the U.S.”

Andrew P.

Previous chunks:
- [176] "this plane" - 440ms base / 440ms effective - normal - 1 content word(s) - 10 chars - quote=true/none - parenthetical=false/0 - navigation=39%/p8
- [177] "used outside the" - 600ms base / 600ms effective - dense - 2 content word(s) - 16 chars - quote=true/none - parenthetical=false/0 - navigation=40%/p8
- [178] "U.S.” Andrew" - 600ms base / 600ms effective - dense - 2 content word(s) - 12 chars - quote=true/close - parenthetical=false/0 - navigation=40%/p8

Next chunks:
- [180] "Hunter," - 400ms base / 400ms effective - normal - 1 content word(s) - 7 chars - quote=false/none - parenthetical=false/0 - navigation=40%/p9
- [181] "the former" - 440ms base / 440ms effective - normal - 1 content word(s) - 10 chars - quote=false/none - parenthetical=false/0 - navigation=40%/p9
- [182] "Air Force" - 660ms base / 660ms effective - dense - 2 content word(s) - 9 chars - quote=false/none - parenthetical=false/0 - navigation=40%/p9

## Session Summary

Event count: 106
Rewind count: 37
Pause count: 19
Speed change count: 2
Adaptation count: 2
Completed: false
Elapsed session ms: 1377022
Estimated remaining chunks: 250
Average effective duration ms: 560
Last adaptation reason: rewinds
Last adaptation direction: slower

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

<!-- Source: defect_20260710_044318_3ccbb9.md.gz -->

# Semantic RSVP Defect Report

Report ID: defect_20260710_044318_3ccbb9
Created at: 2026-07-10T04:43:18.589942Z

## Classification

Category: proper_name_split
Severity: 2
Notes:
AirForceOne repeat

Preferred behavior:
AirForceOne repeat

## Reader State

Current index: 187
Sentence index: 13
Playback speed: 1x
Adaptation enabled: false

Current chunk:
Force One

## Timing Context

Base duration ms: 660
Effective duration ms: 660
Playback speed: 1x
Duration source: schedule
Current syntactic hint: dense
Current content word count: 2
Character length: 9
In quote: false
Quote boundary: none
In parenthetical: false
Parenthetical depth: 0
Navigation progress percent: 41
Navigation paragraph index: 9

Original sentence:
Hunter, the former Air Force assistant secretary who was in charge of the Air Force One program during the Biden administration, also said that a true retrofit of a 747 jet to prepare it to become Air Force One would require more than a year of work.

Previous chunks:
- [184] "who was" - 400ms base / 400ms effective - normal - 1 content word(s) - 7 chars - quote=false/none - parenthetical=false/0 - navigation=41%/p9
- [185] "in charge of" - 440ms base / 440ms effective - normal - 1 content word(s) - 12 chars - quote=false/none - parenthetical=false/0 - navigation=41%/p9
- [186] "the Air" - 400ms base / 400ms effective - normal - 1 content word(s) - 7 chars - quote=false/none - parenthetical=false/0 - navigation=41%/p9

Next chunks:
- [188] "program during the" - 600ms base / 600ms effective - dense - 2 content word(s) - 18 chars - quote=false/none - parenthetical=false/0 - navigation=42%/p9
- [189] "Biden administration," - 690ms base / 690ms effective - dense - 2 content word(s) - 21 chars - quote=false/none - parenthetical=false/0 - navigation=42%/p9
- [190] "also said that" - 600ms base / 600ms effective - dense - 2 content word(s) - 14 chars - quote=false/none - parenthetical=false/0 - navigation=42%/p9

## Session Summary

Event count: 110
Rewind count: 38
Pause count: 20
Speed change count: 2
Adaptation count: 2
Completed: false
Elapsed session ms: 1436820
Estimated remaining chunks: 242
Average effective duration ms: 560
Last adaptation reason: rewinds
Last adaptation direction: slower

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

<!-- Source: defect_20260710_044355_85cb58.md.gz -->

# Semantic RSVP Defect Report

Report ID: defect_20260710_044355_85cb58
Created at: 2026-07-10T04:43:55.893310Z

## Classification

Category: honorific_name_split
Severity: 2
Notes:
Mr. Trump is one thing

Preferred behavior:
Mr. Trump repeat

## Reader State

Current index: 201
Sentence index: 14
Playback speed: 1x
Adaptation enabled: false

Current chunk:
Trump left for

## Timing Context

Base duration ms: 600
Effective duration ms: 600
Playback speed: 1x
Duration source: schedule
Current syntactic hint: dense
Current content word count: 2
Character length: 14
In quote: false
Quote boundary: none
In parenthetical: false
Parenthetical depth: 0
Navigation progress percent: 45
Navigation paragraph index: 10

Original sentence:
The day before Mr. Trump left for Turkey, Senate Democrats wrote to the Air Force asking questions about the modifications to the Qatari plane and questioning whether it had all the necessary security upgrades.

Previous chunks:
- [198] "a year of work." - 820ms base / 820ms effective - dense - 2 content word(s) - 15 chars - quote=false/none - parenthetical=false/0 - navigation=44%/p9
- [199] "The day" - 400ms base / 400ms effective - normal - 1 content word(s) - 7 chars - quote=false/none - parenthetical=false/0 - navigation=44%/p10
- [200] "before Mr." - 820ms base / 820ms effective - dense - 2 content word(s) - 10 chars - quote=false/none - parenthetical=false/0 - navigation=44%/p10

Next chunks:
- [202] "Turkey," - 400ms base / 400ms effective - normal - 1 content word(s) - 7 chars - quote=false/none - parenthetical=false/0 - navigation=45%/p10
- [203] "Senate Democrats" - 710ms base / 710ms effective - dense - 2 content word(s) - 16 chars - quote=false/none - parenthetical=false/0 - navigation=45%/p10
- [204] "wrote to" - 400ms base / 400ms effective - normal - 1 content word(s) - 8 chars - quote=false/none - parenthetical=false/0 - navigation=45%/p10

## Session Summary

Event count: 113
Rewind count: 38
Pause count: 21
Speed change count: 2
Adaptation count: 2
Completed: false
Elapsed session ms: 1474121
Estimated remaining chunks: 228
Average effective duration ms: 560
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

<!-- Source: defect_20260710_044438_e9753e.md.gz -->

# Semantic RSVP Defect Report

Report ID: defect_20260710_044438_e9753e
Created at: 2026-07-10T04:44:38.087706Z

## Classification

Category: proper_name_split
Severity: 2
Notes:
AirForce repeat

Preferred behavior:
AirForce repeat

## Reader State

Current index: 206
Sentence index: 14
Playback speed: 1x
Adaptation enabled: false

Current chunk:
Force asking

## Timing Context

Base duration ms: 600
Effective duration ms: 600
Playback speed: 1x
Duration source: schedule
Current syntactic hint: dense
Current content word count: 2
Character length: 12
In quote: false
Quote boundary: none
In parenthetical: false
Parenthetical depth: 0
Navigation progress percent: 46
Navigation paragraph index: 10

Original sentence:
The day before Mr. Trump left for Turkey, Senate Democrats wrote to the Air Force asking questions about the modifications to the Qatari plane and questioning whether it had all the necessary security upgrades.

Previous chunks:
- [203] "Senate Democrats" - 710ms base / 710ms effective - dense - 2 content word(s) - 16 chars - quote=false/none - parenthetical=false/0 - navigation=45%/p10
- [204] "wrote to" - 400ms base / 400ms effective - normal - 1 content word(s) - 8 chars - quote=false/none - parenthetical=false/0 - navigation=45%/p10
- [205] "the Air" - 400ms base / 400ms effective - normal - 1 content word(s) - 7 chars - quote=false/none - parenthetical=false/0 - navigation=45%/p10

Next chunks:
- [207] "questions about the" - 690ms base / 690ms effective - dense - 2 content word(s) - 19 chars - quote=false/none - parenthetical=false/0 - navigation=46%/p10
- [208] "modifications to" - 440ms base / 440ms effective - normal - 1 content word(s) - 16 chars - quote=false/none - parenthetical=false/0 - navigation=46%/p10
- [209] "the Qatari" - 440ms base / 440ms effective - normal - 1 content word(s) - 10 chars - quote=false/none - parenthetical=false/0 - navigation=46%/p10

## Session Summary

Event count: 117
Rewind count: 39
Pause count: 22
Speed change count: 2
Adaptation count: 2
Completed: false
Elapsed session ms: 1516210
Estimated remaining chunks: 223
Average effective duration ms: 560
Last adaptation reason: rewinds
Last adaptation direction: slower

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

<!-- Source: defect_20260710_044548_a1e240.md.gz -->

# Semantic RSVP Defect Report

Report ID: defect_20260710_044548_a1e240
Created at: 2026-07-10T04:45:48.459455Z

## Classification

Category: orphan_function_word
Severity: 2
Notes:
This is the posessive s from the previous chunk

Preferred behavior:
Don't split posessive s from its quote mark

## Reader State

Current index: 220
Sentence index: 15
Playback speed: 1x
Adaptation enabled: false

Current chunk:
s ever

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
Navigation progress percent: 49
Navigation paragraph index: 11

Original sentence:
“Trump’s own statements — including his celebration of ‘a level of luxury that nobody’s ever seen before’ — make it clear that these decisions prioritized Trump’s personal comfort and tastes over U.S. national security,” they wrote in the letter sent by Senator Christopher S.

Previous chunks:
- [217] "including his" - 650ms base / 650ms effective - dense - 2 content word(s) - 13 chars - quote=false/none - parenthetical=false/0 - navigation=48%/p11
- [218] "celebration of‘ a level" - 690ms base / 690ms effective - dense - 2 content word(s) - 23 chars - quote=false/none - parenthetical=false/0 - navigation=49%/p11
- [219] "of luxury that nobody’" - 640ms base / 640ms effective - dense - 2 content word(s) - 22 chars - quote=false/none - parenthetical=false/0 - navigation=49%/p11

Next chunks:
- [221] "seen before’—" - 600ms base / 600ms effective - dense - 2 content word(s) - 13 chars - quote=false/none - parenthetical=false/0 - navigation=49%/p11
- [222] "make it clear" - 600ms base / 600ms effective - dense - 2 content word(s) - 13 chars - quote=false/none - parenthetical=false/0 - navigation=50%/p11
- [223] "that these decisions" - 480ms base / 480ms effective - normal - 1 content word(s) - 20 chars - quote=false/none - parenthetical=false/0 - navigation=50%/p11

## Session Summary

Event count: 125
Rewind count: 42
Pause count: 23
Speed change count: 2
Adaptation count: 2
Completed: false
Elapsed session ms: 1586717
Estimated remaining chunks: 209
Average effective duration ms: 560
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

<!-- Source: defect_20260710_044620_d07703.md.gz -->

# Semantic RSVP Defect Report

Report ID: defect_20260710_044620_d07703
Created at: 2026-07-10T04:46:20.206109Z

## Classification

Category: orphan_function_word
Severity: 2
Notes:
Posessive s repeat

Preferred behavior:
Posessive s repeat

## Reader State

Current index: 225
Sentence index: 15
Playback speed: 1x
Adaptation enabled: false

Current chunk:
s personal

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
Navigation progress percent: 51
Navigation paragraph index: 11

Original sentence:
“Trump’s own statements — including his celebration of ‘a level of luxury that nobody’s ever seen before’ — make it clear that these decisions prioritized Trump’s personal comfort and tastes over U.S. national security,” they wrote in the letter sent by Senator Christopher S.

Previous chunks:
- [222] "make it clear" - 600ms base / 600ms effective - dense - 2 content word(s) - 13 chars - quote=false/none - parenthetical=false/0 - navigation=50%/p11
- [223] "that these decisions" - 480ms base / 480ms effective - normal - 1 content word(s) - 20 chars - quote=false/none - parenthetical=false/0 - navigation=50%/p11
- [224] "prioritized Trump’" - 650ms base / 650ms effective - dense - 2 content word(s) - 18 chars - quote=false/none - parenthetical=false/0 - navigation=50%/p11

Next chunks:
- [226] "comfort" - 400ms base / 400ms effective - normal - 1 content word(s) - 7 chars - quote=false/none - parenthetical=false/0 - navigation=51%/p11
- [227] "and tastes" - 440ms base / 440ms effective - normal - 1 content word(s) - 10 chars - quote=false/none - parenthetical=false/0 - navigation=51%/p11
- [228] "over U.S." - 820ms base / 820ms effective - dense - 2 content word(s) - 9 chars - quote=false/none - parenthetical=false/0 - navigation=51%/p11

## Session Summary

Event count: 130
Rewind count: 44
Pause count: 24
Speed change count: 2
Adaptation count: 2
Completed: false
Elapsed session ms: 1618444
Estimated remaining chunks: 204
Average effective duration ms: 560
Last adaptation reason: rewinds
Last adaptation direction: slower

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

<!-- Source: defect_20260710_044721_524f39.md.gz -->

# Semantic RSVP Defect Report

Report ID: defect_20260710_044721_524f39
Created at: 2026-07-10T04:47:21.476173Z

## Classification

Category: proper_name_split
Severity: 2
Notes:
Christopher S. Murphy is one thing

Preferred behavior:
Firat-initial.-last name format again

## Reader State

Current index: 234
Sentence index: 16
Playback speed: 1x
Adaptation enabled: false

Current chunk:
Murphy,

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
Navigation progress percent: 52
Navigation paragraph index: 11

Original sentence:
Murphy, Democrat of Connecticut, and 12 other senators.

Previous chunks:
- [231] "the letter" - 440ms base / 440ms effective - normal - 1 content word(s) - 10 chars - quote=false/none - parenthetical=false/0 - navigation=52%/p11
- [232] "sent by Senator" - 600ms base / 600ms effective - dense - 2 content word(s) - 15 chars - quote=false/none - parenthetical=false/0 - navigation=52%/p11
- [233] "Christopher S." - 870ms base / 870ms effective - dense - 2 content word(s) - 14 chars - quote=false/none - parenthetical=false/0 - navigation=52%/p11

Next chunks:
- [235] "Democrat of Connecticut," - 750ms base / 750ms effective - dense - 2 content word(s) - 24 chars - quote=false/none - parenthetical=false/0 - navigation=53%/p11
- [236] "and 12" - 400ms base / 400ms effective - normal - 1 content word(s) - 6 chars - quote=false/none - parenthetical=false/0 - navigation=53%/p11
- [237] "other senators." - 820ms base / 820ms effective - dense - 2 content word(s) - 15 chars - quote=false/none - parenthetical=false/0 - navigation=53%/p11

## Session Summary

Event count: 136
Rewind count: 45
Pause count: 26
Speed change count: 2
Adaptation count: 2
Completed: false
Elapsed session ms: 1679735
Estimated remaining chunks: 195
Average effective duration ms: 560
Last adaptation reason: rewinds
Last adaptation direction: slower

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

<!-- Source: defect_20260710_044857_647887.md.gz -->

# Semantic RSVP Defect Report

Report ID: defect_20260710_044857_647887
Created at: 2026-07-10T04:48:57.708471Z

## Classification

Category: proper_name_split
Severity: 2
Notes:
Qassim Sulimani is one thing

Preferred behavior:
First-last name shouldn't be splkt

## Reader State

Current index: 315
Sentence index: 23
Playback speed: 1x
Adaptation enabled: false

Current chunk:
Suleimani,

## Timing Context

Base duration ms: 460
Effective duration ms: 460
Playback speed: 1x
Duration source: schedule
Current syntactic hint: normal
Current content word count: 1
Character length: 10
In quote: true
Quote boundary: none
In parenthetical: false
Parenthetical depth: 0
Navigation progress percent: 73
Navigation paragraph index: 16

Original sentence:
U.S. officials have said that Iran has been targeting Mr. Trump since he ordered the drone strike that killed Qassim Suleimani, in January 2020.

Previous chunks:
- [312] "he ordered the" - 600ms base / 600ms effective - dense - 2 content word(s) - 14 chars - quote=true/none - parenthetical=false/0 - navigation=72%/p16
- [313] "drone strike that" - 600ms base / 600ms effective - dense - 2 content word(s) - 17 chars - quote=true/none - parenthetical=false/0 - navigation=73%/p16
- [314] "killed Qassim" - 600ms base / 600ms effective - dense - 2 content word(s) - 13 chars - quote=true/none - parenthetical=false/0 - navigation=73%/p16

Next chunks:
- [316] "in January" - 440ms base / 440ms effective - normal - 1 content word(s) - 10 chars - quote=true/none - parenthetical=false/0 - navigation=73%/p16
- [317] "2020." - 580ms base / 580ms effective - normal - 1 content word(s) - 5 chars - quote=true/none - parenthetical=false/0 - navigation=73%/p16
- [318] "During the 2024" - 600ms base / 600ms effective - dense - 2 content word(s) - 15 chars - quote=true/none - parenthetical=false/0 - navigation=74%/p16

## Session Summary

Event count: 145
Rewind count: 47
Pause count: 29
Speed change count: 2
Adaptation count: 2
Completed: false
Elapsed session ms: 1775933
Estimated remaining chunks: 114
Average effective duration ms: 560
Last adaptation reason: rewinds
Last adaptation direction: slower

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

<!-- Source: defect_20260710_045028_e52228.md.gz -->

# Semantic RSVP Defect Report

Report ID: defect_20260710_045028_e52228
Created at: 2026-07-10T04:50:28.726059Z

## Classification

Category: proper_name_split
Severity: 2
Notes:
Butler, Pa is one thing

Preferred behavior:
Don't split Place-State pairs with 2 letter state codes

## Reader State

Current index: 327
Sentence index: 24
Playback speed: 1x
Adaptation enabled: false

Current chunk:
Pa.

## Timing Context

Base duration ms: 580
Effective duration ms: 580
Playback speed: 1x
Duration source: schedule
Current syntactic hint: normal
Current content word count: 1
Character length: 3
In quote: true
Quote boundary: none
In parenthetical: false
Parenthetical depth: 0
Navigation progress percent: 75
Navigation paragraph index: 16

Original sentence:
During the 2024 campaign, the Secret Service increased protection for Mr. Trump, even before the attempt on his life in Butler, Pa., because of intelligence about Iran’s plotting against him.

Previous chunks:
- [324] "even before the" - 600ms base / 600ms effective - dense - 2 content word(s) - 15 chars - quote=true/none - parenthetical=false/0 - navigation=75%/p16
- [325] "attempt on his" - 600ms base / 600ms effective - dense - 2 content word(s) - 14 chars - quote=true/none - parenthetical=false/0 - navigation=75%/p16
- [326] "life in Butler," - 600ms base / 600ms effective - dense - 2 content word(s) - 15 chars - quote=true/none - parenthetical=false/0 - navigation=75%/p16

Next chunks:
- [328] "because of intelligence" - 690ms base / 690ms effective - dense - 2 content word(s) - 23 chars - quote=true/none - parenthetical=false/0 - navigation=76%/p16
- [329] "about Iran’" - 600ms base / 600ms effective - dense - 2 content word(s) - 11 chars - quote=true/none - parenthetical=false/0 - navigation=76%/p16
- [330] "s plotting" - 600ms base / 600ms effective - dense - 2 content word(s) - 10 chars - quote=true/none - parenthetical=false/0 - navigation=76%/p16

## Session Summary

Event count: 151
Rewind count: 48
Pause count: 31
Speed change count: 2
Adaptation count: 2
Completed: false
Elapsed session ms: 1866979
Estimated remaining chunks: 102
Average effective duration ms: 560
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

<!-- Source: defect_20260710_045138_675234.md.gz -->

# Semantic RSVP Defect Report

Report ID: defect_20260710_045138_675234
Created at: 2026-07-10T04:51:38.317801Z

## Classification

Category: proper_name_split
Severity: 2
Notes:
White House is one thing

Preferred behavior:
Don't split proper names

## Reader State

Current index: 403
Sentence index: 29
Playback speed: 1x
Adaptation enabled: false

Current chunk:
House official

## Timing Context

Base duration ms: 600
Effective duration ms: 600
Playback speed: 1x
Duration source: schedule
Current syntactic hint: dense
Current content word count: 2
Character length: 14
In quote: true
Quote boundary: none
In parenthetical: false
Parenthetical depth: 0
Navigation progress percent: 93
Navigation paragraph index: 20

Original sentence:
One former senior White House official involved in discussions about military aircraft used for presidential travel said that there were frequently points of tension between White House staff and the military advisers and Secret Service over travel plans when security questions emerged.

Previous chunks:
- [400] "is“ magnificent." - 620ms base / 620ms effective - normal - 1 content word(s) - 16 chars - quote=true/open - parenthetical=false/0 - navigation=92%/p19
- [401] "One former" - 600ms base / 600ms effective - dense - 2 content word(s) - 10 chars - quote=true/none - parenthetical=false/0 - navigation=92%/p20
- [402] "senior White" - 600ms base / 600ms effective - dense - 2 content word(s) - 12 chars - quote=true/none - parenthetical=false/0 - navigation=92%/p20

Next chunks:
- [404] "involved in discussions" - 690ms base / 690ms effective - dense - 2 content word(s) - 23 chars - quote=true/none - parenthetical=false/0 - navigation=93%/p20
- [405] "about military" - 600ms base / 600ms effective - dense - 2 content word(s) - 14 chars - quote=true/none - parenthetical=false/0 - navigation=93%/p20
- [406] "aircraft used for" - 600ms base / 600ms effective - dense - 2 content word(s) - 17 chars - quote=true/none - parenthetical=false/0 - navigation=94%/p20

## Session Summary

Event count: 157
Rewind count: 49
Pause count: 33
Speed change count: 2
Adaptation count: 2
Completed: false
Elapsed session ms: 1936592
Estimated remaining chunks: 26
Average effective duration ms: 560
Last adaptation reason: rewinds
Last adaptation direction: slower

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

<!-- Source: defect_20260710_045210_9855b5.md.gz -->

# Semantic RSVP Defect Report

Report ID: defect_20260710_045210_9855b5
Created at: 2026-07-10T04:52:10.477386Z

## Classification

Category: proper_name_split
Severity: 2
Notes:
White House repeat

Preferred behavior:
White House repeat

## Reader State

Current index: 412
Sentence index: 29
Playback speed: 1x
Adaptation enabled: false

Current chunk:
House staff

## Timing Context

Base duration ms: 600
Effective duration ms: 600
Playback speed: 1x
Duration source: schedule
Current syntactic hint: dense
Current content word count: 2
Character length: 11
In quote: true
Quote boundary: none
In parenthetical: false
Parenthetical depth: 0
Navigation progress percent: 95
Navigation paragraph index: 20

Original sentence:
One former senior White House official involved in discussions about military aircraft used for presidential travel said that there were frequently points of tension between White House staff and the military advisers and Secret Service over travel plans when security questions emerged.

Previous chunks:
- [409] "were frequently" - 440ms base / 440ms effective - normal - 1 content word(s) - 15 chars - quote=true/none - parenthetical=false/0 - navigation=94%/p20
- [410] "points of tension" - 600ms base / 600ms effective - dense - 2 content word(s) - 17 chars - quote=true/none - parenthetical=false/0 - navigation=95%/p20
- [411] "between White" - 600ms base / 600ms effective - dense - 2 content word(s) - 13 chars - quote=true/none - parenthetical=false/0 - navigation=95%/p20

Next chunks:
- [413] "and the military" - 440ms base / 440ms effective - normal - 1 content word(s) - 16 chars - quote=true/none - parenthetical=false/0 - navigation=95%/p20
- [414] "advisers" - 400ms base / 400ms effective - normal - 1 content word(s) - 8 chars - quote=true/none - parenthetical=false/0 - navigation=96%/p20
- [415] "and Secret" - 440ms base / 440ms effective - normal - 1 content word(s) - 10 chars - quote=true/none - parenthetical=false/0 - navigation=96%/p20

## Session Summary

Event count: 161
Rewind count: 50
Pause count: 34
Speed change count: 2
Adaptation count: 2
Completed: false
Elapsed session ms: 1968731
Estimated remaining chunks: 17
Average effective duration ms: 560
Last adaptation reason: rewinds
Last adaptation direction: slower

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

<!-- Source: defect_20260710_045257_ed9b3e.md.gz -->

# Semantic RSVP Defect Report

Report ID: defect_20260710_045257_ed9b3e
Created at: 2026-07-10T04:52:57.339257Z

## Classification

Category: proper_name_split
Severity: 2
Notes:
The Secret Service is one thing

Preferred behavior:
Don't split proper names or their articles

## Reader State

Current index: 416
Sentence index: 29
Playback speed: 1x
Adaptation enabled: false

Current chunk:
Service over

## Timing Context

Base duration ms: 600
Effective duration ms: 600
Playback speed: 1x
Duration source: schedule
Current syntactic hint: dense
Current content word count: 2
Character length: 12
In quote: true
Quote boundary: none
In parenthetical: false
Parenthetical depth: 0
Navigation progress percent: 96
Navigation paragraph index: 20

Original sentence:
One former senior White House official involved in discussions about military aircraft used for presidential travel said that there were frequently points of tension between White House staff and the military advisers and Secret Service over travel plans when security questions emerged.

Previous chunks:
- [413] "and the military" - 440ms base / 440ms effective - normal - 1 content word(s) - 16 chars - quote=true/none - parenthetical=false/0 - navigation=95%/p20
- [414] "advisers" - 400ms base / 400ms effective - normal - 1 content word(s) - 8 chars - quote=true/none - parenthetical=false/0 - navigation=96%/p20
- [415] "and Secret" - 440ms base / 440ms effective - normal - 1 content word(s) - 10 chars - quote=true/none - parenthetical=false/0 - navigation=96%/p20

Next chunks:
- [417] "travel plans" - 600ms base / 600ms effective - dense - 2 content word(s) - 12 chars - quote=true/none - parenthetical=false/0 - navigation=96%/p20
- [418] "when security" - 600ms base / 600ms effective - dense - 2 content word(s) - 13 chars - quote=true/none - parenthetical=false/0 - navigation=96%/p20
- [419] "questions emerged." - 870ms base / 870ms effective - dense - 2 content word(s) - 18 chars - quote=true/none - parenthetical=false/0 - navigation=97%/p20

## Session Summary

Event count: 165
Rewind count: 51
Pause count: 35
Speed change count: 2
Adaptation count: 2
Completed: false
Elapsed session ms: 2015599
Estimated remaining chunks: 13
Average effective duration ms: 560
Last adaptation reason: rewinds
Last adaptation direction: slower

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

<!-- Source: defect_20260710_045539_06bf50.md.gz -->

# Semantic RSVP Defect Report

Report ID: defect_20260710_045539_06bf50
Created at: 2026-07-10T04:55:39.497161Z

## Classification

Category: title_name_split
Severity: 2
Notes:
Dr. Kudrenko is one thing

Preferred behavior:
Don't splot title and name

## Reader State

Current index: 41
Sentence index: 2
Playback speed: 1x
Adaptation enabled: false

Current chunk:
Kudrenko said.

## Timing Context

Base duration ms: 820
Effective duration ms: 820
Playback speed: 1x
Duration source: schedule
Current syntactic hint: dense
Current content word count: 2
Character length: 14
In quote: true
Quote boundary: none
In parenthetical: false
Parenthetical depth: 0
Navigation progress percent: 16
Navigation paragraph index: 0

Original sentence:
For instance, a 5 corresponded to the movement of military vehicles; an 8 meant cruise missiles; a 10 was reserved for “the noisiest and the most destructive type of armed conflict activity,” such as aerial bombardments or artillery shelling, Dr. Kudrenko said.

Previous chunks:
- [38] "or artillery" - 440ms base / 440ms effective - normal - 1 content word(s) - 12 chars - quote=true/none - parenthetical=false/0 - navigation=15%/p0
- [39] "shelling," - 460ms base / 460ms effective - normal - 1 content word(s) - 9 chars - quote=true/none - parenthetical=false/0 - navigation=16%/p0
- [40] "Dr." - 580ms base / 580ms effective - normal - 1 content word(s) - 3 chars - quote=true/none - parenthetical=false/0 - navigation=16%/p0

Next chunks:
- [42] "They also" - 600ms base / 600ms effective - dense - 2 content word(s) - 9 chars - quote=true/none - parenthetical=false/0 - navigation=17%/p1
- [43] "used satellite" - 650ms base / 650ms effective - dense - 2 content word(s) - 14 chars - quote=true/none - parenthetical=false/0 - navigation=17%/p1
- [44] "data to identify" - 600ms base / 600ms effective - dense - 2 content word(s) - 16 chars - quote=true/none - parenthetical=false/0 - navigation=18%/p1

## Session Summary

Event count: 10
Rewind count: 0
Pause count: 2
Speed change count: 2
Adaptation count: 2
Completed: false
Elapsed session ms: 71416
Estimated remaining chunks: 194
Average effective duration ms: 546
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

<!-- Source: defect_20260710_045627_38797e.md.gz -->

# Semantic RSVP Defect Report

Report ID: defect_20260710_045627_38797e
Created at: 2026-07-10T04:56:27.657988Z

## Classification

Category: title_name_split
Severity: 2
Notes:
Dr. Kudrenko repeat

Preferred behavior:
Dr. Kudrenko repeat

## Reader State

Current index: 82
Sentence index: 7
Playback speed: 1x
Adaptation enabled: false

Current chunk:
Kudrenko said.

## Timing Context

Base duration ms: 820
Effective duration ms: 820
Playback speed: 1x
Duration source: schedule
Current syntactic hint: dense
Current content word count: 2
Character length: 14
In quote: false
Quote boundary: none
In parenthetical: false
Parenthetical depth: 0
Navigation progress percent: 33
Navigation paragraph index: 3

Original sentence:
Those opposing responses may stem from differences in the two species’ basic behavior and ecology, Dr. Kudrenko said.

Previous chunks:
- [79] "behavior" - 400ms base / 400ms effective - normal - 1 content word(s) - 8 chars - quote=false/none - parenthetical=false/0 - navigation=32%/p3
- [80] "and ecology," - 440ms base / 440ms effective - normal - 1 content word(s) - 12 chars - quote=false/none - parenthetical=false/0 - navigation=33%/p3
- [81] "Dr." - 580ms base / 580ms effective - normal - 1 content word(s) - 3 chars - quote=false/none - parenthetical=false/0 - navigation=33%/p3

Next chunks:
- [83] "Roe deer," - 600ms base / 600ms effective - dense - 2 content word(s) - 9 chars - quote=false/none - parenthetical=false/0 - navigation=34%/p4
- [84] "which are known" - 600ms base / 600ms effective - dense - 2 content word(s) - 15 chars - quote=false/none - parenthetical=false/0 - navigation=34%/p4
- [85] "to be shy," - 440ms base / 440ms effective - normal - 1 content word(s) - 10 chars - quote=false/none - parenthetical=false/0 - navigation=34%/p4

## Session Summary

Event count: 14
Rewind count: 1
Pause count: 3
Speed change count: 2
Adaptation count: 2
Completed: false
Elapsed session ms: 119585
Estimated remaining chunks: 153
Average effective duration ms: 546
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

<!-- Source: defect_20260710_045807_2986d4.md.gz -->

# Semantic RSVP Defect Report

Report ID: defect_20260710_045807_2986d4
Created at: 2026-07-10T04:58:07.616465Z

## Classification

Category: proper_name_split
Severity: 2
Notes:
Chernoby Exclusion Zone os one thing

Preferred behavior:
 Don't split proper names

## Reader State

Current index: 167
Sentence index: 16
Playback speed: 1x
Adaptation enabled: false

Current chunk:
Exclusion Zone— it’

## Timing Context

Base duration ms: 750
Effective duration ms: 750
Playback speed: 1x
Duration source: schedule
Current syntactic hint: dense
Current content word count: 2
Character length: 19
In quote: true
Quote boundary: none
In parenthetical: false
Parenthetical depth: 0
Navigation progress percent: 68
Navigation paragraph index: 7

Original sentence:
But it’s also possible that some of the unique characteristics of the Chernobyl Exclusion Zone — it’s enormous size and extremely restricted human activity — helped buffer the effects of armed conflict, Dr. Kudrenko said.

Previous chunks:
- [164] "the unique" - 440ms base / 440ms effective - normal - 1 content word(s) - 10 chars - quote=true/none - parenthetical=false/0 - navigation=67%/p7
- [165] "characteristics of" - 440ms base / 440ms effective - normal - 1 content word(s) - 18 chars - quote=true/none - parenthetical=false/0 - navigation=67%/p7
- [166] "the Chernobyl" - 440ms base / 440ms effective - normal - 1 content word(s) - 13 chars - quote=true/none - parenthetical=false/0 - navigation=68%/p7

Next chunks:
- [168] "s enormous" - 600ms base / 600ms effective - dense - 2 content word(s) - 10 chars - quote=true/none - parenthetical=false/0 - navigation=69%/p7
- [169] "size" - 400ms base / 400ms effective - normal - 1 content word(s) - 4 chars - quote=true/none - parenthetical=false/0 - navigation=69%/p7
- [170] "and extremely" - 440ms base / 440ms effective - normal - 1 content word(s) - 13 chars - quote=true/none - parenthetical=false/0 - navigation=69%/p7

## Session Summary

Event count: 18
Rewind count: 2
Pause count: 4
Speed change count: 2
Adaptation count: 2
Completed: false
Elapsed session ms: 219546
Estimated remaining chunks: 68
Average effective duration ms: 546
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

<!-- Source: defect_20260710_045906_db22bb.md.gz -->

# Semantic RSVP Defect Report

Report ID: defect_20260710_045906_db22bb
Created at: 2026-07-10T04:59:06.626688Z

## Classification

Category: proper_name_split
Severity: 2
Notes:
Kaitlyn Gaynor is one thing

Preferred behavior:
Don't split first-last name pairs

## Reader State

Current index: 191
Sentence index: 17
Playback speed: 1x
Adaptation enabled: false

Current chunk:
Gaynor,

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
Navigation progress percent: 78
Navigation paragraph index: 8

Original sentence:
The study highlights the fact that there is rarely a “one-size-fits-all response” to warfare and provides valuable insight into wildlife responses on a day-to-day basis, said Kaitlyn Gaynor, an ecologist at the University of British Columbia who was not involved in the new research.

Previous chunks:
- [188] "a day- to-" - 440ms base / 440ms effective - normal - 1 content word(s) - 10 chars - quote=false/none - parenthetical=false/0 - navigation=77%/p8
- [189] "day basis," - 600ms base / 600ms effective - dense - 2 content word(s) - 10 chars - quote=false/none - parenthetical=false/0 - navigation=77%/p8
- [190] "said Kaitlyn" - 600ms base / 600ms effective - dense - 2 content word(s) - 12 chars - quote=false/none - parenthetical=false/0 - navigation=78%/p8

Next chunks:
- [192] "an ecologist at" - 440ms base / 440ms effective - normal - 1 content word(s) - 15 chars - quote=false/none - parenthetical=false/0 - navigation=79%/p8
- [193] "the University of British" - 750ms base / 750ms effective - dense - 2 content word(s) - 25 chars - quote=false/none - parenthetical=false/0 - navigation=79%/p8
- [194] "Columbia who" - 600ms base / 600ms effective - dense - 2 content word(s) - 12 chars - quote=false/none - parenthetical=false/0 - navigation=80%/p8

## Session Summary

Event count: 25
Rewind count: 4
Pause count: 6
Speed change count: 2
Adaptation count: 2
Completed: false
Elapsed session ms: 278552
Estimated remaining chunks: 44
Average effective duration ms: 546
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

<!-- Source: defect_20260710_050001_5e8585.md.gz -->

# Semantic RSVP Defect Report

Report ID: defect_20260710_050001_5e8585
Created at: 2026-07-10T05:00:01.257528Z

## Classification

Category: proper_name_split
Severity: 2
Notes:
University of British Columbia is one thing

Preferred behavior:
Don't split proper names

## Reader State

Current index: 194
Sentence index: 17
Playback speed: 1x
Adaptation enabled: false

Current chunk:
Columbia who

## Timing Context

Base duration ms: 600
Effective duration ms: 600
Playback speed: 1x
Duration source: schedule
Current syntactic hint: dense
Current content word count: 2
Character length: 12
In quote: false
Quote boundary: none
In parenthetical: false
Parenthetical depth: 0
Navigation progress percent: 80
Navigation paragraph index: 8

Original sentence:
The study highlights the fact that there is rarely a “one-size-fits-all response” to warfare and provides valuable insight into wildlife responses on a day-to-day basis, said Kaitlyn Gaynor, an ecologist at the University of British Columbia who was not involved in the new research.

Previous chunks:
- [191] "Gaynor," - 400ms base / 400ms effective - normal - 1 content word(s) - 7 chars - quote=false/none - parenthetical=false/0 - navigation=78%/p8
- [192] "an ecologist at" - 440ms base / 440ms effective - normal - 1 content word(s) - 15 chars - quote=false/none - parenthetical=false/0 - navigation=79%/p8
- [193] "the University of British" - 750ms base / 750ms effective - dense - 2 content word(s) - 25 chars - quote=false/none - parenthetical=false/0 - navigation=79%/p8

Next chunks:
- [195] "was not involved" - 440ms base / 440ms effective - normal - 1 content word(s) - 16 chars - quote=false/none - parenthetical=false/0 - navigation=80%/p8
- [196] "in the new" - 440ms base / 440ms effective - normal - 1 content word(s) - 10 chars - quote=false/none - parenthetical=false/0 - navigation=81%/p8
- [197] "research." - 620ms base / 620ms effective - normal - 1 content word(s) - 9 chars - quote=false/none - parenthetical=false/0 - navigation=81%/p8

## Session Summary

Event count: 28
Rewind count: 4
Pause count: 7
Speed change count: 2
Adaptation count: 2
Completed: false
Elapsed session ms: 333175
Estimated remaining chunks: 41
Average effective duration ms: 546
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

<!-- Source: defect_20260710_050110_3b75b3.md.gz -->

# Semantic RSVP Defect Report

Report ID: defect_20260710_050110_3b75b3
Created at: 2026-07-10T05:01:10.027306Z

## Classification

Category: honorific_name_split
Severity: 2
Notes:
Dr. Gaynor is one thing

Preferred behavior:
Don't split honorific and name

## Reader State

Current index: 225
Sentence index: 20
Playback speed: 1x
Adaptation enabled: false

Current chunk:
Gaynor said.

## Timing Context

Base duration ms: 820
Effective duration ms: 820
Playback speed: 1x
Duration source: schedule
Current syntactic hint: dense
Current content word count: 2
Character length: 12
In quote: false
Quote boundary: none
In parenthetical: false
Parenthetical depth: 0
Navigation progress percent: 94
Navigation paragraph index: 10

Original sentence:
“There are all of these unintended consequences of armed conflict,” Dr. Gaynor said.

Previous chunks:
- [222] "consequences of armed" - 690ms base / 690ms effective - dense - 2 content word(s) - 21 chars - quote=false/none - parenthetical=false/0 - navigation=94%/p10
- [223] "conflict," - 460ms base / 460ms effective - normal - 1 content word(s) - 9 chars - quote=false/none - parenthetical=false/0 - navigation=94%/p10
- [224] "Dr." - 580ms base / 580ms effective - normal - 1 content word(s) - 3 chars - quote=false/none - parenthetical=false/0 - navigation=94%/p10

Next chunks:
- [226] "And I" - 400ms base / 400ms effective - normal - 1 content word(s) - 5 chars - quote=false/none - parenthetical=false/0 - navigation=95%/p10
- [227] "think the study" - 600ms base / 600ms effective - dense - 2 content word(s) - 15 chars - quote=false/none - parenthetical=false/0 - navigation=95%/p10
- [228] "shows that wildlife" - 640ms base / 640ms effective - dense - 2 content word(s) - 19 chars - quote=false/none - parenthetical=false/0 - navigation=96%/p10

## Session Summary

Event count: 34
Rewind count: 5
Pause count: 9
Speed change count: 2
Adaptation count: 2
Completed: false
Elapsed session ms: 401962
Estimated remaining chunks: 10
Average effective duration ms: 546
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

<!-- Source: defect_20260710_050343_d64379.md.gz -->

# Semantic RSVP Defect Report

Report ID: defect_20260710_050343_d64379
Created at: 2026-07-10T05:03:43.746048Z

## Classification

Category: proper_name_split
Severity: 2
Notes:
Board of Trustees is one thing

Preferred behavior:
Don't split proper names

## Reader State

Current index: 7
Sentence index: 1
Playback speed: 1x
Adaptation enabled: true

Current chunk:
Trustees resolved

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
Navigation progress percent: 8
Navigation paragraph index: 0

Original sentence:
In 1876, Dartmouth's Board of Trustees resolved to fill some upcoming vacancies with alumni.

Previous chunks:
- [4] "nineteenth century." - 910ms base / 910ms effective - dense - 2 content word(s) - 19 chars - quote=false/none - parenthetical=false/0 - navigation=5%/p0
- [5] "In 1876," - 400ms base / 400ms effective - normal - 1 content word(s) - 8 chars - quote=false/none - parenthetical=false/0 - navigation=5%/p0
- [6] "Dartmouth's Board of" - 750ms base / 750ms effective - dense - 2 content word(s) - 20 chars - quote=false/none - parenthetical=false/0 - navigation=6%/p0

Next chunks:
- [8] "to fill" - 400ms base / 400ms effective - normal - 1 content word(s) - 7 chars - quote=false/none - parenthetical=false/0 - navigation=8%/p0
- [9] "some upcoming" - 600ms base / 600ms effective - dense - 2 content word(s) - 13 chars - quote=false/none - parenthetical=false/0 - navigation=9%/p0
- [10] "vacancies with alumni." - 910ms base / 910ms effective - dense - 2 content word(s) - 22 chars - quote=false/none - parenthetical=false/0 - navigation=10%/p0

## Session Summary

Event count: 4
Rewind count: 1
Pause count: 1
Speed change count: 0
Adaptation count: 0
Completed: false
Elapsed session ms: 49614
Estimated remaining chunks: 109
Average effective duration ms: 562
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

<!-- Source: defect_20260710_050453_98d6be.md.gz -->

# Semantic RSVP Defect Report

Report ID: defect_20260710_050453_98d6be
Created at: 2026-07-10T05:04:53.905601Z

## Classification

Category: proper_name_split
Severity: 2
Notes:
The Association of Alumni is one thing

Preferred behavior:
Don't split proper names

## Reader State

Current index: 43
Sentence index: 4
Playback speed: 1.3x
Adaptation enabled: true

Current chunk:
of Alumni of Dartmouth

## Timing Context

Base duration ms: 750
Effective duration ms: 577
Playback speed: 1.3x
Duration source: schedule
Current syntactic hint: dense
Current content word count: 2
Character length: 22
In quote: false
Quote boundary: none
In parenthetical: false
Parenthetical depth: 0
Navigation progress percent: 38
Navigation paragraph index: 0

Original sentence:
The nomination process would be handled by the Association of Alumni of Dartmouth College, of which every matriculated student becomes a member automatically upon graduation.

Previous chunks:
- [40] "The nomination" - 440ms base / 338ms effective - normal - 1 content word(s) - 14 chars - quote=false/none - parenthetical=false/0 - navigation=34%/p0
- [41] "process would be handled" - 640ms base / 492ms effective - dense - 2 content word(s) - 24 chars - quote=false/none - parenthetical=false/0 - navigation=35%/p0
- [42] "by the Association" - 440ms base / 338ms effective - normal - 1 content word(s) - 18 chars - quote=false/none - parenthetical=false/0 - navigation=36%/p0

Next chunks:
- [44] "College," - 420ms base / 323ms effective - normal - 1 content word(s) - 8 chars - quote=false/none - parenthetical=false/0 - navigation=38%/p0
- [45] "of which" - 400ms base / 308ms effective - normal - 1 content word(s) - 8 chars - quote=false/none - parenthetical=false/0 - navigation=39%/p0
- [46] "every matriculated" - 650ms base / 500ms effective - dense - 2 content word(s) - 18 chars - quote=false/none - parenthetical=false/0 - navigation=40%/p0

## Session Summary

Event count: 15
Rewind count: 5
Pause count: 2
Speed change count: 0
Adaptation count: 4
Completed: false
Elapsed session ms: 119777
Estimated remaining chunks: 73
Average effective duration ms: 432
Last adaptation reason: rewinds
Last adaptation direction: slower

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

<!-- Source: defect_20260710_050523_ebce24.md.gz -->

# Semantic RSVP Defect Report

Report ID: defect_20260710_050523_ebce24
Created at: 2026-07-10T05:05:23.499149Z

## Classification

Category: proper_name_split
Severity: 2
Notes:
Dartmouth College is one thing

Preferred behavior:
Don't sllit proper names

## Reader State

Current index: 44
Sentence index: 4
Playback speed: 1x
Adaptation enabled: true

Current chunk:
College,

## Timing Context

Base duration ms: 420
Effective duration ms: 420
Playback speed: 1x
Duration source: schedule
Current syntactic hint: normal
Current content word count: 1
Character length: 8
In quote: false
Quote boundary: none
In parenthetical: false
Parenthetical depth: 0
Navigation progress percent: 38
Navigation paragraph index: 0

Original sentence:
The nomination process would be handled by the Association of Alumni of Dartmouth College, of which every matriculated student becomes a member automatically upon graduation.

Previous chunks:
- [41] "process would be handled" - 640ms base / 640ms effective - dense - 2 content word(s) - 24 chars - quote=false/none - parenthetical=false/0 - navigation=35%/p0
- [42] "by the Association" - 440ms base / 440ms effective - normal - 1 content word(s) - 18 chars - quote=false/none - parenthetical=false/0 - navigation=36%/p0
- [43] "of Alumni of Dartmouth" - 750ms base / 750ms effective - dense - 2 content word(s) - 22 chars - quote=false/none - parenthetical=false/0 - navigation=38%/p0

Next chunks:
- [45] "of which" - 400ms base / 400ms effective - normal - 1 content word(s) - 8 chars - quote=false/none - parenthetical=false/0 - navigation=39%/p0
- [46] "every matriculated" - 650ms base / 650ms effective - dense - 2 content word(s) - 18 chars - quote=false/none - parenthetical=false/0 - navigation=40%/p0
- [47] "student becomes a" - 600ms base / 600ms effective - dense - 2 content word(s) - 17 chars - quote=false/none - parenthetical=false/0 - navigation=41%/p0

## Session Summary

Event count: 23
Rewind count: 8
Pause count: 3
Speed change count: 0
Adaptation count: 6
Completed: false
Elapsed session ms: 149392
Estimated remaining chunks: 72
Average effective duration ms: 562
Last adaptation reason: rewinds
Last adaptation direction: slower

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

<!-- Source: defect_20260710_050601_7a6499.md.gz -->

# Semantic RSVP Defect Report

Report ID: defect_20260710_050601_7a6499
Created at: 2026-07-10T05:06:01.697430Z

## Classification

Category: proper_name_split
Severity: 2
Notes:
Williams College is one thing

Preferred behavior:
Don't split proper names

## Reader State

Current index: 70
Sentence index: 5
Playback speed: 1.3x
Adaptation enabled: true

Current chunk:
College.

## Timing Context

Base duration ms: 580
Effective duration ms: 446
Playback speed: 1.3x
Duration source: schedule
Current syntactic hint: normal
Current content word count: 1
Character length: 8
In quote: false
Quote boundary: none
In parenthetical: false
Parenthetical depth: 0
Navigation progress percent: 61
Navigation paragraph index: 0

Original sentence:
Soon after the Board issued its 1891 resolution, five members resigned to open seats for the new nominees, and Dartmouth's first effective means of granting alumni influence on the composition of its Board was under way; the arrangement was described as being based on the system in use at Williams College.

Previous chunks:
- [67] "as being based" - 440ms base / 338ms effective - normal - 1 content word(s) - 14 chars - quote=false/none - parenthetical=false/0 - navigation=58%/p0
- [68] "on the system" - 440ms base / 338ms effective - normal - 1 content word(s) - 13 chars - quote=false/none - parenthetical=false/0 - navigation=59%/p0
- [69] "in use at Williams" - 600ms base / 462ms effective - dense - 2 content word(s) - 18 chars - quote=false/none - parenthetical=false/0 - navigation=60%/p0

Next chunks:
- [71] "The Board has expanded" - 700ms base / 538ms effective - dense - 2 content word(s) - 22 chars - quote=false/none - parenthetical=false/0 - navigation=62%/p1
- [72] "three times" - 600ms base / 462ms effective - dense - 2 content word(s) - 11 chars - quote=false/none - parenthetical=false/0 - navigation=63%/p1
- [73] "since it" - 400ms base / 308ms effective - normal - 1 content word(s) - 8 chars - quote=false/none - parenthetical=false/0 - navigation=63%/p1

## Session Summary

Event count: 29
Rewind count: 9
Pause count: 4
Speed change count: 0
Adaptation count: 8
Completed: false
Elapsed session ms: 187583
Estimated remaining chunks: 46
Average effective duration ms: 432
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

<!-- Source: defect_20260710_050652_a0ee17.md.gz -->

# Semantic RSVP Defect Report

Report ID: defect_20260710_050652_a0ee17
Created at: 2026-07-10T05:06:52.322505Z

## Classification

Category: proper_name_split
Severity: 2
Notes:
The New-Hampshire Legislature is one thing

Preferred behavior:
Don't split proper names

## Reader State

Current index: 78
Sentence index: 7
Playback speed: 1.3x
Adaptation enabled: true

Current chunk:
Hampshire Legislature

## Timing Context

Base duration ms: 750
Effective duration ms: 577
Playback speed: 1.3x
Duration source: schedule
Current syntactic hint: dense
Current content word count: 2
Character length: 21
In quote: false
Quote boundary: none
In parenthetical: false
Parenthetical depth: 0
Navigation progress percent: 68
Navigation paragraph index: 1

Original sentence:
The New Hampshire Legislature approved an amendment to the Charter that expanded the Board to sixteen in 1961.

Previous chunks:
- [75] "a twelve- person" - 600ms base / 462ms effective - dense - 2 content word(s) - 16 chars - quote=false/none - parenthetical=false/0 - navigation=65%/p1
- [76] "organization in 1769." - 910ms base / 700ms effective - dense - 2 content word(s) - 21 chars - quote=false/none - parenthetical=false/0 - navigation=67%/p1
- [77] "The New" - 400ms base / 308ms effective - normal - 1 content word(s) - 7 chars - quote=false/none - parenthetical=false/0 - navigation=67%/p1

Next chunks:
- [79] "approved an amendment" - 690ms base / 531ms effective - dense - 2 content word(s) - 21 chars - quote=false/none - parenthetical=false/0 - navigation=70%/p1
- [80] "to the Charter" - 440ms base / 338ms effective - normal - 1 content word(s) - 14 chars - quote=false/none - parenthetical=false/0 - navigation=70%/p1
- [81] "that expanded the Board" - 640ms base / 492ms effective - dense - 2 content word(s) - 23 chars - quote=false/none - parenthetical=false/0 - navigation=72%/p1

## Session Summary

Event count: 38
Rewind count: 13
Pause count: 5
Speed change count: 0
Adaptation count: 10
Completed: false
Elapsed session ms: 238209
Estimated remaining chunks: 38
Average effective duration ms: 432
Last adaptation reason: rewinds
Last adaptation direction: slower

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

<!-- Source: defect_20260710_050813_fbfba5.md.gz -->

# Semantic RSVP Defect Report

Report ID: defect_20260710_050813_fbfba5
Created at: 2026-07-10T05:08:13.457348Z

## Classification

Category: parenthetical_state_confusion
Severity: 2
Notes:
This is just a bullet point, not a parentheses

Preferred behavior:
Ignore bullet point style parentheses

## Reader State

Current index: 89
Sentence index: 8
Playback speed: 0.75x
Adaptation enabled: true

Current chunk:
3] This expansion

## Timing Context

Base duration ms: 650
Effective duration ms: 867
Playback speed: 0.75x
Duration source: schedule
Current syntactic hint: dense
Current content word count: 2
Character length: 17
In quote: false
Quote boundary: none
In parenthetical: true
Parenthetical depth: 0
Navigation progress percent: 78
Navigation paragraph index: 1

Original sentence:
In 2003, the Board grew to eighteen and stated plans to reach twenty-two.[3] This expansion was the Board's first act under its new authority to amend its own charter, an authority granted by the Legislature during the same period.

Previous chunks:
- [86] "and stated" - 440ms base / 587ms effective - normal - 1 content word(s) - 10 chars - quote=false/none - parenthetical=false/0 - navigation=76%/p1
- [87] "plans to reach" - 600ms base / 800ms effective - dense - 2 content word(s) - 14 chars - quote=false/none - parenthetical=false/0 - navigation=77%/p1
- [88] "twenty- two." - 820ms base / 1093ms effective - dense - 2 content word(s) - 12 chars - quote=false/none - parenthetical=false/0 - navigation=77%/p1

Next chunks:
- [90] "was the Board's" - 440ms base / 587ms effective - normal - 1 content word(s) - 15 chars - quote=false/none - parenthetical=false/0 - navigation=79%/p1
- [91] "first act" - 600ms base / 800ms effective - dense - 2 content word(s) - 9 chars - quote=false/none - parenthetical=false/0 - navigation=80%/p1
- [92] "under its" - 600ms base / 800ms effective - dense - 2 content word(s) - 9 chars - quote=false/none - parenthetical=false/0 - navigation=80%/p1

## Session Summary

Event count: 62
Rewind count: 26
Pause count: 6
Speed change count: 0
Adaptation count: 16
Completed: false
Elapsed session ms: 319368
Estimated remaining chunks: 27
Average effective duration ms: 749
Last adaptation reason: rewinds
Last adaptation direction: slower

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

<!-- Source: defect_20260710_051112_de0edb.md.gz -->

# Semantic RSVP Defect Report

Report ID: defect_20260710_051112_de0edb
Created at: 2026-07-10T05:11:12.630601Z

## Classification

Category: proper_name_split
Severity: 2
Notes:
Bandar Abbas is one place

Preferred behavior:
Don't split proper names

## Reader State

Current index: 29
Sentence index: 1
Playback speed: 1.15x
Adaptation enabled: true

Current chunk:
Abbas.

## Timing Context

Base duration ms: 580
Effective duration ms: 504
Playback speed: 1.15x
Duration source: schedule
Current syntactic hint: normal
Current content word count: 1
Character length: 6
In quote: false
Quote boundary: none
In parenthetical: false
Parenthetical depth: 0
Navigation progress percent: 17
Navigation paragraph index: 0

Original sentence:
Iranian media later reported multiple explosions across southern Iran, including Bushehr, where one of the country's nuclear plants is located, along with Konarak, Choghadak and Bandar Abbas.

Previous chunks:
- [26] "along with Konarak," - 640ms base / 557ms effective - dense - 2 content word(s) - 19 chars - quote=false/none - parenthetical=false/0 - navigation=15%/p0
- [27] "Choghadak" - 440ms base / 383ms effective - normal - 1 content word(s) - 9 chars - quote=false/none - parenthetical=false/0 - navigation=16%/p0
- [28] "and Bandar" - 440ms base / 383ms effective - normal - 1 content word(s) - 10 chars - quote=false/none - parenthetical=false/0 - navigation=16%/p0

Next chunks:
- [30] "The Reuters" - 440ms base / 383ms effective - normal - 1 content word(s) - 11 chars - quote=false/none - parenthetical=false/0 - navigation=17%/p1
- [31] "Iran Briefing" - 660ms base / 574ms effective - dense - 2 content word(s) - 13 chars - quote=false/none - parenthetical=false/0 - navigation=18%/p1
- [32] "newsletter keeps" - 650ms base / 565ms effective - dense - 2 content word(s) - 16 chars - quote=false/none - parenthetical=false/0 - navigation=18%/p1

## Session Summary

Event count: 12
Rewind count: 4
Pause count: 1
Speed change count: 0
Adaptation count: 3
Completed: false
Elapsed session ms: 57987
Estimated remaining chunks: 142
Average effective duration ms: 501
Last adaptation reason: rewinds
Last adaptation direction: slower

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

<!-- Source: defect_20260710_051211_da374c.md.gz -->

# Semantic RSVP Defect Report

Report ID: defect_20260710_051211_da374c
Created at: 2026-07-10T05:12:11.344125Z

## Classification

Category: proper_name_split
Severity: 2
Notes:
Supreme Leader is one thing

Preferred behavior:
Don't split proper name

## Reader State

Current index: 50
Sentence index: 5
Playback speed: 1.15x
Adaptation enabled: true

Current chunk:
Leader Ayatollah

## Timing Context

Base duration ms: 710
Effective duration ms: 617
Playback speed: 1.15x
Duration source: schedule
Current syntactic hint: dense
Current content word count: 2
Character length: 16
In quote: false
Quote boundary: none
In parenthetical: false
Parenthetical depth: 0
Navigation progress percent: 27
Navigation paragraph index: 1

Original sentence:
The attacks came as Iran buried its slain Supreme Leader Ayatollah Ali Khamenei at a shrine in Mashhad, capping a week of funeral processions and rallies.

Previous chunks:
- [47] "came as Iran" - 600ms base / 522ms effective - dense - 2 content word(s) - 12 chars - quote=false/none - parenthetical=false/0 - navigation=26%/p1
- [48] "buried its" - 600ms base / 522ms effective - dense - 2 content word(s) - 10 chars - quote=false/none - parenthetical=false/0 - navigation=26%/p1
- [49] "slain Supreme" - 600ms base / 522ms effective - dense - 2 content word(s) - 13 chars - quote=false/none - parenthetical=false/0 - navigation=27%/p1

Next chunks:
- [51] "Ali Khamenei at" - 660ms base / 574ms effective - dense - 2 content word(s) - 15 chars - quote=false/none - parenthetical=false/0 - navigation=28%/p1
- [52] "a shrine in Mashhad," - 640ms base / 557ms effective - dense - 2 content word(s) - 20 chars - quote=false/none - parenthetical=false/0 - navigation=29%/p1
- [53] "capping a week" - 600ms base / 522ms effective - dense - 2 content word(s) - 14 chars - quote=false/none - parenthetical=false/0 - navigation=29%/p1

## Session Summary

Event count: 18
Rewind count: 5
Pause count: 2
Speed change count: 0
Adaptation count: 5
Completed: false
Elapsed session ms: 116714
Estimated remaining chunks: 121
Average effective duration ms: 501
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

<!-- Source: defect_20260710_051246_c4249b.md.gz -->

# Semantic RSVP Defect Report

Report ID: defect_20260710_051246_c4249b
Created at: 2026-07-10T05:12:46.825589Z

## Classification

Category: title_name_split
Severity: 2
Notes:
Ayatollah Ali Khamenei is one thing

Preferred behavior:
Don't split title and name

## Reader State

Current index: 51
Sentence index: 5
Playback speed: 1.15x
Adaptation enabled: true

Current chunk:
Ali Khamenei at

## Timing Context

Base duration ms: 660
Effective duration ms: 574
Playback speed: 1.15x
Duration source: schedule
Current syntactic hint: dense
Current content word count: 2
Character length: 15
In quote: false
Quote boundary: none
In parenthetical: false
Parenthetical depth: 0
Navigation progress percent: 28
Navigation paragraph index: 1

Original sentence:
The attacks came as Iran buried its slain Supreme Leader Ayatollah Ali Khamenei at a shrine in Mashhad, capping a week of funeral processions and rallies.

Previous chunks:
- [48] "buried its" - 600ms base / 522ms effective - dense - 2 content word(s) - 10 chars - quote=false/none - parenthetical=false/0 - navigation=26%/p1
- [49] "slain Supreme" - 600ms base / 522ms effective - dense - 2 content word(s) - 13 chars - quote=false/none - parenthetical=false/0 - navigation=27%/p1
- [50] "Leader Ayatollah" - 710ms base / 617ms effective - dense - 2 content word(s) - 16 chars - quote=false/none - parenthetical=false/0 - navigation=27%/p1

Next chunks:
- [52] "a shrine in Mashhad," - 640ms base / 557ms effective - dense - 2 content word(s) - 20 chars - quote=false/none - parenthetical=false/0 - navigation=29%/p1
- [53] "capping a week" - 600ms base / 522ms effective - dense - 2 content word(s) - 14 chars - quote=false/none - parenthetical=false/0 - navigation=29%/p1
- [54] "of funeral" - 440ms base / 383ms effective - normal - 1 content word(s) - 10 chars - quote=false/none - parenthetical=false/0 - navigation=30%/p1

## Session Summary

Event count: 20
Rewind count: 5
Pause count: 2
Speed change count: 0
Adaptation count: 5
Completed: false
Elapsed session ms: 152177
Estimated remaining chunks: 120
Average effective duration ms: 501
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

<!-- Source: defect_20260710_051414_c5a136.md.gz -->

# Semantic RSVP Defect Report

Report ID: defect_20260710_051414_c5a136
Created at: 2026-07-10T05:14:14.144542Z

## Classification

Category: proper_name_split
Severity: 2
Notes:
President Donald Trump is one thing

Preferred behavior:
Don't split title and first name from surname

## Reader State

Current index: 80
Sentence index: 7
Playback speed: 1.3x
Adaptation enabled: true

Current chunk:
Trump declaring the

## Timing Context

Base duration ms: 690
Effective duration ms: 531
Playback speed: 1.3x
Duration source: schedule
Current syntactic hint: dense
Current content word count: 2
Character length: 19
In quote: false
Quote boundary: none
In parenthetical: false
Parenthetical depth: 0
Navigation progress percent: 45
Navigation paragraph index: 1

Original sentence:
Attacks on Qatari and Saudi shipping vessels earlier this week upended the ceasefire, with U.S. President ​Donald Trump declaring the truce "over."

Previous chunks:
- [77] "upended the ceasefire," - 690ms base / 531ms effective - dense - 2 content word(s) - 22 chars - quote=false/none - parenthetical=false/0 - navigation=43%/p1
- [78] "with U.S." - 620ms base / 477ms effective - normal - 1 content word(s) - 9 chars - quote=false/none - parenthetical=false/0 - navigation=43%/p1
- [79] "President​ Donald" - 710ms base / 546ms effective - dense - 2 content word(s) - 17 chars - quote=false/none - parenthetical=false/0 - navigation=44%/p1

Next chunks:
- [81] "truce" - 400ms base / 308ms effective - normal - 1 content word(s) - 5 chars - quote=false/none - parenthetical=false/0 - navigation=45%/p1
- [82] ""over."" - 450ms base / 346ms effective - punctuation - 1 content word(s) - 7 chars - quote=true/both - parenthetical=false/0 - navigation=45%/p1
- [83] "Washington was" - 440ms base / 338ms effective - normal - 1 content word(s) - 14 chars - quote=false/none - parenthetical=false/0 - navigation=46%/p1

## Session Summary

Event count: 28
Rewind count: 7
Pause count: 3
Speed change count: 0
Adaptation count: 8
Completed: false
Elapsed session ms: 239509
Estimated remaining chunks: 91
Average effective duration ms: 443
Last adaptation reason: rewinds
Last adaptation direction: slower

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

<!-- Source: defect_20260710_051521_be5b13.md.gz -->

# Semantic RSVP Defect Report

Report ID: defect_20260710_051521_be5b13
Created at: 2026-07-10T05:15:21.264456Z

## Classification

Category: proper_name_split
Severity: 2
Notes:
The IRGN is one thing

Preferred behavior:
Don't split proper names

## Reader State

Current index: 117
Sentence index: 11
Playback speed: 1.3x
Adaptation enabled: true

Current chunk:
Guards Navy

## Timing Context

Base duration ms: 660
Effective duration ms: 508
Playback speed: 1.3x
Duration source: schedule
Current syntactic hint: dense
Current content word count: 2
Character length: 11
In quote: false
Quote boundary: none
In parenthetical: false
Parenthetical depth: 0
Navigation progress percent: 66
Navigation paragraph index: 1

Original sentence:
Iran's Revolutionary Guards Navy said the U.S. attacks and intervention in redirecting shipping through the Strait of Hormuz were disrupting the waterway's reopening.

Previous chunks:
- [114] ""We Will Kill" - 730ms base / 562ms effective - dense - 2 content word(s) - 13 chars - quote=true/open - parenthetical=false/0 - navigation=65%/p1
- [115] "Trump."" - 450ms base / 346ms effective - punctuation - 1 content word(s) - 7 chars - quote=true/close - parenthetical=false/0 - navigation=65%/p1
- [116] "Iran's Revolutionary" - 750ms base / 577ms effective - dense - 2 content word(s) - 20 chars - quote=false/none - parenthetical=false/0 - navigation=66%/p1

Next chunks:
- [118] "said the U.S." - 820ms base / 631ms effective - dense - 2 content word(s) - 13 chars - quote=false/none - parenthetical=false/0 - navigation=67%/p1
- [119] "attacks" - 400ms base / 308ms effective - normal - 1 content word(s) - 7 chars - quote=false/none - parenthetical=false/0 - navigation=67%/p1
- [120] "and intervention in redirecting" - 750ms base / 577ms effective - dense - 2 content word(s) - 31 chars - quote=false/none - parenthetical=false/0 - navigation=68%/p1

## Session Summary

Event count: 38
Rewind count: 11
Pause count: 4
Speed change count: 0
Adaptation count: 10
Completed: false
Elapsed session ms: 306636
Estimated remaining chunks: 54
Average effective duration ms: 443
Last adaptation reason: rewinds
Last adaptation direction: slower

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
