# Task: solve logic puzzles

Solve each puzzle below by reasoning. Every puzzle has exactly one solution. Work carefully; you
cannot run code. Give a complete answer for every puzzle even if unsure.

Output: write a single JSON object to the file D:\Puzzle-generation-with-guaranteed-uniqueness\data\llm_tasks\e3_solve\e3_zebra_opus_012.out.json with this exact structure
{"answers": [{"id": "<puzzle id>", "answer": <answer>}, ...]}
where <answer> has the format stated for each puzzle.

The puzzles follow.


## Puzzle zebra-00647

Grid logic puzzle. Deduce which value of each category belongs to each house. Every value is used exactly once.

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- job: farmer, teacher, doctor, baker, pilot
- drink: tea, coffee, juice, milk, cocoa
- hobby: cooking, golf, tennis, chess, hiking
- pet: bird, fish, horse, dog, rabbit

Clues:
1. The baker lives in the house just left of the one where the pilot lives.
2. The person who drinks cocoa lives in the second house.
3. The juice drinker and the pilot are different people.
4. The farmer and the milk drinker are neighbours.
5. The doctor and the person who enjoys hiking live in adjacent houses.
6. The teacher lives in the last house.
7. The person who drinks tea lives directly to the left of the person who enjoys golf.
8. The juice drinker lives in house 4.
9. The person who drinks juice lives directly to the left of the cooking enthusiast.
10. The person who keeps the bird lives immediately to the right of the pilot.
11. The doctor keeps the fish.
12. The pilot lives next to the person who keeps the rabbit.
13. The chess enthusiast either works as the doctor or works as the teacher.
14. The person who keeps the horse does not enjoy tennis.

Answer format for this puzzle: {"1": {"<category>": "<value>", ...}, "2": {...}, ...} -- one entry per house number, giving the value of every category.
