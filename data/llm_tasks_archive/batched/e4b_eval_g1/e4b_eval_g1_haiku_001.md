# Task: solve logic puzzles

Solve each puzzle below by reasoning. Every puzzle has exactly one solution. Work carefully; you
cannot run code. Give a complete answer for every puzzle even if unsure.

Output: write a single JSON object to the file D:\Puzzle-generation-with-guaranteed-uniqueness\data\llm_tasks\e4b_eval_g1\e4b_eval_g1_haiku_001.out.json with this exact structure
{"answers": [{"id": "<puzzle id>", "answer": <answer>}, ...]}
where <answer> has the format stated for each puzzle.

The puzzles follow.


## Puzzle e4b-g1-13

Grid logic puzzle. Deduce which value of each category belongs to each house. Every value is used exactly once.

There are 6 houses in a row, numbered 1 to 6 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- drink: juice, cocoa, milk, coffee, tea, water
- nationality: Brit, German, Norwegian, Spaniard, Dane, Swede
- pet: dog, cat, horse, fish, bird, rabbit
- color: white, purple, yellow, green, red, blue
- job: farmer, baker, teacher, pilot, lawyer, doctor
- hobby: painting, tennis, hiking, golf, chess, cooking

Clues:
1. The Spaniard enjoys tennis.
2. The German keeps the dog.
3. The person who enjoys golf and the person who enjoys chess live in adjacent houses.
4. The Brit lives in the house just left of the one where the person in the blue house lives.
5. The person who enjoys cooking and whoever lives in the yellow house live two houses apart.
6. The doctor and the tennis enthusiast live in adjacent houses.
7. The person in the yellow house lives somewhere to the right of whoever lives in the green house.
8. The bird owner lives in the second house.
9. The person who enjoys golf is the Swede.
10. The person who enjoys chess lives in the second house.
11. The water drinker lives in the house just left of the one where whoever lives in the white house lives.
12. There is exactly one house between the person who drinks cocoa and the Spaniard.
13. The teacher lives in the white house.
14. Whoever lives in the white house drinks juice.
15. The person who keeps the bird and the fish owner are not neighbours.
16. The lawyer and the milk drinker live two houses apart.
17. The painting enthusiast lives somewhere to the right of the teacher.
18. Whoever lives in the white house is the Brit.
19. The rabbit owner lives in the house just left of the one where the person who enjoys tennis lives.
20. The occupant of the purple house keeps the horse.
21. The doctor lives in the red house.
22. The baker lives in the green house.
23. The person who enjoys golf either works as the farmer or works as the pilot.
24. The Dane lives in the house just left of the one where the farmer lives.
25. The tennis enthusiast lives in the house just left of the one where the cooking enthusiast lives.
26. The person who drinks coffee lives next to the Norwegian.

Answer format for this puzzle: {"1": {"<category>": "<value>", ...}, "2": {...}, ...} -- one entry per house number, giving the value of every category.

## Puzzle e4b-g0-04

Grid logic puzzle. Deduce which value of each category belongs to each house. Every value is used exactly once.

There are 6 houses in a row, numbered 1 to 6 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- drink: milk, water, tea, juice, coffee, cocoa
- nationality: Swede, Norwegian, Brit, German, Dane, Spaniard
- color: blue, yellow, white, red, purple, green
- pet: horse, cat, rabbit, fish, bird, dog
- job: teacher, doctor, lawyer, farmer, pilot, baker
- hobby: cooking, tennis, painting, hiking, golf, chess

Clues:
1. The person in the white house lives in the third house.
2. The person who keeps the bird lives directly to the left of the person who keeps the horse.
3. The Spaniard lives in the last house.
4. The cat owner lives directly to the left of the juice drinker.
5. The person who drinks cocoa lives at one end of the row.
6. The golf enthusiast lives in the fourth house.
7. The person who keeps the horse lives in the yellow house.
8. The baker lives in the house just left of the one where the occupant of the green house lives.
9. The chess enthusiast lives in one of the two end houses.
10. Whoever lives in the blue house lives in the sixth house.
11. The German keeps the fish.
12. There is exactly one house between the owner of the dog and the person who drinks milk.
13. There is exactly one house between the person in the blue house and the Norwegian.
14. Whoever lives in the purple house is the Dane.
15. The person who drinks tea works as the doctor.
16. The horse owner and the lawyer are neighbours.
17. The pilot lives somewhere to the right of the person who drinks tea.
18. The German works as the teacher.
19. The painting enthusiast keeps the rabbit.
20. The farmer keeps the bird.
21. The Swede lives in the fifth house.
22. The owner of the bird lives immediately to the right of the person who drinks coffee.
23. The golf enthusiast and the tennis enthusiast live two houses apart.
24. The hiking enthusiast lives next to the person in the white house.

