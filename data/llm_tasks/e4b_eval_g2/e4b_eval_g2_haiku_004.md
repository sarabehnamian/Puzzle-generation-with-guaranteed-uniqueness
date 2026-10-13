# Task: solve logic puzzles

Solve each puzzle below by reasoning. Every puzzle has exactly one solution. Work carefully; you
cannot run code. Give a complete answer for every puzzle even if unsure.

Output: write a single JSON object to the file /home/user/Puzzle-generation-with-guaranteed-uniqueness/data/llm_tasks/e4b_eval_g2/e4b_eval_g2_haiku_004.out.json with this exact structure
{"answers": [{"id": "<puzzle id>", "answer": <answer>}, ...]}
where <answer> has the format stated for each puzzle.

The puzzles follow.


## Puzzle e4b-g1-00

Grid logic puzzle. Deduce which value of each category belongs to each house. Every value is used exactly once.

There are 6 houses in a row, numbered 1 to 6 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- pet: rabbit, dog, bird, cat, horse, fish
- drink: milk, juice, water, coffee, cocoa, tea
- color: blue, purple, yellow, red, white, green
- nationality: Dane, Spaniard, German, Swede, Norwegian, Brit
- job: doctor, baker, teacher, pilot, farmer, lawyer
- hobby: chess, painting, cooking, golf, tennis, hiking

Clues:
1. The dog owner lives in a lower-numbered house than the tea drinker.
2. The teacher enjoys tennis.
3. The cat owner lives immediately to the right of the juice drinker.
4. The Swede and the person in the white house live two houses apart.
5. The horse owner works as the pilot.
6. Whoever lives in the purple house lives next to the Spaniard.
7. The tea drinker and the tennis enthusiast live two houses apart.
8. The owner of the cat enjoys cooking.
9. The person who drinks cocoa and the owner of the dog live in adjacent houses.
10. The occupant of the blue house lives in house 3.
11. The owner of the bird is the Dane.
12. The Brit drinks tea.
13. The person who drinks cocoa and the Norwegian live in adjacent houses.
14. The hiking enthusiast lives in the green house.
15. Whoever lives in the green house lives next to the occupant of the red house.
16. The person who enjoys chess lives in the yellow house.
17. The farmer lives in the house just left of the one where the person who keeps the rabbit lives.
18. The doctor lives next to the person in the red house.
19. The baker lives next to the person who drinks cocoa.
20. The person who drinks coffee enjoys golf.
21. There is exactly one house between the person who keeps the cat and the lawyer.
22. The person who keeps the rabbit lives in the house just left of the one where the painting enthusiast lives.
23. The juice drinker lives in house 2.
24. The person who drinks milk lives in a lower-numbered house than the person who drinks juice.

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

## Puzzle e4b-g2-07

Grid logic puzzle. Deduce which value of each category belongs to each house. Every value is used exactly once.

There are 6 houses in a row, numbered 1 to 6 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- pet: rabbit, dog, bird, cat, horse, fish
- drink: milk, juice, water, coffee, cocoa, tea
- color: blue, purple, yellow, red, white, green
- nationality: Dane, Spaniard, German, Swede, Norwegian, Brit
- job: doctor, baker, teacher, pilot, farmer, lawyer
- hobby: chess, painting, cooking, golf, tennis, hiking

Clues:
1. The lawyer lives in the white house.
2. The cat owner lives immediately to the right of the juice drinker.
3. The person who enjoys chess lives in the yellow house.
4. The person in the blue house and the occupant of the green house are not neighbours.
5. The person who enjoys cooking keeps the cat.
6. The owner of the rabbit lives in the house just left of the one where the painting enthusiast lives.
7. The person who drinks tea lives somewhere to the right of the dog owner.
8. The cocoa drinker and the Norwegian are neighbours.
9. The person who drinks milk lives in one of the two end houses.
10. The person in the green house and the occupant of the red house are neighbours.
11. The person who enjoys chess drinks tea.
12. The cocoa drinker lives next to the person who keeps the dog.
13. The person who drinks juice lives somewhere to the right of the milk drinker.
14. The owner of the rabbit lives immediately to the right of the farmer.
15. Whoever lives in the purple house and the Spaniard live in adjacent houses.
16. The coffee drinker enjoys golf.
17. The Swede and whoever lives in the white house live two houses apart.
18. The tea drinker is the Brit.
19. The doctor and whoever lives in the red house are neighbours.
20. The Dane keeps the bird.
21. The owner of the cat and the lawyer live two houses apart.
22. The person who enjoys tennis works as the teacher.
23. The person who enjoys painting lives directly to the left of the horse owner.
24. The person who drinks tea and the person who enjoys tennis live two houses apart.
25. The baker and the person who drinks cocoa live in adjacent houses.
26. The owner of the horse works as the pilot.
27. The hiking enthusiast lives in the green house.

Answer format for this puzzle: {"1": {"<category>": "<value>", ...}, "2": {...}, ...} -- one entry per house number, giving the value of every category.

## Puzzle e4b-g2-06

Grid logic puzzle. Deduce which value of each category belongs to each house. Every value is used exactly once.

There are 6 houses in a row, numbered 1 to 6 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- nationality: Dane, Swede, Brit, Spaniard, German, Norwegian
- pet: bird, rabbit, dog, horse, fish, cat
- hobby: cooking, tennis, painting, golf, hiking, chess
- job: teacher, baker, pilot, doctor, farmer, lawyer
- drink: juice, coffee, milk, water, tea, cocoa
- color: yellow, white, purple, blue, red, green

Clues:
1. The owner of the bird lives in a lower-numbered house than the Swede.
2. The person who drinks cocoa lives somewhere to the left of the person who drinks coffee.
3. The milk drinker lives in the third house.
4. The Norwegian lives directly to the left of the tennis enthusiast.
5. The occupant of the yellow house keeps the horse.
6. The farmer lives directly to the left of the person who enjoys chess.
7. The Swede lives somewhere to the left of the Brit.
8. The Dane and the rabbit owner live two houses apart.
9. The teacher and the tennis enthusiast live two houses apart.
10. Whoever lives in the green house lives somewhere to the right of the person in the yellow house.
11. The tea drinker lives in the green house.
12. The German enjoys painting.
13. The person in the blue house lives in house 4.
14. Whoever lives in the purple house lives immediately to the right of the Spaniard.
15. The painting enthusiast and the pilot live two houses apart.
16. The doctor and whoever lives in the red house are neighbours.
17. The farmer lives next to the owner of the rabbit.
18. The juice drinker lives in the house just left of the one where the fish owner lives.
19. The person who keeps the cat lives at one end of the row.
20. The cat owner lives immediately to the right of the hiking enthusiast.
21. The person who drinks cocoa either lives in the blue house or lives in the yellow house.
22. The lawyer is the Swede.
23. The fish owner and the pilot are not neighbours.
24. The Swede lives in house 3.
25. The cooking enthusiast works as the baker.
26. The person who drinks cocoa and the teacher live two houses apart.

Answer format for this puzzle: {"1": {"<category>": "<value>", ...}, "2": {...}, ...} -- one entry per house number, giving the value of every category.
