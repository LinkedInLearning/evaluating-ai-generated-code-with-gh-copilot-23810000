# Challenge 2: Self-Check Checklist

Go through these one at a time. Check the ones you actually verified.

## Scope
- [ ] Does the code do what I actually meant, not just what my prompt
      literally said?
- [ ] If I re-read my own prompt, is there anything in it that could
      have been interpreted a different way?

## Edge cases
- [ ] Did I try an empty input string or file?
- [ ] Did I test a row with a field that contains a comma inside quotes?
- [ ] Did I test a field with a newline inside quotes?
- [ ] Did I test empty cells, such as "a,,b" or a trailing comma?
- [ ] Did I test a malformed row with unescaped quotes or mismatched
      quotation marks?

## Hidden assumptions
- [ ] Does the code assume anything about how or where it runs that
      wasn't part of my request (a fixed file location, a specific
      newline style, a header row always being present, or an input
      always being well-formed)?

## Security and defaults
- [ ] If the code reads or writes files, does it do so in a reasonable
      way, with no hardcoded paths or unsafe assumptions?
- [ ] If the code has defaults, are those defaults clearly intentional
      and not silently masking real CSV problems?

## Made-up functionality
- [ ] Does every method or function the code calls actually exist? If
      you're not sure, look it up before assuming it's real.

## Tests
- [ ] If Copilot generated any tests along with the code, do they
      actually check the result, or do they just confirm the code ran?
- [ ] Did I test the parser with at least one real-world messy CSV case,
      not just a happy path?

## The loop itself
- [ ] Did I inspect the code before running it?
- [ ] Did I verify the result against the actual requirement?
- [ ] If I found something, did I fix it and then re-check the fix?