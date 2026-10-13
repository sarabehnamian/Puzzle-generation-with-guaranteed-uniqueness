# Task: solve logic puzzles

Solve each puzzle below by reasoning. Every puzzle has exactly one solution. Work carefully; you
cannot run code. Give a complete answer for every puzzle even if unsure.

Output: write a single JSON object to the file /home/user/Puzzle-generation-with-guaranteed-uniqueness/data/llm_tasks/e4b_heldout/e4b_heldout_sonnet_001.out.json with this exact structure
{"answers": [{"id": "<puzzle id>", "answer": <answer>}, ...]}
where <answer> has the format stated for each puzzle.

The puzzles follow.


## Puzzle e4b-g0-06

Grid logic puzzle. Deduce which value of each category belongs to each house. Every value is used exactly once.

There are 6 houses in a row, numbered 1 to 6 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- nationality: Dane, Swede, Brit, Spaniard, German, Norwegian
- pet: bird, rabbit, dog, horse, fish, cat
- hobby: cooking, tennis, painting, golf, hiking, chess
- job: teacher, baker, pilot, doctor, farmer, lawyer
- drink: juice, coffee, milk, water, tea, cocoa
- color: yellow, white, purple, blue, red, green

Clues:
1. The occupant of the green house lives somewhere to the right of whoever lives in the yellow house.
2. Whoever lives in the blue house lives in house 4.
3. The person who enjoys hiking lives in the house just left of the one where the owner of the cat lives.
4. The Spaniard lives directly to the left of whoever lives in the purple house.
5. The milk drinker lives in the third house.
6. The person who keeps the fish does not live next to the pilot.
7. The fish owner lives immediately to the right of the person who drinks juice.
8. The Brit lives in house 5.
9. The person who drinks cocoa and the teacher live two houses apart.
10. The cocoa drinker either lives in the blue house or lives in the yellow house.
11. The owner of the horse lives in the yellow house.
12. The doctor lives next to the person in the red house.
13. The occupant of the green house drinks tea.
14. The painting enthusiast and the pilot live two houses apart.
15. The Norwegian lives directly to the left of the tennis enthusiast.
16. The cocoa drinker lives somewhere to the left of the coffee drinker.
17. There is exactly one house between the teacher and the person who enjoys tennis.
18. The person who enjoys cooking works as the baker.
19. The owner of the bird lives somewhere to the left of the Swede.
20. The Swede lives in the third house.
21. The lawyer is the Swede.
22. The farmer lives in the house just left of the one where the person who enjoys chess lives.
23. The cat owner lives in house 6.
24. There is exactly one house between the Dane and the person who keeps the rabbit.

Answer format for this puzzle: {"1": {"<category>": "<value>", ...}, "2": {...}, ...} -- one entry per house number, giving the value of every category.

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

## Puzzle e4b-g0-00

Grid logic puzzle. Deduce which value of each category belongs to each house. Every value is used exactly once.

There are 6 houses in a row, numbered 1 to 6 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- pet: rabbit, dog, bird, cat, horse, fish
- drink: milk, juice, water, coffee, cocoa, tea
- color: blue, purple, yellow, red, white, green
- nationality: Dane, Spaniard, German, Swede, Norwegian, Brit
- job: doctor, baker, teacher, pilot, farmer, lawyer
- hobby: chess, painting, cooking, golf, tennis, hiking

Clues:
1. The person who enjoys golf drinks coffee.
2. The Swede and the occupant of the white house live two houses apart.
3. The baker and the cocoa drinker live in adjacent houses.
4. The person who keeps the dog lives somewhere to the left of the tea drinker.
5. The person who enjoys hiking lives in the green house.
6. The doctor and the occupant of the red house live in adjacent houses.
7. The Brit drinks tea.
8. The painting enthusiast lives immediately to the right of the person who keeps the rabbit.
9. The person who drinks water lives in the fifth house.
10. The farmer lives directly to the left of the owner of the rabbit.
11. There is exactly one house between the person who keeps the cat and the lawyer.
12. The person who drinks juice lives directly to the left of the owner of the cat.
13. The person who enjoys chess lives in the yellow house.
14. The occupant of the blue house lives in the third house.
15. The juice drinker lives in house 2.
16. The owner of the bird is the Dane.
17. The person in the purple house lives next to the Spaniard.
18. The pilot keeps the horse.
19. The teacher enjoys tennis.
20. The person who drinks coffee lives in the last house.
21. Whoever lives in the green house and whoever lives in the red house are neighbours.
22. The cocoa drinker and the Norwegian live in adjacent houses.
23. The tea drinker and the tennis enthusiast live two houses apart.

Answer format for this puzzle: {"1": {"<category>": "<value>", ...}, "2": {...}, ...} -- one entry per house number, giving the value of every category.
