# Task: solve logic puzzles

Solve each puzzle below by reasoning. Every puzzle has exactly one solution. Work carefully; you
cannot run code. Give a complete answer for every puzzle even if unsure.

Output: write a single JSON object to the file D:\Puzzle-generation-with-guaranteed-uniqueness\data\llm_tasks\e3_solve\e3_zebra_haiku_013.out.json with this exact structure
{"answers": [{"id": "<puzzle id>", "answer": <answer>}, ...]}
where <answer> has the format stated for each puzzle.

The puzzles follow.


## Puzzle zebra-01137

Grid logic puzzle. Deduce which value of each category belongs to each house. Every value is used exactly once.

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- hobby: cooking, chess, painting, hiking, tennis
- job: teacher, farmer, doctor, baker, lawyer
- nationality: Swede, Brit, Dane, Spaniard, Norwegian
- pet: horse, dog, bird, rabbit, cat

Clues:
1. The person who keeps the bird lives in the house just left of the one where the owner of the cat lives.
2. The farmer lives directly to the left of the baker.
3. The Brit and the teacher are not neighbours.
4. The Swede and the tennis enthusiast are neighbours.
5. The chess enthusiast keeps the rabbit.
6. The person who enjoys cooking is the Swede.
7. The person who enjoys painting works as the lawyer.
8. The person who keeps the dog lives in one of the two end houses.
9. The person who keeps the horse lives in the house just left of the one where the Spaniard lives.
10. The person who enjoys chess either works as the baker or works as the teacher.
11. The Norwegian lives in the fifth house.
12. The painting enthusiast lives in house 3.
13. The bird owner lives in the house just left of the one where the tennis enthusiast lives.

Answer format for this puzzle: {"1": {"<category>": "<value>", ...}, "2": {...}, ...} -- one entry per house number, giving the value of every category.
