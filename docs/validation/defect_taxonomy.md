# Defect Taxonomy

Use these categories when logging issues during manual validation. Severity is recorded separately for each defect:

- 1: minor annoyance
- 2: noticeable friction
- 3: comprehension-impacting
- 4: session-breaking

## bad_chunk_split

Definition: A chunk boundary interrupts a phrase, clause, or idea in a way that feels unnatural.

Example symptom: "not because" appears alone, then the reason arrives too late to feel connected.

Likely source area: chunking

Severity scale: use the shared 1-4 scale above.

## orphan_function_word

Definition: A low-content connector, article, auxiliary, or preposition is stranded as its own chunk or attached to the wrong side of a phrase.

Example symptom: A chunk displays only "and the" or begins with "of" after the meaningful noun has already passed.

Likely source area: chunking

Severity scale: use the shared 1-4 scale above.

## honorific_name_split

Definition: An honorific or courtesy title is separated from the personal name it identifies.

Example symptom: `Dr.` appears alone before `Mira Patel`, or `Ms.` is attached to the previous phrase instead of the name.

Likely source area: chunking

Severity scale: use the shared 1-4 scale above.

## title_name_split

Definition: A role title, institutional title, or named office is split from the name or noun phrase it modifies.

Example symptom: `Professor` appears as one chunk and `Nguyen` arrives separately, or `Chief Justice` separates from the surname.

Likely source area: chunking

Severity scale: use the shared 1-4 scale above.

## proper_name_split

Definition: A multi-token proper name, organization, place, or formal named entity is divided in a way that makes recognition harder.

Example symptom: `New` appears apart from `York`, or an organization name arrives one weak token at a time.

Likely source area: chunking

Severity scale: use the shared 1-4 scale above.

## article_noun_split

Definition: An article or determiner is separated from the noun phrase it introduces.

Example symptom: `the` appears alone before `quiet room`, or `a` is stranded after the meaningful noun phrase has passed.

Likely source area: chunking

Severity scale: use the shared 1-4 scale above.

## weak_boundary_chunk

Definition: A chunk boundary lands on a weak syntactic or semantic edge, creating a beat that feels arbitrary even when no word is completely orphaned.

Example symptom: A short modifier or connector is technically readable but the phrase clearly wants to stay with its neighbor.

Likely source area: chunking

Severity scale: use the shared 1-4 scale above.

## pronoun_or_preposition_bookend

Definition: A pronoun or preposition is left as the leading or trailing bookend of a chunk where it weakens comprehension.

Example symptom: `of` starts a chunk after its object is separated, or `it` trails a phrase that should have carried the pronoun into the next idea.

Likely source area: chunking

Severity scale: use the shared 1-4 scale above.

## overlong_chunk

Definition: A chunk contains too much text to read comfortably at the displayed size or duration.

Example symptom: A long phrase fills the phone width and disappears before it can be understood.

Likely source area: chunking

Severity scale: use the shared 1-4 scale above.

## underdense_chunk

Definition: A chunk is technically readable but carries too little meaning to justify its own beat.

Example symptom: A short transition such as "in this way" receives the same attention as a substantive claim.

Likely source area: chunking

Severity scale: use the shared 1-4 scale above.

## rushed_dense_chunk

Definition: A conceptually dense chunk is displayed for too little time.

Example symptom: A definition, contrast, or qualification passes before the reader can integrate it.

Likely source area: timing

Severity scale: use the shared 1-4 scale above.

## overpaused_light_chunk

Definition: A simple or low-content chunk receives too much dwell time or too much pause around it.

Example symptom: The reader feels stalled on a phrase that merely connects two ideas.

Likely source area: timing

Severity scale: use the shared 1-4 scale above.

## punctuation_rhythm_issue

Definition: Punctuation creates a pause, acceleration, or grouping that does not match the felt rhythm of the sentence.

Example symptom: A comma creates a heavy pause, but the phrase should flow into the next chunk.

Likely source area: timing

Note: Use this only when the quote/parenthetical visual state is clear and the remaining discomfort is about dwell or rhythm.

Severity scale: use the shared 1-4 scale above.

## quote_state_confusion

Definition: A quoted span is hard to track because the reader does not make quote entry, quote exit, or inside-quote state clear enough.

Example symptom: The text enters a quotation but later chunks no longer feel visibly connected to that quote, even if timing is acceptable.

Likely source area: display state / frontend

Severity scale: use the shared 1-4 scale above.

## parenthetical_state_confusion

Definition: A parenthetical or bracketed aside is hard to track because the reader does not make the parenthetical state clear enough.

Example symptom: A chunk inside parentheses reads like mainline prose, or the return from a parenthetical aside is unclear.

Likely source area: display state / frontend

Severity scale: use the shared 1-4 scale above.

## gesture_interference

Definition: Touch gestures trigger the wrong reader action or conflict with browser/device gestures.

Example symptom: A swipe intended to rewind navigates the browser or fails after several successful attempts.

Likely source area: frontend

Severity scale: use the shared 1-4 scale above.

## adaptation_annoyance

Definition: Automatic speed adaptation changes pace in a way that feels surprising, distracting, or unjustified.

Example symptom: The reader slows down after intentional pauses used for note-taking.

Likely source area: adaptation

Severity scale: use the shared 1-4 scale above.

## completion_or_reset_confusion

Definition: End-of-session, reset, or edit behavior makes it unclear what state the reader is in.

Example symptom: The reader reaches the final chunk, but the play button or progress indicator implies playback is still active.

Likely source area: frontend

Severity scale: use the shared 1-4 scale above.

## layout_or_visibility_issue

Definition: Text, controls, overlays, or debug details overlap, disappear, or become difficult to reach.

Example symptom: A speed overlay covers the displayed chunk, or a long word overflows the screen.

Likely source area: frontend

Severity scale: use the shared 1-4 scale above.

## comprehension_drop

Definition: The reader can complete the passage but cannot accurately summarize a point that was clear in normal reading.

Example symptom: The second summary misses a qualification or reverses a contrast.

Likely source area: validation/user

Severity scale: use the shared 1-4 scale above.

## fatigue_or_discomfort

Definition: The session causes unusual eye strain, tension, irritation, or effort even when comprehension remains adequate.

Example symptom: The fixed display reduces scanning but becomes tiring after several minutes.

Likely source area: validation/user

Severity scale: use the shared 1-4 scale above.

## other

Definition: A meaningful issue that does not fit the current taxonomy.

Example symptom: The tester notices a repeatable problem but cannot yet identify the source.

Likely source area: validation/user

Severity scale: use the shared 1-4 scale above.
