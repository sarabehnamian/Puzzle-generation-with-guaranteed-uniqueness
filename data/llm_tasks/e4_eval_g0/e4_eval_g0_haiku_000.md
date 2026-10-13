# Task: solve logic puzzles

Solve each puzzle below by reasoning. Every puzzle has exactly one solution. Work carefully; you
cannot run code. Give a complete answer for every puzzle even if unsure.

Output: write a single JSON object to the file /home/user/Puzzle-generation-with-guaranteed-uniqueness/data/llm_tasks/e4_eval_g0/e4_eval_g0_haiku_000.out.json with this exact structure
{"answers": [{"id": "<puzzle id>", "answer": <answer>}, ...]}
where <answer> has the format stated for each puzzle.

The puzzles follow.


## Puzzle evo-g0-05

Grid logic puzzle. Deduce which value of each category belongs to each house. Every value is used exactly once.

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- hobby: golf, painting, tennis, cooking, hiking
- nationality: Norwegian, Swede, German, Spaniard, Dane
- color: red, green, blue, yellow, white
- drink: cocoa, water, tea, milk, juice

Clues:
1. The person who drinks cocoa lives directly to the left of whoever lives in the red house.
2. The Dane lives next to the German.
3. The tea drinker either lives in the red house or lives in the white house.
4. The Swede lives in the house just left of the one where the milk drinker lives.
5. The golf enthusiast drinks water.
6. The German and the occupant of the red house are neighbours.
7. The Dane lives in the house just left of the one where the person in the yellow house lives.
8. The Swede enjoys painting.
9. The person who enjoys golf does not live next to the juice drinker.
10. The Norwegian enjoys tennis.
11. The person in the blue house lives directly to the left of whoever lives in the yellow house.
12. Whoever lives in the white house lives somewhere to the left of the person who enjoys hiking.
13. The painting enthusiast lives in the house just left of the one where the person who enjoys cooking lives.
14. The German and the painting enthusiast are neighbours.

Answer format for this puzzle: {"1": {"<category>": "<value>", ...}, "2": {...}, ...} -- one entry per house number, giving the value of every category.

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
