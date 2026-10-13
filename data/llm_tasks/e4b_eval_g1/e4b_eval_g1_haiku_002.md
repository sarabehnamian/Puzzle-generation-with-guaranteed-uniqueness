# Task: solve logic puzzles

Solve each puzzle below by reasoning. Every puzzle has exactly one solution. Work carefully; you
cannot run code. Give a complete answer for every puzzle even if unsure.

Output: write a single JSON object to the file /home/user/Puzzle-generation-with-guaranteed-uniqueness/data/llm_tasks/e4b_eval_g1/e4b_eval_g1_haiku_002.out.json with this exact structure
{"answers": [{"id": "<puzzle id>", "answer": <answer>}, ...]}
where <answer> has the format stated for each puzzle.

The puzzles follow.


## Puzzle e4b-g0-07

Grid logic puzzle. Deduce which value of each category belongs to each house. Every value is used exactly once.

There are 6 houses in a row, numbered 1 to 6 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- color: purple, blue, white, yellow, red, green
- job: farmer, doctor, pilot, lawyer, teacher, baker
- pet: dog, bird, fish, horse, rabbit, cat
- hobby: hiking, chess, painting, golf, cooking, tennis
- drink: cocoa, coffee, milk, water, juice, tea
- nationality: Spaniard, Swede, German, Dane, Brit, Norwegian

Clues:
1. The dog owner lives in the house just left of the one where the Spaniard lives.
2. There is exactly one house between the Brit and the person who keeps the dog.
3. The baker and the German live two houses apart.
4. The pilot lives in the fourth house.
5. The Brit lives in the house just left of the one where the golf enthusiast lives.
6. There is exactly one house between the person who keeps the rabbit and the person who drinks tea.
7. The occupant of the green house lives at one end of the row.
8. The person who drinks milk and the person who drinks tea are neighbours.
9. Whoever lives in the purple house and the occupant of the red house are neighbours.
10. The cooking enthusiast lives in house 1.
11. The person who drinks cocoa lives in the red house.
12. Whoever lives in the blue house lives immediately to the right of the German.
13. The German lives in a lower-numbered house than the owner of the rabbit.
14. Whoever lives in the red house is the Norwegian.
15. The person in the white house lives in the house just left of the one where the lawyer lives.
16. The doctor lives in the first house.
17. The Brit keeps the cat.
18. The lawyer lives next to the teacher.
19. The water drinker is the Brit.
20. The person who drinks juice enjoys chess.
21. The juice drinker lives immediately to the right of the Norwegian.
22. There is exactly one house between the German and the teacher.
23. The bird owner enjoys painting.
24. The German and the tennis enthusiast are neighbours.
25. The fish owner lives directly to the left of the Dane.

Answer format for this puzzle: {"1": {"<category>": "<value>", ...}, "2": {...}, ...} -- one entry per house number, giving the value of every category.

## Puzzle e4b-g0-04

Grid logic puzzle. Deduce which value of each category belongs to each house. Every value is used exactly once.

There are 6 houses in a row, numbered 1 to 6 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- drink: juice, milk, coffee, tea, water, cocoa
- hobby: cooking, chess, painting, hiking, tennis, golf
- job: teacher, farmer, doctor, lawyer, baker, pilot
- color: red, white, green, blue, yellow, purple
- nationality: Swede, Dane, Brit, German, Spaniard, Norwegian
- pet: fish, cat, horse, bird, dog, rabbit

Clues:
1. The occupant of the green house lives next to the person in the yellow house.
2. The Brit and the person in the red house live two houses apart.
3. The teacher keeps the dog.
4. The person who drinks water does not live in house 2.
5. The person in the green house works as the lawyer.
6. The occupant of the red house keeps the horse.
7. The person in the red house lives immediately to the right of the tennis enthusiast.
8. The tea drinker enjoys golf.
9. The coffee drinker lives next to the Dane.
10. The person who drinks milk and the person in the yellow house live two houses apart.
11. The coffee drinker and the juice drinker are neighbours.
12. The person in the white house is the Swede.
13. The person in the red house lives immediately to the right of the person who keeps the cat.
14. The milk drinker is the Spaniard.
15. The person in the red house drinks juice.
16. The Swede works as the doctor.
17. The baker and the dog owner live in adjacent houses.
18. The owner of the rabbit lives in house 4.
19. The bird owner and the German are neighbours.
20. The farmer lives somewhere to the left of the person in the purple house.
21. The person in the green house lives immediately to the right of the occupant of the blue house.
22. The owner of the fish lives directly to the left of the person who enjoys painting.
23. The hiking enthusiast lives in the sixth house.
24. The Spaniard and the person who keeps the fish are different people.
25. The person who enjoys cooking lives in house 2.

