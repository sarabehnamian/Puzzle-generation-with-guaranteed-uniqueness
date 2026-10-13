# Task: solve logic puzzles

Solve each puzzle below by reasoning. Every puzzle has exactly one solution. Work carefully; you
cannot run code. Give a complete answer for every puzzle even if unsure.

Output: write a single JSON object to the file /home/user/Puzzle-generation-with-guaranteed-uniqueness/data/llm_tasks/e4b_eval_g1/e4b_eval_g1_haiku_004.out.json with this exact structure
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

## Puzzle e4b-g0-01

Grid logic puzzle. Deduce which value of each category belongs to each house. Every value is used exactly once.

There are 6 houses in a row, numbered 1 to 6 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- pet: horse, fish, rabbit, dog, bird, cat
- hobby: hiking, tennis, cooking, painting, chess, golf
- job: doctor, farmer, teacher, lawyer, pilot, baker
- drink: coffee, juice, water, cocoa, tea, milk
- color: red, yellow, white, purple, blue, green
- nationality: Swede, German, Norwegian, Brit, Dane, Spaniard

Clues:
1. The bird owner lives in the house just left of the one where the baker lives.
2. The person who drinks milk lives directly to the left of the Norwegian.
3. The person who enjoys chess either keeps the cat or keeps the rabbit.
4. The person in the blue house is the Norwegian.
5. The Brit lives in the fifth house.
6. The person who keeps the rabbit enjoys golf.
7. The Spaniard works as the pilot.
8. The tennis enthusiast lives immediately to the right of the Norwegian.
9. The person who keeps the horse and the painting enthusiast are neighbours.
10. The cocoa drinker and the person who keeps the rabbit live in adjacent houses.
11. The person who drinks coffee lives next to the occupant of the white house.
12. There is exactly one house between the person in the purple house and whoever lives in the white house.
13. The owner of the rabbit drinks juice.
14. The Dane lives in the sixth house.
15. The cooking enthusiast either lives in the green house or lives in the purple house.
16. The teacher drinks tea.
17. The doctor lives in house 3.
18. The person who enjoys chess lives in house 4.
19. The person who drinks tea keeps the fish.
20. The bird owner is the German.
21. The owner of the rabbit lives immediately to the right of the occupant of the yellow house.
22. The German lives somewhere to the right of the person in the yellow house.
23. Whoever lives in the green house either works as the doctor or works as the farmer.
24. The person who drinks tea lives in the red house.

Answer format for this puzzle: {"1": {"<category>": "<value>", ...}, "2": {...}, ...} -- one entry per house number, giving the value of every category.

## Puzzle e4b-g1-09

Grid logic puzzle. Deduce which value of each category belongs to each house. Every value is used exactly once.

There are 6 houses in a row, numbered 1 to 6 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- color: purple, blue, white, yellow, red, green
- job: farmer, doctor, pilot, lawyer, teacher, baker
- pet: dog, bird, fish, horse, rabbit, cat
- hobby: hiking, chess, painting, golf, cooking, tennis
- drink: cocoa, coffee, milk, water, juice, tea
- nationality: Spaniard, Swede, German, Dane, Brit, Norwegian

Clues:
1. Whoever lives in the white house lives in the house just left of the one where the lawyer lives.
2. There is exactly one house between the person who keeps the rabbit and the tea drinker.
3. The German and the person who enjoys tennis live in adjacent houses.
4. The juice drinker enjoys chess.
5. There is exactly one house between the German and the teacher.
6. The occupant of the blue house lives immediately to the right of the German.
7. The person in the yellow house and the pilot are different people.
8. The Norwegian lives directly to the left of the person who drinks juice.
9. There is exactly one house between the Brit and the person who keeps the dog.
10. The cocoa drinker lives in the red house.
11. The painting enthusiast keeps the bird.
12. The milk drinker and the person who drinks tea are neighbours.
13. The person who keeps the fish lives directly to the left of the Dane.
14. The Brit lives directly to the left of the person who enjoys golf.
15. The lawyer and the teacher are neighbours.
16. The baker and the German live two houses apart.
17. The Brit drinks water.
18. Whoever lives in the red house is the Norwegian.
19. The hiking enthusiast keeps the rabbit.
20. The Spaniard lives next to the occupant of the yellow house.
21. The pilot does not live in the fifth house.
22. The occupant of the red house and the occupant of the yellow house live two houses apart.
23. The cat owner is the Brit.
24. Whoever lives in the green house lives in one of the two end houses.
25. The owner of the rabbit lives somewhere to the right of the German.
26. Whoever lives in the purple house and the occupant of the red house are neighbours.
27. The person who keeps the dog lives in the house just left of the one where the Spaniard lives.
28. The doctor lives in one of the two end houses.

Answer format for this puzzle: {"1": {"<category>": "<value>", ...}, "2": {...}, ...} -- one entry per house number, giving the value of every category.
