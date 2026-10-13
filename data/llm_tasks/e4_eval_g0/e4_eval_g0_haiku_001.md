# Task: solve logic puzzles

Solve each puzzle below by reasoning. Every puzzle has exactly one solution. Work carefully; you
cannot run code. Give a complete answer for every puzzle even if unsure.

Output: write a single JSON object to the file /home/user/Puzzle-generation-with-guaranteed-uniqueness/data/llm_tasks/e4_eval_g0/e4_eval_g0_haiku_001.out.json with this exact structure
{"answers": [{"id": "<puzzle id>", "answer": <answer>}, ...]}
where <answer> has the format stated for each puzzle.

The puzzles follow.


## Puzzle evo-g0-01

Grid logic puzzle. Deduce which value of each category belongs to each house. Every value is used exactly once.

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- pet: bird, dog, cat, rabbit, horse
- job: lawyer, pilot, doctor, teacher, baker
- color: yellow, white, blue, green, purple
- hobby: painting, hiking, tennis, golf, chess

Clues:
1. There is exactly one house between the pilot and the person in the white house.
2. The person who keeps the horse lives next to whoever lives in the white house.
3. The horse owner works as the teacher.
4. The bird owner lives in house 1.
5. The tennis enthusiast works as the lawyer.
6. There is exactly one house between whoever lives in the green house and the hiking enthusiast.
7. The golf enthusiast lives in one of the two end houses.
8. Whoever lives in the yellow house either works as the baker or works as the pilot.
9. The owner of the rabbit either lives in the white house or lives in the yellow house.
10. The person who enjoys golf keeps the rabbit.
11. The doctor either lives in the blue house or lives in the purple house.
12. There is exactly one house between the person who keeps the cat and the painting enthusiast.
13. The person in the blue house does not live next to the person in the white house.
14. There is exactly one house between whoever lives in the blue house and whoever lives in the purple house.

Answer format for this puzzle: {"1": {"<category>": "<value>", ...}, "2": {...}, ...} -- one entry per house number, giving the value of every category.

## Puzzle evo-g0-00

Grid logic puzzle. Deduce which value of each category belongs to each house. Every value is used exactly once.

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- hobby: golf, cooking, chess, tennis, hiking
- nationality: Norwegian, Dane, Spaniard, German, Swede
- job: lawyer, baker, farmer, pilot, doctor
- color: yellow, white, purple, red, blue

Clues:
1. The Dane and the occupant of the purple house live two houses apart.
2. The person in the blue house and the German live two houses apart.
3. There is exactly one house between the occupant of the red house and whoever lives in the white house.
4. The Norwegian lives directly to the left of the person in the white house.
5. The occupant of the red house lives directly to the left of the tennis enthusiast.
6. The Dane enjoys golf.
7. The farmer lives in the fourth house.
8. The doctor lives in the fifth house.
9. The baker and the occupant of the purple house live in adjacent houses.
10. Whoever lives in the yellow house lives in a lower-numbered house than the Swede.
11. The person who enjoys hiking and the lawyer live two houses apart.
12. The person in the purple house enjoys chess.

Answer format for this puzzle: {"1": {"<category>": "<value>", ...}, "2": {...}, ...} -- one entry per house number, giving the value of every category.

## Puzzle evo-g0-02

Grid logic puzzle. Deduce which value of each category belongs to each house. Every value is used exactly once.

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- nationality: Swede, Brit, Spaniard, German, Norwegian
- hobby: painting, tennis, golf, cooking, hiking
- job: lawyer, doctor, baker, teacher, farmer
- pet: fish, horse, bird, cat, dog

Clues:
1. The German and the lawyer live in adjacent houses.
2. The person who keeps the fish and the golf enthusiast are not neighbours.
3. The golf enthusiast keeps the cat.
4. The doctor and the golf enthusiast live in adjacent houses.
5. The Norwegian lives immediately to the right of the person who enjoys cooking.
6. The German enjoys cooking.
7. The Norwegian lives next to the Spaniard.
8. The person who keeps the horse enjoys painting.
9. The German lives immediately to the right of the bird owner.
10. The lawyer and the tennis enthusiast live in adjacent houses.
11. The person who keeps the fish lives somewhere to the left of the farmer.
12. There is exactly one house between the farmer and the person who keeps the horse.
13. The person who enjoys hiking either is the Norwegian or is the Swede.
14. The hiking enthusiast lives in the house just left of the one where the teacher lives.

Answer format for this puzzle: {"1": {"<category>": "<value>", ...}, "2": {...}, ...} -- one entry per house number, giving the value of every category.
