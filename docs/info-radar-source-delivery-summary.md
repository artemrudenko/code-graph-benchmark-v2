---
title: "Recent-delivery UI task: redacted quality-gate summary"
status: "evidence-backed, task-specific"
---

# Can a code index improve a small two-layout UI change?

This was one bounded task in a private Python and TypeScript product. A Sources
screen already received a short history of runs. The requested change was to
show an honest recent-delivery count beside the health state in both the
desktop row and mobile card.

The calculation counted a run only when it loaded a positive number of items.
It had to keep missing observations out of the numerator, use the existing
bounded history, and render no meaningless count for an empty history.

## How the quality gate worked

I used five fresh agent sessions per condition:

| Condition | Result |
| --- | ---: |
| Ordinary source navigation | 5 / 5 accepted |
| Code Review Graph 2.3.3 | 5 / 5 accepted |
| Serena CLI 1.3.0 | 5 / 5 accepted |

The two indexed conditions made audited local navigation calls before editing:
12 for Code Review Graph and 13 for Serena across their five runs.

Each candidate started from the same synthetic, single-commit source fixture.
It had no copied Git history or staged diff. A known-good implementation had
to pass the evaluator. The untouched fixture and a calculation-only
implementation had to fail before and after the candidate series.

The evaluator checked the visible calculation with a hidden test, then ran the
candidate's own focused tests. It deliberately broke the positive-delivery
calculation and removed the label from each layout in turn. The candidate's
tests had to fail for all three mutations.

## What I learned

All three conditions produced correct patches for this small UI impact path.
The baseline did not need an index to find the shared calculation and two
layouts. Code Review Graph and Serena preserved that result, but did not show
an observed correctness advantage.

The exact two-sided 95% interval for every 5 / 5 result is still 47.8% to
100%. Five fresh sessions are not five independent human participants. This is
not a tool ranking, a causal result, or proof that the conditions have equal
quality.

## A fixture problem caught before counting

The first candidate batch was discarded before results were evaluated. Its
seed used an uncommitted inverse of a historical change, which made the removed
implementation visible in the staged Git diff. I rebuilt the fixture as a
single synthetic commit and reran all controls before the counted series.

This is part of the result: a benchmark must protect the task from its own
history. Otherwise it can accidentally measure whether an agent can recover a
patch instead of whether it can understand the current code.

## Limits

This task did not measure tokens, elapsed time, index build cost, refresh cost,
long-lived repeated work, production behaviour, or general frontend ability.
The product source, generated indexes, raw agent traces, and evaluator output
remain private. This page is a reviewed, redacted summary of the evidence.
