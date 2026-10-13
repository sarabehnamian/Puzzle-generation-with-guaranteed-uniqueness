# Task: solve logic puzzles

Solve each puzzle below by reasoning. Every puzzle has exactly one solution. Work carefully; you
cannot run code. Give a complete answer for every puzzle even if unsure.

Output: write a single JSON object to the file /home/user/Puzzle-generation-with-guaranteed-uniqueness/data/llm_tasks/e4_eval_g1/e4_eval_g1_haiku_003.out.json with this exact structure
{"answers": [{"id": "<puzzle id>", "answer": <answer>}, ...]}
where <answer> has the format stated for each puzzle.

The puzzles follow.


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

## Puzzle evo-g1-03

Grid logic puzzle. Deduce which value of each category belongs to each house. Every value is used exactly once.

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- color: blue, white, purple, green, yellow
- drink: water, cocoa, milk, coffee, tea
- nationality: Swede, German, Brit, Norwegian, Dane
- hobby: cooking, painting, chess, golf, tennis

Clues:
1. The chess enthusiast either is the German or is the Swede.
2. The Dane lives in one of the two end houses.
3. The German and the Norwegian are neighbours.
4. The German lives immediately to the right of the person who enjoys tennis.
5. The person who drinks coffee lives in the second house.
6. The cooking enthusiast lives directly to the left of the water drinker.
7. The coffee drinker and the milk drinker are not neighbours.
8. The person in the white house enjoys golf.
9. The occupant of the yellow house lives in the house just left of the one where the person who enjoys cooking lives.
10. The coffee drinker lives in the purple house.
11. The person who enjoys painting and whoever lives in the purple house are neighbours.
12. The chess enthusiast and the person who drinks coffee live two houses apart.
13. The cocoa drinker lives next to the Norwegian.
14. The person who drinks water either is the Dane or is the Swede.
15. The person in the blue house is the German.

Answer format for this puzzle: {"1": {"<category>": "<value>", ...}, "2": {...}, ...} -- one entry per house number, giving the value of every category.

## Puzzle evo-g1-09

Grid logic puzzle. Deduce which value of each category belongs to each house. Every value is used exactly once.

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- job: lawyer, doctor, pilot, teacher, baker
- pet: cat, dog, bird, horse, fish
- hobby: chess, golf, cooking, tennis, hiking
- color: white, yellow, purple, red, green

Clues:
1. The occupant of the purple house lives in the second house.
2. The person who enjoys cooking does not live in the third house.
3. The owner of the cat lives immediately to the right of the pilot.
4. The person who keeps the dog either enjoys cooking or enjoys hiking.
5. The occupant of the purple house either enjoys hiking or enjoys tennis.
6. The owner of the horse and the tennis enthusiast live in adjacent houses.
7. The person who keeps the horse lives directly to the left of the person who keeps the cat.
8. The cooking enthusiast lives somewhere to the left of the cat owner.
9. Whoever lives in the purple house and the person in the white house live in adjacent houses.
10. The baker lives in house 4.
11. The person who enjoys chess lives in the red house.
12. The person in the yellow house lives at one end of the row.
13. The chess enthusiast and the doctor live two houses apart.
14. The person who enjoys hiking keeps the bird.
15. The person who keeps the bird and the lawyer are neighbours.

Answer format for this puzzle: {"1": {"<category>": "<value>", ...}, "2": {...}, ...} -- one entry per house number, giving the value of every category.

## Puzzle evo-g1-07

Grid logic puzzle. Deduce which value of each category belongs to each house. Every value is used exactly once.

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- nationality: Swede, Brit, Spaniard, German, Norwegian
- hobby: painting, tennis, golf, cooking, hiking
- job: lawyer, doctor, baker, teacher, farmer
- pet: fish, horse, bird, cat, dog

Clues:
1. The hiking enthusiast either is the Norwegian or is the Swede.
2. The doctor lives next to the person who enjoys golf.
3. The bird owner lives directly to the left of the German.
4. The person who enjoys cooking and the Norwegian live in adjacent houses.
5. The doctor keeps the dog.
6. The farmer and the owner of the horse live two houses apart.
7. The person who keeps the fish lives in a lower-numbered house than the farmer.
8. The German enjoys cooking.
9. The hiking enthusiast lives directly to the left of the teacher.
10. The owner of the fish does not live next to the golf enthusiast.
11. The person who keeps the horse either enjoys painting or enjoys tennis.
12. The owner of the cat enjoys golf.
13. The German and the lawyer live in adjacent houses.
14. The Norwegian and the Spaniard live in adjacent houses.
15. The lawyer and the person who enjoys tennis are neighbours.

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
