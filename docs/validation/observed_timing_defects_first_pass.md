# Observed Defects Review

## Summary

Top recurring issues:
1. Dense chunks are the clearest timing concern, especially when effective dwell drops into the roughly 450-575ms range at elevated playback speeds.
2. Several timing-labeled reports are actually display/layout problems, especially end-of-line hyphenation or wrapping that splits words and makes the chunk feel rushed.
3. A meaningful share of the file is still chunking/tokenization noise, including older reports without timing context, `a.m.` initialism splits, and modal/connector attachment issues such as `whether leaving would`.

Priority for next calibration:
- Separate pure timing reports from chunking and layout reports before changing duration formulas.
- Fix word wrapping/hyphenation artifacts before treating those reports as timing failures.
- After the display and tokenization noise is reduced, run a cleaner timing pass focused on dense chunks at default and elevated speeds.

Review note:
- Reports before the first timing context section do not include base/effective duration details, so they should not drive timing calibration directly.

---

<!-- Source: defect_20260709_211934_3649cf.md.gz -->

# Semantic RSVP Defect Report

Report ID: defect_20260709_211934_3649cf
Created at: 2026-07-09T21:19:34.498642Z

## Classification

Category: bad_chunk_split
Severity: 2
Notes:
asking belonged to the previous chunk and 'to' belongs with 'be'

Preferred behavior:
no splitting auxiliary verbs ('keep' stays with the gerund it describes). Never break up the infinitive like happened with 'to be'.

## Reader State

Current index: 10
Sentence index: 0
Playback speed: 0.85x
Adaptation enabled: true

Current chunk:
asking to

Current duration ms: 440
Current syntactic hint: normal
Current content word count: 1

Original sentence:
Attention is not a single switch that turns toward a page; it is a negotiated pattern between the reader, the sentence, and the surrounding interruptions that keep asking to be noticed.

Previous chunks:
- [7] the sentence,
- [8] and the surrounding
- [9] interruptions that keep

Next chunks:
- [11] be noticed.
- [12] When people
- [13] say they

## Session Summary

Event count: 12
Rewind count: 4
Pause count: 2
Speed change count: 0
Adaptation count: 3
Completed: false

## Client

User agent:
Mozilla/5.0 (Android 16; Mobile; rv:152.0) Gecko/152.0 Firefox/152.0

Viewport:
384x742

---

<!-- Source: defect_20260709_212241_a57a8b.md.gz -->

# Semantic RSVP Defect Report

Report ID: defect_20260709_212241_a57a8b
Created at: 2026-07-09T21:22:41.490187Z

## Classification

Category: bad_chunk_split
Severity: 2
Notes:
the grouping is unnatural to read because is serving the function of a context switch rather than grouping the two adjacent words

Preferred behavior:
Break before 'and' and keep the noun with its adjective if you can 'a quiet room'

## Reader State

Current index: 29
Sentence index: 2
Playback speed: 1x
Adaptation enabled: true

Current chunk:
room and nearly

Current duration ms: 540
Current syntactic hint: dense
Current content word count: 2

Original sentence:
This is why a paragraph can feel easy when read in a quiet room and nearly impossible on a train, even if the words have not changed.

Previous chunks:
- [26] easy when
- [27] read in
- [28] a quiet

Next chunks:
- [30] impossible on
- [31] a train,
- [32] even if

## Session Summary

Event count: 17
Rewind count: 5
Pause count: 3
Speed change count: 0
Adaptation count: 4
Completed: false

## Client

User agent:
Mozilla/5.0 (Android 16; Mobile; rv:152.0) Gecko/152.0 Firefox/152.0

Viewport:
384x742

---

<!-- Source: defect_20260709_212818_c59481.md.gz -->

# Semantic RSVP Defect Report

Report ID: defect_20260709_212818_c59481
Created at: 2026-07-09T21:28:18.671062Z

## Classification

Category: overlong_chunk
Severity: 2
Notes:
it felt like 'rebuilding' was tagged so as not to end on 'of', but 'the cost of' is a perfectly acceptable chunk and rebuilding requires its object for context

Preferred behavior:
Allow ending a chunk with of if it constitutes a legible phrase, and keep verbs with their immediate direct object if present to maintain the action they describe in one unit

## Reader State

Current index: 17
Sentence index: 1
Playback speed: 0.75x
Adaptation enabled: true

Current chunk:
the cost of rebuilding

Current duration ms: 580
Current syntactic hint: dense
Current content word count: 2

Original sentence:
When people say they lost focus, they often mean that the cost of rebuilding context became greater than the reward promised by the next clause.

Previous chunks:
- [14] lost focus,
- [15] they often
- [16] mean that

Next chunks:
- [18] context became
- [19] greater than the
- [20] reward promised by

## Session Summary

Event count: 52
Rewind count: 23
Pause count: 4
Speed change count: 0
Adaptation count: 6
Completed: false

## Client

User agent:
Mozilla/5.0 (Android 16; Mobile; rv:152.0) Gecko/152.0 Firefox/152.0

Viewport:
384x678

---

<!-- Source: defect_20260709_213337_e4941c.md.gz -->

# Semantic RSVP Defect Report

Report ID: defect_20260709_213337_e4941c
Created at: 2026-07-09T21:33:37.361473Z

## Classification

Category: punctuation_rhythm_issue
Severity: 2
Notes:
This is a clear conceptual stop. It shouldn't contain the tail of the previous concept, and reading tool is obviously a compound noun that shouldn't be split

Preferred behavior:
reading tool shouldn't be separated because those two words together represent one thing. Maybe, immediate adj-noun pairs should be preserved where constraints allow. And words like Therefore should obviously be at the start of their chunk unless preceded by a connector like 'and therefore' which would make them a good chunk on their own.

## Reader State

Current index: 43
Sentence index: 4
Playback speed: 0.75x
Adaptation enabled: true

Current chunk:
tool therefore has

Current duration ms: 540
Current syntactic hint: dense
Current content word count: 2

Original sentence:
A reading tool therefore has to respect two different forms of effort.

Previous chunks:
- [40] relationships to become
- [41] visible.
- [42] A reading

Next chunks:
- [44] to respect
- [45] two different
- [46] forms of effort.

## Session Summary

