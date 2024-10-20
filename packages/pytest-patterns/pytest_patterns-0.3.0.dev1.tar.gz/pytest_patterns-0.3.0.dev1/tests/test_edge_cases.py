from pathlib import Path

from pytest_patterns.plugin import PatternsLib

GENERIC_HEADER = [
    "String did not meet the expectations.",
    "",
    "🟢=EXPECTED | ⚪️=OPTIONAL | 🟡=UNEXPECTED | 🔴=REFUSED/UNMATCHED",
    "",
    "Here is the string that was tested: ",
    "",
]


def test_ical_ordering_produces_reasonable_reports(
    patterns: PatternsLib,
) -> None:
    with (Path(__file__).parent / "fixtures" / "ical-ordering.ical").open(
        "r"
    ) as f:
        test_data = f.read()

    # We used this pattern and got a weird match originally. Here's what
    # we expect it to look like:
    p = patterns.schedule
    p.in_order(
        """
BEGIN:VCALENDAR\r
VERSION:2.0\r
PRODID:-//fc.support//fcio//\r

BEGIN:VEVENT
SUMMARY:cedric (1\\, platform)
DTSTART;VALUE=DATE:20110201
DTEND;VALUE=DATE:20110201
DTSTAMP;VALUE=DATE-TIME:19700101T000140Z
UID:46f2574f64d22dc70db2379b08d83c0f51305c0729cb0d0e8852208b0deb4d87
END:VEVENT

BEGIN:VEVENT
SUMMARY:cedric (1\\, platform)
DTSTART;VALUE=DATE:20110202
DTEND;VALUE=DATE:20110202
DTSTAMP;VALUE=DATE-TIME:19700101T000140Z
UID:0b3f15fedfdf1c627afd2efd990b8c52e7f8822eebf62767e38b33cd5763d5c9
END:VEVENT

BEGIN:VEVENT
SUMMARY:cedric (1\\, platform)
DTSTART;VALUE=DATE:20110203
DTEND;VALUE=DATE:20110203
DTSTAMP;VALUE=DATE-TIME:19700101T000140Z
UID:a1d00464af0a25c9292aa72d0bf5236b5749d5e42c13e484080d2abbfb6ad89e
END:VEVENT

BEGIN:VEVENT
SUMMARY:cedric (1\\, platform)
DTSTART;VALUE=DATE:20110204
DTEND;VALUE=DATE:20110204
DTSTAMP;VALUE=DATE-TIME:19700101T000140Z
UID:4d6e48685c893ddf8856c8439f4d6bde05fbe603118fa68ebd7d3f37b4e3e6ed
END:VEVENT

BEGIN:VEVENT
SUMMARY:alice (1\\, platform)
DTSTART;VALUE=DATE:20110205
DTEND;VALUE=DATE:20110205
DTSTAMP;VALUE=DATE-TIME:19700101T000140Z
UID:31638940439cb48412420108cbb265a34baf2714075df401723bf82da0586743
END:VEVENT

BEGIN:VEVENT
SUMMARY:alice (1\\, platform)
DTSTART;VALUE=DATE:20110206
DTEND;VALUE=DATE:20110206
DTSTAMP;VALUE=DATE-TIME:19700101T000140Z
UID:8288d3266bf9cef59ddeafd8ec03d58bc0314dfe9e825617c9de90f856361eff
END:VEVENT

BEGIN:VEVENT
SUMMARY:alice (1\\, appops)
DTSTART;VALUE=DATE:20110201
DTEND;VALUE=DATE:20110201
DTSTAMP;VALUE=DATE-TIME:19700101T000140Z
UID:36a6983685c626a8255f480ec59930ea6f38a257ba79460982149461c733506a
END:VEVENT

BEGIN:VEVENT
SUMMARY:bob (2\\, appops)
DTSTART;VALUE=DATE:20110201
DTEND;VALUE=DATE:20110201
DTSTAMP;VALUE=DATE-TIME:19700101T000140Z
UID:42d5f543bdbb6f589bd19a893fd209fe89f4558c7be5ebcb93bcd12ba9ae9161
END:VEVENT

BEGIN:VEVENT
SUMMARY:alice (1\\, appops)
DTSTART;VALUE=DATE:20110202
DTEND;VALUE=DATE:20110202
DTSTAMP;VALUE=DATE-TIME:19700101T000140Z
UID:6db22f58ee442b51955546b6b617c2e39c07acc0a77b1dcc4230a04d63dc08a4
END:VEVENT

BEGIN:VEVENT
SUMMARY:bob (2\\, appops)
DTSTART;VALUE=DATE:20110202
DTEND;VALUE=DATE:20110202
DTSTAMP;VALUE=DATE-TIME:19700101T000140Z
UID:92100821b84973eccd2fb036c068bd405698af95e16f4420341940e5cc5ac148
END:VEVENT

BEGIN:VEVENT
SUMMARY:alice (1\\, appops)
DTSTART;VALUE=DATE:20110203
DTEND;VALUE=DATE:20110203
DTSTAMP;VALUE=DATE-TIME:19700101T000140Z
UID:bd1b1d019cfdff07456a7be437ecc6c7027f8c4ec6904e65c6f297a52f3eee14
END:VEVENT

BEGIN:VEVENT
SUMMARY:bob (2\\, appops)
DTSTART;VALUE=DATE:20110203
DTEND;VALUE=DATE:20110203
DTSTAMP;VALUE=DATE-TIME:19700101T000140Z
UID:becfafc6c131961b1d8913f3109aef3af1b6142bdbbc4e4642503fcd1cce05a6
END:VEVENT

BEGIN:VEVENT
SUMMARY:alice (1\\, appops)
DTSTART;VALUE=DATE:20110204
DTEND;VALUE=DATE:20110204
DTSTAMP;VALUE=DATE-TIME:19700101T000140Z
UID:834e1ddc937baae355d08f8960967466baab83f172d5f967a49083550cbd9e06
END:VEVENT

BEGIN:VEVENT
SUMMARY:bob (2\\, appops)
DTSTART;VALUE=DATE:20110204
DTEND;VALUE=DATE:20110204
DTSTAMP;VALUE=DATE-TIME:19700101T000140Z
UID:08e07e2b92b3fbb3264abd48e1aa1983962626902630beb6a5b4d5fece22a7da
END:VEVENT

BEGIN:VEVENT
SUMMARY:bob (1\\, appops)
DTSTART;VALUE=DATE:20110205
DTEND;VALUE=DATE:20110205
DTSTAMP;VALUE=DATE-TIME:19700101T000140Z
UID:16f138f3f88c54fe5a6e248de42f6a8e3a9b0c3f941c9f9c760b9aa639c1d457
END:VEVENT

BEGIN:VEVENT
SUMMARY:bob (1\\, appops)
DTSTART;VALUE=DATE:20110206
DTEND;VALUE=DATE:20110206
DTSTAMP;VALUE=DATE-TIME:19700101T000140Z
UID:0afbce38bf534b30031618c9a7c0f884b8ae69ccfe99d32753790edfab033405
END:VEVENT

END:VCALENDAR\r
"""
    )

    audit = p._audit(test_data)
    assert list(audit.report()) == [
        *GENERIC_HEADER,
        "🟢 schedule        | BEGIN:VCALENDAR",
        "🟢 schedule        | VERSION:2.0",
        "🟢 schedule        | PRODID:-//fc.support//fcio//",
        "🟢 schedule        | BEGIN:VEVENT",
        "🟡                 | SUMMARY:alice (1\\, appops)",
        "🟡                 | DTSTART;VALUE=DATE:20110201",
        "🟡                 | DTEND;VALUE=DATE:20110201",
        "🟡                 | DTSTAMP;VALUE=DATE-TIME:19700101T000140Z",
        "🟡                 | "
        "UID:36a6983685c626a8255f480ec59930ea6f38a257ba79460982149461c733506a",
        "🟡                 | END:VEVENT",
        "🟡                 | BEGIN:VEVENT",
        "🟡                 | SUMMARY:bob (2\\, appops)",
        "🟡                 | DTSTART;VALUE=DATE:20110201",
        "🟡                 | DTEND;VALUE=DATE:20110201",
        "🟡                 | DTSTAMP;VALUE=DATE-TIME:19700101T000140Z",
        "🟡                 | "
        "UID:42d5f543bdbb6f589bd19a893fd209fe89f4558c7be5ebcb93bcd12ba9ae9161",
        "🟡                 | END:VEVENT",
        "🟡                 | BEGIN:VEVENT",
        "🟡                 | SUMMARY:alice (1\\, appops)",
        "🟡                 | DTSTART;VALUE=DATE:20110202",
        "🟡                 | DTEND;VALUE=DATE:20110202",
        "🟡                 | DTSTAMP;VALUE=DATE-TIME:19700101T000140Z",
        "🟡                 | "
        "UID:6db22f58ee442b51955546b6b617c2e39c07acc0a77b1dcc4230a04d63dc08a4",
        "🟡                 | END:VEVENT",
        "🟡                 | BEGIN:VEVENT",
        "🟡                 | SUMMARY:bob (2\\, appops)",
        "🟡                 | DTSTART;VALUE=DATE:20110202",
        "🟡                 | DTEND;VALUE=DATE:20110202",
        "🟡                 | DTSTAMP;VALUE=DATE-TIME:19700101T000140Z",
        "🟡                 | "
        "UID:92100821b84973eccd2fb036c068bd405698af95e16f4420341940e5cc5ac148",
        "🟡                 | END:VEVENT",
        "🟡                 | BEGIN:VEVENT",
        "🟡                 | SUMMARY:alice (1\\, appops)",
        "🟡                 | DTSTART;VALUE=DATE:20110203",
        "🟡                 | DTEND;VALUE=DATE:20110203",
        "🟡                 | DTSTAMP;VALUE=DATE-TIME:19700101T000140Z",
        "🟡                 | "
        "UID:bd1b1d019cfdff07456a7be437ecc6c7027f8c4ec6904e65c6f297a52f3eee14",
        "🟡                 | END:VEVENT",
        "🟡                 | BEGIN:VEVENT",
        "🟡                 | SUMMARY:bob (2\\, appops)",
        "🟡                 | DTSTART;VALUE=DATE:20110203",
        "🟡                 | DTEND;VALUE=DATE:20110203",
        "🟡                 | DTSTAMP;VALUE=DATE-TIME:19700101T000140Z",
        "🟡                 | "
        "UID:becfafc6c131961b1d8913f3109aef3af1b6142bdbbc4e4642503fcd1cce05a6",
        "🟡                 | END:VEVENT",
        "🟡                 | BEGIN:VEVENT",
        "🟡                 | SUMMARY:alice (1\\, appops)",
        "🟡                 | DTSTART;VALUE=DATE:20110204",
        "🟡                 | DTEND;VALUE=DATE:20110204",
        "🟡                 | DTSTAMP;VALUE=DATE-TIME:19700101T000140Z",
        "🟡                 | "
        "UID:834e1ddc937baae355d08f8960967466baab83f172d5f967a49083550cbd9e06",
        "🟡                 | END:VEVENT",
        "🟡                 | BEGIN:VEVENT",
        "🟡                 | SUMMARY:bob (2\\, appops)",
        "🟡                 | DTSTART;VALUE=DATE:20110204",
        "🟡                 | DTEND;VALUE=DATE:20110204",
        "🟡                 | DTSTAMP;VALUE=DATE-TIME:19700101T000140Z",
        "🟡                 | "
        "UID:08e07e2b92b3fbb3264abd48e1aa1983962626902630beb6a5b4d5fece22a7da",
        "🟡                 | END:VEVENT",
        "🟡                 | BEGIN:VEVENT",
        "🟡                 | SUMMARY:bob (1\\, appops)",
        "🟡                 | DTSTART;VALUE=DATE:20110205",
        "🟡                 | DTEND;VALUE=DATE:20110205",
        "🟡                 | DTSTAMP;VALUE=DATE-TIME:19700101T000140Z",
        "🟡                 | "
        "UID:16f138f3f88c54fe5a6e248de42f6a8e3a9b0c3f941c9f9c760b9aa639c1d457",
        "🟡                 | END:VEVENT",
        "🟡                 | BEGIN:VEVENT",
        "🟡                 | SUMMARY:bob (1\\, appops)",
        "🟡                 | DTSTART;VALUE=DATE:20110206",
        "🟡                 | DTEND;VALUE=DATE:20110206",
        "🟡                 | DTSTAMP;VALUE=DATE-TIME:19700101T000140Z",
        "🟡                 | "
        "UID:0afbce38bf534b30031618c9a7c0f884b8ae69ccfe99d32753790edfab033405",
        "🟡                 | END:VEVENT",
        "🟡                 | BEGIN:VEVENT",
        "🟢 schedule        | SUMMARY:cedric (1\\, platform)",
        "🟢 schedule        | DTSTART;VALUE=DATE:20110201",
        "🟢 schedule        | DTEND;VALUE=DATE:20110201",
        "🟢 schedule        | DTSTAMP;VALUE=DATE-TIME:19700101T000140Z",
        "🟢 schedule        | "
        "UID:46f2574f64d22dc70db2379b08d83c0f51305c0729cb0d0e8852208b0deb4d87",
        "🟢 schedule        | END:VEVENT",
        "🟢 schedule        | BEGIN:VEVENT",
        "🟢 schedule        | SUMMARY:cedric (1\\, platform)",
        "🟢 schedule        | DTSTART;VALUE=DATE:20110202",
        "🟢 schedule        | DTEND;VALUE=DATE:20110202",
        "🟢 schedule        | DTSTAMP;VALUE=DATE-TIME:19700101T000140Z",
        "🟢 schedule        | "
        "UID:0b3f15fedfdf1c627afd2efd990b8c52e7f8822eebf62767e38b33cd5763d5c9",
        "🟢 schedule        | END:VEVENT",
        "🟢 schedule        | BEGIN:VEVENT",
        "🟢 schedule        | SUMMARY:cedric (1\\, platform)",
        "🟢 schedule        | DTSTART;VALUE=DATE:20110203",
        "🟢 schedule        | DTEND;VALUE=DATE:20110203",
        "🟢 schedule        | DTSTAMP;VALUE=DATE-TIME:19700101T000140Z",
        "🟢 schedule        | "
        "UID:a1d00464af0a25c9292aa72d0bf5236b5749d5e42c13e484080d2abbfb6ad89e",
        "🟢 schedule        | END:VEVENT",
        "🟢 schedule        | BEGIN:VEVENT",
        "🟢 schedule        | SUMMARY:cedric (1\\, platform)",
        "🟢 schedule        | DTSTART;VALUE=DATE:20110204",
        "🟢 schedule        | DTEND;VALUE=DATE:20110204",
        "🟢 schedule        | DTSTAMP;VALUE=DATE-TIME:19700101T000140Z",
        "🟢 schedule        | "
        "UID:4d6e48685c893ddf8856c8439f4d6bde05fbe603118fa68ebd7d3f37b4e3e6ed",
        "🟢 schedule        | END:VEVENT",
        "🟢 schedule        | BEGIN:VEVENT",
        "🟢 schedule        | SUMMARY:alice (1\\, platform)",
        "🟢 schedule        | DTSTART;VALUE=DATE:20110205",
        "🟢 schedule        | DTEND;VALUE=DATE:20110205",
        "🟢 schedule        | DTSTAMP;VALUE=DATE-TIME:19700101T000140Z",
        "🟢 schedule        | "
        "UID:31638940439cb48412420108cbb265a34baf2714075df401723bf82da0586743",
        "🟢 schedule        | END:VEVENT",
        "🟢 schedule        | BEGIN:VEVENT",
        "🟢 schedule        | SUMMARY:alice (1\\, platform)",
        "🟢 schedule        | DTSTART;VALUE=DATE:20110206",
        "🟢 schedule        | DTEND;VALUE=DATE:20110206",
        "🟢 schedule        | DTSTAMP;VALUE=DATE-TIME:19700101T000140Z",
        "🟢 schedule        | "
        "UID:8288d3266bf9cef59ddeafd8ec03d58bc0314dfe9e825617c9de90f856361eff",
        "🟢 schedule        | END:VEVENT",
        "🟡                 | END:VCALENDAR",
        "",
        "These are the unmatched expected lines: ",
        "",
        "🔴 schedule        | BEGIN:VEVENT",
        "🔴 schedule        | SUMMARY:alice (1\\, appops)",
        "🔴 schedule        | DTSTART;VALUE=DATE:20110201",
        "🔴 schedule        | DTEND;VALUE=DATE:20110201",
        "🔴 schedule        | DTSTAMP;VALUE=DATE-TIME:19700101T000140Z",
        "🔴 schedule        | "
        "UID:36a6983685c626a8255f480ec59930ea6f38a257ba79460982149461c733506a",
        "🔴 schedule        | END:VEVENT",
        "🔴 schedule        | BEGIN:VEVENT",
        "🔴 schedule        | SUMMARY:bob (2\\, appops)",
        "🔴 schedule        | DTSTART;VALUE=DATE:20110201",
        "🔴 schedule        | DTEND;VALUE=DATE:20110201",
        "🔴 schedule        | DTSTAMP;VALUE=DATE-TIME:19700101T000140Z",
        "🔴 schedule        | "
        "UID:42d5f543bdbb6f589bd19a893fd209fe89f4558c7be5ebcb93bcd12ba9ae9161",
        "🔴 schedule        | END:VEVENT",
        "🔴 schedule        | BEGIN:VEVENT",
        "🔴 schedule        | SUMMARY:alice (1\\, appops)",
        "🔴 schedule        | DTSTART;VALUE=DATE:20110202",
        "🔴 schedule        | DTEND;VALUE=DATE:20110202",
        "🔴 schedule        | DTSTAMP;VALUE=DATE-TIME:19700101T000140Z",
        "🔴 schedule        | "
        "UID:6db22f58ee442b51955546b6b617c2e39c07acc0a77b1dcc4230a04d63dc08a4",
        "🔴 schedule        | END:VEVENT",
        "🔴 schedule        | BEGIN:VEVENT",
        "🔴 schedule        | SUMMARY:bob (2\\, appops)",
        "🔴 schedule        | DTSTART;VALUE=DATE:20110202",
        "🔴 schedule        | DTEND;VALUE=DATE:20110202",
        "🔴 schedule        | DTSTAMP;VALUE=DATE-TIME:19700101T000140Z",
        "🔴 schedule        | "
        "UID:92100821b84973eccd2fb036c068bd405698af95e16f4420341940e5cc5ac148",
        "🔴 schedule        | END:VEVENT",
        "🔴 schedule        | BEGIN:VEVENT",
        "🔴 schedule        | SUMMARY:alice (1\\, appops)",
        "🔴 schedule        | DTSTART;VALUE=DATE:20110203",
        "🔴 schedule        | DTEND;VALUE=DATE:20110203",
        "🔴 schedule        | DTSTAMP;VALUE=DATE-TIME:19700101T000140Z",
        "🔴 schedule        | "
        "UID:bd1b1d019cfdff07456a7be437ecc6c7027f8c4ec6904e65c6f297a52f3eee14",
        "🔴 schedule        | END:VEVENT",
        "🔴 schedule        | BEGIN:VEVENT",
        "🔴 schedule        | SUMMARY:bob (2\\, appops)",
        "🔴 schedule        | DTSTART;VALUE=DATE:20110203",
        "🔴 schedule        | DTEND;VALUE=DATE:20110203",
        "🔴 schedule        | DTSTAMP;VALUE=DATE-TIME:19700101T000140Z",
        "🔴 schedule        | "
        "UID:becfafc6c131961b1d8913f3109aef3af1b6142bdbbc4e4642503fcd1cce05a6",
        "🔴 schedule        | END:VEVENT",
        "🔴 schedule        | BEGIN:VEVENT",
        "🔴 schedule        | SUMMARY:alice (1\\, appops)",
        "🔴 schedule        | DTSTART;VALUE=DATE:20110204",
        "🔴 schedule        | DTEND;VALUE=DATE:20110204",
        "🔴 schedule        | DTSTAMP;VALUE=DATE-TIME:19700101T000140Z",
        "🔴 schedule        | "
        "UID:834e1ddc937baae355d08f8960967466baab83f172d5f967a49083550cbd9e06",
        "🔴 schedule        | END:VEVENT",
        "🔴 schedule        | BEGIN:VEVENT",
        "🔴 schedule        | SUMMARY:bob (2\\, appops)",
        "🔴 schedule        | DTSTART;VALUE=DATE:20110204",
        "🔴 schedule        | DTEND;VALUE=DATE:20110204",
        "🔴 schedule        | DTSTAMP;VALUE=DATE-TIME:19700101T000140Z",
        "🔴 schedule        | "
        "UID:08e07e2b92b3fbb3264abd48e1aa1983962626902630beb6a5b4d5fece22a7da",
        "🔴 schedule        | END:VEVENT",
        "🔴 schedule        | BEGIN:VEVENT",
        "🔴 schedule        | SUMMARY:bob (1\\, appops)",
        "🔴 schedule        | DTSTART;VALUE=DATE:20110205",
        "🔴 schedule        | DTEND;VALUE=DATE:20110205",
        "🔴 schedule        | DTSTAMP;VALUE=DATE-TIME:19700101T000140Z",
        "🔴 schedule        | "
        "UID:16f138f3f88c54fe5a6e248de42f6a8e3a9b0c3f941c9f9c760b9aa639c1d457",
        "🔴 schedule        | END:VEVENT",
        "🔴 schedule        | BEGIN:VEVENT",
        "🔴 schedule        | SUMMARY:bob (1\\, appops)",
        "🔴 schedule        | DTSTART;VALUE=DATE:20110206",
        "🔴 schedule        | DTEND;VALUE=DATE:20110206",
        "🔴 schedule        | DTSTAMP;VALUE=DATE-TIME:19700101T000140Z",
        "🔴 schedule        | "
        "UID:0afbce38bf534b30031618c9a7c0f884b8ae69ccfe99d32753790edfab033405",
        "🔴 schedule        | END:VEVENT",
        "🔴 schedule        | END:VCALENDAR",
    ]
    assert not audit.is_ok()


