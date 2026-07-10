import re

from semantic_rsvp.chunking.interface import Chunker
from semantic_rsvp.chunking.models import Chunk

STOPWORDS = {
    "a",
    "an",
    "the",
    "and",
    "or",
    "but",
    "if",
    "not",
    "only",
    "then",
    "of",
    "to",
    "in",
    "on",
    "for",
    "with",
    "by",
    "from",
    "at",
    "as",
    "is",
    "are",
    "was",
    "were",
    "be",
    "been",
    "being",
    "do",
    "does",
    "did",
    "have",
    "has",
    "had",
    "may",
    "might",
    "can",
    "could",
    "should",
    "would",
    "will",
    "shall",
    "must",
    "too",
    "much",
    "few",
    "many",
    "little",
    "still",
    "rather",
    "than",
    "therefore",
    "whether",
    "it",
    "this",
    "that",
    "these",
    "those",
}

_TOKEN_PATTERN = re.compile(
    r"(?:[A-Za-z]\.){2,}|[A-Za-z0-9]+(?:'[A-Za-z0-9]+)?|[^\w\s]"
)
_PUNCTUATION = set(".,!?;:)]}\"'")
_OPENING_PUNCTUATION = set("([{\"")
_CLOSING_PUNCTUATION = set(")]}\"'")
_INDEFINITE_ARTICLES = {"a", "an"}
_BOUNDARY_CONNECTORS = {"and", "or", "but", "therefore"}
_AUXILIARIES = {
    "am",
    "are",
    "be",
    "been",
    "being",
    "can",
    "could",
    "did",
    "do",
    "does",
    "had",
    "has",
    "have",
    "is",
    "may",
    "might",
    "must",
    "shall",
    "should",
    "was",
    "were",
    "will",
    "would",
}
_INFLECTIONAL_SUPPORT = {"to", "not"}
_QUALIFIERS = {"too", "still", "not", "only"}


def tokenize(sentence: str) -> list[str]:
    if not isinstance(sentence, str):
        raise TypeError("tokenize expects a string.")
    return _TOKEN_PATTERN.findall(sentence)


def is_stopword(token: str) -> bool:
    return token.lower() in STOPWORDS


def count_content_words(tokens: list[str]) -> int:
    return sum(1 for token in tokens if _is_word(token) and not is_stopword(token))


class RuleBasedChunker(Chunker):
    def __init__(self, max_chars: int = 32, max_content_words: int = 2):
        if max_chars < 1:
            raise ValueError("max_chars must be at least 1.")
        if max_content_words < 1:
            raise ValueError("max_content_words must be at least 1.")
        self.max_chars = max_chars
        self.max_content_words = max_content_words

    def chunk_sentence(self, sentence: str) -> list[Chunk]:
        tokens = tokenize(sentence)
        if not tokens:
            return []

        chunks: list[Chunk] = []
        current: list[str] = []
        quote_is_open = False

        for index, token in enumerate(tokens):
            next_token = tokens[index + 1] if index + 1 < len(tokens) else None
            if _is_punctuation(token):
                if token == '"':
                    if quote_is_open:
                        if current:
                            current.append(token)
                        quote_is_open = False
                    else:
                        if current:
                            self._flush(current, chunks)
                        current = [token]
                        quote_is_open = True
                    continue
                if token in _OPENING_PUNCTUATION and current:
                    self._flush(current, chunks)
                    current = [token]
                    continue
                if current:
                    current.append(token)
                    if token in ".,!?;:" and next_token not in _CLOSING_PUNCTUATION:
                        self._flush(current, chunks)
                        current = []
                continue

            if not current:
                current.append(token)
                continue

            candidate = [*current, token]
            if self._should_split_before(current, candidate, token, next_token):
                self._flush(current, chunks)
                current = [token]
            else:
                current.append(token)

        self._flush(current, chunks)
        return chunks

    def _should_split_before(
        self,
        current: list[str],
        candidate: list[str],
        token: str,
        next_token: str | None = None,
    ) -> bool:
        if _unavoidable_long_token(token, self.max_chars):
            return bool(current)
        if _render_chunk(candidate) and len(_render_chunk(candidate)) > self.max_chars:
            return True
        if count_content_words(candidate) > self.max_content_words:
            return True

        current_words = _word_count(current)
        current_content_words = count_content_words(current)
        last_token = current[-1]
        token_lower = token.lower()

        if _starts_new_phrase(current, token, next_token):
            return True

        if _should_preserve_candidate(candidate):
            return False

        if is_stopword(token):
            if _is_word(last_token) and is_stopword(last_token) and current_content_words > 0:
                return True
            if _is_auxiliary_chain(candidate):
                return False
            if token_lower in _INFLECTIONAL_SUPPORT and _next_is_auxiliary_or_word(next_token):
                return current_content_words > 0
            return current_words >= 3

        if current_content_words >= 1 and current_words >= 2 and not is_stopword(last_token):
            return True

        return current_words >= 4

    def _flush(self, tokens: list[str], chunks: list[Chunk]) -> None:
        text = _render_chunk(tokens).strip()
        if not text or all(_is_punctuation(token) for token in tokens):
            return

        content_word_count = count_content_words(tokens)
        chunks.append(
            Chunk(
                text=text,
                content_word_count=content_word_count,
                char_length=len(text),
                syntactic_hint=_syntactic_hint(tokens, content_word_count),
            )
        )


