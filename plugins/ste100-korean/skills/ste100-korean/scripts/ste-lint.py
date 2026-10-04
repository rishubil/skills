#!/usr/bin/env python3
# /// script
# requires-python = ">=3.10"
# dependencies = ["kiwipiepy>=0.24"]
# ///
"""Deterministic bilingual (Korean + English) linter for the structural STE rules.

Checks only rules verifiable without ASD's dictionary. Deliberately never
flags hedges or modality (may/might/could, ~ㄹ 수 있다, ~것 같다, ~로 보인다):
confidence is content, and a linter that pressures hedges out would rewrite
claims.

Usage:
    uv run ste-lint.py FILE [FILE ...]
    echo "text" | uv run ste-lint.py [--json]
    ste-lint.py --baseline 5 FILE           # pass unless hard findings exceed 5
    ste-lint.py --disable passive-voice,ko-passive FILE
    ste-lint.py --glossary docs/GLOSSARY.md FILE
    ste-lint.py --no-glossary --no-morph FILE
    ste-lint.py --ko-max 20 --en-max 25 FILE
    ste-lint.py --selftest

Each sentence is routed by script: a sentence with any Hangul syllable gets the
Korean rules (ids prefixed `ko-`), every other sentence gets the English rules.
The semicolon and arrow-speak rules apply to both. Korean morphology rules use kiwipiepy when
it is importable and fall back to regex heuristics otherwise (lower precision).

Exit codes: 0 pass, 1 hard findings exceed the baseline, 2 usage error or
missing file. Advisory findings never fail the run.
"""

# English rules adapted from danyuchn/asd-ste100-skill (scripts/ste-lint.py),
# MIT License, (c) 2026 Dustin Yuchen Teng.
# The stem-expansion technique (expanding a stem's last syllable so conjugated
# and contracted Korean forms match) is adapted from beamonic/ste-ko,
# MIT License, (c) 2026 Beamonic.
# Several Korean rule ideas (translationese additions, plain-word, ai-tell,
# middle-dot, dash, genitive-chain, honorific-object) come from
# Turtle-Hwan/im-ai-copyeditor, MIT License, (c) 2026 Turtle-Hwan. Only the
# ideas are used; the patterns here are written independently.
# Several English style rules (ai-vocabulary, filler-phrase, plain-word,
# fancy-is, chatbot-phrase, em-dash, curly-quote, arrow-speak,
# title-case-heading, inline-header) take their ideas from the `unslop` skill
# in cursor/plugins (pstack), MIT License, (c) 2026 Lauren Tan. Only the ideas
# are used; the patterns here are written independently.

import argparse
import json
import os
import re
import sys
import unicodedata
from collections import namedtuple

# ponytail: regex heuristics plus an optional morphological analyzer, not a
# parser. No ellipsis rule by owner's choice: technical writing sometimes
# earns one.

NOTICE = ("ste-lint: kiwipiepy unavailable; Korean morphology rules use "
          "regex fallback (lower precision)")

HANGUL = re.compile("[가-힣]")

# --------------------------------------------------------------------------
# English rules (ported from upstream)
# --------------------------------------------------------------------------

# Irregular past participles used by the present-perfect heuristic.
IRREGULAR_PARTICIPLES = "given|taken|made|done|found|seen|known|shown|written|built|sent|set|run|read|kept|held|left|put|cut|hit|let|shut|split|spread|begun|become|come|gone|got|gotten|lost|met|paid|said|sold|told|thought|brought|bought|caught|taught|won|worn|torn|born|drawn|grown|thrown|flown|driven|risen|chosen|broken|spoken|frozen|hidden|ridden|forgotten|fallen|eaten|beaten|understood|stood|struck|stuck|swung|hung|led|fed|bled|fled|sped|bound|wound|dug|spun|slid|bit|lit|quit"

# Preserve the original passive heuristic; perfects also include intransitive verbs.
PASSIVE_PARTICIPLES = "given|taken|made|done|found|seen|known|shown|written|built|sent|set|run|read|kept|held|left|put"
MODAL_PERFECT_PREFIX = re.compile(
    r"\b(?:may|might|could|should|would|must|can|will|shall)"
    r"(?:\s+not|n['’]t)?\s+$", re.I,
)

SEMICOLON = re.compile(r";")
SEMICOLON_MSG_EN = "STE bans the semicolon (Rule 8.1). Split into separate sentences."
SEMICOLON_MSG_KO = "국어 문장 부호에 쌍반점은 없습니다. 문장을 나누십시오."

RULES = [
    ("phrasal-verb", "hard",
     re.compile(r"\b(spin(?:ning|s)? up|spun up|reach(?:ing|es|ed)? out|div(?:e|es|ing|ed) into|dove into|kick(?:ing|s|ed)? off|circl(?:e|es|ing|ed) back|touch(?:ing|es|ed)? base)\b", re.I),
     "Soft phrasal verb. Use the single plain verb (start, contact, read, begin)."),
    ("marketing-adjective", "hard",
     re.compile(r"\b(seamless(?:ly)?|robust(?:ly)?|cutting-edge|effortless(?:ly)?|blazing[- ]fast|world-class|state-of-the-art|game-chang(?:ing|er))\b", re.I),
     "Marketing adjective. Delete, or replace with the measurement that earns the claim."),
    ("nominalization", "hard",
     re.compile(r"\b(perform|performs|performed|conduct|conducts|conducted|carry out|carries out|carried out)\s+(?:a|an|the)\s+\w+(?:tion|sion|ment|ance|ence|ysis)\b", re.I),
     "Action frozen into a noun. Use the verb (analyze, not perform an analysis of)."),
    ("passive-voice", "advisory",
     re.compile(r"\b(is|are|was|were|been|being)\s+(\w+ed|" + PASSIVE_PARTICIPLES + r")\b(?!\s+(?:to|for|by)\s+\w+ing)", re.I),
     "Possible passive voice. Name the actor and use an active verb, unless the actor is unknown or irrelevant."),
    ("present-perfect", "advisory",
     # modal + perfect infinitive ("may have failed") is a protected hedge, not present perfect
     re.compile(r"(?<!\bmay )(?<!\bmight )(?<!\bcould )(?<!\bshould )(?<!\bwould )(?<!\bmust )\b(has|have|had)\s+(?:been\s+)?(?:\w+(?:ed|en)|" + IRREGULAR_PARTICIPLES + r")\b", re.I),
     "Compound tense. Use simple past/present unless current relevance is the point (then keep and flag)."),
]

# One word, one meaning: groups of verbs commonly rotated for the same action.
# Only pairs where the members are genuinely interchangeable — error/fault/failure
# are distinct concepts and stay out.
SYNONYM_GROUPS = [
    ("check", "verify", "confirm", "validate"),
    ("delete", "remove", "erase"),
    ("start", "launch", "begin", "initiate"),
    ("stop", "halt", "terminate"),
    ("show", "display"),
    ("use", "utilize", "employ"),
    ("fix", "repair", "correct"),
    ("send", "transmit"),
    ("get", "retrieve", "fetch", "obtain"),
    ("change", "modify", "alter"),
]

# Advisory style rules for English prose (ideas from cursor/plugins pstack
# `unslop`). Plain regex tables; _lint_english_style applies them.
_DET_WORDS = "the|a|an|our|your|this|that|these|those|its|their"
_DET = r"(?:" + _DET_WORDS + r")"
AI_VOCABULARY = re.compile("|".join((
    r"\bdelv(?:e|es|ed|ing)\b",
    r"\b(?:crucial|pivotal|tapestry|testament|intricate|interplay|vibrant"
    r"|enduring)\b",
    # `underscore` as a verb: noun uses (an underscore, use underscores in
    # names) are not followed by a determiner or that/how.
    r"(?<!\bthe )(?<!\ban )(?<!\ba )\bunderscor(?:e|es|ed|ing)\b"
    r"(?=\s+(?:" + _DET_WORDS + r"|how|why|what)\b)",
    r"\bshowcas(?:e|es|ed|ing)\b",
    r"\bfoster(?:s|ed|ing)?\b",
    r"\bgarner(?:s|ed|ing)?\b",
    r"^\s*Additionally,",
)), re.I)
AI_VOCABULARY_MSG = "AI vocabulary. Use the plain word."
# (pattern, replacement); a replacement of None means delete the phrase.
FILLER_PHRASES = [
    (re.compile(r"\bin order to\b", re.I), "to"),
    (re.compile(r"\bdue to the fact that\b", re.I), "because"),
    (re.compile(r"\bit is important to note that\b", re.I), None),
    (re.compile(r"\bit['’]s worth noting that\b", re.I), None),
    (re.compile(r"\bin the event that\b", re.I), "if"),
    (re.compile(r"\bat this point in time\b", re.I), "now"),
]
PLAIN_WORDS_EN = [
    (re.compile(r"\butiliz(?:e|es|ed|ing)\b", re.I), "use"),
    # `leverage` is also a noun (financial leverage); only the verb frame.
    (re.compile(r"\bleverag(?:e|es|ed|ing)(?=\s+" + _DET + r"\b)", re.I), "use"),
    (re.compile(r"\bfacilitat(?:e|es|ed|ing)\b", re.I), "help"),
    (re.compile(r"\bnumerous\b", re.I), "many"),
]
FANCY_IS = re.compile(r"\b(?:serves|stands) as\b|\bboasts\b", re.I)
CHATBOT_PHRASE = re.compile(
    r"\bI hope this helps\b|\bLet me know if\b|\bGreat question\b"
    r"|\bCertainly!|\bOf course!|\bYou['’]re absolutely right\b"
    r"|\bHappy to help\b", re.I)
EM_DASH = re.compile(r"—|(?<=\s)--(?=\s)")
CURLY_QUOTE = re.compile("[“”‘’]")
# `->` and `=>` need spaces around them (`ptr->next` is not prose); `→` does not.
ARROW = re.compile(r"(?<=\w)\s*→\s*(?=\w)|(?<=\w)\s+(?:->|=>)\s+(?=\w)")
INLINE_HEADER = re.compile(
    r"^ {0,3}(?:[-*+]|[0-9]+[.)])[ \t]+(?:\[[ xX]\][ \t]+)?"
    r"\*\*([^*\n]+?)(?::\*\*|\*\*:)[ \t]+(\S.*)$")

EN_MAX = 25  # descriptions cap; instructions cap is 20 but undetectable without context
KO_MAX = 20  # 어절 cap for Korean sentences

# --------------------------------------------------------------------------
# Korean rules
# --------------------------------------------------------------------------

# A trailing vowel/final consonant merges with the next ending, so `되어지` +
# `-ㅂ니다` becomes `되어집니다`. Expand the last syllable of a stem to every
# final consonant plus its contracted vowel (ㅏ→ㅐ, ㅓ→ㅔ, ㅗ→ㅘ, ㅚ→ㅙ,
# ㅜ→ㅝ, ㅣ→ㅕ) so conjugated and contracted forms still match.
_CONTRACT = {0: 1, 4: 5, 8: 9, 11: 12, 13: 14, 20: 6}


def syllable_class(ch):
    """Expand one syllable to a character class of all its inflected shapes."""
    if not ("가" <= ch <= "힣"):
        return re.escape(ch)
    code = ord(ch) - 0xAC00
    cho, jung = code // 588, (code % 588) // 28
    jungs = {jung} | ({_CONTRACT[jung]} if jung in _CONTRACT else set())
    chars = "".join(chr(0xAC00 + cho * 588 + j * 28 + t)
                    for j in sorted(jungs) for t in range(28))
    return f"[{chars}]"


def stem_pattern(stem, expand=True, left=True):
    """Regex for a stem plus any suffix, expanding the last syllable if asked.

    Hangul has no `\\b`, so the left boundary is a negative lookbehind and the
    tail is any run of Hangul (particles, endings).
    """
    words = stem.split()
    parts = []
    for wi, word in enumerate(words):
        last_word = wi == len(words) - 1
        parts.append("".join(
            syllable_class(c) if (expand and last_word and j == len(word) - 1)
            else re.escape(c) for j, c in enumerate(word)))
    return (r"(?<![가-힣])" if left else "") + r"\s*".join(parts) + r"[가-힣]*"


# 되어지 etc. are always double passives, so there is no left boundary: the
# stem normally sits at the end of a longer word (`삭제되어졌다`).
DOUBLE_PASSIVE_STEMS = ("되어지", "보여지", "잊혀지", "쓰여지", "불려지",
                        "놓여지", "쌓여지", "닫혀지", "열려지", "읽혀지",
                        "잡혀지", "담겨지", "나뉘어지")
KO_DOUBLE_PASSIVE = re.compile("|".join(
    stem_pattern(s, left=False) for s in DOUBLE_PASSIVE_STEMS))
# `만들어지다` is a standard 피동, not a double passive: advisory only.
KO_MAKE_PASSIVE = re.compile(stem_pattern("만들어지", left=False))
PASSIVE_STEMS = {"보이", "잊히", "쓰이", "불리", "놓이", "쌓이", "닫히", "열리",
                 "읽히", "잡히", "담기", "나뉘"}

