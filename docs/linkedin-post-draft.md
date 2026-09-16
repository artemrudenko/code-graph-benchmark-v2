# LinkedIn post draft

AI coding agents often look fast on the first task.

The slower part appears later. The agent reopens the same files, rediscovers
the same relationships, and can still miss one place where a change must be
made.

That costs more than tokens. It slows the route from an idea to a working
product, and it gives code review more ways to find an incomplete patch.

I wanted to know whether persistent code context could work as an agent’s
memory: less repeated navigation, with the same or better patch quality.

So I stopped asking “which code graph is best?” and tried a narrower question.
Could ordinary source navigation, Code Review Graph, or Serena complete real
product changes without losing behaviour?

I ran three fixed tasks in a Python and TypeScript product. Every condition had
five fresh agent sessions. A patch counted only when it met a source-derived
behaviour contract, its focused test passed, and that test failed again after I
deliberately reintroduced the defect.

The result did not produce a winner:

• On a shared access-rule fix and a small two-layout UI change, every condition
  passed 5 out of 5 times.
• On a harder change that had to carry one value through SQL, pagination,
  TypeScript, and two reader surfaces, ordinary source navigation passed 1 out
  of 5, Code Review Graph passed 1 out of 5, and Serena passed 0 out of 5.

For me, that is more useful than a ranking.

Structured context can give an agent a better starting point. It does not turn
an incomplete product contract into a safe change. A smaller answer helps only
when the patch still holds up under source checks and tests.

I also discarded an early batch when I found that its Git history accidentally
exposed the old solution. The benchmark was feeding the agent its own answer.
Fixing that mistake was part of the work, and part of the conclusion: claims
about agent memory need the same checks as claims about the code it changes.

The next question is the one I care about most: can a prepared index preserve
quality across a sequence of real tickets and then reduce the *total* repeated
work after setup and refresh costs?

I wrote up the method, evidence, limits, and a small testbench here:
**[replace with published DEV URL]**

What does your coding agent keep re-investigating in the same repository?

---

Editorial note: use `assets/images/cover-context-to-verified-change-linkedin.png` as the attachment. Add the final DEV URL before publishing. Keep this note out of the post.
