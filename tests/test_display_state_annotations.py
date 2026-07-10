from semantic_rsvp.timing.display_state import DisplayStateTracker
from semantic_rsvp.timing.schedule import schedule_text


def test_tracker_marks_straight_quote_boundaries_across_chunks():
    tracker = DisplayStateTracker()

    opening = tracker.annotate('"Air Force')
    inside = tracker.annotate("One is ready")
    closing = tracker.annotate('now."')
    after = tracker.annotate("The pilot waited.")

    assert opening.in_quote
    assert opening.quote_boundary == "open"
    assert inside.in_quote
    assert inside.quote_boundary == "none"
    assert closing.in_quote
    assert closing.quote_boundary == "close"
    assert not after.in_quote


def test_tracker_marks_curly_quotes():
    tracker = DisplayStateTracker()

    opening = tracker.annotate("\u201cAir Force")
    closing = tracker.annotate("One.\u201d")

    assert opening.in_quote
    assert opening.quote_boundary == "open"
    assert closing.in_quote
    assert closing.quote_boundary == "close"


def test_tracker_marks_parenthetical_depth_and_recovers_from_malformed_close():
    tracker = DisplayStateTracker()

    opening = tracker.annotate("(briefly")
    closing = tracker.annotate(")")
    malformed = tracker.annotate(")")

    assert opening.in_parenthetical
    assert opening.parenthetical_depth == 1
    assert closing.in_parenthetical
    assert closing.parenthetical_depth == 0
    assert malformed.in_parenthetical
    assert malformed.parenthetical_depth == 0


def test_schedule_marks_quote_state_for_quoted_span():
    schedule = schedule_text('The pilot said, "Air Force One is ready."')

    quoted = [item for item in schedule if item.display_state.in_quote]

    assert quoted
    assert any(item.display_state.quote_boundary == "open" for item in quoted)
    assert any(item.display_state.quote_boundary == "close" for item in quoted)
    assert schedule[-1].display_state.parenthetical_depth == 0


def test_schedule_marks_parenthetical_state():
    schedule = schedule_text("The system pauses (briefly) before continuing.")

    parenthetical = [item for item in schedule if item.display_state.in_parenthetical]

    assert parenthetical
    assert all(item.display_state.parenthetical_depth >= 0 for item in schedule)
    assert schedule[-1].display_state.parenthetical_depth == 0


def test_schedule_state_survives_multiple_quote_spans():
    schedule = schedule_text('"He hesitated," she said, "then continued." Then silence followed.')

    quote_boundaries = [
        item.display_state.quote_boundary
        for item in schedule
        if item.display_state.quote_boundary != "none"
    ]

    assert quote_boundaries == ["both", "both"]
    assert not schedule[-1].display_state.in_quote