# Passives that express the writer's confidence: modality, not rewrite targets.
HEDGE_PASSIVE_NOUNS = ("예상", "추정", "판단", "생각", "예측", "전망", "우려",
                       "기대", "간주", "평가")
# Intransitive/stative passives where the subject itself changes state and no
# actor is hidden (서버가 시작되지 않으면). Not worth a rewrite.
MIDDLE_PASSIVE_NOUNS = ("시작", "종료", "만료", "완료", "포함", "구성", "해당",
                        "발생", "발급")
SKIP_PASSIVE_NOUNS = HEDGE_PASSIVE_NOUNS + MIDDLE_PASSIVE_NOUNS
# Receive-verbs that look like `NOUN+받` but are not passives of a noun act.
RECEIVE_PREFIXES = ("내려", "돌려", "넘겨", "물려", "빌려", "건네", "이어",
                    "되돌려", "전해")
KO_PASSIVE_RE = re.compile(
    r"(?<![가-힣])([가-힣]{2,}?)"
    r"(?:(되었|되|됩|된|됐|받(?!침)|당하|당했)|(될)(?!\s*[것수]))")

KO_LIGHT_VERB_RE = re.compile(
    r"[가-힣]+[을를]\s*(?:진행|실시|수행|시행)(?:하|합|한|했|할|해)"
    r"|[가-힣]+[이가]\s*이루어(?:지|졌|집)")
LIGHT_NOUNS = {"진행", "실시", "수행", "시행"}
LIGHT_MSG = ("동작을 명사로 굳혔습니다. 동사를 바로 쓰십시오"
             "(백업 작업을 진행합니다 → 백업합니다).")

TILDE_RANGE = re.compile(r"\d\s*~\s*\d")

# (pattern, suggestion). Every hit is advisory: a pattern can be legitimate in
# its literal sense ("파일을 가지고 있다" can mean physical possession).
_RIEUL = "".join(chr(c) for c in range(0xAC00, 0xD7A4) if (c - 0xAC00) % 28 == 8)
TRANSLATIONESE = [
    (re.compile(r"에\s*대(?:한(?!민국)|해서?|하여)"), "을/를, 의, 또는 삭제"),
    (re.compile(r"[을를]\s*통(?:해서?|한|하여)"), "(으)로, 에"),
    (re.compile(r"에\s*있어(?:서(?:는|도|만)?)?(?![가-힣])"), "에서, ~할 때"),
    (re.compile(r"(?<=[가-힣])(?:으)?로부터"), "에게서, 에서"),
    (re.compile(r"에\s*의(?:해서?|한|하여)"), "(으)로, 또는 능동문"),
    (re.compile(r"[을를]\s*필요로\s*하"), "~이 필요하다"),
    (re.compile(r"(?<![가-힣])[가-힣]{2,}\s*중에\s*있"), "~고 있다"),
    (re.compile(r"하는\s*것이\s*가능하"), "할 수 있다"),
    (re.compile(r"[을를]\s*가지고\s*있"), "~이 있다"),
    (re.compile(r"[가-힣]*(?:[" + _RIEUL + r"]|을|는)\s*경우"), "~하면"),
    (re.compile(r"(?<=[가-힣]{2})시(?:키(?:다|는|고|며|면|지|도록|게|기|어)|켜|켰|킨|킵|킬|킴)"),
     "~하다"),
    (re.compile(r"(?:으)?로\s*인(?:하여|해서?|한)"), "(으)로, 때문에"),
    (re.compile(r"의\s*경우"), "~은/는, ~에는"),
    (re.compile(r"에도\s*불구하고"), "~지만"),
    (re.compile(r"에\s*다름\s*아(?:니|닙|닌)"), "바로 ~다"),
    (re.compile(r"[을를]\s*요(?:하|합|한|해|했)"), "~해야 한다"),
    (re.compile(r"에\s*의거(?:하여|한|해)"), "~에 따라"),
    (re.compile(r"에\s*위치(?:하|합|한|해|했)"), "~에 있다"),
    # Purpose clauses are often fine; the hit only asks whether it is needed.
    (re.compile(r"기\s*위(?:해서?|하여)"), "~려고, ~도록"),
]

# Official-document Hanja words with a plain replacement. 하기 is noisy, so it
# only counts before the nouns it points at; 불가 must not match 불가능/불가피.
_L = r"(?<![가-힣])"
PLAIN_WORDS = [
    (re.compile(_L + "금번"), "이번"),
    (re.compile(_L + "금일"), "오늘"),
    (re.compile(_L + "익일"), "다음 날"),
    (re.compile(_L + r"상기(?:의)?(?![가-힣])"), "위"),
    (re.compile(_L + r"하기(?:의)?(?=\s*(?:내용|사항|와\s*같이|표))"), "아래"),
    (re.compile(_L + "소정의"), "정해진"),
    (re.compile(_L + "제고"), "높임"),
    (re.compile(_L + "득하"), "받"),
    (re.compile(_L + r"불가(?:하[가-힣]*|합[가-힣]*|함[가-힣]*|(?![가-힣]))"), "할 수 없다"),
    (re.compile(_L + "숙지"), "확인/익히다"),
]

# Stock phrases that frame a claim instead of making it.
AI_TELL = re.compile("|".join((
    r"단순(?:한|히)\s+[^.]{0,20}[이가]\s*아니라",
    r"중요한\s*(?:것|점)은",
    r"(?:라는|다는)\s*(?:것|점)(?:이다|입니다)[.!?…\"'”’)]*$",
    r"[을를]\s*가능하게\s*(?:한다|합니다|해)",
    r"^[\s\"'“‘(\[]*(?:좋은 질문입니다|결론적으로|요약하자면|간단히 말하자면"
    r"|다음과 같습니다|말씀하신 (?:대로|것처럼)|확인해 보겠습니다)",
    r"[가-힣]+[을를]\s*넘어\s*[가-힣]+(?:으)?로",
)))

# English-style cataphoric frames ("Here's what X is"): the sentence announces
# content instead of giving it. Only at sentence end, so a real predicate that
# starts the same way ("이것으로 해결됩니다") never matches.
KO_CATAPHORIC = re.compile(
    r"[가-힣]+(?:은|는)\s*(?:이것입니다|이렇습니다|다음입니다)[.:]?\s*$"
    r"|여기서부터는\s*[가-힣]+입니다[.:]?\s*$")
KO_CATAPHORIC_MSG = ("영어식 앞가리킴 틀입니다('Here is...'). 내용을 바로 "
                     "쓰십시오(예: '로그를 보면 ...').")

MIDDLE_DOT = re.compile(r"[가-힣]+(?:[·‧・･][가-힣]+)+")
# A dash used as a separator. Needs a non-space on both sides, so list
# markers and table separators never match; digit-dash-digit is a range.
DASH = re.compile(r"(?<=\S)\s*(?:[—–]|(?<=\s)--?(?=\s))\s*(?=\S)")
# 의 inside these whole words is part of the word, not the genitive particle
# (whole-word match: 설정의 is a genitive even though it ends in 정의).
GENITIVE_STEM_WORDS = ("회의", "주의", "정의", "동의", "합의", "논의", "문의",
                       "강의", "협의", "의의")
GENITIVE_RE = re.compile(r"(?<![가-힣])[가-힣]+의(?=\s)")
GENITIVE_MAX = 2

# Object honorifics: -시- on a thing, not a person.
HONORIFIC_OBJECT = re.compile(
    r"(?:나오|준비되|완료되|확인되|처리되|접수되)셨습니다"
    r"|품절이십니다|[0-9,]+원이십니다")

DOUBLE_NEGATION = re.compile(
    r"지\s*않을\s*수\s*없|없지\s*않|아니지\s*않|않(?:은|는)\s*것(?:은|이)\s*아니")

MARKETING_KO = [
    stem_pattern("혁신적", expand=False),
    stem_pattern("획기적", expand=False),
    stem_pattern("원활하"), stem_pattern("원활히", expand=False),
    stem_pattern("완벽하"), stem_pattern("완벽히", expand=False),
    stem_pattern("강력하"), stem_pattern("강력히", expand=False),
    r"(?<![가-힣])매끄(?:럽|러[운워웠우울움])[가-힣]*",
    stem_pattern("최첨단", expand=False),
    stem_pattern("압도적", expand=False),
    r"(?<![가-힣])놀(?:라(?:운|워|웠)|랍)[가-힣]*",
    r"(?<![가-힣])손쉽[가-힣]*|(?<![가-힣])손쉬(?:운|워|웠|우|울|움)[가-힣]*",
    stem_pattern("차세대", expand=False),
    stem_pattern("극대화", expand=False),
    stem_pattern("세계 최고", expand=False),
    stem_pattern("업계 최고", expand=False),
]
KO_MARKETING = re.compile("|".join(MARKETING_KO))

KO_VAGUE_QUANTITY = re.compile(
    r"(?<![가-힣])(?:많은|다수의|대량의|상당한|적지\s*않은)(?=\s*[가-힣])"
    r"|(?<![가-힣])일부(?=\s+[가-힣])")

# Same-meaning groups. Members match at a word start with any suffix, so
# 삭제하다 / 삭제됩니다 count. `사용(?!자)` keeps 사용자 out of the 사용 group.
KO_SYNONYM_GROUPS = [
    ("삭제", "제거"),
    ("중지", "중단", "정지"),
    ("사용", "이용", "활용"),
    ("시작", "개시", "착수"),
    ("오류", "에러"),
    ("사용자", "유저"),
    ("설정", "세팅"),
    ("확인", "검증", "점검"),
    ("수정", "변경"),
    ("표시", "출력"),
]
_KO_SYN_EXCLUDE = {"사용": "(?!자)", "이용": "(?!자)"}

NOUN_STACK_MAX = 3
ADNOMINAL_MAX = 2
NOUNISH = {"NNG", "NNP", "SL", "SN", "XR"}
CONTENT_NOUNS = {"NNG", "NNP", "SL"}
PASSIVE_MARKERS = {"어", "아", "여"}
FUTURE_ETM = {"ᆯ", "을", "ㄹ"}

# --------------------------------------------------------------------------
# Markdown handling
# --------------------------------------------------------------------------

CODE_FENCE = re.compile(r"^(```|~~~)")
INLINE_CODE = re.compile(r"`[^`]*`")
LIST_ITEM_START = re.compile(
    r"^(?P<indent> {0,3})(?P<marker>[-*+]|[0-9]+[.)])(?P<gap> +)(?P<body>.*)$"
)
CONJUNCTION_END = re.compile(
    r"(?:\b(?:and|or)|(?<![가-힣])(?:및|또는|그리고|혹은))\s*$", re.I)
TABLE_SEPARATOR_CELL = re.compile(r"^:?-{3,}:?$")
HEADING = re.compile(r"^ {0,3}#{1,6}(?:[ \t]+|$)")
BLOCKQUOTE = re.compile(r"^ {0,3}(?:>[ \t]?)+")
TASK_BOX = re.compile(r"^\[[ xX]\][ \t]+")
HRULE = re.compile(r"^ {0,3}([-*_])(?:\s*\1){2,}\s*$")
SETEXT = re.compile(r"^ {0,3}=+\s*$")
REFDEF = re.compile(r"^ {0,3}\[[^\]]+\]:\s")
EN_SPLIT = re.compile(r"(?<=[.!?])\s+")

# Cleaning passes applied to the text of one unit. Each is (pattern, repl).
# Inline code becomes a placeholder word so counts stay sane; links keep their
# text; URLs, HTML tags, entities and emphasis marks vanish.
CLEAN_PASSES = [
    (INLINE_CODE, "CODE"),
    (re.compile(r"!?\[(?=[^\]]*\]\([^)]*\))"), ""),
    (re.compile(r"\]\([^)]*\)"), ""),
    (re.compile(r"&#?\w+;"), ""),
    (re.compile(r"<https?://[^>\s]*>"), ""),
    (re.compile(r"https?://[^\s)\]>]+"), ""),
    (re.compile(r"</?[A-Za-z!][^>\n]*>"), ""),
    (re.compile(r"\*+"), ""),
]


def josa(word, with_final, without_final):
    """Pick a Korean particle by whether the last syllable has a final consonant."""
    last = word[-1]
    if "가" <= last <= "힣" and (ord(last) - 0xAC00) % 28:
        return with_final
    return without_final


def _word_re(base):
    return re.compile(r"\b" + base + r"(?:s|es|ed|d|ing)?\b", re.I)


def _ko_syn_re(base):
    return re.compile(r"(?<![가-힣])" + base + _KO_SYN_EXCLUDE.get(base, ""))


def _leading_spaces(line):
    return len(line) - len(line.lstrip(" "))


def _is_list_continuation(line, content_indent):
    if not line.strip():
        return True
    if LIST_ITEM_START.match(line):
        return False
    return _leading_spaces(line) >= content_indent


