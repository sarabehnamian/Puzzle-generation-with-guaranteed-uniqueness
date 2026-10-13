# Task: solve logic puzzles

Solve each puzzle below by reasoning. Every puzzle has exactly one solution. Work carefully; you
cannot run code. Give a complete answer for every puzzle even if unsure.

Output: write a single JSON object to the file /home/user/Puzzle-generation-with-guaranteed-uniqueness/data/llm_tasks/e4_eval_g1/e4_eval_g1_haiku_002.out.json with this exact structure
{"answers": [{"id": "<puzzle id>", "answer": <answer>}, ...]}
where <answer> has the format stated for each puzzle.

The puzzles follow.


## Puzzle evo-g0-03

Grid logic puzzle. Deduce which value of each category belongs to each house. Every value is used exactly once.

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- color: blue, white, purple, green, yellow
- drink: water, cocoa, milk, coffee, tea
- nationality: Swede, German, Brit, Norwegian, Dane
- hobby: cooking, painting, chess, golf, tennis

Clues:
1. Whoever lives in the purple house drinks coffee.
2. The person who enjoys cooking lives immediately to the right of the occupant of the yellow house.
3. The Dane lives at one end of the row.
4. The person who enjoys cooking lives in the house just left of the one where the water drinker lives.
5. The person who enjoys chess either is the German or is the Swede.
6. The person who drinks water either is the Dane or is the Swede.
7. The tea drinker lives in the leftmost house.
8. The occupant of the blue house is the German.
9. The person who drinks cocoa and the Norwegian live in adjacent houses.
10. The German lives in the house just left of the one where the Norwegian lives.
11. The person who enjoys golf lives in the white house.
12. The German lives immediately to the right of the person who enjoys tennis.
13. The person who drinks coffee and the milk drinker are not neighbours.

Answer format for this puzzle: {"1": {"<category>": "<value>", ...}, "2": {...}, ...} -- one entry per house number, giving the value of every category.

## Puzzle evo-g1-12

Grid logic puzzle. Deduce which value of each category belongs to each house. Every value is used exactly once.

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- drink: coffee, water, milk, cocoa, juice
- pet: cat, horse, bird, dog, fish
- hobby: tennis, painting, cooking, hiking, chess
- color: red, purple, green, blue, white

Clues:
1. There is exactly one house between the horse owner and the occupant of the white house.
2. The occupant of the purple house enjoys hiking.
3. The owner of the dog lives somewhere to the right of the person who enjoys tennis.
4. The milk drinker does not live next to the painting enthusiast.
5. The person in the green house lives in house 4.
6. The occupant of the blue house drinks cocoa.
7. The juice drinker does not live in house 3.
8. The hiking enthusiast lives directly to the left of the person who keeps the fish.
9. The person who keeps the bird and the occupant of the red house live two houses apart.
10. The occupant of the purple house lives in the house just left of the one where the tennis enthusiast lives.
11. The person who enjoys cooking lives at one end of the row.
12. There is exactly one house between the person who keeps the bird and the fish owner.
13. The bird owner enjoys chess.
14. The coffee drinker lives somewhere to the right of the cat owner.
15. The person who drinks water lives in the fourth house.
16. The person who drinks coffee lives in one of the two end houses.

Answer format for this puzzle: {"1": {"<category>": "<value>", ...}, "2": {...}, ...} -- one entry per house number, giving the value of every category.

## Puzzle evo-g1-00

Grid logic puzzle. Deduce which value of each category belongs to each house. Every value is used exactly once.

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- hobby: golf, cooking, chess, tennis, hiking
- nationality: Norwegian, Dane, Spaniard, German, Swede
- job: lawyer, baker, farmer, pilot, doctor
- color: yellow, white, purple, red, blue

Clues:
1. The doctor lives in the fifth house.
2. There is exactly one house between the Dane and the person in the purple house.
3. Whoever lives in the red house and the occupant of the white house live two houses apart.
4. The Norwegian lives directly to the left of whoever lives in the white house.
5. The chess enthusiast and the cooking enthusiast are neighbours.
6. The Dane lives immediately to the right of the German.
7. The person in the yellow house lives somewhere to the left of the Swede.
8. The hiking enthusiast and the lawyer live two houses apart.
9. The chess enthusiast works as the pilot.
10. There is exactly one house between the person in the blue house and the German.
11. The person who enjoys golf is the Dane.
12. The person who enjoys chess lives in a lower-numbered house than the lawyer.
13. The baker lives next to the person in the purple house.
14. Whoever lives in the red house lives directly to the left of the person who enjoys tennis.

Answer format for this puzzle: {"1": {"<category>": "<value>", ...}, "2": {...}, ...} -- one entry per house number, giving the value of every category.

## Puzzle evo-g0-07

Grid logic puzzle. Deduce which value of each category belongs to each house. Every value is used exactly once.

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- drink: coffee, water, milk, cocoa, juice
- pet: cat, horse, bird, dog, fish
- hobby: tennis, painting, cooking, hiking, chess
- color: red, purple, green, blue, white

Clues:
1. Whoever lives in the purple house lives directly to the left of the tennis enthusiast.
2. There is exactly one house between the owner of the bird and the fish owner.
3. The person who drinks milk does not live next to the person who enjoys painting.
4. The owner of the dog lives somewhere to the right of the person who enjoys tennis.
5. There is exactly one house between the owner of the bird and the occupant of the red house.
6. Whoever lives in the green house lives in house 4.
7. The owner of the horse and the occupant of the white house live two houses apart.
8. The person who drinks coffee lives somewhere to the right of the cat owner.
9. The cooking enthusiast lives in the last house.
10. The juice drinker lives in the second house.
11. The coffee drinker lives in one of the two end houses.
12. The cocoa drinker lives in the blue house.
13. The owner of the bird enjoys chess.
14. The person who enjoys hiking lives directly to the left of the fish owner.

Answer format for this puzzle: {"1": {"<category>": "<value>", ...}, "2": {...}, ...} -- one entry per house number, giving the value of every category.

## Puzzle evo-g1-01

Grid logic puzzle. Deduce which value of each category belongs to each house. Every value is used exactly once.

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- color: purple, blue, red, green, yellow
- hobby: tennis, painting, golf, hiking, cooking
- pet: horse, cat, bird, rabbit, dog
- nationality: Swede, Spaniard, Norwegian, German, Brit

Clues:
1. The German and the person who keeps the bird are different people.
2. The person who enjoys cooking and the painting enthusiast live in adjacent houses.
3. The person who keeps the dog lives immediately to the right of the occupant of the purple house.
4. The Brit either lives in the red house or lives in the yellow house.
5. The Norwegian keeps the bird.
6. The rabbit owner lives in a lower-numbered house than the Brit.
7. The person who enjoys cooking and the Swede live two houses apart.
8. The Spaniard lives directly to the left of the owner of the cat.
9. The painting enthusiast lives directly to the left of the occupant of the blue house.
10. The person in the yellow house lives in the house just left of the one where the person in the red house lives.
11. The German and the person who enjoys hiking are neighbours.
12. The bird owner and the owner of the horse live two houses apart.
13. The German either enjoys cooking or enjoys hiking.
14. The person who enjoys golf does not live next to the person who enjoys hiking.
15. The hiking enthusiast lives somewhere to the left of the horse owner.

Answer format for this puzzle: {"1": {"<category>": "<value>", ...}, "2": {...}, ...} -- one entry per house number, giving the value of every category.