Event count: 67
Rewind count: 29
Pause count: 6
Speed change count: 0
Adaptation count: 10
Completed: false

## Client

User agent:
Mozilla/5.0 (Android 16; Mobile; rv:152.0) Gecko/152.0 Firefox/152.0

Viewport:
384x678

---

<!-- Source: defect_20260709_213829_c45241.md.gz -->

# Semantic RSVP Defect Report

Report ID: defect_20260709_213829_c45241
Created at: 2026-07-09T21:38:29.585349Z

## Classification

Category: overlong_chunk
Severity: 2
Notes:
Relationships is a heavy concept and feels like it's pushing out the rest

Preferred behavior:
Split long (4+ syllables) concepts from any trailing infinitives

## Reader State

Current index: 40
Sentence index: 3
Playback speed: 0.75x
Adaptation enabled: true

Current chunk:
relationships to become

Current duration ms: 580
Current syntactic hint: dense
Current content word count: 2

Original sentence:
The material does not simply enter the mind; it must be held long enough for relationships to become visible.

Previous chunks:
- [37] mind;
- [38] it must be held
- [39] long enough for

Next chunks:
- [41] visible.
- [42] A reading
- [43] tool therefore has

## Session Summary

Event count: 81
Rewind count: 38
Pause count: 8
Speed change count: 0
Adaptation count: 10
Completed: false

## Client

User agent:
Mozilla/5.0 (Android 16; Mobile; rv:152.0) Gecko/152.0 Firefox/152.0

Viewport:
384x678

---

<!-- Source: defect_20260709_214327_04e70f.md.gz -->

# Semantic RSVP Defect Report

Report ID: defect_20260709_214327_04e70f
Created at: 2026-07-09T21:43:27.360705Z

## Classification

Category: bad_chunk_split
Severity: 2
Notes:
sentence belonged with previous chunk, and is revising needed to be chunked with a claim

Preferred behavior:
Don't separate qualifier adj from their nouns (which x, this x, that x, any x, no x, etc...). And again, verbs followed by a single direct object ought to be chunked together.

## Reader State

Current index: 67
Sentence index: 6
Playback speed: 0.75x
Adaptation enabled: true

Current chunk:
sentence is revising

Current duration ms: 580
Current syntactic hint: dense
Current content word count: 2

Original sentence:
The second is conceptual effort: deciding which words carry the argument, which phrases merely connect ideas, and which sentence is revising a claim rather than adding a new one.

Previous chunks:
- [64] merely connect
- [65] ideas,
- [66] and which

Next chunks:
- [68] a claim
- [69] rather than
- [70] adding a new

## Session Summary

Event count: 105
Rewind count: 50
Pause count: 11
Speed change count: 0
Adaptation count: 14
Completed: false

## Client

User agent:
Mozilla/5.0 (Android 16; Mobile; rv:152.0) Gecko/152.0 Firefox/152.0

Viewport:
384x742

---

<!-- Source: defect_20260709_214736_f60b41.md.gz -->

# Semantic RSVP Defect Report

Report ID: defect_20260709_214736_f60b41
Created at: 2026-07-09T21:47:36.086807Z

## Classification

Category: bad_chunk_split
Severity: 2
Notes:
this noun wasn't just split from its article and adjective, but divorced from any context as a result.

Preferred behavior:
in the case of verb-article-adj-d.obj we want to chunk them all together only if they fit constraints, otherwise we want to chunk verb-article followed by adj-d.obj

## Reader State

Current index: 71
Sentence index: 6
Playback speed: 0.75x
Adaptation enabled: true

Current chunk:
one.

Current duration ms: 580
Current syntactic hint: normal
Current content word count: 1

Original sentence:
The second is conceptual effort: deciding which words carry the argument, which phrases merely connect ideas, and which sentence is revising a claim rather than adding a new one.

Previous chunks:
- [68] a claim
- [69] rather than
- [70] adding a new

Next chunks:
- [72] Reducing mechanical
- [73] effort is useful,
- [74] but it does not

## Session Summary

Event count: 119
Rewind count: 57
Pause count: 13
Speed change count: 0
Adaptation count: 14
Completed: false

## Client

User agent:
Mozilla/5.0 (Android 16; Mobile; rv:152.0) Gecko/152.0 Firefox/152.0

Viewport:
384x742

---

<!-- Source: defect_20260709_214744_755ab5.md.gz -->

# Semantic RSVP Defect Report

Report ID: defect_20260709_214744_755ab5
Created at: 2026-07-09T21:47:44.241141Z

## Classification

Category: bad_chunk_split
Severity: 2
Notes:
this noun wasn't just split from its article and adjective, but divorced from any context as a result.

Preferred behavior:
in the case of verb-article-adj-d.obj we want to chunk them all together only if they fit constraints, otherwise we want to chunk verb-article followed by adj-d.obj

## Reader State

Current index: 71
Sentence index: 6
Playback speed: 0.75x
Adaptation enabled: true

Current chunk:
one.

Current duration ms: 580
Current syntactic hint: normal
Current content word count: 1

Original sentence:
The second is conceptual effort: deciding which words carry the argument, which phrases merely connect ideas, and which sentence is revising a claim rather than adding a new one.

Previous chunks:
- [68] a claim
- [69] rather than
- [70] adding a new

Next chunks:
- [72] Reducing mechanical
- [73] effort is useful,
- [74] but it does not

## Session Summary

Event count: 120
Rewind count: 57
Pause count: 13
Speed change count: 0
Adaptation count: 14
Completed: false

## Client

User agent:
Mozilla/5.0 (Android 16; Mobile; rv:152.0) Gecko/152.0 Firefox/152.0

Viewport:
384x678

---

<!-- Source: defect_20260709_215101_0c924d.md.gz -->

# Semantic RSVP Defect Report

Report ID: defect_20260709_215101_0c924d
Created at: 2026-07-09T21:51:01.348763Z

## Classification

Category: orphan_function_word
Severity: 2
Notes:
Separating the quotes from the adjacent word they enclose isn't right

Preferred behavior:
When " introduced around a phrase keep start quotes chunked with next token and end quotes chunked with end token

## Reader State

Current index: 99
Sentence index: 11
Playback speed: 0.75x
Adaptation enabled: true

Current chunk:
such as "

Current duration ms: 440
Current syntactic hint: normal
Current content word count: 1

