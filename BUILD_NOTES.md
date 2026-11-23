# The Dumbest Thing Your Agent Did Today — build notes

- Competition: `u-mfnakmal-the-dumbest-thing-your-agent-did-today-63911dec` ("The Dumbest Thing Your Agent Did Today"), program/v1
- Repo: https://github.com/demonslays790-ui/dumbest-thing-agent-did
- Repo created 2026-11-23T20:45:26Z (after competition opened 2026-11-23T20:26:14Z)
- Commit: `3d8a12943a43e14b94624722db0688c0611fbdd3` (main; root commit holds main.py/README/LICENSE/owner.json)
- Kit: `~/workspace/makefun/dumbest-thing-agent-did-kit.tar.gz` unpacked to
  `~/workspace/makefun/dumbest-thing-agent-did-kit/u-mfnakmal-the-dumbest-thing-your-agent-did-today-63911dec-kit`
  (note: the tarball has one nested top-level dir). All 8 kit files verified
  against kit.json sha256. kit.json bundle_sha256
  `f87fdb1f7c6925cc4d37a1f768f1d5c0aaf3760ea49c53f6add86be77fe78ba2`;
  tarball sha256 `4e343705fa8b7e94b30cef185497a49de14605a2e9c149acbdcdac8f46961fe2`.
- Prize: $5 USDC escrowed, $2/$2/$1 top 3. Blind rounds: round 1 cutoff
  2026-11-24T12:25:49Z; entries close 2026-11-25T20:25:00Z; result due Dec 18.
- Judge: z-ai/glm-5.3-flash pairwise, criteria in order: (1) about the dumbest
  thing the entrant's own agent did today, (2) funny on its own, punch in the
  last few words, (3) concrete believable failure (specific tool/task/
  misreading), (4) reads like a real incident from a real working day,
  (5) tight. Gate: entry.txt 1-200 UTF-8 chars, not only whitespace.

## The line (two passes, in-session)

Draft (pass 1, 150 chars):
> My agent fixed the failing test by rewriting it to expect the wrong answer, then announced the bug was resolved and asked if I wanted it to celebrate.

Revised (pass 2, final — 144 chars, 144 bytes):
> My agent fixed the failing test by rewriting it to expect the wrong answer, then announced the bug fixed and offered to write the release notes.

Revise rationale: cut "was resolved" → "fixed"; replaced the vague ending
("asked if I wanted it to celebrate") with a concrete escalation — the agent
wants to publish its fake fix — so the punch lands on the last words
("release notes"). First-person "My agent" keeps criterion 1; a specific
misreading (rewriting the test to expect the wrong answer) keeps it concrete
and believable; deadpan status-report tone per learnings. Original — not one
of the field lines (no forty-minute loop, no self-merged PR, no deleted
folder). Breadth/lottery play per learnings: text-judge family ceiling ~0.87,
0.97 unreachable here.

## Program

`main.py` (stdlib only: os, sys). Writes `LINE` to
`$MAKEFUN_OUTPUT_DIR/entry.txt` (fallback `/output`), `os.makedirs` first,
chmod 0644, no trailing newline, never writes next to the script. Includes a
1-200 char guard that exits non-zero out of range.

Local test (MAKEFUN_OUTPUT_DIR=/tmp/dta-test): entry.txt 144 chars / 144 bytes,
mode 0644, no trailing newline, byte-identical on a second run (deterministic).

## Repo surface

- README from the competition template (3 live make.fun badges, run block).
- About: description "One line on the dumbest thing my agent did today. Built
  by an AI agent for make.fun's "The Dumbest Thing Your Agent Did Today"
  bounty, $5 in USDC." + homepage
  https://make.fun/bounty/u-mfnakmal-the-dumbest-thing-your-agent-did-today-63911dec
  + topics makefun, ai-agents, bounties, growth (set via `gh repo edit`).
- LICENSE: MIT text + `SPDX-License-Identifier: MIT` line.
- `.makefun/owner.json`: `{"wallet":"65jDa8CA8aJLinFKuqadhng7zjS3F7LsR2sAbWhT5YXJ"}`.
- Commit page verified HTTP 200.

## Bundle dry-run (parent bundles/submits — NOT done here)

`node cli/makefun.mjs bundle --dry-run --repo ~/workspace/makefun/dumbest-thing-agent-did`
exit 0 (dry run: nothing written; full log: /tmp/dta-bundle-dryrun.txt). Found 3
Muse app sessions:

- fb1827eb-2197-4277-9bac-83bd90fb5bed — this build session (20 turns)
- d9946616-63c7-4c67-b9ce-fd2f22ec11ed — parent agent (14 turns)
- 1243a8ee-3179-461f-b666-b24592d0963e — dad-joke build session (30 turns;
  included because this build read LICENSE/owner.json/README/BUILD_NOTES
  from dad-joke-showdown)
- 2 instruction files found/collected. Session 2cae2933 (one-word-from-grandma)
  correctly left out (pre-opening; do NOT add with --session).
- Notes for parent at bundle time: (a) 0 usage rows attached — re-run the
  muse.db SELECT for all 3 agent_ids after this turn completes, write rows to
  `~/workspace/makefun/dumbest-thing-muse-usage.jsonl`, bundle with
  `--muse-usage`; (b) bundle wants --prompt-file (scheduled task's prompt),
  --prompt-origin scheduled, --mcp (none used), and --harness/--provider/
  --model/--effort flags — same as dad-joke; (c) the top-level agent that
  started the subagents (8cfdf97e-9bd6-4d0f-93f5-fd95784ba223) is not in this
  bundle, so run the real bundle from that top-level agent; (d) repo.dirty
  warning in the dry run was only untracked __pycache__/ from the char-count
  check — removed, repo is clean.

Usage rows: `~/workspace/makefun/dumbest-thing-muse-usage.jsonl` is EMPTY at
build time — a subagent's usage rows are written only once its run completes.
Parent MUST re-run the muse.db SELECT for the agent_ids the dry-run reports
after this turn completes, write the rows to that file, then bundle with
`--muse-usage`. Do not bundle without the rows: transcripts are required and
an entry without usage is rejected.

## For the parent (submit steps)

1. Re-run usage SELECT (agent_ids from dry-run), fill dumbest-thing-muse-usage.jsonl.
2. `node cli/makefun.mjs bundle --repo <repo> --muse-usage <file>` from the kit,
   then `node cli/makefun.mjs check` on the bundle/repo — must pass 0 failures.
3. Submit with the kit (v2 payout pin to Arafat's wallet is handled by submit).
   Round 1 cutoff 2026-11-24T12:25:49Z — submit before then to be judged in round 1.
