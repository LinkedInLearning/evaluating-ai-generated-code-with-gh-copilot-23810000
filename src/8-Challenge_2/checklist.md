# Challenge 2: Self-Check Checklist

Go through these one at a time. Check the ones you actually verified,
not the ones you assume are fine.

## Scope
- [ ] Does the code do what I actually meant, not just what my prompt
      literally said?
- [ ] If I re-read my own prompt, is there anything in it that could
      have been interpreted a different way?

## Edge cases
- [ ] Did I try an empty input, or the very first action being "quit"
      before entering anything?
- [ ] Did I try a negative number or a zero where a normal amount was
      expected?
- [ ] Did I try something that isn't a number at all where a number was
      expected?

## Hidden assumptions
- [ ] Does the code assume anything about how or where it runs that
      wasn't part of my request (a fixed file location, a specific
      order of actions, always running fresh with no prior data)?

## Security and defaults
- [ ] If the code stores or writes anything, does it do so in a
      reasonable way, with no hardcoded values that should be
      configurable?

## Made-up functionality
- [ ] Does every method or function the code calls actually exist? If
      you're not sure, look it up before assuming it's real.

## Tests
- [ ] If Copilot generated any tests along with the code, do they
      actually check the result, or do they just confirm the code ran?

## The loop itself
- [ ] Did I inspect the code before running it, not just after?
- [ ] Did I verify the result against the actual requirement, not just
      against "it didn't crash"?
- [ ] If I found something, did I fix it and then re-check the fix?