Original sentence:
A phrase such as "not because the evidence is weak, but because the explanation is incomplete" asks the reader to hold a contrast in working memory.

Previous chunks:
- [96] while several
- [97] qualifications pass by.
- [98] A phrase

Next chunks:
- [100] not because the
- [101] evidence is weak,
- [102] but because the explanation

## Session Summary

Event count: 152
Rewind count: 76
Pause count: 17
Speed change count: 0
Adaptation count: 18
Completed: false

## Client

User agent:
Mozilla/5.0 (Android 16; Mobile; rv:152.0) Gecko/152.0 Firefox/152.0

Viewport:
384x678

---

<!-- Source: defect_20260709_215700_a81bf2.md.gz -->

# Semantic RSVP Defect Report

Report ID: defect_20260709_215700_a81bf2
Created at: 2026-07-09T21:57:00.631224Z

## Classification

Category: bad_chunk_split
Severity: 2
Notes:
'or', 'simply different' and 'from what was written' feels like a more natural split

Preferred behavior:
Or can be chunked alone if it's costing us a more meaningful chunk ahead. It also makes a natural wait point. Simply different are a single chunk naturally, qualifier-adj pair. Despite the length, 'from what was written' represents an single concept in this case and the mostly monosyllabic phrase feels more natural chunked togethet.

## Reader State

Current index: 117
Sentence index: 12
Playback speed: 0.75x
Adaptation enabled: true

Current chunk:
different from what

Current duration ms: 580
Current syntactic hint: dense
Current content word count: 2

Original sentence:
If a display rushes through the first half and overemphasizes the second, the argument may feel stronger, weaker, or simply different from what was written.

Previous chunks:
- [114] stronger,
- [115] weaker,
- [116] or simply

Next chunks:
- [118] was written.

## Session Summary

Event count: 161
Rewind count: 79
Pause count: 17
Speed change count: 0
Adaptation count: 20
Completed: true

## Client

User agent:
Mozilla/5.0 (Android 16; Mobile; rv:152.0) Gecko/152.0 Firefox/152.0

Viewport:
384x678

---

<!-- Source: defect_20260709_215934_e25a27.md.gz -->

# Semantic RSVP Defect Report

Report ID: defect_20260709_215934_e25a27
Created at: 2026-07-09T21:59:34.608992Z

## Classification

Category: orphan_function_word
Severity: 2
Notes:
It's easy to lose context when presented with a noun and a full stop

Preferred behavior:
Keep objects with their prepositions at the price of separating that chunk from the preceding verb if you must

## Reader State

Current index: 12
Sentence index: 0
Playback speed: 0.85x
Adaptation enabled: true

Current chunk:
units,

Current duration ms: 400
Current syntactic hint: normal
Current content word count: 1

Original sentence:
A small scheduling service can look simple from the outside because each request appears to follow the same path: accept input, normalize it, divide it into units, compute durations, and return a response.

Previous chunks:
- [9] accept input,
- [10] normalize it,
- [11] divide it into

Next chunks:
- [13] compute durations,
- [14] and return a response.
- [15] The difficulty is

## Session Summary

Event count: 12
Rewind count: 5
Pause count: 1
Speed change count: 0
Adaptation count: 3
Completed: false

## Client

User agent:
Mozilla/5.0 (Android 16; Mobile; rv:152.0) Gecko/152.0 Firefox/152.0

Viewport:
384x742

---

<!-- Source: defect_20260709_220422_f2a366.md.gz -->

# Semantic RSVP Defect Report

Report ID: defect_20260709_220422_f2a366
Created at: 2026-07-09T22:04:22.244456Z

## Classification

Category: bad_chunk_split
Severity: 2
Notes:
'too much' is a single functional unit

Preferred behavior:
Don't split quantifier and qualifier pairs like too much/few/many/little. Generally speaking unless 'too' is followed by a wait it belongs with the next token's chunk, it's also perfectly fine to start a chunk with 'too' despite it qualifying a direct obj following a verb because it's going to be too long to chunk with the verb.

## Reader State

Current index: 24
Sentence index: 2
Playback speed: 0.85x
Adaptation enabled: true

Current chunk:
much punctuation,

Current duration ms: 540
Current syntactic hint: dense
Current content word count: 2

Original sentence:
If normalization removes too much punctuation, the segmenter may not know where the writer changed direction.

Previous chunks:
- [21] depends on.
- [22] If normalization
- [23] removes too

Next chunks:
- [25] the segmenter
- [26] may not
- [27] know where the

## Session Summary

Event count: 21
Rewind count: 8
Pause count: 2
Speed change count: 0
Adaptation count: 5
Completed: false

## Client

User agent:
Mozilla/5.0 (Android 16; Mobile; rv:152.0) Gecko/152.0 Firefox/152.0

Viewport:
384x678

---

<!-- Source: defect_20260709_220636_d3a643.md.gz -->

# Semantic RSVP Defect Report

Report ID: defect_20260709_220636_d3a643
Created at: 2026-07-09T22:06:36.406961Z

## Classification

Category: underdense_chunk
Severity: 2
Notes:
This feels too short, may not what, who may not. 

Preferred behavior:
May not can be ap- or prepended to the shorter between the preceding or trailing chunk

## Reader State

Current index: 26
Sentence index: 2
Playback speed: 0.75x
Adaptation enabled: true

Current chunk:
may not

Current duration ms: 500
Current syntactic hint: dense
Current content word count: 2

Original sentence:
If normalization removes too much punctuation, the segmenter may not know where the writer changed direction.

Previous chunks:
- [23] removes too
- [24] much punctuation,
- [25] the segmenter

Next chunks:
- [27] know where the
- [28] writer changed
- [29] direction.

## Session Summary

Event count: 33
Rewind count: 16
Pause count: 3
Speed change count: 0
Adaptation count: 6
Completed: false

## Client

User agent:
Mozilla/5.0 (Android 16; Mobile; rv:152.0) Gecko/152.0 Firefox/152.0

Viewport:
384x678

---

<!-- Source: defect_20260709_220904_fbfd16.md.gz -->

# Semantic RSVP Defect Report

Report ID: defect_20260709_220904_fbfd16
Created at: 2026-07-09T22:09:04.623725Z

## Classification

