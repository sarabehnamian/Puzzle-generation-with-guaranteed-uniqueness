# Task: solve logic puzzles

Solve each puzzle below by reasoning. Every puzzle has exactly one solution. Work carefully; you
cannot run code. Give a complete answer for every puzzle even if unsure.

Output: write a single JSON object to the file D:\Puzzle-generation-with-guaranteed-uniqueness\data\llm_tasks\e3_solve\e3_zebra_sonnet_014.out.json with this exact structure
{"answers": [{"id": "<puzzle id>", "answer": <answer>}, ...]}
where <answer> has the format stated for each puzzle.

The puzzles follow.


## Puzzle zebra-01459

Grid logic puzzle. Deduce which value of each category belongs to each house. Every value is used exactly once.

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- color: green, white, red, blue, yellow
- job: lawyer, doctor, teacher, pilot, baker
- nationality: Spaniard, Dane, German, Brit, Norwegian
- pet: horse, rabbit, bird, cat, dog

Clues:
1. The person in the red house lives in one of the two end houses.
2. The person who keeps the rabbit lives in the house just left of the one where the German lives.
3. The person who keeps the bird and the person in the yellow house live in adjacent houses.
4. The lawyer lives immediately to the right of the dog owner.
5. The pilot and the teacher live in adjacent houses.
6. The person who keeps the cat lives in house 3.
7. The pilot is not the Brit.
8. The Brit lives directly to the left of whoever lives in the yellow house.
9. The Dane lives somewhere to the left of the Brit.
10. The baker lives in house 3.
11. Whoever lives in the blue house and the teacher are not neighbours.
12. The Spaniard lives directly to the left of the baker.
13. The Spaniard and the person in the white house live two houses apart.

Answer format for this puzzle: {"1": {"<category>": "<value>", ...}, "2": {...}, ...} -- one entry per house number, giving the value of every category.
