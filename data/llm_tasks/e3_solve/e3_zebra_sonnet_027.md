# Task: solve logic puzzles

Solve each puzzle below by reasoning. Every puzzle has exactly one solution. Work carefully; you
cannot run code. Give a complete answer for every puzzle even if unsure.

Output: write a single JSON object to the file D:\Puzzle-generation-with-guaranteed-uniqueness\data\llm_tasks\e3_solve\e3_zebra_sonnet_027.out.json with this exact structure
{"answers": [{"id": "<puzzle id>", "answer": <answer>}, ...]}
where <answer> has the format stated for each puzzle.

The puzzles follow.


## Puzzle zebra-00755

Grid logic puzzle. Deduce which value of each category belongs to each house. Every value is used exactly once.

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- nationality: Dane, Norwegian, Swede, German, Brit
- hobby: golf, hiking, tennis, chess, cooking
- drink: juice, cocoa, tea, milk, water
- job: farmer, lawyer, pilot, baker, teacher

Clues:
1. The teacher either enjoys golf or enjoys hiking.
2. The pilot lives in one of the two end houses.
3. The tennis enthusiast lives in house 2.
4. The baker lives in the fourth house.
5. The baker lives immediately to the right of the tea drinker.
6. There is exactly one house between the lawyer and the Swede.
7. The water drinker is the Dane.
8. The milk drinker is the Brit.
9. The Norwegian and the Swede are neighbours.
10. The Dane lives somewhere to the left of the pilot.
11. The Swede lives immediately to the right of the baker.
12. The Brit and the person who enjoys cooking live in adjacent houses.
13. The chess enthusiast lives next to the Swede.
14. The juice drinker is the Norwegian.
15. The hiking enthusiast lives somewhere to the left of the person who drinks juice.

Answer format for this puzzle: {"1": {"<category>": "<value>", ...}, "2": {...}, ...} -- one entry per house number, giving the value of every category.