Category: comprehension_drop
Severity: 3
Notes:
We don't split not from the verb it's negating like that in natural speech. 

Preferred behavior:
not should be chunked with the verb it's negating.

## Reader State

Current index: 77
Sentence index: 10
Playback speed: 1x
Adaptation enabled: true

Current chunk:
not begin with

Current duration ms: 540
Current syntactic hint: dense
Current content word count: 2

Original sentence:
This is why validation should not begin with a large automated benchmark.

Previous chunks:
- [74] the text.
- [75] This is why
- [76] validation should

Next chunks:
- [78] a large
- [79] automated benchmark.
- [80] The system is still

## Session Summary

Event count: 44
Rewind count: 18
Pause count: 5
Speed change count: 0
Adaptation count: 10
Completed: false

## Client

User agent:
Mozilla/5.0 (Android 16; Mobile; rv:152.0) Gecko/152.0 Firefox/152.0

Viewport:
384x678

---

<!-- Source: defect_20260709_221244_c00d94.md.gz -->

# Semantic RSVP Defect Report

Report ID: defect_20260709_221244_c00d94
Created at: 2026-07-09T22:12:44.647651Z

## Classification

Category: comprehension_drop
Severity: 2
Notes:
Still describes young, 'the system is' is just fine without still.

Preferred behavior:
The verb to be can end chunks when not followed by a gerund. Preserve qualifier-adjective pairs chunked together if they are two adjacent words.

## Reader State

Current index: 81
Sentence index: 11
Playback speed: 0.75x
Adaptation enabled: true

Current chunk:
young,

Current duration ms: 400
Current syntactic hint: normal
Current content word count: 1

Original sentence:
The system is still young, and the failures are likely to be qualitative: a chunk that begins with "however," a pause after a phrase that should flow, or a dense definition that disappears too quickly.

Previous chunks:
- [78] a large
- [79] automated benchmark.
- [80] The system is still

Next chunks:
- [82] and the failures
- [83] are likely to
- [84] be qualitative:

## Session Summary

Event count: 62
Rewind count: 27
Pause count: 7
Speed change count: 0
Adaptation count: 12
Completed: false

## Client

User agent:
Mozilla/5.0 (Android 16; Mobile; rv:152.0) Gecko/152.0 Firefox/152.0

Viewport:
384x678

---

<!-- Source: defect_20260709_221825_7aab44.md.gz -->

# Semantic RSVP Defect Report

Report ID: defect_20260709_221825_7aab44
Created at: 2026-07-09T22:18:25.516914Z

## Classification

Category: underdense_chunk
Severity: 2
Notes:
Or can stand alone here. More important to keep a dense definition chunked

Preferred behavior:
Unironically, this chunk was underdense because dense wasn't chunked with what it was describing as such. Try to chunk 'article-adj-noun' units as a whole within constraints. Clear connecting operators like a capitalized 'or', 'therefore', 'and', 'also', 'except' are the perfect less dense chunks meant for cognition to catch up. Fhey can be chunked along and weighted for a higher wait.

## Reader State

Current index: 91
Sentence index: 11
Playback speed: 0.75x
Adaptation enabled: true

Current chunk:
or a dense

Current duration ms: 440
Current syntactic hint: normal
Current content word count: 1

Original sentence:
The system is still young, and the failures are likely to be qualitative: a chunk that begins with "however," a pause after a phrase that should flow, or a dense definition that disappears too quickly.

Previous chunks:
- [88] after a phrase
- [89] that should
- [90] flow,

Next chunks:
- [92] definition that disappears
- [93] too quickly.
- [94] A repeatable

## Session Summary

Event count: 120
Rewind count: 55
Pause count: 9
Speed change count: 0
Adaptation count: 16
Completed: true

## Client

User agent:
Mozilla/5.0 (Android 16; Mobile; rv:152.0) Gecko/152.0 Firefox/152.0

Viewport:
384x678

---

<!-- Source: defect_20260709_224331_0316ff.md.gz -->

# Semantic RSVP Defect Report

Report ID: defect_20260709_224331_0316ff
Created at: 2026-07-09T22:43:31.742671Z

## Classification

Category: rushed_dense_chunk
Severity: 2
Notes:
Too fast to take in

Preferred behavior:
Add time to hyphenated words due to EoL

## Reader State

Current index: 46
Sentence index: 5
Playback speed: 1.15x
Adaptation enabled: true

Current chunk:
The first is mechanical

## Timing Context

Base duration ms: 580
Effective duration ms: 504
Playback speed: 1.15x
Duration source: schedule
Current syntactic hint: dense
Current content word count: 2
Character length: 23

Original sentence:
The first is mechanical effort: moving the eyes, finding the next line, and correcting small jumps when the page shifts or the body moves.

Previous chunks:
- [43] "therefore has to respect" - 480ms base / 417ms effective - normal - 1 content word(s) - 24 chars
- [44] "two different" - 540ms base / 470ms effective - dense - 2 content word(s) - 13 chars
- [45] "forms of effort." - 720ms base / 626ms effective - dense - 2 content word(s) - 16 chars

Next chunks:
- [47] "effort:" - 400ms base / 348ms effective - normal - 1 content word(s) - 7 chars
- [48] "moving the eyes," - 540ms base / 470ms effective - dense - 2 content word(s) - 16 chars
- [49] "finding the next" - 540ms base / 470ms effective - dense - 2 content word(s) - 16 chars

## Session Summary

Event count: 14
Rewind count: 6
Pause count: 1
Speed change count: 0
Adaptation count: 5
Completed: false
Elapsed session ms: 141654
Estimated remaining chunks: 67
Average effective duration ms: 439
Last adaptation reason: rewinds
Last adaptation direction: slower

## Client

User agent:
Mozilla/5.0 (Android 16; Mobile; rv:152.0) Gecko/152.0 Firefox/152.0

Viewport:
384x742

---

<!-- Source: defect_20260709_224443_1128af.md.gz -->

# Semantic RSVP Defect Report

Report ID: defect_20260709_224443_1128af
Created at: 2026-07-09T22:44:43.759614Z

## Classification

Category: rushed_dense_chunk
Severity: 2
Notes:
Too rushed

Preferred behavior:
Again, an EoL hyphenation requires more time to process in dense chunks

## Reader State