def _split_table_row(line):
    """Return trimmed table cells and their zero-based source columns.

    A pipe must separate at least two cells. Escaped pipes stay in their cell.
    This deliberately implements only the ordinary Markdown table shape; it is
    enough to distinguish a table from prose that happens to contain a pipe.
    """
    left = len(line) - len(line.lstrip())
    right = len(line.rstrip())
    content = line[left:right]
    if "|" not in content:
        return None
    if content.startswith("|"):
        content = content[1:]
        left += 1
    if content.endswith("|"):
        content = content[:-1]
    raw_cells = re.split(r"(?<!\\)\|", content)
    if len(raw_cells) < 2:
        return None

    cells = []
    column = left
    for raw_cell in raw_cells:
        leading = len(raw_cell) - len(raw_cell.lstrip())
        cells.append((raw_cell.strip(), column + leading))
        column += len(raw_cell) + 1
    return cells


def _markdown_table_cells(lines):
    """Map ordinary Markdown table rows to their prose cells.

    The separator row anchors detection, so pipe-containing prose is not
    treated as a table. Both leading-pipe and no-leading-pipe table styles are
    accepted when their header and body use the same number of cells.
    """
    table_cells = {}
    index = 1
    while index < len(lines):
        separator = _split_table_row(lines[index])
        header = _split_table_row(lines[index - 1])
        if (not separator or not header or len(separator) != len(header)
                or not all(TABLE_SEPARATOR_CELL.fullmatch(cell)
                           for cell, _ in separator)):
            index += 1
            continue

        table_cells[index - 1] = header
        table_cells[index] = []
        index += 1
        while index < len(lines):
            row = _split_table_row(lines[index])
            if not row or len(row) != len(separator):
                break
            table_cells[index] = row
            index += 1
    return table_cells


def mask_lines(raw_lines):
    """Blank YAML frontmatter, fenced code and HTML comments.

    Line count and (for partially masked lines) columns are preserved, so
    line numbers stay valid and masked text never reaches a rule.
    """
    n = len(raw_lines)
    skip_until = -1
    if n and raw_lines[0].strip() == "---":
        for j in range(1, n):
            if raw_lines[j].strip() in ("---", "..."):
                skip_until = j
                break
    out = []
    fence = None
    in_comment = False
    for i, line in enumerate(raw_lines):
        if i <= skip_until:
            out.append("")
            continue
        # HTML comments (may span lines): replace with spaces.
        if in_comment or "<!--" in line:
            res, pos = [], 0
            while pos < len(line):
                if in_comment:
                    end = line.find("-->", pos)
                    if end < 0:
                        res.append(" " * (len(line) - pos))
                        pos = len(line)
                    else:
                        res.append(" " * (end + 3 - pos))
                        pos = end + 3
                        in_comment = False
                else:
                    start = line.find("<!--", pos)
                    if start < 0:
                        res.append(line[pos:])
                        break
                    res.append(line[pos:start] + "    ")
                    pos = start + 4
                    in_comment = True
            line = "".join(res)
        stripped = line.strip()
        if fence:
            if stripped.startswith(fence):
                fence = None
            out.append("")
            continue
        m = CODE_FENCE.match(stripped)
        if m:
            fence = m.group(1)
            out.append("")
            continue
        out.append(line)
    return out


def sub_map(text, cols, pattern, repl):
    """re.sub that also keeps `cols[i]` = original column of text[i]."""
    out, ocols, pos = [], [], 0
    for m in pattern.finditer(text):
        out.append(text[pos:m.start()])
        ocols.extend(cols[pos:m.start()])
        r = repl(m) if callable(repl) else repl
        out.append(r)
        ocols.extend([cols[m.start()]] * len(r))
        pos = m.end()
    out.append(text[pos:])
    ocols.extend(cols[pos:])
    return "".join(out), ocols


class Unit:
    """A run of prose to lint: one heading, table cell, or joined paragraph.

    `cols[i]` and `linenos[i]` map text[i] back to its raw column (0-based)
    and raw line (1-based), so a paragraph soft-wrapped over several lines is
    analyzed as one text while findings still point at the raw location.
    """
    __slots__ = ("lineno", "text", "cols", "kind", "linenos")

    def __init__(self, lineno, text, cols, kind, linenos=None):
        self.lineno = lineno
        self.text = text
        self.cols = cols
        self.kind = kind
        self.linenos = linenos if linenos is not None else [lineno] * len(text)

    def pos(self, off):
        """(line, col), both 1-based, of text[off]."""
        if not self.cols:
            return self.lineno, 1
        i = min(max(off, 0), len(self.cols) - 1)
        return self.linenos[i], self.cols[i] + 1

    def append(self, other):
        """Join `other` (the next soft-wrapped line) with a single space."""
        text, cols, linenos = self.text.rstrip(), self.cols, self.linenos
        keep = len(text)
        cols, linenos = cols[:keep], linenos[:keep]
        add = other.text.lstrip()
        if not add:
            self.text, self.cols, self.linenos = text, cols, linenos
            return
        skip = len(other.text) - len(add)
        if text:
            cols = cols + [cols[-1] + 1]
            linenos = linenos + [linenos[-1]]
            text += " "
        self.text = text + add
        self.cols = cols + other.cols[skip:]
        self.linenos = linenos + other.linenos[skip:]


def _make_unit(lineno, raw, start, kind, end=None):
    text = raw[start:end]
    cols = list(range(start, start + len(text)))
    for pattern, repl in CLEAN_PASSES:
        text, cols = sub_map(text, cols, pattern, repl)
    if kind == "heading":
        text, cols = sub_map(text, cols, re.compile(r"\s+#+\s*$"), "")
    return Unit(lineno, text, cols, kind)


def build_units(lines):
    """Turn masked lines into units: heading, list, table cell or paragraph.

    Consecutive prose lines of one paragraph (and the continuation lines of a
    list item) are joined into a single unit, so a soft-wrapped sentence is
    analyzed whole. A paragraph ends at a blank line, heading, list item
    start, fence, table row, or a change of blockquote nesting.
    """
    tables = _markdown_table_cells(lines)
    units = []
    list_indent = None
    prev_blank = True
    joinable = None  # (kind, in_quote) of units[-1] while the paragraph runs

    def add(unit, quote, can_join=False):
        nonlocal joinable
        if can_join and joinable == (unit.kind, quote):
            units[-1].append(unit)
        else:
            units.append(unit)
        joinable = (unit.kind, quote) if unit.kind in ("prose", "list") else None

    for idx, line in enumerate(lines):
        lineno = idx + 1
        if not line.strip():
            prev_blank = True
            joinable = None
            continue
        was_blank, prev_blank = prev_blank, False
        if idx in tables:
            list_indent = None
            joinable = None
            for cell, col in tables[idx]:
                if cell:
                    units.append(_make_unit(lineno, line, col, "table",
                                            col + len(cell)))
            continue
        if HRULE.match(line) or SETEXT.match(line) or REFDEF.match(line):
            joinable = None
            continue
        quote = BLOCKQUOTE.match(line)
        pos = quote.end() if quote else 0
        rest = line[pos:]
        in_quote = bool(quote)
        # Indented code block: 4+ spaces after a blank line, outside lists.
        if (not quote and list_indent is None and was_blank
                and (line.startswith("\t") or _leading_spaces(line) >= 4)):
            joinable = None
            continue
        if HEADING.match(rest):
            list_indent = None
            hm = HEADING.match(rest)
            add(_make_unit(lineno, line, pos + hm.end(), "heading"), in_quote)
            continue
        lm = LIST_ITEM_START.match(rest)
        if lm:
            list_indent = (len(lm.group("indent")) + len(lm.group("marker"))
                           + len(lm.group("gap")))
            start = pos + lm.start("body")
            tb = TASK_BOX.match(line[start:])
            if tb:
                start += tb.end()
            add(_make_unit(lineno, line, start, "list"), in_quote)
        elif list_indent is not None and _leading_spaces(rest) >= list_indent:
            add(_make_unit(lineno, line, pos, "list"), in_quote, can_join=True)
        else:
            list_indent = None
            add(_make_unit(lineno, line, pos, "prose"), in_quote, can_join=True)
    return units


def _dangling_conjunction_findings(lines, filename):
    """Lists whose item ends with and/or (및, 또는, 그리고, 혹은).

    `lines` are already masked (no fences, frontmatter or comments).
    """
    findings = []
    index = 0
    while index < len(lines):
        line = lines[index]
        start = LIST_ITEM_START.match(line)
        if not start:
            index += 1
            continue

        content_indent = (len(start.group("indent"))
                          + len(start.group("marker"))
                          + len(start.group("gap")))
        item_lines = [(index, start.group("body"))]
        next_index = index + 1
        while next_index < len(lines):
            candidate = lines[next_index]
            if not _is_list_continuation(candidate, content_indent):
                break
            item_lines.append((next_index, candidate))
            next_index += 1

        meaningful = []
        for line_index, item_line in item_lines:
            # Preserve code spans as neutral operands while ignoring their contents.
            cleaned = INLINE_CODE.sub(" CODE ", item_line).strip()
            if cleaned:
                meaningful.append((line_index, cleaned))
        if meaningful:
            end_line_index, end_line = meaningful[-1]
            conjunction = CONJUNCTION_END.search(end_line)
        else:
            end_line_index, end_line, conjunction = None, None, None
        if conjunction:
            if end_line_index == index:
                finding_line = index + 1
                finding_col = start.start("marker") + 1
            else:
                raw_end_line = next(
                    raw for line_index, raw in item_lines
                    if line_index == end_line_index
                )
                masked_end_line = INLINE_CODE.sub(
                    lambda match: " " * len(match.group(0)), raw_end_line
                )
                raw_conjunction = CONJUNCTION_END.search(masked_end_line)
                finding_line = end_line_index + 1
                finding_col = raw_conjunction.start() + 1 if raw_conjunction else 1
            if HANGUL.search(conjunction.group(0)):
                message = ("목록 항목이 접속어로 끝납니다. 항목을 끝맺거나 "
                           "다음 항목과 합치십시오.")
            else:
                message = ("List item ends with a coordinating conjunction. "
                           "Complete the item or join it with the next item.")
            findings.append({
                "file": filename,
                "line": finding_line,
                "col": finding_col,
                "rule": "dangling-conjunction",
                "level": "hard",
                "match": end_line,
                "message": message,
            })
        index = next_index
    return findings


# --------------------------------------------------------------------------
# Morphology (kiwipiepy, optional)
# --------------------------------------------------------------------------

_KIWI = {"obj": None, "tried": False, "version": None}
Tok = namedtuple("Tok", "form tag start end")


def _kiwi_version():
    try:
        from importlib.metadata import version
        return version("kiwipiepy")
    except Exception:
        return None


def get_kiwi():
    """Build Kiwi once, on first need. Returns None (with one notice) if absent."""
    if _KIWI["tried"]:
        return _KIWI["obj"]
    _KIWI["tried"] = True
    try:
        from kiwipiepy import Kiwi
        # Multi-word and typo dictionaries off, one worker: halves init time and memory (about 1.5 s to 0.75 s, 512 MB to 325 MB) with identical tokens on a 999-sentence sample.
        _KIWI["obj"] = Kiwi(load_multi_dict=False, load_typo_dict=False, num_workers=1)
        _KIWI["version"] = _kiwi_version()
    except Exception:  # ImportError, or a model/binary load failure
        print(NOTICE, file=sys.stderr)
    return _KIWI["obj"]


def morphology_label(enabled=True):
    if _KIWI["obj"] is not None:
        return f"kiwipiepy {_KIWI['version'] or '?'}"
    if enabled and not _KIWI["tried"]:
        ver = _kiwi_version()
        if ver:
            return f"kiwipiepy {ver}"
    return "regex fallback"


def kiwi_tokens(kiwi, s):
    out = []
    for t in kiwi.tokenize(s):
        out.append(Tok(unicodedata.normalize("NFC", t.form),
                       t.tag.split("-")[0], t.start, t.start + t.len))
    return out


def kiwi_split(kiwi, piece):
    """Sentence-split one Hangul-bearing piece with Kiwi; [(offset, text)]."""
    out = []
    for sent in kiwi.split_into_sents(piece):
        seg = piece[sent.start:sent.end]
        lead = len(seg) - len(seg.lstrip())
        if seg.strip():
            out.append((sent.start + lead, seg.strip()))
    return out or [(0, piece)]


def _word_span(s, a, b):
    """Expand [a, b) to the surrounding whitespace-delimited word(s)."""
    while a > 0 and not s[a - 1].isspace():
        a -= 1
    while b < len(s) and not s[b].isspace():
        b += 1
    return a, b


# --------------------------------------------------------------------------
# Glossary
# --------------------------------------------------------------------------

GLOSSARY_CANDIDATES = ("GLOSSARY.md", "docs/GLOSSARY.md", "docs/glossary.md")
_GLOSS_SEP = re.compile(r"^:?-+:?$")
# A Korean Avoid term ends at a non-Hangul char, end of text, or the start of
# a common particle or copula. Longer particles first; the lookahead only needs
# the start, so `CI 파이프` hits `CI 파이프를` but not `CI 파이프라인`.
_KO_PARTICLES = ("이다", "입니다", "이고", "이며", "에서", "에게", "으로",
                 "처럼", "보다", "까지", "부터", "하고", "이", "가", "을", "를",
                 "은", "는", "의", "에", "로", "와", "과", "도", "만")
