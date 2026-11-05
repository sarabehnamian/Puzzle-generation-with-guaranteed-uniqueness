# Task: solve logic puzzles

Solve each puzzle below by reasoning. Every puzzle has exactly one solution. Work carefully; you
cannot run code. Give a complete answer for every puzzle even if unsure.

Output: write a single JSON object to the file D:\Puzzle-generation-with-guaranteed-uniqueness\data\llm_tasks\e3_solve\e3_zebra_sonnet_025.out.json with this exact structure
{"answers": [{"id": "<puzzle id>", "answer": <answer>}, ...]}
where <answer> has the format stated for each puzzle.

The puzzles follow.


## Puzzle zebra-00518

Grid logic puzzle. Deduce which value of each category belongs to each house. Every value is used exactly once.

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- color: white, red, yellow, blue, green
- pet: horse, cat, dog, rabbit, bird
- hobby: golf, cooking, painting, chess, hiking
- nationality: Brit, Spaniard, Norwegian, Dane, Swede

Clues:
1. The person who keeps the cat and the chess enthusiast are neighbours.
2. The Norwegian lives in the red house.
3. The golf enthusiast does not live next to the person in the red house.
4. The person who keeps the rabbit and the person in the white house live in adjacent houses.
5. The occupant of the blue house enjoys golf.
6. The occupant of the red house keeps the dog.
7. Whoever lives in the green house keeps the horse.
8. The cat owner lives directly to the left of the Spaniard.
9. The person who enjoys painting is the Dane.
10. The person who enjoys painting lives in the house just left of the one where the Swede lives.
11. The horse owner lives immediately to the right of the person who enjoys hiking.
12. Whoever lives in the red house lives immediately to the right of the owner of the rabbit.

Answer format for this puzzle: {"1": {"<category>": "<value>", ...}, "2": {...}, ...} -- one entry per house number, giving the value of every category.