Current index: 57
Sentence index: 6
Playback speed: 1x
Adaptation enabled: true

Current chunk:
The second is conceptual

## Timing Context

Base duration ms: 580
Effective duration ms: 580
Playback speed: 1x
Duration source: schedule
Current syntactic hint: dense
Current content word count: 2
Character length: 24

Original sentence:
The second is conceptual effort: deciding which words carry the argument, which phrases merely connect ideas, and which sentence is revising a claim rather than adding a new one.

Previous chunks:
- [54] "shifts" - 400ms base / 400ms effective - normal - 1 content word(s) - 6 chars
- [55] "or the body" - 440ms base / 440ms effective - normal - 1 content word(s) - 11 chars
- [56] "moves." - 580ms base / 580ms effective - normal - 1 content word(s) - 6 chars

Next chunks:
- [58] "effort:" - 400ms base / 400ms effective - normal - 1 content word(s) - 7 chars
- [59] "deciding which" - 540ms base / 540ms effective - dense - 2 content word(s) - 14 chars
- [60] "words carry the" - 540ms base / 540ms effective - dense - 2 content word(s) - 15 chars

## Session Summary

Event count: 25
Rewind count: 11
Pause count: 2
Speed change count: 0
Adaptation count: 8
Completed: false
Elapsed session ms: 213657
Estimated remaining chunks: 56
Average effective duration ms: 504
Last adaptation reason: rewinds
Last adaptation direction: slower

## Client

User agent:
Mozilla/5.0 (Android 16; Mobile; rv:152.0) Gecko/152.0 Firefox/152.0

Viewport:
384x742

---

<!-- Source: defect_20260709_224646_257e2b.md.gz -->

# Semantic RSVP Defect Report

Report ID: defect_20260709_224646_257e2b
Created at: 2026-07-09T22:46:46.917047Z

## Classification

Category: rushed_dense_chunk
Severity: 2
Notes:
Too rushed

Preferred behavior:
3rd EoL hyphenation in a dense chunk, same jarring effect. The added step of reconstructing the hyphenated word may indicate it would be best to fit it to the width on its own line in order to avoid EoL hyphenation

## Reader State

Current index: 66
Sentence index: 6
Playback speed: 1.15x
Adaptation enabled: true

Current chunk:
sentence is revising

## Timing Context

Base duration ms: 580
Effective duration ms: 504
Playback speed: 1.15x
Duration source: schedule
Current syntactic hint: dense
Current content word count: 2
Character length: 20

Original sentence:
The second is conceptual effort: deciding which words carry the argument, which phrases merely connect ideas, and which sentence is revising a claim rather than adding a new one.

Previous chunks:
- [63] "merely connect" - 540ms base / 470ms effective - dense - 2 content word(s) - 14 chars
- [64] "ideas," - 400ms base / 348ms effective - normal - 1 content word(s) - 6 chars
- [65] "and which" - 440ms base / 383ms effective - normal - 1 content word(s) - 9 chars

Next chunks:
- [67] "a claim rather" - 440ms base / 383ms effective - normal - 1 content word(s) - 14 chars
- [68] "than adding a new" - 540ms base / 470ms effective - dense - 2 content word(s) - 17 chars
- [69] "one." - 580ms base / 504ms effective - normal - 1 content word(s) - 4 chars

## Session Summary

Event count: 31
Rewind count: 12
Pause count: 3
Speed change count: 0
Adaptation count: 9
Completed: false
Elapsed session ms: 336803
Estimated remaining chunks: 47
Average effective duration ms: 439
Last adaptation reason: smooth_run
Last adaptation direction: faster

## Client

User agent:
Mozilla/5.0 (Android 16; Mobile; rv:152.0) Gecko/152.0 Firefox/152.0

Viewport:
384x742

---

<!-- Source: defect_20260709_224819_57c7f8.md.gz -->

# Semantic RSVP Defect Report

Report ID: defect_20260709_224819_57c7f8
Created at: 2026-07-09T22:48:19.618581Z

## Classification

Category: rushed_dense_chunk
Severity: 2
Notes:
Too ruahed

Preferred behavior:
Again the cognitive burden of reconstructong EoL hypenation makes the dense chunk feel rushed.

## Reader State

Current index: 98
Sentence index: 11
Playback speed: 0.75x
Adaptation enabled: true

Current chunk:
but because the explanation

## Timing Context

Base duration ms: 580
Effective duration ms: 773
Playback speed: 0.75x
Duration source: schedule
Current syntactic hint: dense
Current content word count: 2
Character length: 27

Original sentence:
A phrase such as "not because the evidence is weak, but because the explanation is incomplete" asks the reader to hold a contrast in working memory.

Previous chunks:
- [95] "as" - 300ms base / 400ms effective - light - 0 content word(s) - 2 chars
- [96] ""not because the evidence" - 580ms base / 773ms effective - dense - 2 content word(s) - 25 chars
- [97] "is weak," - 400ms base / 533ms effective - normal - 1 content word(s) - 8 chars

Next chunks:
- [99] "is incomplete"" - 440ms base / 587ms effective - normal - 1 content word(s) - 14 chars
- [100] "asks the reader" - 540ms base / 720ms effective - dense - 2 content word(s) - 15 chars
- [101] "to hold a contrast" - 540ms base / 720ms effective - dense - 2 content word(s) - 18 chars

## Session Summary

Event count: 56
Rewind count: 25
Pause count: 5
Speed change count: 0
Adaptation count: 16
Completed: false
Elapsed session ms: 429526
Estimated remaining chunks: 15
Average effective duration ms: 672
Last adaptation reason: rewinds
Last adaptation direction: slower

## Client

User agent:
Mozilla/5.0 (Android 16; Mobile; rv:152.0) Gecko/152.0 Firefox/152.0

Viewport:
384x678

---

<!-- Source: defect_20260709_225107_f0347a.md.gz -->

# Semantic RSVP Defect Report

Report ID: defect_20260709_225107_f0347a
Created at: 2026-07-09T22:51:07.913906Z

## Classification

Category: overpaused_light_chunk
Severity: 2
Notes:
Felt unnaturally long

Preferred behavior:
We need to treat short single word stops as lighter waits.

## Reader State

Current index: 11
Sentence index: 0
Playback speed: 1.3x
Adaptation enabled: true

