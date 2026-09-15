# LinkedIn post draft

**Status:** Add the published DEV article URL before posting.

**Suggested attachment:** `assets/images/cover-context-to-verified-change-linkedin.png`. It works as a quiet visual anchor; the post itself carries the argument.

My coding agent could trace a relationship today, then reopen the same files and rediscover it in the next task.

At first I called that a token problem. It is also a navigation and working-memory problem. The questions repeat: who calls this code, what else changes with it, and which tests should I check?

I started testing persistent code context. The goal was not to name a winning tool. I wanted to know what an agent can safely reuse when it plans a change or a refactor.

The source checks were useful, but they were only half of the story. A short answer can still point to the wrong overload, include mostly test code, or come from an index that is already old.

So I added one small, repeatable change task in Next.js. I ran it twice with ordinary source navigation, twice with Code Review Graph, and twice with Serena. All six patches passed the same source check, focused test, mutation check, and diff boundary. There was no winner.

The useful rule was simpler: context can help an agent find the route. Current source and a test decide whether the change is safe. Token savings matter only after the patch is correct.

I wrote the method, examples, and a small testbench here: **[replace with published DEV URL]**

What question does your coding agent keep re-investigating in the same repository?
