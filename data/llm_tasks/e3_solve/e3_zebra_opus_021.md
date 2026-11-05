# Task: solve logic puzzles

Solve each puzzle below by reasoning. Every puzzle has exactly one solution. Work carefully; you
cannot run code. Give a complete answer for every puzzle even if unsure.

Output: write a single JSON object to the file D:\Puzzle-generation-with-guaranteed-uniqueness\data\llm_tasks\e3_solve\e3_zebra_opus_021.out.json with this exact structure
{"answers": [{"id": "<puzzle id>", "answer": <answer>}, ...]}
where <answer> has the format stated for each puzzle.

The puzzles follow.


## Puzzle zebra-01430

Grid logic puzzle. Deduce which value of each category belongs to each house. Every value is used exactly once.

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- drink: water, juice, milk, cocoa, tea
- hobby: hiking, painting, cooking, tennis, chess
- job: teacher, lawyer, farmer, baker, pilot
- nationality: Spaniard, Norwegian, Brit, German, Swede

Clues:
1. The person who drinks juice either enjoys chess or enjoys painting.
2. The teacher lives immediately to the right of the person who drinks milk.
3. The baker lives next to the juice drinker.
4. The Brit and the person who enjoys cooking live two houses apart.
5. The person who drinks tea works as the farmer.
6. The person who drinks water lives in the fifth house.
7. The person who enjoys painting and the person who enjoys tennis are neighbours.
8. The lawyer does not live in house 4.
9. The Spaniard enjoys cooking.
10. The juice drinker and the water drinker live in adjacent houses.
11. The Norwegian lives at one end of the row.
12. The chess enthusiast works as the teacher.
13. The water drinker is the Swede.

Answer format for this puzzle: {"1": {"<category>": "<value>", ...}, "2": {...}, ...} -- one entry per house number, giving the value of every category.