Current chunk:
units,

## Timing Context

Base duration ms: 400
Effective duration ms: 308
Playback speed: 1.3x
Duration source: schedule
Current syntactic hint: normal
Current content word count: 1
Character length: 6

Original sentence:
A small scheduling service can look simple from the outside because each request appears to follow the same path: accept input, normalize it, divide it into units, compute durations, and return a response.

Previous chunks:
- [8] "accept input," - 540ms base / 415ms effective - dense - 2 content word(s) - 13 chars
- [9] "normalize it," - 440ms base / 338ms effective - normal - 1 content word(s) - 13 chars
- [10] "divide it into" - 540ms base / 415ms effective - dense - 2 content word(s) - 14 chars

Next chunks:
- [12] "compute durations," - 540ms base / 415ms effective - dense - 2 content word(s) - 18 chars
- [13] "and return a response." - 760ms base / 585ms effective - dense - 2 content word(s) - 22 chars
- [14] "The difficulty is" - 440ms base / 338ms effective - normal - 1 content word(s) - 17 chars

## Session Summary

Event count: 12
Rewind count: 2
Pause count: 2
Speed change count: 0
Adaptation count: 4
Completed: false
Elapsed session ms: 140437
Estimated remaining chunks: 95
Average effective duration ms: 389
Last adaptation reason: rewinds
Last adaptation direction: slower

## Client

User agent:
Mozilla/5.0 (Android 16; Mobile; rv:152.0) Gecko/152.0 Firefox/152.0

Viewport:
384x678

---

<!-- Source: defect_20260709_225320_911cba.md.gz -->

# Semantic RSVP Defect Report

Report ID: defect_20260709_225320_911cba
Created at: 2026-07-09T22:53:20.228335Z

## Classification

Category: rushed_dense_chunk
Severity: 2
Notes:
Too fast to take in

Preferred behavior:
In this case I think 'that actually' should have been split off to its own chunk.

## Reader State

Current index: 105
Sentence index: 13
Playback speed: 1.3x
Adaptation enabled: true

Current chunk:
the rules that actually

## Timing Context

Base duration ms: 580
Effective duration ms: 446
Playback speed: 1.3x
Duration source: schedule
Current syntactic hint: dense
Current content word count: 2
Character length: 23

Original sentence:
Later, when the defect patterns become stable, tests can protect the rules that actually improved reading.

Previous chunks:
- [102] "patterns become" - 540ms base / 415ms effective - dense - 2 content word(s) - 15 chars
- [103] "stable," - 400ms base / 308ms effective - normal - 1 content word(s) - 7 chars
- [104] "tests can protect" - 540ms base / 415ms effective - dense - 2 content word(s) - 17 chars

Next chunks:
- [106] "improved reading." - 720ms base / 554ms effective - dense - 2 content word(s) - 17 chars

## Session Summary

Event count: 33
Rewind count: 8
Pause count: 3
Speed change count: 0
Adaptation count: 10
Completed: true
Elapsed session ms: 272742
Estimated remaining chunks: 1
Average effective duration ms: 389
Last adaptation reason: rewinds
Last adaptation direction: slower

## Client

User agent:
Mozilla/5.0 (Android 16; Mobile; rv:152.0) Gecko/152.0 Firefox/152.0

Viewport:
384x742

---

<!-- Source: defect_20260709_225330_4192f7.md.gz -->

# Semantic RSVP Defect Report

Report ID: defect_20260709_225330_4192f7
Created at: 2026-07-09T22:53:30.346021Z

## Classification

Category: rushed_dense_chunk
Severity: 2
Notes:
Too fast to take in

Preferred behavior:
In this case I think 'that actually' should have been split off to its own chunk.

## Reader State

Current index: 105
Sentence index: 13
Playback speed: 1.3x
Adaptation enabled: true

Current chunk:
the rules that actually

## Timing Context

Base duration ms: 580
Effective duration ms: 446
Playback speed: 1.3x
Duration source: schedule
Current syntactic hint: dense
Current content word count: 2
Character length: 23

Original sentence:
Later, when the defect patterns become stable, tests can protect the rules that actually improved reading.

Previous chunks:
- [102] "patterns become" - 540ms base / 415ms effective - dense - 2 content word(s) - 15 chars
- [103] "stable," - 400ms base / 308ms effective - normal - 1 content word(s) - 7 chars
- [104] "tests can protect" - 540ms base / 415ms effective - dense - 2 content word(s) - 17 chars

Next chunks:
- [106] "improved reading." - 720ms base / 554ms effective - dense - 2 content word(s) - 17 chars

## Session Summary

Event count: 34
Rewind count: 8
Pause count: 3
Speed change count: 0
Adaptation count: 10
Completed: true
Elapsed session ms: 282873
Estimated remaining chunks: 1
Average effective duration ms: 389
Last adaptation reason: rewinds
Last adaptation direction: slower

## Client

User agent:
Mozilla/5.0 (Android 16; Mobile; rv:152.0) Gecko/152.0 Firefox/152.0

Viewport:
384x678

---

<!-- Source: defect_20260709_225517_4d25d6.md.gz -->

# Semantic RSVP Defect Report

Report ID: defect_20260709_225517_4d25d6
Created at: 2026-07-09T22:55:17.496598Z

## Classification

Category: rushed_dense_chunk
Severity: 2
Notes:
Too rushed

Preferred behavior:
Unfortunately long word, we should display it on its own line and fit to width to avoid hyphenation

## Reader State

Current index: 64
Sentence index: 10
Playback speed: 1.5x
Adaptation enabled: true

Current chunk:
the name of seriousness.

## Timing Context

Base duration ms: 760
Effective duration ms: 507
Playback speed: 1.5x
Duration source: schedule
Current syntactic hint: dense
Current content word count: 2
Character length: 24

Original sentence:
The point is not to slow everything down in the name of seriousness.

Previous chunks:
- [61] "The point" - 440ms base / 293ms effective - normal - 1 content word(s) - 9 chars
- [62] "is not to slow" - 440ms base / 293ms effective - normal - 1 content word(s) - 14 chars
- [63] "everything down in" - 540ms base / 360ms effective - dense - 2 content word(s) - 18 chars