_KO_AVOID_END = (r"(?:(?![가-힣])|(?=(?:" + "|".join(_KO_PARTICLES) + r")))")
# Characters that make an English term part of an identifier (node-a, a.b).
_ID_CHARS = "-_./:@"


def _ascii_term_re(term):
    return re.compile(r"(?<![A-Za-z0-9_])" + re.escape(term) + r"(?![A-Za-z0-9_])",
                      re.I)


def _identifier_like(text, start, end):
    """True when text[start:end] is one piece of an identifier-like token.

    A `-_/@` neighbor always joins it. A `.` or `:` joins it only when an
    alphanumeric follows (`token.refresh`), so a sentence-final `token.` or a
    label `token:` still counts as the bare term.
    """
    before = text[start - 1] if start > 0 else ""
    after = text[end] if end < len(text) else ""
    after2 = text[end + 1] if end + 1 < len(text) else ""
    if before and (before in _ID_CHARS or (before.isascii() and before.isalnum())):
        return True
    if after in "-_/@" and after:
        return True
    if after in ".:" and after and after2.isascii() and after2.isalnum():
        return True
    return bool(after and after.isascii() and after.isalnum())


class Glossary:
    def __init__(self, path):
        self.path = path
        self.entries = []   # dicts: en, ko, avoid, line
        self.problems = []  # glossary-duplicate findings
        self._avoid_res = []
        self._load()

    def _load(self):
        with open(self.path, encoding="utf-8") as fh:
            lines = fh.read().splitlines()
        cols = None
        for i, line in enumerate(lines):
            cells = _split_table_row(line)
            if cells is None:
                cols = None
                continue
            values = [c.replace("`", "").strip() for c, _ in cells]
            if cols is None:
                low = [v.lower() for v in values]
                if "english" in low and ("한국어" in low or "korean" in low):
                    ko_name = "한국어" if "한국어" in low else "korean"
                    cols = {"en": low.index("english"), "ko": low.index(ko_name),
                            "avoid": low.index("avoid") if "avoid" in low else None}
                    cols["pending_sep"] = True
                continue
            if cols.get("pending_sep"):
                cols["pending_sep"] = False
                if all(_GLOSS_SEP.match(v) for v in values):
                    continue
            if all(_GLOSS_SEP.match(v) for v in values if v):
                continue

            def cell(key):
                k = cols[key]
                return values[k] if k is not None and k < len(values) else ""
            en, ko = cell("en"), cell("ko")
            if not en or not ko:
                continue
            avoid = [a.strip() for a in re.split(r"[,，]", cell("avoid"))
                     if a.strip() and a.strip() not in ("-", "—")]
            self.entries.append({"en": en, "ko": ko, "avoid": avoid,
                                 "line": i + 1})
        self._check_duplicates()
        for e in self.entries:
            for a in e["avoid"]:
                if HANGUL.search(a):
                    rx = re.compile(r"(?<![가-힣])" + re.escape(a) + _KO_AVOID_END)
                    self._avoid_res.append((rx, a, e, True))
                else:
                    self._avoid_res.append((_ascii_term_re(a), a, e, False))

    def _problem(self, line, match, message):
        self.problems.append({"file": self.path, "line": line, "col": 1,
                              "rule": "glossary-duplicate", "level": "hard",
                              "match": match, "message": message})

    def _check_duplicates(self):
        by_en, by_ko = {}, {}
        for e in self.entries:
            en_k, ko_k = e["en"].casefold(), e["ko"].casefold()
            if en_k in by_en and by_en[en_k]["ko"].casefold() != ko_k:
                first = by_en[en_k]
                self._problem(e["line"], e["en"],
                              f"English term '{e['en']}' maps to two Korean terms: "
                              f"'{first['ko']}' (line {first['line']}) and '{e['ko']}'.")
            by_en.setdefault(en_k, e)
            if ko_k in by_ko and by_ko[ko_k]["en"].casefold() != en_k:
                first = by_ko[ko_k]
                self._problem(e["line"], e["ko"],
                              f"Korean term '{e['ko']}' maps to two English terms: "
                              f"'{first['en']}' (line {first['line']}) and '{e['en']}'.")
            by_ko.setdefault(ko_k, e)
        terms = set(by_en) | set(by_ko)
        for e in self.entries:
            for a in e["avoid"]:
                if a.casefold() in terms:
                    self._problem(e["line"], a,
                                  f"Avoid term '{a}' is also a glossary term. "
                                  "Remove it from Avoid or from the term columns.")

    def avoid_hits(self, sentence, is_ko):
        """Yield (index, match, avoid, entry) for Avoid terms in a sentence."""
        for rx, avoid, entry, hangul in self._avoid_res:
            if hangul and not is_ko:
                continue
            m = rx.search(sentence)
            if m:
                yield m.start(), m.group(0), avoid, entry

    def bare_english_hits(self, sentence):
        """English glossary terms in Korean text without their Korean term."""
        for e in self.entries:
            if e["ko"].casefold() == e["en"].casefold():
                continue
            if not re.search("[A-Za-z]", e["en"]):
                continue
            if e["ko"] in sentence:
                continue
            for m in _ascii_term_re(e["en"]).finditer(sentence):
                if _identifier_like(sentence, m.start(), m.end()):
                    continue
                yield m.start(), m.group(0), e
                break


def find_glossary(cwd=None):
    base = cwd or os.getcwd()
    for rel in GLOSSARY_CANDIDATES:
        p = os.path.join(base, rel)
        if os.path.isfile(p):
            return p
    return None


# --------------------------------------------------------------------------
# Linting
# --------------------------------------------------------------------------

def speech_class(sentence):
    t = re.sub(r"[\s.!?…\"'”’)\]}>*:~]+$", "", sentence)
    if re.search(r"(?:니다|니까|십시오|시오)$", t):
        return "합니다체"
    if t.endswith("요"):
        return "해요체"
    if t.endswith("다"):
        return "한다체"
    return None


class _Ctx:
    """Per-file lint state."""

    def __init__(self, filename, ko_max, en_max, glossary, kiwi):
        self.filename = filename
        self.ko_max = ko_max
        self.en_max = en_max
        self.glossary = glossary
        self.kiwi = kiwi
        self.findings = []
        self.seen_en = {}
        self.seen_ko = {}
        self.speech = []  # (class, lineno, col, match)

    def add(self, unit, off, rule, level, match, message):
        line, col = unit.pos(off)
        self.findings.append({"file": self.filename, "line": line,
                              "col": col, "rule": rule, "level": level,
                              "match": match, "message": message})


def _regex_pieces(text):
    pieces, pos = [], 0
    for m in EN_SPLIT.finditer(text):
        pieces.append((pos, text[pos:m.start()]))
        pos = m.end()
    pieces.append((pos, text[pos:]))
    return [(off, piece) for off, piece in pieces if piece.strip()]


def _split_sentences(text, kiwi):
    """Split a unit's text into [(offset, sentence)] with the upstream regex,
    refining Hangul-bearing pieces with Kiwi when available."""
    out = []
    for off, piece in _regex_pieces(text):
        if kiwi is not None and HANGUL.search(piece):
            for o, s in kiwi_split(kiwi, piece):
                out.append((off + o, s))
        else:
            lead = len(piece) - len(piece.lstrip())
            out.append((off + lead, piece.strip()))
    return out


def _lint_english_style(ctx, unit, off, s):
    """Advisory style rules for English prose (pstack `unslop` ideas)."""
    for m in AI_VOCABULARY.finditer(s):
        ctx.add(unit, off + m.start(), "ai-vocabulary", "advisory",
                m.group(0).strip(), AI_VOCABULARY_MSG)
    for pattern, replacement in FILLER_PHRASES:
        use = f"Use '{replacement}'." if replacement else "Delete it."
        for m in pattern.finditer(s):
            ctx.add(unit, off + m.start(), "filler-phrase", "advisory",
                    m.group(0), f"Filler phrase. {use}")
    for pattern, replacement in PLAIN_WORDS_EN:
        for m in pattern.finditer(s):
            ctx.add(unit, off + m.start(), "plain-word", "advisory",
                    m.group(0), f"Fancy word. Use '{replacement}'.")
    for m in FANCY_IS.finditer(s):
        ctx.add(unit, off + m.start(), "fancy-is", "advisory", m.group(0),
                "Fancy copula. Say 'is' or 'has'.")
    for m in CHATBOT_PHRASE.finditer(s):
        ctx.add(unit, off + m.start(), "chatbot-phrase", "advisory",
                m.group(0), "Chatbot phrase. Delete it and respond directly.")
    if unit.kind not in ("heading", "table"):
        for m in EM_DASH.finditer(s):
            ctx.add(unit, off + m.start(), "em-dash", "advisory",
                    m.group(0), "Em dash. End the sentence or use a comma.")
    for m in CURLY_QUOTE.finditer(s):
        ctx.add(unit, off + m.start(), "curly-quote", "advisory", m.group(0),
                "Use straight quotes.")


def _lint_arrow(ctx, unit, off, piece):
    """arrow-speak runs on regex-split pieces for both languages. A neighbor
    that is the inline-code placeholder (`CODE`) exempts the arrow."""
    if unit.kind in ("heading", "table"):
        return
    for m in ARROW.finditer(piece):
        left = re.search(r"(\w+)\s*$", piece[:m.start()])
        right = re.match(r"\s*(\w+)", piece[m.end():])
        if (left and left.group(1) == "CODE") or \
                (right and right.group(1) == "CODE"):
            continue
        msg = ("화살표 기호 대신 문장으로 관계를 쓰십시오."
               if HANGUL.search(piece)
               else "Symbol-speak. Write the relation as words.")
        ctx.add(unit, off + m.start(), "arrow-speak", "advisory",
                m.group(0).strip(), msg)


TITLE_CASE_MIN_WORDS = 3


def _title_case_findings(units, filename):
    """English headings where every word of 4+ letters is capitalized.

    Needs 3+ words and 2+ capitalized long words after the first, so a
    sentence-case heading with one proper noun ("Install Kafka now") passes.
    Acronyms, words with digits and the inline-code placeholder are ignored.
    """
    findings = []
    for unit in units:
        if unit.kind != "heading" or HANGUL.search(unit.text):
            continue
        words = unit.text.split()
        if len(words) < TITLE_CASE_MIN_WORDS:
            continue
        long_caps, ok = 0, True
        for i, w in enumerate(words):
            core = w.strip("\"'“”‘’()[]{}.,:;!?")
            letters = re.sub(r"[^A-Za-z]", "", core)
            if (len(letters) < 4 or re.search(r"[0-9_`/\\]", core)
                    or core.isupper()):
                continue
            if not core[:1].isupper():
                ok = False
                break
            if i:
                long_caps += 1
        if ok and long_caps >= 2:
            line, col = unit.pos(0)
            findings.append({
                "file": filename, "line": line, "col": col,
                "rule": "title-case-heading", "level": "advisory",
                "match": unit.text.strip(),
                "message": "Use sentence case for headings."})
    return findings


def _inline_header_findings(lines, filename):
    """`- **Label:** text` where the text opens with the label's first word.

    `lines` are masked (no fences, frontmatter or comments). The `**` marks
    are gone from unit text, so this reads the raw masked line.
    """
    findings = []
    for idx, line in enumerate(lines):
        m = INLINE_HEADER.match(line)
        if not m or HANGUL.search(line):
            continue
        label, text = m.group(1), m.group(2)
        key = re.match(r"[A-Za-z0-9]+", label.strip())
        first = re.match(r"[A-Za-z0-9]+", text)
        if key and first and key.group(0).casefold() == first.group(0).casefold():
            findings.append({
                "file": filename, "line": idx + 1, "col": m.start(1) - 1,
                "rule": "inline-header", "level": "advisory",
                "match": f"**{label.strip()}:**",
                "message": "Bold label restates the line. Write it as prose."})
    return findings


def _lint_english(ctx, unit, off, s):
    _lint_english_style(ctx, unit, off, s)
    for rule_id, level, pattern, msg in RULES:
        for m in pattern.finditer(s):
            if rule_id == "present-perfect" and MODAL_PERFECT_PREFIX.search(s[:m.start()]):
                continue
            ctx.add(unit, off + m.start(), rule_id, level, m.group(0), msg)
    for gi, group in enumerate(SYNONYM_GROUPS):
        for base in group:
            if (gi, base) in ctx.seen_en:
                continue
            m = _word_re(base).search(s)
            if m:
                ctx.seen_en[(gi, base)] = (unit, off + m.start(), m.group(0))
    n = len(s.split())
    if n > ctx.en_max and unit.kind != "heading":
        ctx.add(unit, off, "long-sentence", "hard", f"{n} words",
                f"Sentence has {n} words (cap {ctx.en_max}). Split it.")


