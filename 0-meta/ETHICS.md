# Research ethics and participant data

**Binding on humans and agents. Read before recording anyone.**

This project records interviews and sessions with ExRobotics engineers. That
creates real obligations — to the participants, to the company, and under GDPR
(the Netherlands, so the AVG applies). This file is the operating procedure.

## The one rule that matters

> **Identifiable participant data lives in `private/` and never leaves it.**
> Only pseudonymised, consent-cleared material enters a tracked file.

`private/` is gitignored in full. Nothing in it is ever committed, pasted into
a tracked document, quoted in Figma, or included in a deliverable.

### Agent rules — non-negotiable

1. **Never write a real name, employer-internal identifier, or contact detail
   into a tracked file.** Not in notes, not in commit messages, not in
   `3-insights/`, not in a Figma node, not in a screenshot caption.
2. **Never copy content out of `private/` into a tracked file** without an
   explicit anonymisation pass. Reading a transcript to analyse it is fine;
   moving text out of it is a deliberate, checked action.
3. **Do not send participant data to any external service.** No transcription
   API, no cloud summariser, no web search containing a quote, unless the user
   has explicitly approved that specific service for that specific data.
4. **If unsure whether something is identifying, treat it as identifying** and
   ask. In a company of this size, a role plus a project is often enough to
   identify someone.

## Layout

```
private/                          # gitignored, never committed
├── participants.csv              # THE key: real name ↔ P01. Nothing else holds this.
├── consent/                      # signed forms, one per participant
│   └── P01-consent-2026-09-03.pdf
└── raw/
    └── S01/                      # per study
        ├── P01-audio.m4a
        └── P01-transcript-verbatim.md

2-research/studies/S01/           # tracked
├── plan.md
├── sessions/
│   └── P01.md                    # pseudonymised notes + cleared quotes only
└── findings.md
```

`participants.csv` columns: `pseudonym, real_name, role, recruited, consent_signed, withdraw_deadline, notes`.

## Consent

Get it in writing, before recording, per participant. The form must state:

- **Who** is doing the research, for what, and who the client is (ExRobotics).
- **What is recorded** — audio, video, screen — and **why**.
- **Where recordings are stored**, who can access them, and for how long.
- **What is published or shared**, and in what form (pseudonymised excerpts).
- **The right to withdraw**, how to exercise it, and until when.
- **Contact details** for questions and withdrawal.

Two separate permissions, ticked separately — do not bundle them:

- [ ] I consent to being recorded.
- [ ] I consent to anonymised quotes being used in project documentation and
      the final handover to ExRobotics.

Ask again verbally at the start of the recording, on the recording. Note the
timestamp in `sessions/P0n.md`.

### The employment problem

Participants are employees of the client. Two consequences, and both need
saying out loud at recruitment:

- **Participation is voluntary and non-participation is invisible.** Their
  manager must not be told who took part or declined.
- **Nothing attributable to an individual goes back to the company.** Findings
  are reported in aggregate. If a participant says something critical about a
  colleague, a process, or management, it does not appear in a form that
  identifies them. This is the commitment most likely to be tested, so decide
  it now rather than under pressure at handover.

## Pseudonymisation

Applied at transcription, not later:

| Replace | With |
|---|---|
| Names | `P01`, `P02`, … (colleagues: `[colleague]`) |
| Customer or site names | `[customer site]` |
| Specific dates that pin an incident to a person | `[date]` |
| Distinctive role descriptions | Generalised: "an engineer who…" |
| Unique incidents identifiable internally | Generalise the detail, keep the mechanism |

Keep enough context for the finding to mean something. Over-anonymising to the
point of uselessness helps nobody — generalise the identifier, preserve the
mechanism.

**Before any quote enters a tracked file, ask:** could someone at ExRobotics
work out who said this? If plausibly yes, paraphrase or drop it.

## Retention

- Recordings: delete when the project closes, or 12 months from capture,
  whichever is sooner — unless the consent form states otherwise. State the
  actual period on the form and honour it.
- `participants.csv` and consent forms: keep until recordings are deleted,
  then delete the key.
- Pseudonymised notes and insights: retained; they carry no identifiers.

Log deletion in `6-log/decisions.md` when it happens.

## Withdrawal

If a participant withdraws: delete their raw data, remove their session file,
and re-check every insight that cited them. An insight resting only on a
withdrawn participant is withdrawn too. Note it in the study's `findings.md` —
the absence should be visible, not silently patched over.

## Transcription

Transcribing through a cloud service uploads identifiable audio to a third
party. Either:

- transcribe locally, or
- use a service the participant was told about **by name** on the consent form
  and that has an acceptable data-processing position.

Do not default to whatever is convenient. If in doubt, transcribe locally.

## Before the first session — checklist

- [ ] Consent form written, covering everything above
- [ ] Retention period decided and stated on the form
- [ ] Transcription route decided and named on the form
- [ ] `private/` confirmed gitignored (`git check-ignore -v private/test`)
- [ ] Recruitment framing agreed with ExRobotics: voluntary, non-attributed
- [ ] `participants.csv` created with no entries yet

## Scope note

This is a company project, not university research, so no ethics-committee
approval is in play. That lowers the procedural bar and not the ethical one —
the obligations above stand on their own. If the project later acquires an
academic component, revisit this file first.