Next chunks:
- [65] "The better" - 440ms base / 293ms effective - normal - 1 content word(s) - 10 chars
- [66] "argument is" - 440ms base / 293ms effective - normal - 1 content word(s) - 11 chars
- [67] "that speed should" - 440ms base / 293ms effective - normal - 1 content word(s) - 17 chars

## Session Summary

Event count: 7
Rewind count: 1
Pause count: 1
Speed change count: 0
Adaptation count: 3
Completed: false
Elapsed session ms: 92781
Estimated remaining chunks: 42
Average effective duration ms: 349
Last adaptation reason: smooth_run
Last adaptation direction: faster

## Client

User agent:
Mozilla/5.0 (Android 16; Mobile; rv:152.0) Gecko/152.0 Firefox/152.0

Viewport:
384x678

---

<!-- Source: defect_20260709_225911_15814d.md.gz -->

# Semantic RSVP Defect Report

Report ID: defect_20260709_225911_15814d
Created at: 2026-07-09T22:59:11.005815Z

## Classification

Category: rushed_dense_chunk
Severity: 3
Notes:
Too fast

Preferred behavior:
EoL hyphenation broke up a short word into a semantic nightmare by splitting it into a prefix and a fossil word.

## Reader State

Current index: 22
Sentence index: 2
Playback speed: 1x
Adaptation enabled: true

Current chunk:
change should reduce

## Timing Context

Base duration ms: 580
Effective duration ms: 580
Playback speed: 1x
Duration source: schedule
Current syntactic hint: dense
Current content word count: 2
Character length: 20

Original sentence:
Supporters said the change should reduce congestion without removing permanent parking, while opponents warned that enforcement would be inconsistent unless the city assigns staff to monitor the zones.

Previous chunks:
- [19] "during the morning" - 540ms base / 540ms effective - dense - 2 content word(s) - 18 chars
- [20] "rush." - 580ms base / 580ms effective - normal - 1 content word(s) - 5 chars
- [21] "Supporters said the" - 580ms base / 580ms effective - dense - 2 content word(s) - 19 chars

Next chunks:
- [23] "congestion without" - 540ms base / 540ms effective - dense - 2 content word(s) - 18 chars
- [24] "removing permanent" - 540ms base / 540ms effective - dense - 2 content word(s) - 18 chars
- [25] "parking," - 400ms base / 400ms effective - normal - 1 content word(s) - 8 chars

## Session Summary

Event count: 7
Rewind count: 2
Pause count: 1
Speed change count: 1
Adaptation count: 1
Completed: false
Elapsed session ms: 104989
Estimated remaining chunks: 87
Average effective duration ms: 529
Last adaptation reason: rewinds
Last adaptation direction: slower

## Client

User agent:
Mozilla/5.0 (Android 16; Mobile; rv:152.0) Gecko/152.0 Firefox/152.0

Viewport:
384x678

---

<!-- Source: defect_20260709_230028_5760de.md.gz -->

# Semantic RSVP Defect Report

Report ID: defect_20260709_230028_5760de
Created at: 2026-07-09T23:00:28.685540Z

## Classification

Category: rushed_dense_chunk
Severity: 3
Notes:
Too fast

Preferred behavior:
EoL hyphenation wreaking semantic havoc again, get rid of it altogether!

## Reader State

Current index: 34
Sentence index: 3
Playback speed: 1x
Adaptation enabled: true

Current chunk:
department will install

## Timing Context

Base duration ms: 580
Effective duration ms: 580
Playback speed: 1x
Duration source: schedule
Current syntactic hint: dense
Current content word count: 2
Character length: 23

Original sentence:
Under the pilot, the transportation department will install temporary signs on Oak Street, Mercer Avenue, and the north side of Grand Market Square.

Previous chunks:
- [31] "to monitor the zones." - 760ms base / 760ms effective - dense - 2 content word(s) - 21 chars
- [32] "Under the pilot," - 540ms base / 540ms effective - dense - 2 content word(s) - 16 chars
- [33] "the transportation" - 440ms base / 440ms effective - normal - 1 content word(s) - 18 chars

Next chunks:
- [35] "temporary signs on" - 540ms base / 540ms effective - dense - 2 content word(s) - 18 chars
- [36] "Oak Street," - 540ms base / 540ms effective - dense - 2 content word(s) - 11 chars
- [37] "Mercer Avenue," - 540ms base / 540ms effective - dense - 2 content word(s) - 14 chars

## Session Summary

Event count: 15
Rewind count: 5
Pause count: 2
Speed change count: 1
Adaptation count: 3
Completed: false
Elapsed session ms: 182672
Estimated remaining chunks: 75
Average effective duration ms: 529
Last adaptation reason: rewinds
Last adaptation direction: slower

## Client

User agent:
Mozilla/5.0 (Android 16; Mobile; rv:152.0) Gecko/152.0 Firefox/152.0

Viewport:
384x678

---

<!-- Source: defect_20260709_230209_ce7bfc.md.gz -->

# Semantic RSVP Defect Report

Report ID: defect_20260709_230209_ce7bfc
Created at: 2026-07-09T23:02:09.252938Z

## Classification

Category: orphan_function_word
Severity: 2
Notes:
This is part of 'a.m."

Preferred behavior:
Initialisms should be chunked together especially when denoted by full stops.

## Reader State

Current index: 45
Sentence index: 4
Playback speed: 1x
Adaptation enabled: true

Current chunk:
m.

## Timing Context

Base duration ms: 580
Effective duration ms: 580
Playback speed: 1x
Duration source: schedule
Current syntactic hint: normal
Current content word count: 1
Character length: 2

Original sentence:
Commercial vehicles will have priority access from 6 a.m.

Previous chunks:
- [42] "have priority" - 440ms base / 440ms effective - normal - 1 content word(s) - 13 chars
- [43] "access from 6" - 540ms base / 540ms effective - dense - 2 content word(s) - 13 chars
- [44] "a." - 480ms base / 480ms effective - light - 0 content word(s) - 2 chars

Next chunks:
- [46] "to 11 a." - 580ms base / 580ms effective - normal - 1 content word(s) - 8 chars
- [47] "m." - 580ms base / 580ms effective - normal - 1 content word(s) - 2 chars
- [48] "and short" - 440ms base / 440ms effective - normal - 1 content word(s) - 9 chars

## Session Summary