def test_ical_with_multiple_patterns(patterns: PatternsLib) -> None:
    # This is a testing approach where we may have multiple orderings for the
    # same ical file and want to see it matched better
    p = patterns.schedule
    p.in_order(
        """
BEGIN:VCALENDAR\r
VERSION:2.0\r
PRODID:-//fc.support//fcio//\r

BEGIN:VEVENT
END:VEVENT

BEGIN:VEVENT
END:VEVENT

BEGIN:VEVENT
END:VEVENT

BEGIN:VEVENT
END:VEVENT

BEGIN:VEVENT
END:VEVENT

BEGIN:VEVENT
END:VEVENT

BEGIN:VEVENT
END:VEVENT

BEGIN:VEVENT
END:VEVENT

BEGIN:VEVENT
END:VEVENT

BEGIN:VEVENT
END:VEVENT

BEGIN:VEVENT
END:VEVENT

BEGIN:VEVENT
END:VEVENT

BEGIN:VEVENT
END:VEVENT

BEGIN:VEVENT
END:VEVENT

BEGIN:VEVENT
END:VEVENT

BEGIN:VEVENT
END:VEVENT

END:VCALENDAR\r
"""
    )

    p.continuous("""
BEGIN:VEVENT
SUMMARY:alice (1\\, appops)
DTSTART;VALUE=DATE:20110201
DTEND;VALUE=DATE:20110201
DTSTAMP;VALUE=DATE-TIME:19700101T000140Z
UID:36a6983685c626a8255f480ec59930ea6f38a257ba79460982149461c733506a
END:VEVENT
""")

    p.continuous("""
BEGIN:VEVENT
SUMMARY:cedric (1\\, platform)
DTSTART;VALUE=DATE:20110201
DTEND;VALUE=DATE:20110201
DTSTAMP;VALUE=DATE-TIME:19700101T000140Z
UID:46f2574f64d22dc70db2379b08d83c0f51305c0729cb0d0e8852208b0deb4d87
END:VEVENT
""")

    p.continuous("""
BEGIN:VEVENT
SUMMARY:cedric (1\\, platform)
DTSTART;VALUE=DATE:20110202
DTEND;VALUE=DATE:20110202
DTSTAMP;VALUE=DATE-TIME:19700101T000140Z
UID:0b3f15fedfdf1c627afd2efd990b8c52e7f8822eebf62767e38b33cd5763d5c9
END:VEVENT
""")

    p.continuous("""
BEGIN:VEVENT
SUMMARY:cedric (1\\, platform)
DTSTART;VALUE=DATE:20110203
DTEND;VALUE=DATE:20110203
DTSTAMP;VALUE=DATE-TIME:19700101T000140Z
UID:a1d00464af0a25c9292aa72d0bf5236b5749d5e42c13e484080d2abbfb6ad89e
END:VEVENT
""")

    p.continuous("""
BEGIN:VEVENT
SUMMARY:cedric (1\\, platform)
DTSTART;VALUE=DATE:20110204
DTEND;VALUE=DATE:20110204
DTSTAMP;VALUE=DATE-TIME:19700101T000140Z
UID:4d6e48685c893ddf8856c8439f4d6bde05fbe603118fa68ebd7d3f37b4e3e6ed
END:VEVENT
""")

    p.continuous("""
BEGIN:VEVENT
SUMMARY:alice (1\\, platform)
DTSTART;VALUE=DATE:20110205
DTEND;VALUE=DATE:20110205
DTSTAMP;VALUE=DATE-TIME:19700101T000140Z
UID:31638940439cb48412420108cbb265a34baf2714075df401723bf82da0586743
END:VEVENT
""")

    p.continuous("""
BEGIN:VEVENT
SUMMARY:alice (1\\, platform)
DTSTART;VALUE=DATE:20110206
DTEND;VALUE=DATE:20110206
DTSTAMP;VALUE=DATE-TIME:19700101T000140Z
UID:8288d3266bf9cef59ddeafd8ec03d58bc0314dfe9e825617c9de90f856361eff
END:VEVENT
""")

    p.continuous("""
BEGIN:VEVENT
SUMMARY:bob (2\\, appops)
DTSTART;VALUE=DATE:20110201
DTEND;VALUE=DATE:20110201
DTSTAMP;VALUE=DATE-TIME:19700101T000140Z
UID:42d5f543bdbb6f589bd19a893fd209fe89f4558c7be5ebcb93bcd12ba9ae9161
END:VEVENT
""")

    p.continuous("""
BEGIN:VEVENT
SUMMARY:alice (1\\, appops)
DTSTART;VALUE=DATE:20110202
DTEND;VALUE=DATE:20110202
DTSTAMP;VALUE=DATE-TIME:19700101T000140Z
UID:6db22f58ee442b51955546b6b617c2e39c07acc0a77b1dcc4230a04d63dc08a4
END:VEVENT
""")

    p.continuous("""
BEGIN:VEVENT
SUMMARY:bob (2\\, appops)
DTSTART;VALUE=DATE:20110202
DTEND;VALUE=DATE:20110202
DTSTAMP;VALUE=DATE-TIME:19700101T000140Z
UID:92100821b84973eccd2fb036c068bd405698af95e16f4420341940e5cc5ac148
END:VEVENT
""")

    p.continuous("""
BEGIN:VEVENT
SUMMARY:alice (1\\, appops)
DTSTART;VALUE=DATE:20110203
DTEND;VALUE=DATE:20110203
DTSTAMP;VALUE=DATE-TIME:19700101T000140Z
UID:bd1b1d019cfdff07456a7be437ecc6c7027f8c4ec6904e65c6f297a52f3eee14
END:VEVENT
""")

    p.continuous("""
BEGIN:VEVENT
SUMMARY:bob (2\\, appops)
DTSTART;VALUE=DATE:20110203
DTEND;VALUE=DATE:20110203
DTSTAMP;VALUE=DATE-TIME:19700101T000140Z
UID:becfafc6c131961b1d8913f3109aef3af1b6142bdbbc4e4642503fcd1cce05a6
END:VEVENT
""")

    p.continuous("""
BEGIN:VEVENT
SUMMARY:alice (1\\, appops)
DTSTART;VALUE=DATE:20110204
DTEND;VALUE=DATE:20110204
DTSTAMP;VALUE=DATE-TIME:19700101T000140Z
UID:834e1ddc937baae355d08f8960967466baab83f172d5f967a49083550cbd9e06
END:VEVENT
""")

    p.continuous("""
BEGIN:VEVENT
SUMMARY:bob (2\\, appops)
DTSTART;VALUE=DATE:20110204
DTEND;VALUE=DATE:20110204
DTSTAMP;VALUE=DATE-TIME:19700101T000140Z
UID:08e07e2b92b3fbb3264abd48e1aa1983962626902630beb6a5b4d5fece22a7da
END:VEVENT
""")

    p.continuous("""
BEGIN:VEVENT
SUMMARY:bob (1\\, appops)
DTSTART;VALUE=DATE:20110205
DTEND;VALUE=DATE:20110205
DTSTAMP;VALUE=DATE-TIME:19700101T000140Z
UID:16f138f3f88c54fe5a6e248de42f6a8e3a9b0c3f941c9f9c760b9aa639c1d457
END:VEVENT
""")

    p.continuous("""
BEGIN:VEVENT
SUMMARY:bob (1\\, appops)
DTSTART;VALUE=DATE:20110206
DTEND;VALUE=DATE:20110206
DTSTAMP;VALUE=DATE-TIME:19700101T000140Z
UID:0afbce38bf534b30031618c9a7c0f884b8ae69ccfe99d32753790edfab033405
END:VEVENT
""")

    with (Path(__file__).parent / "fixtures" / "ical-ordering.ical").open(
        "r"
    ) as f:
        test_data = f.read()
        assert p == test_data

    with (Path(__file__).parent / "fixtures" / "ical-ordering2.ical").open(
        "r"
    ) as f:
        test_data = f.read()
        assert p == test_data


