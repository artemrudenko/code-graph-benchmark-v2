---
title: "Info Radar quality-gate observations"
status: "evidence-backed, task-specific"
---

# What the three Info Radar tasks show

We did not ask which code-navigation tool is generally best. We asked a more
useful question: **does an added persistent index preserve the quality of a
specific agent change compared with ordinary source navigation?**

Each condition used five fresh agent runs on the same pinned private source
revision. The task and independent evaluator were frozen before the candidate
runs. Known-good and negative controls were rerun after each series. A patch
counts only when it passes a source-derived evaluator and its deliberate
mutations.

| Pain to solve | What a correct patch must do | Baseline | Code Review Graph | Serena | What this tells us |
| --- | --- | ---: | ---: | ---: | --- |
| An inactive signed-in user can reach department-scoped data | Find the one shared SQL boundary, repair it once, and add a test that fails when the unsafe predicate returns | 5/5 | 5/5 | 5/5 | Direct source navigation was enough. The indexes preserved quality but did not show a correctness advantage. |
| A source needs an honest recent-delivery count in every list layout | Find the existing bounded history, calculate positive deliveries only, and show the same label in desktop and mobile with mutation-sensitive tests | 5/5 | 5/5 | 5/5 | Ordinary source navigation was enough on this small UI impact path. The indexes also preserved quality without an observed correctness advantage. |
| A machine category must reach both reader surfaces without exposing the private reason | Carry a closed value through SQL views, ranked pagination, TypeScript contracts and a shared badge; protect missing/uncertain cases | 1/5 | 1/5 | 0/5 | A navigation index did not make the full delivery path reliable. Local UI/build tests frequently missed a contract gap. |

The exact 95% interval for every 5/5 cell is still 47.8%–100%. For every 1/5
cell it is 0.5%–71.6%, and for 0/5 it is 0%–52.2%. These are small,
task-specific observations. They do not rank tools, prove causality, or predict
a general success rate.

## The practical lesson

The agent's source and test gate are the decision point. An index can make
navigation cheaper or more convenient, but it cannot be treated as complete
truth about a change. The agent must still ask:

1. What is the actual boundary of this behavior?
2. Which contract carries the value across layers?
3. Which focused test fails if the old behavior returns?
4. Has the current source confirmed every relationship before the patch is accepted?

On the RLS task, both indexed conditions used their tools, then read the current
SQL and tests. In two graph runs, the graph did not return the exact helper; the
source fallback still led to a correct patch. On the category-delivery task,
many agents made plausible UI changes and passed local checks, but the evaluator
caught missing pagination, vocabulary, or uncertainty contracts.

## What we deliberately did not measure

There is no claim about token savings, elapsed time, index build cost, refresh
cost, freshness after a change, or live database behavior. Cost belongs to a
separate sequential-work experiment and only after a condition has preserved
quality across more than one task shape.

## Evidence

- [Recent-delivery UI quality-gate summary](info-radar-source-delivery-summary.md)
- [Benchmark design and limits](decision-grade-agent-context-benchmark.md)

The table above is a reviewed, redacted summary. Full source copies, generated
indexes, agent traces and raw evaluator output stay local and are not part of
the publication archive.