def _lint_korean_regex(ctx, unit, off, s):
    """Regex fallbacks for the morphology-dependent rules."""
    for m in KO_DOUBLE_PASSIVE.finditer(s):
        a, b = _word_span(s, m.start(), m.end())
        ctx.add(unit, off + a, "ko-double-passive", "hard", s[a:b],
                "이중피동입니다. '~되어지다/보여지다'를 '~되다/보이다'로 줄이십시오.")
    for m in KO_MAKE_PASSIVE.finditer(s):
        a, b = _word_span(s, m.start(), m.end())
        _add_passive(ctx, unit, off, s, a, b)
    for m in KO_PASSIVE_RE.finditer(s):
        stem = m.group(1)
        if stem.endswith(SKIP_PASSIVE_NOUNS) or stem == "오래":
            continue
        if m.group(2) and m.group(2).startswith("받") and stem.endswith(RECEIVE_PREFIXES):
            continue
        if KO_DOUBLE_PASSIVE.match(s, m.start()) or \
                KO_DOUBLE_PASSIVE.search(s[m.start():m.end() + 4]):
            continue
        a, b = _word_span(s, m.start(), m.end())
        _add_passive(ctx, unit, off, s, a, b)
    hits = [m for m in GENITIVE_RE.finditer(s)
            if m.group(0) not in GENITIVE_STEM_WORDS]
    if len(hits) > GENITIVE_MAX:
        _genitive(ctx, unit, off, hits[0].end() - 1, len(hits))
    for m in KO_LIGHT_VERB_RE.finditer(s):
        a, b = _word_span(s, m.start(), m.end())
        ctx.add(unit, off + m.start(), "ko-light-verb", "hard", s[m.start():b], LIGHT_MSG)


# A passive inside a hedge frame ("해결된 것으로 보입니다") carries the
# writer's confidence. Rewriting it to active would change the claim.
HEDGE_FRAME_AFTER = re.compile(
    r"^[ㄴㄹ]?\s*(?:것(?:으로)?\s*(?:보이|보입|추정|판단|예상|생각)|것\s*같"
    r"|수(?:도)?\s*있)")


def _add_passive(ctx, unit, off, s, a, b):
    """Report a ko-passive at s[a:b] unless a hedge frame follows it."""
    if HEDGE_FRAME_AFTER.match(s[b:]):
        return
    ctx.add(unit, off + a, "ko-passive", "advisory", s[a:b], PASSIVE_MSG)


PASSIVE_MSG = ("행위자를 숨기는 피동입니다. 행위자를 주어로 쓰십시오"
               "(행위자를 모르거나 무관하면 유지).")


def _genitive(ctx, unit, off, at, count):
    ctx.add(unit, off + at, "ko-genitive-chain", "advisory", "의",
            f"'의'가 {count}번 이어집니다. 조사나 동사로 풀어 쓰십시오.")


def _lint_korean_morph(ctx, unit, off, s, toks):
    n = len(toks)
    jkg = [t for t in toks if t.tag == "JKG"]
    if len(jkg) > GENITIVE_MAX:
        _genitive(ctx, unit, off, jkg[0].start, len(jkg))
    double_at = set()
    for i, t in enumerate(toks):
        if t.tag == "VX" and t.form == "지" and i >= 2 and toks[i - 1].tag == "EC" \
                and toks[i - 1].form in PASSIVE_MARKERS:
            prev = toks[i - 2]
            a, b = _word_span(s, prev.start, t.end)
            if (prev.tag == "XSV" and prev.form == "되") or \
                    (prev.tag == "VV" and prev.form in PASSIVE_STEMS):
                double_at.add(i - 2)
                ctx.add(unit, off + a, "ko-double-passive", "hard", s[a:b],
                        "이중피동입니다. '~되어지다/보여지다'를 '~되다/보이다'로 줄이십시오.")
            elif prev.tag == "VV" and prev.form == "만들":
                double_at.add(i - 2)
                _add_passive(ctx, unit, off, s, a, b)
    for i, t in enumerate(toks):
        prev = toks[i - 1] if i else None
        if i in double_at:
            continue
        passive = False
        if t.tag == "XSV" and t.form == "되" and prev and prev.tag in ("NNG", "XR", "XSN"):
            passive = prev.form not in SKIP_PASSIVE_NOUNS
            nxt = toks[i + 1] if i + 1 < n else None
            nxt2 = toks[i + 2] if i + 2 < n else None
            # "-될 것이다 / -될 수 있다" is a prediction or hedge frame.
            if nxt and nxt.tag == "ETM" and nxt.form in FUTURE_ETM \
                    and nxt2 and nxt2.tag == "NNB" and nxt2.form in ("것", "수"):
                passive = False
        elif t.tag == "VV" and t.form in ("받", "당하") and prev and prev.tag == "NNG":
            passive = prev.form not in SKIP_PASSIVE_NOUNS
        if passive:
            a, b = _word_span(s, prev.start, t.end)
            _add_passive(ctx, unit, off, s, a, b)
    # light verbs: NOUN + 을/를 + 진행/실시/수행/시행 + 하, NOUN + 이/가 + 이루어지
    for i, t in enumerate(toks):
        if i < 1 or toks[i - 1].tag not in CONTENT_NOUNS:
            continue
        if t.tag == "JKO" and i + 2 < n and toks[i + 1].tag == "NNG" \
                and toks[i + 1].form in LIGHT_NOUNS \
                and toks[i + 2].tag == "XSV" and toks[i + 2].form == "하":
            a, b = _word_span(s, toks[i - 1].start, toks[i + 2].end)
            ctx.add(unit, off + a, "ko-light-verb", "hard", s[a:b], LIGHT_MSG)
        elif t.tag == "JKS" and i + 1 < n and toks[i + 1].tag == "VV" \
                and toks[i + 1].form in ("이루어지", "이뤄지"):
            a, b = _word_span(s, toks[i - 1].start, toks[i + 1].end)
            ctx.add(unit, off + a, "ko-light-verb", "hard", s[a:b], LIGHT_MSG)
    # noun stack (not on headings)
    if unit.kind != "heading":
        run, count, prev_tag = [], 0, None
        for t in toks + [Tok("", "END", len(s), len(s))]:
            if t.tag == "SN":
                continue  # a number is transparent: "2GB 이상" is one quantity
            if t.tag in NOUNISH:
                # A multi-word foreign name (Apache Kafka) is one noun.
                if not (t.tag == "SL" and prev_tag == "SL"):
                    count += 1
                run.append(t)
            else:
                if count > NOUN_STACK_MAX:
                    ctx.add(unit, off + run[0].start, "ko-noun-stack", "hard",
                            s[run[0].start:run[-1].end],
                            f"명사가 {count}개 이어집니다({NOUN_STACK_MAX}개까지). "
                            "조사나 절로 푸십시오.")
                run, count = [], 0
            prev_tag = t.tag
    # stacked adnominal clauses
    etms = [i for i, t in enumerate(toks)
            if t.tag == "ETM" and i + 1 < n and toks[i + 1].tag in CONTENT_NOUNS
            and not (i > 0 and toks[i - 1].tag == "VA")]
    if len(etms) > ADNOMINAL_MAX:
        a, b = _word_span(s, toks[etms[0]].start, toks[etms[0]].end)
        ctx.add(unit, off + a, "ko-adnominal-stack", "advisory", s[a:b],
                f"관형절이 {len(etms)}개 겹칩니다. 수식 범위가 모호해집니다. "
                "문장을 나누십시오.")


def _lint_korean(ctx, unit, off, s):
    if TILDE_RANGE.search(s):
        for m in TILDE_RANGE.finditer(s):
            ctx.add(unit, off + m.start(), "ko-tilde-range", "hard", m.group(0),
                    "숫자 사이의 ~는 취소선으로 읽히는 Markdown 렌더러가 많습니다. "
                    "'3-5개' 또는 '3개 이상 5개 이하'로 쓰십시오.")
    n = len(s.split())
    if n > ctx.ko_max and unit.kind != "heading":
        ctx.add(unit, off, "ko-long-sentence", "hard", f"{n} 어절",
                f"문장이 {n}어절입니다(상한 {ctx.ko_max}). 문장을 나누십시오.")
    if ctx.kiwi is not None:
        try:
            toks = kiwi_tokens(ctx.kiwi, s)
        except Exception:
            toks = None
    else:
        toks = None
    if toks is not None:
        _lint_korean_morph(ctx, unit, off, s, toks)
    else:
        _lint_korean_regex(ctx, unit, off, s)
    for pattern, suggestion in TRANSLATIONESE:
        for m in pattern.finditer(s):
            ctx.add(unit, off + m.start(), "ko-translationese", "advisory",
                    m.group(0).strip(),
                    f"번역투입니다. 이렇게 바꾸십시오: {suggestion}")
    for pattern, replacement in PLAIN_WORDS:
        for m in pattern.finditer(s):
            ctx.add(unit, off + m.start(), "ko-plain-word", "advisory",
                    m.group(0),
                    f"공문서투 한자어입니다. 이렇게 바꾸십시오: {replacement}")
    for m in AI_TELL.finditer(s):
        ctx.add(unit, off + m.start(), "ko-ai-tell", "advisory", m.group(0),
                "AI 상투 표현입니다. 틀을 풀고 내용을 바로 쓰십시오.")
    for m in KO_CATAPHORIC.finditer(s):
        ctx.add(unit, off + m.start(), "ko-ai-tell", "advisory", m.group(0),
                KO_CATAPHORIC_MSG)
    if unit.kind not in ("heading", "table"):
        for m in MIDDLE_DOT.finditer(s):
            ctx.add(unit, off + m.start(), "ko-middle-dot", "advisory",
                    m.group(0),
                    "가운뎃점 나열입니다. '와/과'나 쉼표로 풀어 쓰십시오.")
    for m in HONORIFIC_OBJECT.finditer(s):
        ctx.add(unit, off + m.start(), "ko-honorific-object", "advisory",
                m.group(0),
                "사물에 높임 '-시-'를 붙였습니다(사물존칭). '-시-'를 빼십시오.")
    for m in DOUBLE_NEGATION.finditer(s):
        ctx.add(unit, off + m.start(), "ko-double-negation", "advisory",
                m.group(0), "이중부정입니다. 긍정문으로 쓰십시오.")
    for m in KO_MARKETING.finditer(s):
        ctx.add(unit, off + m.start(), "ko-marketing", "hard", m.group(0),
                "근거 없는 품질 주장입니다. 지우거나 측정값으로 바꾸십시오.")
    for m in KO_VAGUE_QUANTITY.finditer(s):
        ctx.add(unit, off + m.start(), "ko-vague-quantity", "advisory",
                m.group(0).strip(),
                "모호한 수량입니다. 구체적인 수치와 이상/이하/초과/미만을 쓰십시오.")
    for gi, group in enumerate(KO_SYNONYM_GROUPS):
        for base in group:
            if (gi, base) in ctx.seen_ko:
                continue
            m = _ko_syn_re(base).search(s)
            if m:
                ctx.seen_ko[(gi, base)] = (unit, off + m.start(), base)
    if unit.kind == "prose":
        cls = speech_class(s)
        if cls:
            line, col = unit.pos(off)
            ctx.speech.append((cls, line, col, s[-12:], len(s)))


def _lint_dash(ctx, unit, off, piece):
    """ko-dash runs on regex-split pieces: Kiwi would split at the dash itself
    and hide it between two sentences."""
    if unit.kind in ("heading", "table") or not HANGUL.search(piece):
        return
    for m in DASH.finditer(piece):
        before, after = piece[:m.start()].rstrip()[-1:], piece[m.end():][:1]
        if before.isdigit() and after.isdigit():
            continue
        ctx.add(unit, off + m.start(), "ko-dash", "advisory",
                m.group(0).strip() or "-",
                "줄표로 문장을 덧대고 있습니다. 문장을 나누거나 쉼표, 콜론으로 쓰십시오.")


def _lint_glossary(ctx, unit, off, s, is_ko):
    g = ctx.glossary
    for idx, match, avoid, e in g.avoid_hits(s, is_ko):
        ctx.add(unit, off + idx, "glossary-avoid", "hard", match,
                f"'{avoid}' is listed under Avoid for '{e['en']}/{e['ko']}'. "
                f"Use '{e['ko']}' (Korean text) or '{e['en']}' (English text).")
    if is_ko:
        for idx, match, e in g.bare_english_hits(s):
            ctx.add(unit, off + idx, "glossary-bare-english", "advisory", match,
                    f"English term '{e['en']}' appears without its Korean term. "
                    f"Write '{e['ko']}' or '{e['ko']}({e['en']})' on first use.")


