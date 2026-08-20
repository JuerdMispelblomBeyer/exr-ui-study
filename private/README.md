# private/ — participant data. Not tracked.

Everything in this directory except this file is gitignored and must stay that
way. Raw recordings, verbatim transcripts, signed consent forms, and the
`participants.csv` name↔pseudonym key live here.

**Nothing in here is ever committed, quoted verbatim in a tracked file, or sent
to an external service.** See `0-meta/ETHICS.md` for the full procedure.

Expected layout:

```
participants.csv          # pseudonym, real_name, role, recruited, consent_signed, withdraw_deadline, notes
consent/                  # signed forms, one per participant
raw/S0n/                  # audio, video, verbatim transcripts, per study
```

Back this up somewhere encrypted. It is not in version control, so a disk
failure loses it permanently.
