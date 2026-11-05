# Task: solve logic puzzles

Solve each puzzle below by reasoning. Every puzzle has exactly one solution. Work carefully; you
cannot run code. Give a complete answer for every puzzle even if unsure.

Output: write a single JSON object to the file D:\Puzzle-generation-with-guaranteed-uniqueness\data\llm_tasks\e3_solve\e3_zebra_sonnet_000.out.json with this exact structure
{"answers": [{"id": "<puzzle id>", "answer": <answer>}, ...]}
where <answer> has the format stated for each puzzle.

The puzzles follow.


## Puzzle zebra-01412

Grid logic puzzle. Deduce which value of each category belongs to each house. Every value is used exactly once.

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- nationality: Brit, Norwegian, Swede, German, Spaniard
- drink: cocoa, water, juice, coffee, tea
- pet: rabbit, bird, dog, horse, cat
- hobby: tennis, golf, painting, hiking, chess

Clues:
1. The person who drinks coffee either enjoys golf or enjoys painting.
2. The tennis enthusiast lives immediately to the right of the juice drinker.
3. There is exactly one house between the owner of the dog and the person who enjoys painting.
4. The juice drinker lives directly to the left of the person who keeps the bird.
5. The golf enthusiast is not the Brit.
6. The German drinks tea.
7. The Norwegian lives in the leftmost house.
8. The dog owner and the owner of the rabbit live two houses apart.
9. The Norwegian and the painting enthusiast are neighbours.
10. The cocoa drinker and the owner of the dog are neighbours.
11. The golf enthusiast lives in the house just left of the one where the person who enjoys hiking lives.
12. The German enjoys painting.
13. The owner of the horse and the Spaniard live in adjacent houses.

Answer format for this puzzle: {"1": {"<category>": "<value>", ...}, "2": {...}, ...} -- one entry per house number, giving the value of every category.
