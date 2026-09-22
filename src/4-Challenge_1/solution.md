# Challenge 1: Example Solution

## The main bug: the split doesn't add back up to the total

Try `bill=100`, `tax=20`, `tip=25`, `people=7` and you'll get this output:

```
Tax: $20.00
Tip: $25.00
Total: $145.00
Each person pays: $20.71
```

Looks fine, except $20.71 x 7 = $144.97, which is three cents short of the actual
$145.00 total. The program rounds each person's share independently and
never checks whether those rounded shares still add up to the real bill.

This is a missed edge case: the code works whenever the total divides
evenly among the group, and breaks silently when it doesn't. Since
most real bills don't divide evenly, this isn't a rare corner case, but
rather closer to the common case.

### A fix

Round everyone's share the normal way, then add whatever's left over
(the difference between the sum of the rounded shares and the real
total) onto one person's payment so the numbers reconcile exactly:

```python
share = round(total / people, 2)
shares = [share] * people
shortfall = round(total - sum(shares), 2)
shares[-1] = round(shares[-1] + shortfall, 2)
```

Now `sum(shares)` always equals `total`, to the penny.

## Bonus: no handling for invalid input

Typing anything that isn't a number for the bill amount, tax, tip, or
number of people crashes the program with an unhandled `ValueError` and
a full traceback. A minimal fix is wrapping the input parsing in a
`try/except` and asking again instead of crashing:

```python
while True:
    try:
        bill = float(input("Bill amount: $"))
        break
    except ValueError:
        print("Please enter a number.")
```

This one wasn't the main focus of the challenge, but it's worth noticing
since it's the same underlying lesson: code that runs cleanly on the
input you tried isn't the same as code that's actually correct.