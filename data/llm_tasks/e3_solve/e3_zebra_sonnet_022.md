# Task: solve logic puzzles

Solve each puzzle below by reasoning. Every puzzle has exactly one solution. Work carefully; you
cannot run code. Give a complete answer for every puzzle even if unsure.

Output: write a single JSON object to the file D:\Puzzle-generation-with-guaranteed-uniqueness\data\llm_tasks\e3_solve\e3_zebra_sonnet_022.out.json with this exact structure
{"answers": [{"id": "<puzzle id>", "answer": <answer>}, ...]}
where <answer> has the format stated for each puzzle.

The puzzles follow.


## Puzzle zebra-01240

Grid logic puzzle. Deduce which value of each category belongs to each house. Every value is used exactly once.

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- pet: dog, horse, fish, cat, rabbit
- job: doctor, pilot, teacher, baker, lawyer
- color: purple, green, white, yellow, blue
- nationality: Brit, Dane, Swede, German, Spaniard

Clues:
1. The owner of the horse lives next to the occupant of the purple house.
2. The Dane lives directly to the left of the teacher.
3. The person who keeps the cat and the Swede live in adjacent houses.
4. The owner of the rabbit lives in the house just left of the one where whoever lives in the green house lives.
5. The Brit lives in the yellow house.
6. The person in the purple house lives somewhere to the left of the occupant of the green house.
7. The Brit and the German live two houses apart.
8. The baker and the doctor live in adjacent houses.
9. The owner of the dog lives in the green house.
10. The Dane lives in the house just left of the one where the occupant of the blue house lives.
11. The doctor and the owner of the horse live two houses apart.
12. The Brit lives immediately to the right of the pilot.
13. The Dane and the Spaniard are neighbours.

Answer format for this puzzle: {"1": {"<category>": "<value>", ...}, "2": {...}, ...} -- one entry per house number, giving the value of every category.