def test_fc_qemu_output_unclear_reason_why_missing_matches(
    patterns: PatternsLib,
) -> None:
    data = """connect-rados machine=simplevm subsystem=ceph
pre-start machine=simplevm subsystem=ceph volume_spec=root
ensure-presence machine=simplevm subsystem=ceph volume_spec=root
lock machine=simplevm subsystem=ceph volume=rbd.ssd/simplevm.root
ensure-size machine=simplevm subsystem=ceph volume_spec=root
start machine=simplevm subsystem=ceph volume_spec=root
start-root machine=simplevm subsystem=ceph volume=rbd.ssd/simplevm.root
root-found-in current_pool=rbd.ssd machine=simplevm subsystem=ceph volume=rbd.ssd/simplevm.root
rbd args=status --format json rbd.ssd/simplevm.root machine=simplevm subsystem=ceph volume=rbd.ssd/simplevm.root
rbd>\t{"watchers":[{"address":"192.168.4.6:0/21401552","client":4167,"cookie":140282356059680}]}
rbd machine=simplevm returncode=0 subsystem=ceph volume=rbd.ssd/simplevm.root
migrate-vm-root-disk action=start machine=simplevm pool_from=rbd.ssd pool_to=rbd.hdd subsystem=ceph volume=rbd.ssd/simplevm.root
unlock machine=simplevm subsystem=ceph volume=rbd.ssd/simplevm.root
rbd args=migration prepare rbd.ssd/simplevm.root rbd.hdd/simplevm.root machine=simplevm subsystem=ceph volume=simplevm.root
rbd machine=simplevm returncode=0 subsystem=ceph volume=simplevm.root
pre-start machine=simplevm subsystem=ceph volume_spec=swap
delete-outdated-swap image=simplevm.swap machine=simplevm pool=rbd.ssd subsystem=ceph volume=simplevm.swap
ensure-presence machine=simplevm subsystem=ceph volume_spec=swap
lock machine=simplevm subsystem=ceph volume=rbd.hdd/simplevm.swap
ensure-size machine=simplevm subsystem=ceph volume_spec=swap
start machine=simplevm subsystem=ceph volume_spec=swap
start-swap machine=simplevm subsystem=ceph volume=rbd.hdd/simplevm.swap
rbd args=-c "/etc/ceph/ceph.conf" --id "host1" map "rbd.hdd/simplevm.swap" machine=simplevm subsystem=ceph volume=rbd.hdd/simplevm.swap
rbd>\t/dev/rbd0
rbd machine=simplevm returncode=0 subsystem=ceph volume=rbd.hdd/simplevm.swap
mkswap args=-f -L "swap" /dev/rbd/rbd.hdd/simplevm.swap machine=simplevm subsystem=ceph volume=rbd.hdd/simplevm.swap
mkswap>\tSetting up swapspace version 1, size = 50 MiB (52424704 bytes)
mkswap>\tLABEL=swap, UUID=b0f90aaa-a839-4da9-9acf-bad039e4c7e2
mkswap machine=simplevm returncode=0 subsystem=ceph volume=rbd.hdd/simplevm.swap
rbd args=-c "/etc/ceph/ceph.conf" --id "host1" unmap "/dev/rbd/rbd.hdd/simplevm.swap" machine=simplevm subsystem=ceph volume=rbd.hdd/simplevm.swap
rbd machine=simplevm returncode=0 subsystem=ceph volume=rbd.hdd/simplevm.swap
pre-start machine=simplevm subsystem=ceph volume_spec=tmp
delete-outdated-tmp image=simplevm.tmp machine=simplevm pool=rbd.ssd subsystem=ceph volume=simplevm.tmp
ensure-presence machine=simplevm subsystem=ceph volume_spec=tmp
lock machine=simplevm subsystem=ceph volume=rbd.hdd/simplevm.tmp
ensure-size machine=simplevm subsystem=ceph volume_spec=tmp
start machine=simplevm subsystem=ceph volume_spec=tmp
start-tmp machine=simplevm subsystem=ceph volume=rbd.hdd/simplevm.tmp
rbd args=-c "/etc/ceph/ceph.conf" --id "host1" map "rbd.hdd/simplevm.tmp" machine=simplevm subsystem=ceph volume=rbd.hdd/simplevm.tmp
rbd>\t/dev/rbd0
rbd machine=simplevm returncode=0 subsystem=ceph volume=rbd.hdd/simplevm.tmp
create-fs machine=simplevm subsystem=ceph volume=rbd.hdd/simplevm.tmp
sgdisk args=-o "/dev/rbd/rbd.hdd/simplevm.tmp" machine=simplevm subsystem=ceph volume=rbd.hdd/simplevm.tmp
sgdisk>\tCreating new GPT entries in memory.
sgdisk>\tThe operation has completed successfully.
sgdisk machine=simplevm returncode=0 subsystem=ceph volume=rbd.hdd/simplevm.tmp
sgdisk args=-a 8192 -n 1:8192:0 -c "1:tmp" -t 1:8300 "/dev/rbd/rbd.hdd/simplevm.tmp" machine=simplevm subsystem=ceph volume=rbd.hdd/simplevm.tmp
sgdisk>\tSetting name!
sgdisk>\tpartNum is 0
sgdisk>\tThe operation has completed successfully.
sgdisk machine=simplevm returncode=0 subsystem=ceph volume=rbd.hdd/simplevm.tmp
partprobe args=/dev/rbd/rbd.hdd/simplevm.tmp machine=simplevm subsystem=ceph volume=rbd.hdd/simplevm.tmp
partprobe machine=simplevm returncode=0 subsystem=ceph volume=rbd.hdd/simplevm.tmp
waiting interval=0 machine=simplevm remaining=4 subsystem=ceph volume=rbd.hdd/simplevm.tmp
mkfs.xfs args=-q -f -K -L "tmp" /dev/rbd/rbd.hdd/simplevm.tmp-part1 machine=simplevm subsystem=ceph volume=rbd.hdd/simplevm.tmp
mkfs.xfs machine=simplevm returncode=0 subsystem=ceph volume=rbd.hdd/simplevm.tmp
seed machine=simplevm subsystem=ceph volume=rbd.hdd/simplevm.tmp
mount args="/dev/rbd/rbd.hdd/simplevm.tmp-part1" "/mnt/rbd/rbd.hdd/simplevm.tmp" machine=simplevm subsystem=ceph volume=rbd.hdd/simplevm.tmp
mount machine=simplevm returncode=0 subsystem=ceph volume=rbd.hdd/simplevm.tmp
umount args="/mnt/rbd/rbd.hdd/simplevm.tmp" machine=simplevm subsystem=ceph volume=rbd.hdd/simplevm.tmp
umount machine=simplevm returncode=0 subsystem=ceph volume=rbd.hdd/simplevm.tmp
rbd args=-c "/etc/ceph/ceph.conf" --id "host1" unmap "/dev/rbd/rbd.hdd/simplevm.tmp" machine=simplevm subsystem=ceph volume=rbd.hdd/simplevm.tmp
rbd machine=simplevm returncode=0 subsystem=ceph volume=rbd.hdd/simplevm.tmp
rbd-status locker=None machine=simplevm subsystem=ceph volume=rbd.hdd/simplevm.root
rbd args=status --format json rbd.hdd/simplevm.root machine=simplevm subsystem=ceph volume=rbd.hdd/simplevm.root
rbd>\t{"watchers":[{"address":"192.168.4.6:0/21401552","client":4167,"cookie":140282356090848}],"migration":{"source_pool_name":"rbd.ssd","source_pool_namespace":"","source_image_name":"simplevm.root","source_image_id":"1047ad98be25","dest_pool_name":"rbd.hdd","dest_pool_namespace":"","dest_image_name":"simplevm.root","dest_image_id":"104b9066a6e5","state":"prepared","state_description":""}}
rbd machine=simplevm returncode=0 subsystem=ceph volume=rbd.hdd/simplevm.root
root-migration-status machine=simplevm pool_from=rbd.ssd pool_to=rbd.hdd progress= status=prepared subsystem=ceph volume=rbd.hdd/simplevm.root
rbd-status locker=('client.4167', 'host1') machine=simplevm subsystem=ceph volume=rbd.hdd/simplevm.swap
rbd-status locker=('client.4167', 'host1') machine=simplevm subsystem=ceph volume=rbd.hdd/simplevm.tmp"""

    first_start = patterns.first_start
    first_start.in_order(
        """
connect-rados machine=simplevm subsystem=ceph

pre-start machine=simplevm subsystem=ceph volume_spec=root
ensure-presence machine=simplevm subsystem=ceph volume_spec=root
lock machine=simplevm subsystem=ceph volume=rbd.ssd/simplevm.root
ensure-size machine=simplevm subsystem=ceph volume_spec=root
start machine=simplevm subsystem=ceph volume_spec=root
start-root machine=simplevm subsystem=ceph volume=rbd.ssd/simplevm.root
root-found-in current_pool=rbd.ssd machine=simplevm subsystem=ceph volume=rbd.ssd/simplevm.root
rbd args=status --format json rbd.ssd/simplevm.root machine=simplevm subsystem=ceph volume=rbd.ssd/simplevm.root
rbd>    {"watchers":[{"address":"192.168.4.6:0/...","client":4167,"cookie":...}]}
rbd machine=simplevm returncode=0 subsystem=ceph volume=rbd.ssd/simplevm.root

migrate-vm-root-disk action=start machine=simplevm pool_from=rbd.ssd pool_to=rbd.hdd subsystem=ceph volume=rbd.ssd/simplevm.root
unlock machine=simplevm subsystem=ceph volume=rbd.ssd/simplevm.root
rbd args=migration prepare rbd.ssd/simplevm.root rbd.hdd/simplevm.root machine=simplevm subsystem=ceph volume=simplevm.root
rbd machine=simplevm returncode=0 subsystem=ceph volume=simplevm.root

pre-start machine=simplevm subsystem=ceph volume_spec=swap
delete-outdated-swap image=simplevm.swap machine=simplevm pool=rbd.ssd subsystem=ceph volume=simplevm.swap
ensure-presence machine=simplevm subsystem=ceph volume_spec=swap
lock machine=simplevm subsystem=ceph volume=rbd.hdd/simplevm.swap
ensure-size machine=simplevm subsystem=ceph volume_spec=swap
start machine=simplevm subsystem=ceph volume_spec=swap
start-swap machine=simplevm subsystem=ceph volume=rbd.hdd/simplevm.swap
rbd args=-c "/etc/ceph/ceph.conf" --id "host1" map "rbd.hdd/simplevm.swap" machine=simplevm subsystem=ceph volume=rbd.hdd/simplevm.swap
rbd>    /dev/rbd0
rbd machine=simplevm returncode=0 subsystem=ceph volume=rbd.hdd/simplevm.swap
mkswap args=-f -L "swap" /dev/rbd/rbd.hdd/simplevm.swap machine=simplevm subsystem=ceph volume=rbd.hdd/simplevm.swap
mkswap> Setting up swapspace version 1, size = 50 MiB (52424704 bytes)
mkswap> LABEL=swap, UUID=...-...-...-...-...
mkswap machine=simplevm returncode=0 subsystem=ceph volume=rbd.hdd/simplevm.swap
rbd args=-c "/etc/ceph/ceph.conf" --id "host1" unmap "/dev/rbd/rbd.hdd/simplevm.swap" machine=simplevm subsystem=ceph volume=rbd.hdd/simplevm.swap
rbd machine=simplevm returncode=0 subsystem=ceph volume=rbd.hdd/simplevm.swap

pre-start machine=simplevm subsystem=ceph volume_spec=tmp
delete-outdated-tmp image=simplevm.tmp machine=simplevm pool=rbd.ssd subsystem=ceph volume=simplevm.tmp
ensure-presence machine=simplevm subsystem=ceph volume_spec=tmp
lock machine=simplevm subsystem=ceph volume=rbd.hdd/simplevm.tmp
ensure-size machine=simplevm subsystem=ceph volume_spec=tmp
start machine=simplevm subsystem=ceph volume_spec=tmp
start-tmp machine=simplevm subsystem=ceph volume=rbd.hdd/simplevm.tmp
rbd args=-c "/etc/ceph/ceph.conf" --id "host1" map "rbd.hdd/simplevm.tmp" machine=simplevm subsystem=ceph volume=rbd.hdd/simplevm.tmp
rbd>    /dev/rbd0
rbd machine=simplevm returncode=0 subsystem=ceph volume=rbd.hdd/simplevm.tmp
create-fs machine=simplevm subsystem=ceph volume=rbd.hdd/simplevm.tmp
sgdisk args=-o "/dev/rbd/rbd.hdd/simplevm.tmp" machine=simplevm subsystem=ceph volume=rbd.hdd/simplevm.tmp
sgdisk> Creating new GPT entries in memory.
sgdisk> The operation has completed successfully.
sgdisk machine=simplevm returncode=0 subsystem=ceph volume=rbd.hdd/simplevm.tmp
sgdisk args=-a 8192 -n 1:8192:0 -c "1:tmp" -t 1:8300 "/dev/rbd/rbd.hdd/simplevm.tmp" machine=simplevm subsystem=ceph volume=rbd.hdd/simplevm.tmp
sgdisk> Setting name!
sgdisk> partNum is 0
sgdisk> The operation has completed successfully.
sgdisk machine=simplevm returncode=0 subsystem=ceph volume=rbd.hdd/simplevm.tmp
partprobe args=/dev/rbd/rbd.hdd/simplevm.tmp machine=simplevm subsystem=ceph volume=rbd.hdd/simplevm.tmp
partprobe machine=simplevm returncode=0 subsystem=ceph volume=rbd.hdd/simplevm.tmp
waiting interval=0 machine=simplevm remaining=4 subsystem=ceph volume=rbd.hdd/simplevm.tmp
mkfs.xfs args=-q -f -K -L "tmp" /dev/rbd/rbd.hdd/simplevm.tmp-part1 machine=simplevm subsystem=ceph volume=rbd.hdd/simplevm.tmp
mkfs.xfs machine=simplevm returncode=0 subsystem=ceph volume=rbd.hdd/simplevm.tmp
seed machine=simplevm subsystem=ceph volume=rbd.hdd/simplevm.tmp
mount args="/dev/rbd/rbd.hdd/simplevm.tmp-part1" "/mnt/rbd/rbd.hdd/simplevm.tmp" machine=simplevm subsystem=ceph volume=rbd.hdd/simplevm.tmp
mount machine=simplevm returncode=0 subsystem=ceph volume=rbd.hdd/simplevm.tmp
umount args="/mnt/rbd/rbd.hdd/simplevm.tmp" machine=simplevm subsystem=ceph volume=rbd.hdd/simplevm.tmp
umount machine=simplevm returncode=0 subsystem=ceph volume=rbd.hdd/simplevm.tmp
rbd args=-c "/etc/ceph/ceph.conf" --id "host1" unmap "/dev/rbd/rbd.hdd/simplevm.tmp" machine=simplevm subsystem=ceph volume=rbd.hdd/simplevm.tmp
rbd machine=simplevm returncode=0 subsystem=ceph volume=rbd.hdd/simplevm.tmp

rbd-status locker=None machine=simplevm subsystem=ceph volume=rbd.hdd/simplevm.root
rbd args=status --format json rbd.hdd/simplevm.root machine=simplevm subsystem=ceph volume=rbd.hdd/simplevm.root
rbd>    {"watchers":[{"address":"192.168.4.6:0/...","client":...,"cookie":...}],"migration":{"source_pool_name":"rbd.ssd","source_pool_namespace":"","source_image_name":"simplevm.root","source_image_id":"...","dest_pool_name":"rbd.hdd","dest_pool_namespace":"","dest_image_name":"simplevm.root","dest_image_id":"...","state":"prepared","state_description":""}}
rbd machine=simplevm returncode=0 subsystem=ceph volume=rbd.hdd/simplevm.root
root-migration-status machine=simplevm pool_from=rbd.ssd pool_to=rbd.hdd progress= status=prepared subsystem=ceph volume=rbd.hdd/simplevm.root
rbd-status locker=('client...', 'host1') machine=simplevm subsystem=ceph volume=rbd.hdd/simplevm.swap
rbd-status locker=('client...', 'host1') machine=simplevm subsystem=ceph volume=rbd.hdd/simplevm.tmp
"""
    )

    assert data == first_start

    data = """\
rbd>      {"watchers":[{"address":"192.168.4.6:0/163915774","client":4167,"cookie":140008484817952}],"migration":{"source_pool_name":"rbd.ssd","source_pool_namespace":"","source_image_name":"simplevm.root","source_image_id":"1047ef14f18b","dest_pool_name":"rbd.hdd","dest_pool_namespace":"","dest_image_name":"simplevm.root","dest_image_id":"104bd3c88d4f","state":"prepared","state_description":""}}
"""

    p = patterns.unclear2
    p.in_order("""
rbd>      {"watchers":[{"address":"192.168.4.6:0/...","client":...,"cookie":...}],"migration":{"source_pool_name":"rbd.ssd","source_pool_namespace":"","source_image_name":"simplevm.root","source_image_id":"...","dest_pool_name":"rbd.hdd","dest_pool_namespace":"","dest_image_name":"simplevm.root","dest_image_id":"...","state":"prepared","state_description":""}}
""")
    assert p == data
