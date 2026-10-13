# Task: solve logic puzzles

Solve each puzzle below by reasoning. Every puzzle has exactly one solution. Work carefully; you
cannot run code. Give a complete answer for every puzzle even if unsure.

Output: write a single JSON object to the file /home/user/Puzzle-generation-with-guaranteed-uniqueness/data/llm_tasks/e4_eval_g1/e4_eval_g1_haiku_000.out.json with this exact structure
{"answers": [{"id": "<puzzle id>", "answer": <answer>}, ...]}
where <answer> has the format stated for each puzzle.

The puzzles follow.


## Puzzle evo-g1-04

Grid logic puzzle. Deduce which value of each category belongs to each house. Every value is used exactly once.

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- color: blue, white, purple, green, yellow
- drink: water, cocoa, milk, coffee, tea
- nationality: Swede, German, Brit, Norwegian, Dane
- hobby: cooking, painting, chess, golf, tennis

Clues:
1. The person who drinks tea lives in the leftmost house.
2. The person who enjoys cooking lives in the house just left of the one where the water drinker lives.
3. The golf enthusiast lives in the white house.
4. The person who enjoys cooking lives immediately to the right of whoever lives in the yellow house.
5. The person who enjoys tennis lives next to the German.
6. The German either lives in the blue house or lives in the white house.
7. The person who enjoys chess either is the German or is the Swede.
8. The person who drinks cocoa does not enjoy golf.
9. Whoever lives in the blue house lives in the house just left of the one where the person who enjoys golf lives.
10. The German lives directly to the left of the Norwegian.
11. The person in the purple house drinks coffee.
12. The coffee drinker and the milk drinker are not neighbours.
13. The person who drinks water either is the Dane or is the Swede.
14. The person who drinks cocoa and the Norwegian live in adjacent houses.
15. The milk drinker and the tea drinker are not neighbours.
16. The Dane lives at one end of the row.

Answer format for this puzzle: {"1": {"<category>": "<value>", ...}, "2": {...}, ...} -- one entry per house number, giving the value of every category.

## Puzzle evo-g0-06

Grid logic puzzle. Deduce which value of each category belongs to each house. Every value is used exactly once.

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- color: purple, blue, red, green, yellow
- hobby: tennis, painting, golf, hiking, cooking
- pet: horse, cat, bird, rabbit, dog
- nationality: Swede, Spaniard, Norwegian, German, Brit

Clues:
1. The bird owner is the Norwegian.
2. The golf enthusiast and the hiking enthusiast are not neighbours.
3. The owner of the dog lives immediately to the right of the person in the purple house.
4. The German either enjoys cooking or enjoys hiking.
5. The cooking enthusiast and the Swede live two houses apart.
6. Whoever lives in the yellow house lives in the house just left of the one where the occupant of the red house lives.
7. The cooking enthusiast and the person who enjoys painting are neighbours.
8. The person who keeps the bird and the horse owner live two houses apart.
9. The Spaniard lives directly to the left of the cat owner.
10. The hiking enthusiast lives somewhere to the left of the owner of the horse.
11. The painting enthusiast lives in the house just left of the one where the occupant of the blue house lives.
12. The person who enjoys hiking lives immediately to the right of the German.

Answer format for this puzzle: {"1": {"<category>": "<value>", ...}, "2": {...}, ...} -- one entry per house number, giving the value of every category.

## Puzzle evo-g0-04

Grid logic puzzle. Deduce which value of each category belongs to each house. Every value is used exactly once.

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- job: lawyer, doctor, pilot, teacher, baker
- pet: cat, dog, bird, horse, fish
- hobby: chess, golf, cooking, tennis, hiking
- color: white, yellow, purple, red, green

Clues:
1. The cat owner lives immediately to the right of the owner of the horse.
2. The person who enjoys chess lives in the red house.
3. The person in the yellow house lives in the fifth house.
4. The baker lives in house 4.
5. The owner of the bird and the lawyer are neighbours.
6. The bird owner enjoys hiking.
7. The pilot lives directly to the left of the person who keeps the cat.
8. The person who enjoys cooking lives at one end of the row.
9. There is exactly one house between the chess enthusiast and the doctor.
10. Whoever lives in the purple house either enjoys hiking or enjoys tennis.
11. Whoever lives in the purple house and the person in the white house are neighbours.
12. The person who keeps the cat lives somewhere to the right of the person who enjoys cooking.
13. The horse owner lives next to the person who enjoys tennis.
14. The person who keeps the dog either enjoys cooking or enjoys hiking.

Answer format for this puzzle: {"1": {"<category>": "<value>", ...}, "2": {...}, ...} -- one entry per house number, giving the value of every category.

## Puzzle evo-g1-08

Grid logic puzzle. Deduce which value of each category belongs to each house. Every value is used exactly once.

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- job: lawyer, doctor, pilot, teacher, baker
- pet: cat, dog, bird, horse, fish
- hobby: chess, golf, cooking, tennis, hiking
- color: white, yellow, purple, red, green

Clues:
1. The cat owner lives immediately to the right of the person who keeps the horse.
2. The owner of the fish and the chess enthusiast are different people.
3. The bird owner and the lawyer are neighbours.
4. The cooking enthusiast lives at one end of the row.
5. The owner of the cat lives immediately to the right of the pilot.
6. The lawyer keeps the dog.
7. The person who keeps the bird enjoys hiking.
8. The occupant of the purple house either enjoys hiking or enjoys tennis.
9. The person who enjoys chess and the doctor live two houses apart.
10. The owner of the horse and the tennis enthusiast live in adjacent houses.
11. The owner of the dog either enjoys cooking or enjoys hiking.
12. The person who enjoys cooking lives somewhere to the left of the person who keeps the cat.
13. The owner of the fish lives in one of the two end houses.
14. The occupant of the red house enjoys chess.
15. The baker and the lawyer are not neighbours.
16. The person in the purple house and the occupant of the white house are neighbours.
17. The occupant of the yellow house lives in the fifth house.

Answer format for this puzzle: {"1": {"<category>": "<value>", ...}, "2": {...}, ...} -- one entry per house number, giving the value of every category.

## Puzzle evo-g1-13

Grid logic puzzle. Deduce which value of each category belongs to each house. Every value is used exactly once.

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- drink: coffee, water, milk, cocoa, juice
- pet: cat, horse, bird, dog, fish
- hobby: tennis, painting, cooking, hiking, chess
- color: red, purple, green, blue, white

Clues:
1. The owner of the bird enjoys chess.
2. The person who enjoys cooking lives in the last house.
3. The person who keeps the cat lives somewhere to the left of the coffee drinker.
4. There is exactly one house between the bird owner and whoever lives in the red house.
5. The person in the green house lives next to whoever lives in the white house.
6. The owner of the horse and the occupant of the white house live two houses apart.
7. The owner of the dog lives somewhere to the right of the tennis enthusiast.
8. There is exactly one house between the person who drinks coffee and the person who enjoys painting.
9. The milk drinker does not live next to the person who enjoys painting.
10. The person who keeps the fish lives immediately to the right of the person who enjoys hiking.
11. The person who enjoys tennis lives immediately to the right of the occupant of the purple house.
12. The person who drinks juice lives in house 2.
13. Whoever lives in the blue house drinks cocoa.
14. The owner of the bird and the person who keeps the fish live two houses apart.
15. The person who drinks coffee lives in one of the two end houses.

Answer format for this puzzle: {"1": {"<category>": "<value>", ...}, "2": {...}, ...} -- one entry per house number, giving the value of every category.
