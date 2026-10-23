# Stamp Math

Mailing stamp sheet, week, cost and time arithmetic. The 465 stamps at 20 stamps a sheet take 24 sheets, the last sheet holding 5 stamps.

## Named constants

None. Every number is the owner's own entry.

## What it computes

- **The sheets truth** - the stamps (1 to 1000000) divided by the stamps a sheet (1 to 1000), rounded up, with what the last sheet holds.
- **The weeks truth** - the stamps divided by the stamps used a week (1 to 100000), with the stamps left for the next week.
- **The cost truth** - the sheets (1 to 100000) times the sheet price ($0.01 to $999.99) to the cent, and spread over the stamps, half rounded up.
- **The time truth** - the stamps divided by the stamps stamped a minute (1 to 100), rounded up, in minutes and in hours and minutes.

## Boundary

Arithmetic only. Counting applied as written. It has not seen any stamp, sheet or envelope and does not know whether stamps will really stick, a post office will run out or a price will hold, and it gives no verdict that a sheet is worth its price or a stamp is right for a mailing. Every number is the owner's own entry.

## Files

- `index.html` - landing page with the boundary and starting examples.
- `app.html` - the calculator; every box recomputes on each keystroke.
- `engine.js` - the four truths, shared by the page and the tests.
- `oracle.py` - an independent Python re-implementation; writes `expected.json`.
- `test.js` - runs the engine against `expected.json` (99 cases, 20 error cases).

## Tests

```
python3 oracle.py
node test.js
```