def lint(text, filename="<stdin>", *, ko_max=KO_MAX, en_max=EN_MAX,
         glossary=None, morph=True):
    raw_lines = text.splitlines()
    lines = mask_lines(raw_lines)
    units = build_units(lines)
    kiwi = get_kiwi() if morph and HANGUL.search("\n".join(lines)) else None
    ctx = _Ctx(filename, ko_max, en_max, glossary, kiwi)
    words_total = 0
    for unit in units:
        words_total += len(unit.text.split())
        for off, piece in _regex_pieces(unit.text):
            _lint_dash(ctx, unit, off, piece)
            _lint_arrow(ctx, unit, off, piece)
        for off, s in _split_sentences(unit.text, kiwi):
            is_ko = bool(HANGUL.search(s))
            for m in SEMICOLON.finditer(s):
                ctx.add(unit, off + m.start(), "semicolon", "hard", ";",
                        SEMICOLON_MSG_KO if is_ko else SEMICOLON_MSG_EN)
            if is_ko:
                _lint_korean(ctx, unit, off, s)
            else:
                _lint_english(ctx, unit, off, s)
            if glossary is not None:
                _lint_glossary(ctx, unit, off, s, is_ko)
    # synonym rotation: flag each member after the first, at its first occurrence
    for gi, group in enumerate(SYNONYM_GROUPS):
        present = [(ctx.seen_en[(gi, b)], b) for b in group if (gi, b) in ctx.seen_en]
        present.sort(key=lambda p: p[0][0].pos(p[0][1]))
        if len(present) > 1:
            first_base = present[0][1]
            for (unit, off, match), base in present[1:]:
                ctx.add(unit, off, "synonym-rotation", "hard", match,
                        f"'{base}' and '{first_base}' name the same action. "
                        "Pick one and use it every time.")
    for gi, group in enumerate(KO_SYNONYM_GROUPS):
        present = [(ctx.seen_ko[(gi, b)], b) for b in group if (gi, b) in ctx.seen_ko]
        present.sort(key=lambda p: p[0][0].pos(p[0][1]))
        if len(present) > 1:
            first_base = present[0][1]
            for (unit, off, match), base in present[1:]:
                ctx.add(unit, off, "ko-synonym-rotation", "hard", match,
                        f"'{base}'{josa(base, '과', '와')} '{first_base}'"
                        f"{josa(first_base, '은', '는')} 같은 대상을 가리킵니다. "
                        "하나를 골라 일관되게 쓰십시오.")
    # speech level: flag the first sentence of each minority class
    counts = {}
    first_idx = {}
    for i, (cls, *_rest) in enumerate(ctx.speech):
        counts[cls] = counts.get(cls, 0) + 1
        first_idx.setdefault(cls, i)
    if len(counts) > 1:
        major = max(counts, key=lambda c: (counts[c], -first_idx[c]))
        summary = ", ".join(f"{c} {counts[c]}" for c in ("합니다체", "해요체", "한다체")
                            if c in counts)
        for cls in sorted((c for c in counts if c != major), key=first_idx.get):
            _cls, lineno, col, match, _len = ctx.speech[first_idx[cls]]
            ctx.findings.append({
                "file": filename, "line": lineno, "col": col,
                "rule": "ko-speech-level", "level": "advisory", "match": match,
                "message": f"종결어미 등급이 섞였습니다({summary}). 하나로 맞추십시오."})
    ctx.findings.extend(_dangling_conjunction_findings(lines, filename))
    ctx.findings.extend(_title_case_findings(units, filename))
    ctx.findings.extend(_inline_header_findings(lines, filename))
    ctx.findings.sort(key=lambda f: (f["line"], f["col"]))
    return ctx.findings, words_total


def lint_file(text, path, glossary, glossary_resolved, **kw):
    """Lint one file. The loaded glossary file itself gets only
    glossary-duplicate (reported once from `glossary.problems`): its table
    rows pair synonyms on purpose, so no prose rule applies."""
    if glossary_resolved and glossary_resolved == os.path.realpath(path):
        return [], len(text.split())
    return lint(text, filename=path, glossary=glossary, **kw)


def report(findings, words_total, as_json, hard_count, baseline, morphology):
    rate = round(len(findings) * 100 / words_total, 1) if words_total else 0.0
    if as_json:
        print(json.dumps({"violations": findings, "count": len(findings),
                          "hard_count": hard_count, "baseline": baseline,
                          "words": words_total, "per_100_words": rate,
                          "morphology": morphology}, indent=2, ensure_ascii=False))
        return
    for f in findings:
        print(f"{f['file']}:{f['line']}:{f['col']} {f['rule']}: {f['message']} [{f['match']}]")
    print(f"\n{len(findings)} violations ({hard_count} hard, baseline {baseline}), "
          f"{words_total} words, {rate} per 100 words")
    print("Hedges/modality (may, might, could) are never flagged: confidence is content.")
    print("헤지(~ㄹ 수 있다, ~것 같다, ~로 보인다)는 지적하지 않습니다: 확신의 정도도 내용입니다.")
    print(f"morphology: {morphology}")


# --------------------------------------------------------------------------
# Self-test
# --------------------------------------------------------------------------

GLOSSARY_FIXTURE = """\
# Glossary

| English | 한국어 | Definition | Avoid |
|---|---|---|---|
| token | 토큰 | An opaque credential string. | 징표, 토컨 |
| rollback | 롤백 | Restore the previous release. | 되돌리기, revert |
| API | API | Keep as-is. | |
"""

GLOSSARY_DUP_FIXTURE = GLOSSARY_FIXTURE + """\
| Token | 토큰값 | Same English, second Korean. | |
| session | 토큰 | Same Korean, second English. | |
| cache | 캐시 | Avoid equals another term. | rollback |
"""


