# Task: solve logic puzzles

Solve each puzzle below by reasoning. Every puzzle has exactly one solution. Work carefully; you
cannot run code. Give a complete answer for every puzzle even if unsure.

Output: write a single JSON object to the file D:\Puzzle-generation-with-guaranteed-uniqueness\data\llm_tasks\e3_solve\e3_zebra_haiku_017.out.json with this exact structure
{"answers": [{"id": "<puzzle id>", "answer": <answer>}, ...]}
where <answer> has the format stated for each puzzle.

The puzzles follow.


## Puzzle zebra-01458

Grid logic puzzle. Deduce which value of each category belongs to each house. Every value is used exactly once.

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- drink: water, coffee, cocoa, tea, juice
- job: baker, lawyer, pilot, doctor, teacher
- hobby: painting, golf, cooking, tennis, hiking
- color: blue, yellow, purple, green, white

Clues:
1. The person who drinks juice lives in the house just left of the one where the cocoa drinker lives.
2. The baker enjoys golf.
3. The person who enjoys tennis and the person in the yellow house live in adjacent houses.
4. The person who enjoys cooking lives in the house just left of the one where the doctor lives.
5. The person who drinks coffee lives in the middle house.
6. The lawyer lives immediately to the right of the cocoa drinker.
7. The person in the blue house lives directly to the left of the teacher.
8. The person who drinks tea either enjoys golf or enjoys painting.
9. The person who enjoys cooking and the teacher live two houses apart.
10. The doctor lives in the house just left of the one where the person in the white house lives.
11. The occupant of the green house is not the lawyer.
12. The cooking enthusiast and the occupant of the yellow house are neighbours.
13. The tea drinker lives in house 4.

Answer format for this puzzle: {"1": {"<category>": "<value>", ...}, "2": {...}, ...} -- one entry per house number, giving the value of every category.
