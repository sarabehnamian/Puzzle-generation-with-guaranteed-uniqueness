# Task: solve logic puzzles

Solve each puzzle below by reasoning. Every puzzle has exactly one solution. Work carefully; you
cannot run code. Give a complete answer for every puzzle even if unsure.

Output: write a single JSON object to the file /home/user/Puzzle-generation-with-guaranteed-uniqueness/data/llm_tasks/e4b_eval_g2/e4b_eval_g2_haiku_000.out.json with this exact structure
{"answers": [{"id": "<puzzle id>", "answer": <answer>}, ...]}
where <answer> has the format stated for each puzzle.

The puzzles follow.


## Puzzle e4b-g2-11

Grid logic puzzle. Deduce which value of each category belongs to each house. Every value is used exactly once.

There are 6 houses in a row, numbered 1 to 6 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- color: purple, blue, white, yellow, red, green
- job: farmer, doctor, pilot, lawyer, teacher, baker
- pet: dog, bird, fish, horse, rabbit, cat
- hobby: hiking, chess, painting, golf, cooking, tennis
- drink: cocoa, coffee, milk, water, juice, tea
- nationality: Spaniard, Swede, German, Dane, Brit, Norwegian

Clues:
1. Whoever lives in the green house lives at one end of the row.
2. The doctor lives in the first house.
3. The lawyer and the pilot live in adjacent houses.
4. The German lives somewhere to the left of the owner of the rabbit.
5. The person who enjoys tennis lives directly to the left of the tea drinker.
6. The owner of the rabbit and the tea drinker live two houses apart.
7. There is exactly one house between the German and the teacher.
8. There is exactly one house between the baker and the German.
9. The person who keeps the bird enjoys painting.
10. The juice drinker enjoys chess.
11. Whoever lives in the blue house lives immediately to the right of the German.
12. The Norwegian lives in the red house.
13. The lawyer lives next to the teacher.
14. The Brit lives in the house just left of the one where the person who enjoys golf lives.
15. The person who enjoys cooking lives at one end of the row.
16. The person who keeps the dog lives directly to the left of the Spaniard.
17. The German and the tennis enthusiast are neighbours.
18. The pilot and the teacher are not neighbours.
19. The owner of the cat is the Brit.
20. The person who drinks milk lives next to the person who drinks tea.
21. Whoever lives in the purple house and the occupant of the red house are neighbours.
22. The person who drinks water is the Brit.
23. The person in the white house lives directly to the left of the lawyer.
24. The doctor enjoys cooking.
25. The Norwegian lives in the house just left of the one where the person who drinks juice lives.
26. The person who drinks cocoa lives in the red house.
27. The Brit and the dog owner live two houses apart.
28. The owner of the fish lives in the house just left of the one where the Dane lives.

Answer format for this puzzle: {"1": {"<category>": "<value>", ...}, "2": {...}, ...} -- one entry per house number, giving the value of every category.

## Puzzle e4b-g2-09

Grid logic puzzle. Deduce which value of each category belongs to each house. Every value is used exactly once.

There are 6 houses in a row, numbered 1 to 6 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- drink: juice, milk, coffee, tea, water, cocoa
- hobby: cooking, chess, painting, hiking, tennis, golf
- job: teacher, farmer, doctor, lawyer, baker, pilot
- color: red, white, green, blue, yellow, purple
- nationality: Swede, Dane, Brit, German, Spaniard, Norwegian
- pet: fish, cat, horse, bird, dog, rabbit

Clues:
1. The Spaniard drinks milk.
2. The Swede works as the doctor.
3. The person who drinks milk and whoever lives in the yellow house live two houses apart.
4. The hiking enthusiast lives in one of the two end houses.
5. Whoever lives in the red house lives immediately to the right of the person who enjoys tennis.
6. The person in the white house is the Swede.
7. The baker lives next to the person who keeps the dog.
8. The farmer lives somewhere to the left of the occupant of the purple house.
9. The occupant of the red house keeps the horse.
10. The coffee drinker and the person who enjoys hiking live in adjacent houses.
11. The occupant of the green house and the person in the yellow house are neighbours.
12. The person who keeps the fish lives in the house just left of the one where the person who enjoys painting lives.
13. The cooking enthusiast lives in the second house.
14. The cat owner lives directly to the left of the occupant of the red house.
15. Whoever lives in the blue house lives directly to the left of the occupant of the green house.
16. The person who keeps the bird and the German live in adjacent houses.
17. The coffee drinker lives next to the Dane.
18. The person who keeps the fish and the Spaniard are different people.
19. The person who drinks water does not live in the second house.
20. There is exactly one house between the Brit and the person in the red house.
21. The lawyer lives in the green house.
22. The teacher keeps the dog.
23. The person who drinks tea enjoys golf.
24. Whoever lives in the red house drinks juice.
25. There is exactly one house between the owner of the rabbit and the person who enjoys cooking.
26. The person who drinks coffee and the juice drinker are neighbours.

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

## Puzzle e4b-g2-05

Grid logic puzzle. Deduce which value of each category belongs to each house. Every value is used exactly once.

There are 6 houses in a row, numbered 1 to 6 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- nationality: Dane, Swede, Brit, Spaniard, German, Norwegian
- pet: bird, rabbit, dog, horse, fish, cat
- hobby: cooking, tennis, painting, golf, hiking, chess
- job: teacher, baker, pilot, doctor, farmer, lawyer
- drink: juice, coffee, milk, water, tea, cocoa
- color: yellow, white, purple, blue, red, green

Clues:
1. The coffee drinker lives somewhere to the right of the person who drinks cocoa.
2. There is exactly one house between the Dane and the owner of the rabbit.
3. The person in the yellow house lives somewhere to the left of whoever lives in the green house.
4. The teacher and the person who enjoys tennis live two houses apart.
5. The Brit lives in the fifth house.
6. The person who enjoys cooking lives next to the Spaniard.
7. The cat owner lives immediately to the right of the person who enjoys hiking.
8. The person who drinks cocoa and the teacher live two houses apart.
9. The person who drinks coffee and the Dane are neighbours.
10. The tea drinker lives in the green house.
11. The owner of the fish lives next to the person in the green house.
12. The cocoa drinker either lives in the blue house or lives in the yellow house.
13. The farmer lives directly to the left of the chess enthusiast.
14. The Norwegian lives directly to the left of the person who enjoys tennis.
15. There is exactly one house between the milk drinker and the person who drinks coffee.
16. The occupant of the blue house and the occupant of the purple house live in adjacent houses.
17. The owner of the bird lives in a lower-numbered house than the Swede.
18. The Swede lives in the third house.
19. The person who keeps the cat lives in the last house.
20. The lawyer is the Swede.
21. The person who enjoys painting and the pilot live two houses apart.
22. Whoever lives in the yellow house keeps the horse.
23. The doctor and whoever lives in the red house live in adjacent houses.
24. The person who keeps the fish and the pilot are not neighbours.
25. The owner of the fish lives immediately to the right of the person who drinks juice.
26. The cooking enthusiast works as the baker.
27. Whoever lives in the yellow house works as the pilot.
28. The person in the purple house lives immediately to the right of the Spaniard.

Answer format for this puzzle: {"1": {"<category>": "<value>", ...}, "2": {...}, ...} -- one entry per house number, giving the value of every category.