def _suite(morph):
    import tempfile
    use_kiwi = morph and get_kiwi() is not None

    def run(text, **kw):
        kw.setdefault("morph", morph)
        return lint(text, **kw)[0]

    def rules(text, **kw):
        return {f["rule"] for f in run(text, **kw)}

    bad = ("The panel is removed; spin up the job. "
           "Perform an analysis of the seamless log. "
           "We have received the report.")
    found = rules(bad)
    for expected in ("semicolon", "phrasal-verb", "nominalization",
                     "marketing-adjective", "passive-voice", "present-perfect"):
        assert expected in found, expected
    # hedges must never be flagged, including modal + perfect infinitive
    findings = run("The request may have failed. It could be a timeout. "
                   "The disk might have filled.")
    assert findings == [], findings
    # irregular participles: "has run" is a compound tense as much as "has failed"
    findings = run("The task has run. The job has set the flag. We have begun.")
    assert sum(1 for f in findings if f["rule"] == "present-perfect") == 3, findings
    findings = run("The job may have run.")
    assert not any(f["rule"] == "present-perfect" for f in findings), findings
    # Modal perfects remain protected across negation and variable whitespace.
    for modal in ("may", "might", "could", "should", "would", "must"):
        for gap in (" ", "  ", "\t", " not "):
            findings = run(f"The task {modal}{gap}have run.")
            assert not any(f["rule"] == "present-perfect" for f in findings), findings
    findings = run("The task couldn't have run. The task MAY NOT HAVE RUN.")
    assert not any(f["rule"] == "present-perfect" for f in findings), findings
    findings = run("The task has run. We have begun. The flag is set.")
    assert sum(f["rule"] == "present-perfect" for f in findings) == 2, findings
    assert any(f["rule"] == "passive-voice" for f in findings), findings
    findings = run("The task is gone.")
    assert not any(f["rule"] == "passive-voice" for f in findings), findings
    # code blocks skipped
    assert run("```\nx = a; y = b\n```") == []
    # all supported list markers, case variants, and trailing whitespace
    findings = run(
        "- Confirm the target and\n"
        "* Record the result OR  \n"
        "+ Close the panel\n"
        "1. Start the task and\n"
        "2) Stop the task OR"
    )
    dangling = [f for f in findings if f["rule"] == "dangling-conjunction"]
    assert len(dangling) == 4, dangling
    assert [f["line"] for f in dangling] == [1, 2, 4, 5], dangling
    assert [f["col"] for f in dangling] == [1, 1, 1, 1], dangling
    assert all(f["level"] == "hard" for f in dangling), dangling

    # valid continuation lines and standalone four-space code are ignored
    assert "dangling-conjunction" not in rules("  - Confirm the target and\n    record the result.")
    findings = run("- Confirm the target\n  and")
    dangling = [f for f in findings if f["rule"] == "dangling-conjunction"]
    assert len(dangling) == 1 and dangling[0]["line"] == 2, dangling
    assert dangling[0]["col"] == 3, dangling
    assert "dangling-conjunction" not in rules("    - code and")
    assert "dangling-conjunction" not in rules("> - Confirm the target and\n> - Record the result or")
    findings = run("- Do this and\n~~~\ncode and\n~~~")
    dangling = [f for f in findings if f["rule"] == "dangling-conjunction"]
    assert len(dangling) == 1 and dangling[0]["line"] == 1, dangling
    assert "dangling-conjunction" not in rules("```text\n- code and\n```")

    # one- and three-space markers and ordered continuation width
    assert "dangling-conjunction" not in rules(" - Start the task and\n   record the result.")
    assert "dangling-conjunction" not in rules("-  Start the task and\n   record the result.")
    assert "dangling-conjunction" not in rules("-\tStart the task and")
    findings = run("   - Start the task and", filename="fixture.md")
    dangling = [f for f in findings if f["rule"] == "dangling-conjunction"]
    assert len(dangling) == 1 and dangling[0]["col"] == 4, dangling
    assert dangling[0]["file"] == "fixture.md"
    assert dangling[0]["match"].endswith("and")
    assert "Complete the item" in dangling[0]["message"]
    findings = run("100. Start the task and\n  unrelated text")
    assert sum(f["rule"] == "dangling-conjunction" for f in findings) == 1, findings
    assert "dangling-conjunction" not in rules("- Start the task and.\n- Stop the task or,")
    assert "dangling-conjunction" not in rules("- Start the task and\n\n  record the result.")
    findings = run("- Parent item and\n  - Nested item or")
    dangling = [f for f in findings if f["rule"] == "dangling-conjunction"]
    assert [f["line"] for f in dangling] == [1, 2], dangling

    # ordinary prose, inline code, and fenced code are ignored
    assert "dangling-conjunction" not in rules("The process may include steps and")
    assert "dangling-conjunction" not in rules("- Use `and` as a label")
    assert "dangling-conjunction" not in rules("- Combine `left` and `right`")
    assert "dangling-conjunction" not in rules("~~~\n- code and\n~~~")
    assert "long-sentence" in rules(("word " * 30).strip() + ".")
    # Markdown table syntax is layout, not prose. Each cell stays lintable.
    short_cell = " ".join(f"term{number}" for number in range(1, 25)) + "."
    for table in (
            "| Label | Detail |\n| --- | --- |\n" f"| Clear | {short_cell} |",
            "Label | Detail\n--- | ---\n" f"Clear | {short_cell}"):
        findings, words_total = lint(table, morph=morph)
        assert not any(f["rule"] == "long-sentence" for f in findings), findings
        assert words_total == 27, words_total
    long_cell = " ".join(f"term{number}" for number in range(1, 27)) + "."
    findings = run("| Label | Detail |\n| --- | --- |\n" f"| Clear | {long_cell} |")
    long_sentences = [f for f in findings if f["rule"] == "long-sentence"]
    assert len(long_sentences) == 1, long_sentences
    assert long_sentences[0]["match"] == "26 words", long_sentences
    # synonym rotation: second member flagged, first named as the keeper
    findings = run("Check the config file. Then verify the output. Verify twice.")
    rot = [f for f in findings if f["rule"] == "synonym-rotation"]
    assert len(rot) == 1 and "'verify' and 'check'" in rot[0]["message"], rot
    assert "synonym-rotation" not in rules("Check the config. Check the output.")
    # per-file labels
    assert run("a; b", filename="x.md")[0]["file"] == "x.md"
    assert "semicolon" in rules("a; b")
    # --en-max is honored
    assert "long-sentence" in rules("one two three four five.", en_max=4)

    # ---- Korean: hedges are never flagged ----
    for hedge in ("요청이 실패했을 수도 있습니다.", "원인은 시간 초과일 것 같습니다.",
                  "디스크가 가득 찬 것으로 보입니다.",
                  "배포가 지연될 것으로 예상됩니다."):
        findings = run(hedge)
        assert findings == [], (hedge, findings)
    # double passive
    assert "ko-double-passive" in rules("파일이 삭제되어졌습니다.")
    assert "ko-double-passive" in rules("결과가 보여집니다.")
    assert "ko-double-passive" not in rules("결과가 보입니다.")
    assert "ko-double-passive" not in rules("서버가 파일을 삭제합니다.")
    assert "ko-passive" in rules("파일이 삭제됩니다.")
    assert "ko-passive" in rules("이 파일은 만들어집니다.")
    assert "ko-double-passive" not in rules("이 파일은 만들어집니다.")
    # light verb
    found = rules("서버 설정 파일 백업 작업을 진행합니다.")
    assert "ko-light-verb" in found, found
    assert ("ko-noun-stack" in found) == use_kiwi, found
    assert "ko-light-verb" in rules("점검이 이루어집니다.")
    assert "ko-light-verb" not in rules("서버가 백업합니다.")
    # adnominal stack (morph only)
    found = rules("사용자가 업로드한 이미지를 변환한 결과를 저장한 경로를 반환합니다.")
    assert ("ko-adnominal-stack" in found) == use_kiwi, found
    # tilde range, long sentence
    assert "ko-tilde-range" in rules("3~5개를 고릅니다.")
    assert "ko-tilde-range" in rules("3 ~ 5개를 고릅니다.")
    assert "ko-tilde-range" not in rules("3-5개를 고릅니다.")
    assert "ko-long-sentence" in rules(" ".join(["단어"] * 21) + "입니다.")
    assert "ko-long-sentence" not in rules(" ".join(["단어"] * 21) + "입니다.", ko_max=25)
    assert "semicolon" in rules("파일을 지웁니다; 로그를 지웁니다.")
    f = [f for f in run("파일을 지웁니다; 끝.") if f["rule"] == "semicolon"]
    assert f and "쌍반점" in f[0]["message"], f
    # translationese, double negation, marketing, vague quantity
    assert "ko-translationese" in rules("로그에 대한 설명을 읽습니다.")
    assert "ko-translationese" in rules("이 방법을 통해 해결합니다.")
    assert "ko-translationese" in rules("실패할 경우 다시 시도합니다.")
    assert "ko-translationese" in rules("서비스를 활성화시킵니다.")
    assert "ko-translationese" not in rules("서비스를 활성화합니다. 시키는 대로 합니다.")
    assert "ko-double-negation" in rules("확인하지 않을 수 없습니다.")
    # translationese additions
    for pos, neg in (("폭우로 인해 서버가 멈췄습니다.", "폭우 때문에 서버가 멈췄습니다."),
                     ("오류의 경우 다시 시도합니다.", "오류가 나면 다시 시도합니다."),
                     ("경고에도 불구하고 실행했습니다.", "경고가 떴지만 실행했습니다."),
                     ("이것은 실패에 다름 아닙니다.", "이것은 실패가 아닙니다."),
                     ("이 작업은 시간을 요합니다.", "이 작업은 시간이 필요합니다."),
                     ("규정에 의거하여 처리합니다.", "규정에 따라 처리합니다."),
                     ("서버가 서울에 위치합니다.", "서버가 서울에 있습니다."),
                     ("배포하기 위해 빌드합니다.", "빌드한 뒤 배포합니다.")):
        assert "ko-translationese" in rules(pos), pos
        assert "ko-translationese" not in rules(neg), neg
    # plain words
    for pos in ("금번 배포를 시작합니다.", "금일 배포합니다.", "익일 확인합니다.",
                "상기 내용을 확인하십시오.", "하기 사항을 읽으십시오.",
                "소정의 절차를 밟습니다.", "품질 제고에 힘씁니다.", "허가를 득하십시오.",
                "수정이 불가합니다.", "규칙을 숙지하십시오."):
        assert "ko-plain-word" in rules(pos), pos
    for neg in ("이번 배포를 시작합니다.", "이 설정은 하기 쉽습니다.",
                "수정이 불가능합니다.", "지연은 불가피합니다.",
                "상기된 얼굴로 답했습니다.", "허가를 받으십시오."):
        assert "ko-plain-word" not in rules(neg), neg
    # AI tells
    for pos in ("단순한 도구가 아니라 플랫폼입니다.", "중요한 점은 속도입니다.",
                "핵심은 속도라는 것입니다.", "이 기능은 배포를 가능하게 합니다.",
                "결론적으로 빠릅니다.", "경계를 넘어 세계로 나아갑니다.",
                "좋은 질문입니다. 답은 아니오입니다."):
        assert "ko-ai-tell" in rules(pos), pos
    for pos in ("로그로 확인한 사실은 이것입니다.", "결과는 이렇습니다:",
                "원인은 다음입니다.", "여기서부터는 설치입니다."):
        assert "ko-ai-tell" in rules(pos), pos
    for neg in ("문제는 이것으로 해결됩니다.", "이것은 다음입니다 라고 적습니다.",
                "이 도구는 빠릅니다.", "결과는 다음과 같습니다.",
                "속도가 중요합니다.", "이 기능은 배포를 쉽게 합니다."):
        assert "ko-ai-tell" not in rules(neg), neg
    # middle dot, dash
    assert "ko-middle-dot" in rules("읽기·쓰기 권한이 필요합니다.")
    assert "ko-middle-dot" not in rules("읽기와 쓰기 권한이 필요합니다.")
    assert "ko-middle-dot" not in rules("# 읽기·쓰기 권한")
    assert "ko-middle-dot" not in rules("| 항목 | 값 |\n|---|---|\n| 읽기·쓰기 | 있음 |")
    assert "ko-middle-dot" not in rules("`읽기·쓰기`를 씁니다.")
    for pos in ("서버가 멈췄습니다 — 원인은 디스크입니다.", "서버가 멈췄습니다 - 원인은 디스크입니다.",
                "서버가 멈췄습니다 -- 원인은 디스크입니다.", "서버가 멈췄습니다–원인은 디스크입니다."):
        assert "ko-dash" in rules(pos), pos
    for neg in ("3-5개를 고릅니다.", "범위는 3–5개입니다.", "범위는 3 - 5개입니다.",
                "react-joyride를 씁니다.", "- 파일을 지웁니다.", "# 설치 - 안내",
                "| 항목 | 값 |\n|---|---|\n| a - b | 있음 |"):
        assert "ko-dash" not in rules(neg), neg
    # genitive chain
    assert "ko-genitive-chain" in rules("사용자의 서버의 설정의 이력을 봅니다.")
    assert "ko-genitive-chain" not in rules("사용자의 서버 설정을 봅니다.")
    assert "ko-genitive-chain" not in rules("회의 정의 합의 논의 문의 내용을 확인합니다.")
    # honorific object
    for pos in ("결과가 나오셨습니다.", "재고가 품절이십니다.", "합계는 12,000원이십니다."):
        assert "ko-honorific-object" in rules(pos), pos
    for neg in ("손님이 오셨습니다.", "결과가 나왔습니다."):
        assert "ko-honorific-object" not in rules(neg), neg
    # soft-wrapped paragraphs are analyzed as one text
    wrapped_en = " ".join(f"w{n}" for n in range(1, 27))
    wrapped_en = "\n".join([" ".join(wrapped_en.split()[0:9]), " ".join(wrapped_en.split()[9:18]),
                            " ".join(wrapped_en.split()[18:])]) + "."
    findings = run(wrapped_en)
    longs = [f for f in findings if f["rule"] == "long-sentence"]
    assert len(longs) == 1 and longs[0]["line"] == 1 and longs[0]["match"] == "26 words", longs
    words_ko = ["단어"] * 20 + ["끝입니다."]
    wrapped_ko = "\n".join([" ".join(words_ko[0:7]), " ".join(words_ko[7:14]),
                            " ".join(words_ko[14:])])
    longs = [f for f in run(wrapped_ko) if f["rule"] == "ko-long-sentence"]
    assert len(longs) == 1 and longs[0]["line"] == 1 and longs[0]["match"] == "21 어절", longs
    assert not [f for f in run("첫 문장입니다.\n둘째 문장입니다.") if "long" in f["rule"]]
    assert run("First line is short.\nSecond line is short.") == []
    # columns and lines survive the join
    f = [f for f in run("서버가 멈췄습니다.\n그래서 파일을 삭제되어졌습니다; 끝.")
         if f["rule"] == "ko-double-passive"]
    assert f and (f[0]["line"], f[0]["col"]) == (2, 9), f
    f = [f for f in run("긴 설명 문장을 씁니다 그리고\n  이어서 3~5개를 고릅니다.")
         if f["rule"] == "ko-tilde-range"]
    assert f and (f[0]["line"], f[0]["col"]) == (2, 7), f
    f = [f for f in run("첫째 문장입니다\n둘째 문장입니다; 셋째.") if f["rule"] == "semicolon"]
    assert f and (f[0]["line"], f[0]["col"]) == (2, 9), f
    # list item continuation lines join into the item
    longs = [f for f in run("- " + "\n  ".join([" ".join(["단어"] * 7)] * 3) + " 끝입니다.")
             if f["rule"] == "ko-long-sentence"]
    assert len(longs) == 1 and longs[0]["line"] == 1, longs
    # a heading, list item or blank line ends the paragraph
    assert not [f for f in run("가나 다라 마바\n# 제목\n사아 자차 카타\n- 항목\n파하 가나 다라", ko_max=4)
                if f["rule"] == "ko-long-sentence"]
    # speech level across wrapped lines uses the sentence ending, not the wrap
    assert "ko-speech-level" not in rules("이 문장은 줄이 바뀌어도\n하나의 문장입니다.")
    for text in ("혁신적인 도구입니다.", "원활하게 동작합니다.", "원활한 배포입니다.",
                 "완벽하다.", "완벽히 동작합니다.",
                 "강력한 기능입니다.", "매끄러운 전환입니다.", "손쉽게 설치합니다.",
                 "놀라운 속도입니다.", "업계 최고 성능입니다."):
        assert "ko-marketing" in rules(text), text
    assert "ko-marketing" not in rules("강력 범죄를 다룹니다. 놀라지 않습니다.")
    assert "ko-vague-quantity" in rules("많은 파일을 지웁니다.")
    assert "ko-vague-quantity" in rules("일부 사용자는 실패합니다.")
    assert "ko-vague-quantity" not in rules("일부를 지웁니다.")
    # synonym rotation
    findings = run("파일을 삭제합니다. 그다음 로그를 제거합니다.")
    rot = [f for f in findings if f["rule"] == "ko-synonym-rotation"]
    assert len(rot) == 1 and "'삭제'" in rot[0]["message"] and rot[0]["match"] == "제거", rot
    assert "ko-synonym-rotation" not in rules("사용자가 도구를 사용합니다.")
    assert "ko-synonym-rotation" not in rules("파일을 삭제합니다. 로그를 삭제합니다.")
    # speech level
    findings = run("이 문서는 합니다체입니다. 이 문장은 한다체다.")
    sl = [f for f in findings if f["rule"] == "ko-speech-level"]
    assert len(sl) == 1 and sl[0]["col"] > 1 and "한다체 1" in sl[0]["message"], sl
    assert "ko-speech-level" not in rules("첫 문장입니다. 둘째 문장입니다.")
    assert "ko-speech-level" not in rules("- 합니다체입니다.\n- 한다체다.")
    # dangling Korean conjunction
    assert "dangling-conjunction" in rules("- 파일을 삭제하고 로그 및")
    # markdown handling
    assert run("```\n파일이 삭제되어졌습니다; 3~5개\n```") == []
    assert run("`a; b`를 실행합니다.") == []
    assert run("---\ntitle: 삭제; 제거 3~5\n---\n본문입니다.") == []
    assert run("<!-- 삭제; 제거 -->\n본문입니다.") == []
    findings = run("# 서버 설정 파일 백업 작업 안내")
    assert not any(f["rule"] in ("ko-noun-stack", "ko-long-sentence") for f in findings), findings
    findings = run("# " + " ".join(["단어"] * 30))
    assert not any(f["rule"] == "ko-long-sentence" for f in findings), findings
    f = [f for f in run("서버를 `a` 삭제되어졌습니다.") if f["rule"] == "ko-double-passive"]
    assert f and f[0]["col"] == 9, f

    # passive inside a hedge frame keeps the claim: no rewrite advice
    for hedge in ("CI 캐시 문제도 해결된 것으로 보입니다.",
                  "서버가 재시작된 것 같습니다.",
                  "문제가 해결된 것으로 판단합니다.",
                  "원인이 제거된 것으로 추정합니다.",
                  "배포가 완료된 것으로 예상합니다.",
                  "결함이 수정된 것으로 생각합니다.",
                  "캐시가 삭제될 수 있습니다.",
                  "캐시가 삭제될 수도 있습니다.",
                  "캐시가 삭제된 것 같습니다."):
        assert "ko-passive" not in rules(hedge), hedge
    assert "ko-passive" in rules("문제가 해결됩니다.")
    assert "ko-passive" in rules("캐시가 삭제된 파일을 복구합니다.")
    assert "ko-passive" in rules("문제가 해결된 후에 보입니다.")
    # ---- English style rules (pstack unslop ideas): pair each positive with a
    # negative; the hedge selftests above prove none fires on plain hedges ----
    for rule_id, pos, neg in (
            ("ai-vocabulary", "We delve into the log.", "We read the log."),
            ("ai-vocabulary", "This step is crucial.", "This step is required."),
            ("ai-vocabulary", "The fix underscores the cause.", "Use an underscore in the name."),
            ("ai-vocabulary", "It will showcase the result.", "It will print the result."),
            ("ai-vocabulary", "Teams foster trust.", "Teams build trust."),
            ("ai-vocabulary", "Additionally, the job retries.", "The job additionally retries."),
            ("filler-phrase", "In order to start, press the key.", "To start, press the key."),
            ("filler-phrase", "It failed due to the fact that disk is full.", "It failed because disk is full."),
            ("filler-phrase", "It is important to note that disk is full.", "Disk is full."),
            ("filler-phrase", "It's worth noting that disk is full.", "Disk is full."),
            ("filler-phrase", "In the event that it fails, retry.", "If it fails, retry."),
            ("filler-phrase", "At this point in time the job runs.", "The job runs now."),
            ("plain-word", "Utilize the cache.", "Use the cache."),
            ("plain-word", "We leverage the cache.", "The leverage of the lever is high."),
            ("plain-word", "It facilitates the build.", "It helps the build."),
            ("plain-word", "Numerous files fail.", "Many files fail."),
            ("fancy-is", "The file serves as the entry point.", "The file is the entry point."),
            ("fancy-is", "The tool boasts a fast start.", "The tool has a fast start."),
            ("chatbot-phrase", "I hope this helps.", "The fix is in the next line."),
            ("chatbot-phrase", "Let me know if it fails.", "Report a failure to the owner."),
            ("chatbot-phrase", "Great question. The answer is no.", "The answer is no."),
            ("chatbot-phrase", "Certainly! The answer is no.", "The answer is no."),
            ("chatbot-phrase", "You're absolutely right.", "The report is correct."),
            ("chatbot-phrase", "Happy to help.", "The answer is no."),
            ("em-dash", "The disk is full — delete a file.", "The disk is full, so delete a file."),
            ("em-dash", "The disk is full -- delete a file.", "Pass --force to the tool."),
            ("curly-quote", "Press “OK” to go on.", 'Press "OK" to go on.'),
            ("curly-quote", "It doesn’t run.", "It doesn't run."),
            ("arrow-speak", "Open Settings -> Network and save.", "Open Settings, then Network, and save."),
            ("arrow-speak", "Input => output.", "Input becomes output."),
            ("arrow-speak", "Input → output.", "Input becomes output."),
            ("arrow-speak", "설정 → 저장을 눕러야 합니다.",
             "설정에서 저장을 눕러야 합니다."),
            ("title-case-heading", "# Getting Started Guide", "# Getting started guide"),
            ("title-case-heading", "## How To Install Kafka Cluster", "## Install Kafka now"),
            ("inline-header", "- **Cache:** Cache the result.", "- **Cache:** Store the result."),
            ("inline-header", "- **Retry:** retry up to 3 times.", "- Retry up to 3 times.")):
        assert rule_id in rules(pos), (rule_id, pos)
        assert rule_id not in rules(neg), (rule_id, neg)
    # per-rule exclusions
    for text in ("| a | b |\n|---|---|\n| x — y | z |", "# Setup — notes",
                 "`a — b` is code.", "```\nx — y\n```"):
        assert "em-dash" not in rules(text), text
    assert "em-dash" not in rules("서버가 멈췄습니다 — 원인은 디스크입니다.")
    assert "curly-quote" not in rules("“안녕”이라고 말합니다.")
    for text in ("| a | b |\n|---|---|\n| x -> y | z |", "# Menu -> item guide",
                 "Run `a -> b` now.", "```\na -> b\n```", "Call ptr->next now.",
                 "Run `a` -> `b` now."):
        assert "arrow-speak" not in rules(text), text
    assert "title-case-heading" not in rules("# Setup Guide")
    assert "title-case-heading" not in rules("# Use the API Gateway CLI")
    assert "title-case-heading" not in rules("# 설치 Getting Started Guide")
    assert "title-case-heading" not in rules("Getting Started Guide")
    assert "inline-header" not in rules("- **Cache:** the cache is warm.\n".replace("the cache", "a store"))
    assert "inline-header" not in rules("- **Cache** Cache the result.")
    # `leverage` as a noun and `underscore` as a character stay clean
    assert not any(f["rule"] == "plain-word" for f in run("Financial leverage is high.")), "leverage noun"
    assert "ai-vocabulary" not in rules("The underscore is a valid character.")
    # Korean text is not routed to the English-only rules
    assert "ai-vocabulary" not in rules("이 단계는 crucial 합니다.")

    # ---- glossary ----
    with tempfile.TemporaryDirectory() as tmp:
        ok_path = os.path.join(tmp, "GLOSSARY.md")
        with open(ok_path, "w", encoding="utf-8") as fh:
            fh.write(GLOSSARY_FIXTURE)
        dup_path = os.path.join(tmp, "dup.md")
        with open(dup_path, "w", encoding="utf-8") as fh:
            fh.write(GLOSSARY_DUP_FIXTURE)
        g = Glossary(ok_path)
        assert len(g.entries) == 3 and g.problems == [], (g.entries, g.problems)
        assert g.entries[0]["avoid"] == ["징표", "토컨"], g.entries[0]
        d = Glossary(dup_path)
        msgs = [p["message"] for p in d.problems]
        assert len(msgs) == 3, msgs
        assert any("'Token' maps to two Korean" in m for m in msgs), msgs
        assert any("'토큰' maps to two English" in m for m in msgs), msgs
        assert any("Avoid term 'rollback'" in m for m in msgs), msgs
        assert all(p["level"] == "hard" and p["file"] == dup_path for p in d.problems)
        findings = run("징표를 갱신합니다.", glossary=g)
        av = [f for f in findings if f["rule"] == "glossary-avoid"]
        assert len(av) == 1 and "Use '토큰' (Korean text) or 'token' (English text)" in av[0]["message"], av
        assert "glossary-avoid" in rules("Do a revert now.", glossary=g)
        assert "glossary-avoid" not in rules("The reverted file is clean.", glossary=g)
        assert "glossary-bare-english" in rules("token을 갱신합니다.", glossary=g)
        assert "glossary-bare-english" not in rules("토큰(token)을 갱신합니다.", glossary=g)
        assert "glossary-bare-english" not in rules("API를 호출합니다.", glossary=g)
        assert "glossary-bare-english" not in rules("The token is stale.", glossary=g)
        assert "glossary-bare-english" not in rules("`token`을 갱신합니다.", glossary=g)
        assert "glossary-avoid" not in rules("징표를 갱신합니다.", glossary=None)
        # discovery order: GLOSSARY.md, docs/GLOSSARY.md, docs/glossary.md
        base = os.path.join(tmp, "proj")
        os.makedirs(os.path.join(base, "docs"))
        assert find_glossary(base) is None
        with open(os.path.join(base, "docs", "glossary.md"), "w") as fh:
            fh.write(GLOSSARY_FIXTURE)
        assert os.path.basename(find_glossary(base)) == "glossary.md"
        with open(os.path.join(base, "docs", "GLOSSARY.md"), "w") as fh:
            fh.write(GLOSSARY_FIXTURE)
        assert find_glossary(base).endswith(os.path.join("docs", "GLOSSARY.md"))
        with open(os.path.join(base, "GLOSSARY.md"), "w") as fh:
            fh.write(GLOSSARY_FIXTURE)
        assert find_glossary(base) == os.path.join(base, "GLOSSARY.md")

        # Korean Avoid right boundary: particle or end, not a longer word
        pipe_path = os.path.join(tmp, "pipe.md")
        with open(pipe_path, "w", encoding="utf-8") as fh:
            fh.write("| English | 한국어 | Avoid |\n|---|---|---|\n"
                     "| pipeline | 파이프라인 | CI 파이프 |\n")
        pg = Glossary(pipe_path)
        assert "glossary-avoid" not in rules("CI 파이프라인을 실행합니다.", glossary=pg)
        assert "glossary-avoid" not in rules("CI 파이프라인에서 실행합니다.", glossary=pg)
        for pos in ("CI 파이프를 실행합니다.", "CI 파이프가 실패합니다.",
                    "CI 파이프에서 실행합니다.", "CI 파이프입니다.",
                    "새 CI 파이프", "CI 파이프, 빌드 순서입니다.",
                    "CI 파이프처럼 동작합니다.", "CI 파이프의 순서를 봅니다."):
            assert "glossary-avoid" in rules(pos, glossary=pg), pos
        # bare English term: identifier-like tokens are not prose uses
        for neg in ("token-a를 갱신합니다.", "token_1을 갱신합니다.",
                    "token.refresh를 호출합니다.", "api/token/refresh를 호출합니다.",
                    "user@token을 갱신합니다.", "token:refresh를 호출합니다.",
                    "a-token을 갱신합니다.", "id.token을 갱신합니다."):
            assert "glossary-bare-english" not in rules(neg, glossary=g), neg
        for pos in ("token을 갱신합니다.", "새 token. 갱신합니다.",
                    "token: 갱신합니다.", "token-a와 token을 갱신합니다."):
            assert "glossary-bare-english" in rules(pos, glossary=g), pos
        # the loaded glossary file gets only glossary-duplicate
        syn_path = os.path.join(tmp, "syn.md")
        syn_text = ("| English | 한국어 | Definition | Avoid |\n|---|---|---|---|\n"
                    "| config | 설정 | A setting. | |\n"
                    "| setup | 세팅 | An install step. | |\n")
        with open(syn_path, "w", encoding="utf-8") as fh:
            fh.write(syn_text)
        sg = Glossary(syn_path)
        assert "ko-synonym-rotation" in rules(syn_text), "fixture must trip the rule"
        f, _w = lint_file(syn_text, syn_path, sg, os.path.realpath(syn_path), morph=morph)
        assert f == [], f
        f, _w = lint_file(syn_text, syn_path, sg, os.path.realpath(dup_path), morph=morph)
        assert any(x["rule"] == "ko-synonym-rotation" for x in f), f
        dup = Glossary(dup_path)
        assert dup.problems and all(p["rule"] == "glossary-duplicate" for p in dup.problems)
        f, _w = lint_file(GLOSSARY_DUP_FIXTURE, dup_path, dup, os.path.realpath(dup_path),
                          morph=morph)
        assert f == [], f