Answer format for this puzzle: {"1": {"<category>": "<value>", ...}, "2": {...}, ...} -- one entry per house number, giving the value of every category.

## Puzzle e4b-g1-05

Grid logic puzzle. Deduce which value of each category belongs to each house. Every value is used exactly once.

There are 6 houses in a row, numbered 1 to 6 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- drink: milk, water, tea, juice, coffee, cocoa
- nationality: Swede, Norwegian, Brit, German, Dane, Spaniard
- color: blue, yellow, white, red, purple, green
- pet: horse, cat, rabbit, fish, bird, dog
- job: teacher, doctor, lawyer, farmer, pilot, baker
- hobby: cooking, tennis, painting, hiking, golf, chess

Clues:
1. The person who enjoys painting keeps the rabbit.
2. The Spaniard lives in the sixth house.
3. The person who keeps the horse lives immediately to the right of the person who keeps the bird.
4. The baker lives in the house just left of the one where the person in the green house lives.
5. The pilot lives somewhere to the right of the person who drinks tea.
6. The person who keeps the dog and the person who drinks milk live two houses apart.
7. The person who enjoys tennis either keeps the dog or keeps the fish.
8. The doctor drinks tea.
9. The person who drinks cocoa lives at one end of the row.
10. The farmer keeps the bird.
11. The German keeps the fish.
12. The person in the blue house lives in one of the two end houses.
13. There is exactly one house between the golf enthusiast and the tennis enthusiast.
14. The hiking enthusiast and whoever lives in the white house live in adjacent houses.
15. The person who keeps the horse lives in the yellow house.
16. The owner of the horse and the lawyer live in adjacent houses.
17. The coffee drinker lives directly to the left of the owner of the bird.
18. The juice drinker lives immediately to the right of the person who keeps the cat.
19. The pilot lives next to the person who enjoys tennis.
20. The golf enthusiast and the person who enjoys cooking live in adjacent houses.
21. The teacher is the German.
22. The Dane lives in the purple house.
23. Whoever lives in the white house lives in house 3.
24. The chess enthusiast lives in one of the two end houses.
25. Whoever lives in the blue house and the Norwegian live two houses apart.
26. The Swede lives in house 5.
27. The Norwegian lives in house 4.

Answer format for this puzzle: {"1": {"<category>": "<value>", ...}, "2": {...}, ...} -- one entry per house number, giving the value of every category.

## Puzzle e4b-g1-11

Grid logic puzzle. Deduce which value of each category belongs to each house. Every value is used exactly once.

There are 6 houses in a row, numbered 1 to 6 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- color: green, yellow, white, red, purple, blue
- job: teacher, farmer, pilot, baker, lawyer, doctor
- drink: cocoa, juice, milk, water, coffee, tea
- pet: horse, dog, bird, fish, rabbit, cat
- nationality: Spaniard, Swede, German, Brit, Dane, Norwegian
- hobby: hiking, golf, tennis, cooking, painting, chess

Clues:
1. The Norwegian lives in the house just left of the one where the German lives.
2. The Norwegian and the occupant of the yellow house are neighbours.
3. There is exactly one house between the person in the blue house and the doctor.
4. The owner of the cat lives next to the person in the purple house.
5. The cocoa drinker either works as the doctor or works as the pilot.
6. The German lives in the sixth house.
7. The owner of the dog either works as the lawyer or works as the teacher.
8. The baker either keeps the horse or keeps the rabbit.
9. The person who enjoys chess and the lawyer live two houses apart.
10. The occupant of the white house is the Brit.
11. The painting enthusiast drinks coffee.
12. The golf enthusiast works as the lawyer.
13. The water drinker and the Swede live in adjacent houses.
14. The farmer keeps the bird.
15. The farmer and the occupant of the red house live two houses apart.
16. The person in the white house enjoys tennis.
17. The person who enjoys golf lives next to the tea drinker.
18. The cooking enthusiast keeps the fish.
19. The person who enjoys hiking lives immediately to the right of the person who drinks water.
20. The person who keeps the rabbit lives directly to the left of the person who keeps the horse.
21. The person who drinks tea lives directly to the left of the occupant of the green house.
22. The person who keeps the rabbit either is the Dane or is the German.
23. Whoever lives in the yellow house lives in the house just left of the one where the person who keeps the horse lives.
24. The person in the green house and the person who enjoys tennis live in adjacent houses.
25. The juice drinker lives in the blue house.

Answer format for this puzzle: {"1": {"<category>": "<value>", ...}, "2": {...}, ...} -- one entry per house number, giving the value of every category.
