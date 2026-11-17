# E1 manual audit of encoding errors (final API run)

> Supersession note (2026-11-17): this file previously held the hand audit of the
> 2026-11-01 subagent-based run (75 clue encodings), whose numbers no longer match
> the final paper; that text is preserved in the repository's git history. This
> version audits the final Messages API run behind the reported results (call
> ledger `results/ledger.jsonl`). Status of every claim below: MEASURED, from
> `results/e1/error_examples.jsonl` and `results/e1/records.jsonl`.

Every clue-level disagreement between an LLM encoding and the generator's ground
truth (`results/e1/error_examples.jsonl`: 111 clue encodings - Sonnet A 30,
Sonnet B 29, Haiku C 52) was read by hand. They fall into six groups.

1. **Ambiguity in our own generator template (45 clue encodings = 15 puzzles x 3
   encoders, hard style).** The hard-style template "At least one house separates
   X from Y" was generated for the relation *X and Y are not neighbours*
   (`|pX - pY| != 1`). All three encoders, independently, read it as
   `|pX - pY| >= 2`. The encoders' reading is the more natural one; the template
   is wrong. The clue is still true of the intended solution, so no puzzle-level
   answer changed. 42 of the 45 clue encodings sit in puzzles whose encoding
   stayed equivalent to ground truth; the other 3 share their puzzles with a
   counting error (group 2) that broke them. Neither the dual check nor the
   uniqueness check can see this error: all encoders agree, and the clue holds of
   the ground-truth solution. It was found only because we had a formal ground
   truth.

2. **Counting from the right read as counting from the left (18 clue encodings:
   Haiku 17, Sonnet A 1, hard style).** "lives in the fifth (fourth) house from
   the right" was encoded as house 5 (4). Every one changed the encoded puzzle's
   solution set. 15 of the 18 left the encoded puzzle with 0 or 2 solutions, so
   the uniqueness check flags them on its own; the 3 clue encodings whose wrong
   encoding still had exactly one (different) solution were caught by the dual
   check, not by uniqueness.

3. **Direction flips (3 clue encodings, all Haiku).** One on plain template text
   (`plain:zebra-00080`: "somewhere to the left of" encoded as "to the right
   of"), one hard, one paraphrase. All three left the encoded puzzle with 0 or 2
   solutions. The plain one is Haiku's single error on plain text (1 of 3 x
   1,369 clue encodings).

4. **Paraphrase drift, not encoder error (9 clue encodings = 3 puzzles x 3
   encoders, paraphrase style).** The paraphrasing model rewrote "There is exactly
   one house between X and Y" as "Two houses separate X and Y" or "two doors
   apart". All three encoders encoded the paraphrase literally
   (`|pX - pY| == 3`), so the dual check sees agreement. Two of the three puzzles
   lost their unique solution under the literal reading and were rejected by the
   uniqueness check; the third, `paraphrase:zebra-00148`, kept exactly one
   solution - a different one - and passed both checks. It is the one wrong
   encoding the pipeline did not catch (Section 3.2 of the paper).

5. **Paraphrase reordering, "wrong entity" (33 clue encodings = 3 puzzles x 11
   clues per encoder, paraphrase style).** In three puzzles the paraphrase
   enumerated the clues in a different order, and the encoders bound values to
   the wrong clue. All three encoders erred identically, and the resulting
   encodings remained equivalent to ground truth (each puzzle kept its unique
   solution). These are clue-level disagreements only: they inflate the
   clue-level counts of Table 2 but not its puzzle-level error counts.

6. **Too-strong encodings (3 clue encodings, Haiku; 2 hard, 1 paraphrase).** The
   constraint was written stronger than the text; all three sat in puzzles whose
   encoding remained equivalent to ground truth.

Takeaways: (i) on plain template text only 1 of 3 x 1,369 clue encodings was
wrong (a Haiku direction flip); (ii) dual encoding catches independent
misreadings - every puzzle-pair case in which exactly one encoder erred (40 of
40) was flagged - but is blind to shared ones; (iii) the uniqueness check
rejected three of the four shared puzzle-level errors and missed only
`paraphrase:zebra-00148`; (iv) the generator's own template bug was invisible to
both checks and was found only against the formal ground truth.

Count check: Sonnet A 30 = 15 + 1 + 3 + 11; Sonnet B 29 = 15 + 3 + 11; Haiku C
52 = 15 + 17 + 3 + 3 + 11 + 3.
