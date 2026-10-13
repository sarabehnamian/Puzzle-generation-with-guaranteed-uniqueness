# Task: solve logic puzzles

Solve each puzzle below by reasoning. Every puzzle has exactly one solution. Work carefully; you
cannot run code. Give a complete answer for every puzzle even if unsure.

Output: write a single JSON object to the file /home/user/Puzzle-generation-with-guaranteed-uniqueness/data/llm_tasks/e4b_eval_g0/e4b_eval_g0_haiku_001.out.json with this exact structure
{"answers": [{"id": "<puzzle id>", "answer": <answer>}, ...]}
where <answer> has the format stated for each puzzle.

The puzzles follow.


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