def selftest(morph=True):
    if morph and get_kiwi() is not None:
        _suite(True)
        _suite(False)
        print("selftest OK (morphology: kiwi)")
    else:
        _suite(False)
        print("selftest OK (morphology: regex)")


# --------------------------------------------------------------------------
# CLI
# --------------------------------------------------------------------------

def main(argv):
    ap = argparse.ArgumentParser(
        prog="ste-lint.py",
        description="Bilingual (Korean + English) structural STE linter.")
    ap.add_argument("files", nargs="*", metavar="FILE",
                    help="Markdown/text files; stdin when omitted")
    ap.add_argument("--json", action="store_true", help="machine-readable output")
    ap.add_argument("--baseline", type=int, default=0, metavar="N",
                    help="pass unless hard findings exceed N (default 0)")
    ap.add_argument("--disable", default="", metavar="r1,r2",
                    help="comma-separated rule ids to skip")
    ap.add_argument("--no-morph", action="store_true",
                    help="force the regex fallback for Korean morphology rules")
    ap.add_argument("--glossary", metavar="PATH", help="glossary Markdown table")
    ap.add_argument("--no-glossary", action="store_true",
                    help="disable glossary auto-discovery")
    ap.add_argument("--ko-max", type=int, default=KO_MAX, metavar="N",
                    help=f"Korean 어절 cap per sentence (default {KO_MAX})")
    ap.add_argument("--en-max", type=int, default=EN_MAX, metavar="N",
                    help=f"English word cap per sentence (default {EN_MAX})")
    ap.add_argument("--selftest", action="store_true", help="run built-in tests")
    args = ap.parse_args(argv)

    for stream in (sys.stdout, sys.stderr, sys.stdin):
        try:
            stream.reconfigure(encoding="utf-8")
        except Exception:
            pass

    if args.selftest:
        selftest(morph=not args.no_morph)
        return 0

    disabled = {r.strip() for r in args.disable.split(",") if r.strip()}
    morph = not args.no_morph

    for p in args.files:
        if not os.path.isfile(p):
            print(f"ste-lint: no such file: {p}", file=sys.stderr)
            return 2

    glossary = None
    gpath = args.glossary
    if gpath and not os.path.isfile(gpath):
        print(f"ste-lint: no such glossary: {gpath}", file=sys.stderr)
        return 2
    if not gpath and not args.no_glossary:
        gpath = find_glossary()
    if gpath:
        glossary = Glossary(gpath)
    gresolved = os.path.realpath(gpath) if gpath else None

    findings, words_total = [], 0
    if glossary is not None:
        findings.extend(glossary.problems)
    if args.files:
        for p in args.files:
            with open(p, encoding="utf-8") as fh:
                text = fh.read()
            f, w = lint_file(text, p, glossary, gresolved, ko_max=args.ko_max,
                             en_max=args.en_max, morph=morph)
            findings.extend(f)
            words_total += w
    else:
        f, w = lint(sys.stdin.read(), ko_max=args.ko_max, en_max=args.en_max,
                    glossary=glossary, morph=morph)
        findings.extend(f)
        words_total += w

    findings = [f for f in findings if f["rule"] not in disabled]
    hard_count = sum(1 for f in findings if f["level"] == "hard")
    report(findings, words_total, args.json, hard_count, args.baseline,
           morphology_label(morph))
    return 1 if hard_count > args.baseline else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