Event count: 24
Rewind count: 9
Pause count: 3
Speed change count: 1
Adaptation count: 5
Completed: false
Elapsed session ms: 283227
Estimated remaining chunks: 64
Average effective duration ms: 529
Last adaptation reason: rewinds
Last adaptation direction: slower

## Client

User agent:
Mozilla/5.0 (Android 16; Mobile; rv:152.0) Gecko/152.0 Firefox/152.0

Viewport:
384x678

---

<!-- Source: defect_20260709_230245_fff6a9.md.gz -->

# Semantic RSVP Defect Report

Report ID: defect_20260709_230245_fff6a9
Created at: 2026-07-09T23:02:45.226620Z

## Classification

Category: orphan_function_word
Severity: 2
Notes:
'a.m.' is one thing

Preferred behavior:
Initialisms should be chunked together especially when denoted by full stops.

## Reader State

Current index: 47
Sentence index: 5
Playback speed: 1x
Adaptation enabled: true

Current chunk:
m.

## Timing Context

Base duration ms: 580
Effective duration ms: 580
Playback speed: 1x
Duration source: schedule
Current syntactic hint: normal
Current content word count: 1
Character length: 2

Original sentence:
to 11 a.m., and short passenger pickups will be allowed later in the day.

Previous chunks:
- [44] "a." - 480ms base / 480ms effective - light - 0 content word(s) - 2 chars
- [45] "m." - 580ms base / 580ms effective - normal - 1 content word(s) - 2 chars
- [46] "to 11 a." - 580ms base / 580ms effective - normal - 1 content word(s) - 8 chars

Next chunks:
- [48] "and short" - 440ms base / 440ms effective - normal - 1 content word(s) - 9 chars
- [49] "passenger pickups will" - 580ms base / 580ms effective - dense - 2 content word(s) - 22 chars
- [50] "be allowed" - 440ms base / 440ms effective - normal - 1 content word(s) - 10 chars

## Session Summary

Event count: 27
Rewind count: 9
Pause count: 3
Speed change count: 1
Adaptation count: 5
Completed: false
Elapsed session ms: 319218
Estimated remaining chunks: 62
Average effective duration ms: 529
Last adaptation reason: rewinds
Last adaptation direction: slower

## Client

User agent:
Mozilla/5.0 (Android 16; Mobile; rv:152.0) Gecko/152.0 Firefox/152.0

Viewport:
384x742

---

<!-- Source: defect_20260709_230455_1d44d8.md.gz -->

# Semantic RSVP Defect Report

Report ID: defect_20260709_230455_1d44d8
Created at: 2026-07-09T23:04:55.850796Z

## Classification

Category: rushed_dense_chunk
Severity: 2
Notes:
Too fast

Preferred behavior:
No EoL hyphenation, put long words in their own line and fit them to width.

## Reader State

Current index: 27
Sentence index: 2
Playback speed: 1.15x
Adaptation enabled: true

Current chunk:
this was not nervousness.

## Timing Context

Base duration ms: 660
Effective duration ms: 574
Playback speed: 1.15x
Duration source: schedule
Current syntactic hint: normal
Current content word count: 1
Character length: 25

Original sentence:
She checked her ticket again, although she knew the number by then, and told herself that this was not nervousness.

Previous chunks:
- [24] "by then," - 300ms base / 261ms effective - light - 0 content word(s) - 8 chars
- [25] "and told" - 400ms base / 348ms effective - normal - 1 content word(s) - 8 chars
- [26] "herself that" - 440ms base / 383ms effective - normal - 1 content word(s) - 12 chars

Next chunks:
- [28] "It was preparation." - 660ms base / 574ms effective - normal - 1 content word(s) - 19 chars
- [29] "The distinction" - 440ms base / 383ms effective - normal - 1 content word(s) - 15 chars
- [30] "mattered less than" - 540ms base / 470ms effective - dense - 2 content word(s) - 18 chars

## Session Summary

Event count: 9
Rewind count: 3
Pause count: 1
Speed change count: 0
Adaptation count: 3
Completed: false
Elapsed session ms: 63110
Estimated remaining chunks: 79
Average effective duration ms: 450
Last adaptation reason: rewinds
Last adaptation direction: slower

## Client

User agent:
Mozilla/5.0 (Android 16; Mobile; rv:152.0) Gecko/152.0 Firefox/152.0

Viewport:
384x678

---

<!-- Source: defect_20260709_230717_dde561.md.gz -->

# Semantic RSVP Defect Report

Report ID: defect_20260709_230717_dde561
Created at: 2026-07-09T23:07:17.061371Z

## Classification

Category: punctuation_rhythm_issue
Severity: 2
Notes:
The rhythm is off. Would interrupts the flow here

Preferred behavior:
I expected would to be pushed to the next chunk. This may be a bad split issue.

## Reader State

Current index: 98
Sentence index: 14
Playback speed: 1.15x
Adaptation enabled: true

Current chunk:
whether leaving would

## Timing Context

Base duration ms: 580
Effective duration ms: 504
Playback speed: 1.15x
Duration source: schedule
Current syntactic hint: dense
Current content word count: 2
Character length: 21

Original sentence:
She did not know whether leaving would make the problem smaller.

Previous chunks:
- [95] "the glass." - 620ms base / 539ms effective - normal - 1 content word(s) - 10 chars
- [96] "She" - 400ms base / 348ms effective - normal - 1 content word(s) - 3 chars
- [97] "did not know" - 440ms base / 383ms effective - normal - 1 content word(s) - 12 chars

Next chunks:
- [99] "make the problem" - 540ms base / 470ms effective - dense - 2 content word(s) - 16 chars
- [100] "smaller." - 580ms base / 504ms effective - normal - 1 content word(s) - 8 chars
- [101] "She" - 400ms base / 348ms effective - normal - 1 content word(s) - 3 chars

## Session Summary

Event count: 21
Rewind count: 8
Pause count: 2
Speed change count: 0
Adaptation count: 7
Completed: false
Elapsed session ms: 204323
Estimated remaining chunks: 8
Average effective duration ms: 450
Last adaptation reason: rewinds
Last adaptation direction: slower

## Client

User agent:
Mozilla/5.0 (Android 16; Mobile; rv:152.0) Gecko/152.0 Firefox/152.0

Viewport:
384x678