Answer format for this puzzle: {"1": {"<category>": "<value>", ...}, "2": {...}, ...} -- one entry per house number, giving the value of every category.

## Puzzle e4b-g1-05

Grid logic puzzle. Deduce which value of each category belongs to each house. Every value is used exactly once.

There are 6 houses in a row, numbered 1 to 6 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- nationality: Dane, Swede, Brit, Spaniard, German, Norwegian
- pet: bird, rabbit, dog, horse, fish, cat
- hobby: cooking, tennis, painting, golf, hiking, chess
- job: teacher, baker, pilot, doctor, farmer, lawyer
- drink: juice, coffee, milk, water, tea, cocoa
- color: yellow, white, purple, blue, red, green

Clues:
1. The person who drinks milk lives in the third house.
2. The cocoa drinker lives somewhere to the left of the person who drinks coffee.
3. Whoever lives in the green house lives somewhere to the right of the occupant of the yellow house.
4. The farmer lives directly to the left of the person who enjoys chess.
5. The owner of the horse lives in the yellow house.
6. The person who enjoys tennis lives immediately to the right of the Norwegian.
7. The baker enjoys cooking.
8. The cocoa drinker either lives in the blue house or lives in the yellow house.
9. The doctor and the person in the red house live in adjacent houses.
10. The person who drinks cocoa and the teacher live two houses apart.
11. The person in the green house drinks tea.
12. The person who enjoys hiking lives in the house just left of the one where the cat owner lives.
13. The juice drinker lives in the house just left of the one where the fish owner lives.
14. Whoever lives in the blue house lives in the house just left of the one where the person who enjoys hiking lives.
15. The teacher and the tennis enthusiast live two houses apart.
16. The person who keeps the bird lives somewhere to the left of the Swede.
17. The lawyer is the Swede.
18. The Spaniard lives directly to the left of the person in the purple house.
19. Whoever lives in the blue house and the person who drinks cocoa are not neighbours.
20. The Swede lives in the third house.
21. There is exactly one house between the person who enjoys painting and the pilot.
22. The person who keeps the cat lives in house 6.
23. The Brit and the Swede live two houses apart.
24. The person who keeps the fish and the pilot are not neighbours.
25. The Dane and the owner of the rabbit live two houses apart.

Answer format for this puzzle: {"1": {"<category>": "<value>", ...}, "2": {...}, ...} -- one entry per house number, giving the value of every category.

## Puzzle e4b-g0-05

Grid logic puzzle. Deduce which value of each category belongs to each house. Every value is used exactly once.

There are 6 houses in a row, numbered 1 to 6 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- pet: dog, bird, cat, fish, horse, rabbit
- color: green, white, red, yellow, blue, purple
- drink: cocoa, coffee, juice, milk, tea, water
- job: teacher, farmer, pilot, lawyer, baker, doctor
- hobby: painting, cooking, tennis, chess, golf, hiking
- nationality: German, Brit, Swede, Dane, Norwegian, Spaniard

Clues:
1. The Brit keeps the bird.
2. The baker enjoys chess.
3. The owner of the bird works as the lawyer.
4. The person who enjoys hiking and the person who drinks juice live two houses apart.
5. Whoever lives in the white house lives in the leftmost house.
6. The teacher and the tennis enthusiast live in adjacent houses.
7. The Dane lives next to the farmer.
8. The farmer enjoys tennis.
9. The chess enthusiast either lives in the blue house or lives in the yellow house.
10. Whoever lives in the purple house lives in the second house.
11. The Norwegian lives somewhere to the left of the juice drinker.
12. The owner of the horse either works as the farmer or works as the pilot.
13. There is exactly one house between the person who keeps the cat and whoever lives in the purple house.
14. There is exactly one house between the bird owner and whoever lives in the yellow house.
15. The person who drinks milk keeps the fish.
16. The coffee drinker works as the pilot.
17. The Norwegian lives in the house just left of the one where whoever lives in the blue house lives.
18. The cocoa drinker and the golf enthusiast live two houses apart.
19. The Swede keeps the rabbit.
20. The German lives in the house just left of the one where the person who enjoys cooking lives.
21. The Dane drinks tea.
22. The rabbit owner lives immediately to the right of whoever lives in the red house.
23. The farmer drinks juice.

Answer format for this puzzle: {"1": {"<category>": "<value>", ...}, "2": {...}, ...} -- one entry per house number, giving the value of every category.
