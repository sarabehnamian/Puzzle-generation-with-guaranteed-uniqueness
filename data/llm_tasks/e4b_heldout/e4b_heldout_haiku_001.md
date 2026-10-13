# Task: solve logic puzzles

Solve each puzzle below by reasoning. Every puzzle has exactly one solution. Work carefully; you
cannot run code. Give a complete answer for every puzzle even if unsure.

Output: write a single JSON object to the file /home/user/Puzzle-generation-with-guaranteed-uniqueness/data/llm_tasks/e4b_heldout/e4b_heldout_haiku_001.out.json with this exact structure
{"answers": [{"id": "<puzzle id>", "answer": <answer>}, ...]}
where <answer> has the format stated for each puzzle.

The puzzles follow.


## Puzzle e4b-g0-03

Grid logic puzzle. Deduce which value of each category belongs to each house. Every value is used exactly once.

There are 6 houses in a row, numbered 1 to 6 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- nationality: Spaniard, Swede, Dane, Norwegian, Brit, German
- drink: tea, water, coffee, juice, milk, cocoa
- job: lawyer, farmer, doctor, baker, pilot, teacher
- color: red, purple, green, blue, yellow, white
- hobby: chess, painting, tennis, golf, hiking, cooking
- pet: bird, cat, fish, rabbit, horse, dog

Clues:
1. The rabbit owner enjoys tennis.
2. Whoever lives in the blue house lives in house 2.
3. The juice drinker lives somewhere to the right of the occupant of the blue house.
4. The person who keeps the cat lives somewhere to the left of the Swede.
5. There is exactly one house between the cooking enthusiast and the occupant of the yellow house.
6. The owner of the dog drinks juice.
7. The doctor is the Swede.
8. Whoever lives in the purple house lives in the leftmost house.
9. The doctor lives immediately to the right of the person who drinks coffee.
10. The Dane and whoever lives in the green house are neighbours.
11. The golf enthusiast and the teacher live two houses apart.
12. The person who drinks milk is the Dane.
13. The pilot lives in the red house.
14. The cooking enthusiast lives in a lower-numbered house than the person who drinks tea.
15. The Swede either drinks coffee or drinks tea.
16. The bird owner lives immediately to the right of the Spaniard.
17. The person who drinks cocoa and the person who keeps the horse live in adjacent houses.
18. The occupant of the green house lives at one end of the row.
19. The doctor lives in a lower-numbered house than the lawyer.
20. The owner of the rabbit lives directly to the left of the bird owner.
21. The chess enthusiast and the tennis enthusiast live in adjacent houses.
22. The person who enjoys golf lives directly to the left of the painting enthusiast.
23. The Brit lives directly to the left of the farmer.
24. Whoever lives in the green house either is the Norwegian or is the Swede.
25. The owner of the cat either is the Brit or is the Dane.
26. The Brit enjoys chess.

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

## Puzzle e4b-g0-02

Grid logic puzzle. Deduce which value of each category belongs to each house. Every value is used exactly once.

There are 6 houses in a row, numbered 1 to 6 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- job: lawyer, farmer, baker, pilot, doctor, teacher
- hobby: tennis, hiking, golf, chess, painting, cooking
- pet: rabbit, bird, fish, cat, dog, horse
- color: green, blue, white, yellow, red, purple
- drink: cocoa, juice, milk, tea, coffee, water
- nationality: Brit, Norwegian, German, Swede, Spaniard, Dane

Clues:
1. The Norwegian drinks juice.
2. The person who enjoys hiking is the Norwegian.
3. The person who drinks cocoa enjoys golf.
4. The water drinker lives in the first house.
5. The person who keeps the fish works as the lawyer.
6. The person who keeps the bird and the person in the red house live in adjacent houses.
7. The person in the blue house lives in house 1.
8. The teacher lives immediately to the right of the person who enjoys tennis.
9. The person in the yellow house lives in a lower-numbered house than the Swede.
10. The owner of the horse lives directly to the left of the baker.
11. The person in the purple house either drinks juice or drinks tea.
12. The painting enthusiast works as the pilot.
13. The Norwegian and the owner of the rabbit live in adjacent houses.
14. The coffee drinker enjoys painting.
15. The Dane lives next to the person who keeps the rabbit.
16. The person who keeps the rabbit is the Brit.
17. The bird owner lives in the sixth house.
18. The cat owner and the German are neighbours.
19. Whoever lives in the green house lives immediately to the right of the person who enjoys cooking.
20. The occupant of the green house enjoys golf.
21. The person who keeps the rabbit lives directly to the left of whoever lives in the green house.
22. The farmer lives directly to the left of the baker.
23. The person who drinks milk lives immediately to the right of the dog owner.

Answer format for this puzzle: {"1": {"<category>": "<value>", ...}, "2": {...}, ...} -- one entry per house number, giving the value of every category.
