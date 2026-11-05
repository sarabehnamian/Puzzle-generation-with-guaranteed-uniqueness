# Task: solve logic puzzles

Solve each puzzle below by reasoning. Every puzzle has exactly one solution. Work carefully; you
cannot run code. Give a complete answer for every puzzle even if unsure.

Output: write a single JSON object to the file D:\Puzzle-generation-with-guaranteed-uniqueness\data\llm_tasks\e3_solve\e3_zebra_sonnet_018.out.json with this exact structure
{"answers": [{"id": "<puzzle id>", "answer": <answer>}, ...]}
where <answer> has the format stated for each puzzle.

The puzzles follow.


## Puzzle zebra-00388

Grid logic puzzle. Deduce which value of each category belongs to each house. Every value is used exactly once.

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- pet: bird, cat, rabbit, horse, dog
- hobby: cooking, painting, chess, tennis, golf
- drink: juice, cocoa, coffee, milk, tea
- job: pilot, farmer, doctor, baker, teacher

Clues:
1. The farmer and the pilot are neighbours.
2. The person who enjoys painting works as the doctor.
3. The baker and the person who enjoys chess are neighbours.
4. The farmer either enjoys painting or enjoys tennis.
5. The juice drinker either works as the baker or works as the doctor.
6. There is exactly one house between the owner of the cat and the person who drinks cocoa.
7. The owner of the horse lives immediately to the right of the person who drinks tea.
8. The doctor and the dog owner live in adjacent houses.
9. The owner of the horse works as the teacher.
10. The golf enthusiast lives next to the painting enthusiast.
11. The owner of the bird either enjoys chess or enjoys golf.
12. The rabbit owner either works as the baker or works as the doctor.
13. The pilot lives directly to the left of the coffee drinker.

Answer format for this puzzle: {"1": {"<category>": "<value>", ...}, "2": {...}, ...} -- one entry per house number, giving the value of every category.
