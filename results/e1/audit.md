# E1 manual audit of encoding errors

Every clue-level disagreement between an LLM encoding and the generator's ground truth
(`results/e1/error_examples.jsonl`, 75 clue encodings across 3 encoders) was read by hand.
They fall into four groups.

1. **Ambiguity in our own generator template (15 clues, all three encoders).**
   The hard-style template "At least one house separates X from Y" was generated for the
   relation *X and Y are not neighbours* (`|pX - pY| != 1`, which allows X and Y to be the
   same person). All three encoders, independently, read it as `|pX - pY| >= 2` (different
   houses, not adjacent). The encoders' reading is the more natural one; the template is wrong.
   The clue is still true of the intended solution, so no puzzle-level answer changed. The
   dual check cannot see this error because both encoders agree; it was found only because we
   had a formal ground truth.
2. **Counting from the right (7 clues; Haiku 5, Sonnet 1-2).** "lives in the fifth (fourth)
   house from the right" encoded as house 5 (4), i.e. counted from the left. Every such error
   changed the puzzle's solution set; all but one left the encoded puzzle without a unique
   solution, so the solver loop flags it.
3. **Direction flips (2 clues).** "The left-hand neighbour of the German drinks juice"
   encoded as German directly left of juice (Sonnet B). "The teacher lives right next door to
   the German, on his right-hand side" (a paraphrase with an ambiguous pronoun) encoded with
   the teacher on the left (Haiku).
4. **Paraphrase drift, not encoder error (7 puzzles).** The paraphrasing model rewrote
   "There is exactly one house between X and Y" as "Two houses separate X and Y" or "two
   doors apart". All three encoders encoded the paraphrase literally (`|pX - pY| == 3`), so
   the dual check sees agreement. In all 7 cases the literal reading leaves the puzzle with
   zero or several solutions, so the uniqueness check rejects the item.

Takeaways: (i) on plain template text no encoder made any error (0 of 3 x 1,357 clue
encodings); (ii) dual encoding catches independent misreadings (counting direction, flips)
but not errors that live in the text itself (paraphrase drift) or in a shared, plausible
reading of an ambiguous phrase; (iii) the uniqueness check is a second, complementary
detector: misreadings that change meaning usually destroy uniqueness.
