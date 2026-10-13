# Task: solve logic puzzles

Solve each puzzle below by reasoning. Every puzzle has exactly one solution. Work carefully; you
cannot run code. Give a complete answer for every puzzle even if unsure.

Output: write a single JSON object to the file /home/user/Puzzle-generation-with-guaranteed-uniqueness/data/llm_tasks/e4_eval_g1/e4_eval_g1_haiku_001.out.json with this exact structure
{"answers": [{"id": "<puzzle id>", "answer": <answer>}, ...]}
where <answer> has the format stated for each puzzle.

The puzzles follow.


## Puzzle evo-g1-10

Grid logic puzzle. Deduce which value of each category belongs to each house. Every value is used exactly once.

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- hobby: golf, painting, tennis, cooking, hiking
- nationality: Norwegian, Swede, German, Spaniard, Dane
- color: red, green, blue, yellow, white
- drink: cocoa, water, tea, milk, juice

Clues:
1. The person who enjoys golf and the Norwegian live in adjacent houses.
2. The painting enthusiast is the Swede.
3. The German and the painting enthusiast are neighbours.
4. The cocoa drinker lives in the house just left of the one where the occupant of the red house lives.
5. The person who enjoys hiking lives somewhere to the right of whoever lives in the white house.
6. Whoever lives in the blue house lives directly to the left of whoever lives in the yellow house.
7. The Dane and the German live in adjacent houses.
8. The person who enjoys golf drinks water.
9. The hiking enthusiast and the Norwegian are different people.
10. The German and the person in the red house live in adjacent houses.
11. The person who drinks tea either lives in the red house or lives in the white house.
12. The painting enthusiast lives directly to the left of the person who enjoys cooking.
13. Whoever lives in the yellow house lives immediately to the right of the Dane.
14. The golf enthusiast and the person who drinks juice are not neighbours.
15. The milk drinker lives immediately to the right of the Swede.

Answer format for this puzzle: {"1": {"<category>": "<value>", ...}, "2": {...}, ...} -- one entry per house number, giving the value of every category.

## Puzzle evo-g1-05

Grid logic puzzle. Deduce which value of each category belongs to each house. Every value is used exactly once.

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- pet: bird, dog, cat, rabbit, horse
- job: lawyer, pilot, doctor, teacher, baker
- color: yellow, white, blue, green, purple
- hobby: painting, hiking, tennis, golf, chess

Clues:
1. The doctor either lives in the blue house or lives in the purple house.
2. The owner of the dog lives in the yellow house.
3. The occupant of the green house and the hiking enthusiast live two houses apart.
4. The rabbit owner either lives in the white house or lives in the yellow house.
5. The person who enjoys golf lives at one end of the row.
6. The tennis enthusiast lives in the first house.
7. The person in the blue house lives somewhere to the left of whoever lives in the purple house.
8. The pilot and whoever lives in the white house live two houses apart.
9. The occupant of the yellow house either works as the baker or works as the pilot.
10. The owner of the horse and the occupant of the white house are neighbours.
11. The tennis enthusiast works as the lawyer.
12. Whoever lives in the blue house and the occupant of the white house are not neighbours.
13. The teacher keeps the horse.
14. The person who keeps the rabbit enjoys golf.
15. The occupant of the green house lives in house 1.
16. There is exactly one house between the person who keeps the cat and the person who enjoys painting.

Answer format for this puzzle: {"1": {"<category>": "<value>", ...}, "2": {...}, ...} -- one entry per house number, giving the value of every category.

## Puzzle evo-g1-06

Grid logic puzzle. Deduce which value of each category belongs to each house. Every value is used exactly once.

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- pet: bird, dog, cat, rabbit, horse
- job: lawyer, pilot, doctor, teacher, baker
- color: yellow, white, blue, green, purple
- hobby: painting, hiking, tennis, golf, chess

Clues:
1. The person in the blue house and the occupant of the purple house live two houses apart.
2. The baker and the person in the purple house live in adjacent houses.
3. The lawyer either enjoys tennis or enjoys golf.
4. Whoever lives in the blue house and whoever lives in the white house are not neighbours.
5. The owner of the horse and whoever lives in the white house live in adjacent houses.
6. The pilot and the person in the white house live two houses apart.
7. The person who enjoys hiking lives in the house just left of the one where whoever lives in the purple house lives.
8. The person in the yellow house either works as the baker or works as the pilot.
9. The doctor either lives in the blue house or lives in the purple house.
10. The owner of the cat lives in a lower-numbered house than the person who enjoys painting.
11. The horse owner works as the teacher.
12. There is exactly one house between the occupant of the green house and the hiking enthusiast.
13. The owner of the rabbit either lives in the white house or lives in the yellow house.
14. The person who keeps the bird lives in the first house.
15. The person in the green house lives in the house just left of the one where the person who keeps the cat lives.
16. The person who enjoys golf keeps the rabbit.
17. The person who keeps the cat lives somewhere to the left of the owner of the horse.

Answer format for this puzzle: {"1": {"<category>": "<value>", ...}, "2": {...}, ...} -- one entry per house number, giving the value of every category.

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

## Puzzle evo-g1-02

Grid logic puzzle. Deduce which value of each category belongs to each house. Every value is used exactly once.

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- color: purple, blue, red, green, yellow
- hobby: tennis, painting, golf, hiking, cooking
- pet: horse, cat, bird, rabbit, dog
- nationality: Swede, Spaniard, Norwegian, German, Brit

Clues:
1. The horse owner lives somewhere to the right of the person who enjoys hiking.
2. Whoever lives in the purple house lives in the house just left of the one where the person who keeps the dog lives.
3. The person who enjoys cooking lives next to the person who enjoys painting.
4. The person in the purple house and the person who enjoys painting are different people.
5. There is exactly one house between the cooking enthusiast and the Swede.
6. There is exactly one house between the owner of the bird and the person who keeps the horse.
7. The painting enthusiast and the occupant of the blue house are neighbours.
8. The person who keeps the bird is the Norwegian.
9. The Spaniard and the cat owner live in adjacent houses.
10. The person who enjoys hiking lives immediately to the right of the German.
11. The German either enjoys cooking or enjoys hiking.
12. Whoever lives in the yellow house lives in the house just left of the one where the person in the red house lives.
13. The person who enjoys golf does not live next to the person who enjoys hiking.

Answer format for this puzzle: {"1": {"<category>": "<value>", ...}, "2": {...}, ...} -- one entry per house number, giving the value of every category.