def _render_chunk(tokens: list[str]) -> str:
    text = ""
    for token in tokens:
        if not text:
            text = token
        elif token == '"' and text[-1] not in _OPENING_PUNCTUATION:
            text += token
        elif _is_punctuation(token) and token not in _OPENING_PUNCTUATION:
            text += token
        elif token in _OPENING_PUNCTUATION:
            text += f" {token}"
        elif text[-1] in _OPENING_PUNCTUATION:
            text += token
        else:
            text += f" {token}"
    return text


def _syntactic_hint(tokens: list[str], content_word_count: int) -> str:
    punctuation_count = sum(1 for token in tokens if _is_punctuation(token))
    if punctuation_count > len(tokens) / 2:
        return "punctuation"
    if content_word_count == 0:
        return "light"
    if content_word_count == 1:
        return "normal"
    return "dense"


def _is_word(token: str) -> bool:
    return bool(re.search(r"[A-Za-z0-9]", token))


def _is_punctuation(token: str) -> bool:
    return not _is_word(token)


def _word_count(tokens: list[str]) -> int:
    return sum(1 for token in tokens if _is_word(token))


def _unavoidable_long_token(token: str, max_chars: int) -> bool:
    return _is_word(token) and len(token) > max_chars


def _starts_new_phrase(
    current: list[str],
    token: str,
    next_token: str | None,
) -> bool:
    token_lower = token.lower()
    if not current:
        return False
    if token_lower in _BOUNDARY_CONNECTORS and count_content_words(current) > 0:
        return True
    if token_lower == "whether" and count_content_words(current) > 0:
        return True
    if (
        token_lower in _AUXILIARIES
        and current[0].lower() == "whether"
        and count_content_words(current) > 0
        and _next_is_auxiliary_or_word(next_token)
    ):
        return True
    if (
        token_lower in _AUXILIARIES
        and _next_is_auxiliary_or_word(next_token)
        and count_content_words(current) >= 2
    ):
        return True
    if (
        token_lower in _AUXILIARIES
        and next_token
        and next_token.lower() == "not"
        and count_content_words(current) > 0
    ):
        return True
    if token_lower == "to" and _is_auxiliary(next_token) and count_content_words(current) > 0:
        return True
    if (
        token_lower in _QUALIFIERS
        and current[-1].lower() not in _AUXILIARIES
        and count_content_words(current) > 0
    ):
        return True
    if current == ["or"] and token_lower in _INDEFINITE_ARTICLES:
        return True
    return False


def _should_preserve_candidate(candidate: list[str]) -> bool:
    words = [token.lower() for token in candidate if _is_word(token)]
    if _is_article_modifier_head(words):
        return True
    if _is_short_as_phrase(words):
        return True
    if _is_auxiliary_chain(candidate):
        return True
    if _is_quantifier_phrase(words):
        return True
    return False


def _is_article_modifier_head(words: list[str]) -> bool:
    return (
        len(words) == 3
        and words[0] in _INDEFINITE_ARTICLES
        and count_content_words(words) <= 2
    )


def _is_short_as_phrase(words: list[str]) -> bool:
    return len(words) <= 3 and words[:1] == ["as"] and count_content_words(words) <= 2


def _is_auxiliary_chain(tokens: list[str]) -> bool:
    words = [token.lower() for token in tokens if _is_word(token)]
    if not words:
        return False
    support_count = sum(
        1 for word in words if word in _AUXILIARIES or word in _INFLECTIONAL_SUPPORT
    )
    return support_count >= len(words) - 1 and len(words) <= 4


def _is_quantifier_phrase(words: list[str]) -> bool:
    return len(words) >= 2 and words[0] == "too" and words[1] in {
        "much",
        "many",
        "few",
        "little",
    }


def _is_auxiliary(token: str | None) -> bool:
    return bool(token and token.lower() in _AUXILIARIES)


def _next_is_auxiliary_or_word(token: str | None) -> bool:
    return bool(token and _is_word(token))
