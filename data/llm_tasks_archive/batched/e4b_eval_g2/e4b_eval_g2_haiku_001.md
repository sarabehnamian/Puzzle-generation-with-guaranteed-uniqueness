# Task: solve logic puzzles

Solve each puzzle below by reasoning. Every puzzle has exactly one solution. Work carefully; you
cannot run code. Give a complete answer for every puzzle even if unsure.

Output: write a single JSON object to the file D:\Puzzle-generation-with-guaranteed-uniqueness\data\llm_tasks\e4b_eval_g2\e4b_eval_g2_haiku_001.out.json with this exact structure
{"answers": [{"id": "<puzzle id>", "answer": <answer>}, ...]}
where <answer> has the format stated for each puzzle.

The puzzles follow.


## Puzzle e4b-g0-01

Grid logic puzzle. Deduce which value of each category belongs to each house. Every value is used exactly once.

There are 6 houses in a row, numbered 1 to 6 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- hobby: chess, golf, tennis, hiking, painting, cooking
- pet: horse, fish, rabbit, cat, bird, dog
- job: teacher, pilot, lawyer, baker, farmer, doctor
- color: yellow, blue, white, purple, green, red
- nationality: Brit, Norwegian, Swede, Spaniard, Dane, German
- drink: juice, milk, cocoa, tea, coffee, water

Clues:
1. The person in the green house lives next to the Norwegian.
2. The German lives somewhere to the left of the person who keeps the fish.
3. The person who keeps the dog works as the baker.
4. The person who enjoys golf lives at one end of the row.
5. There is exactly one house between the person who drinks cocoa and the milk drinker.
6. The hiking enthusiast lives immediately to the right of the doctor.
7. The person in the green house works as the lawyer.
8. Whoever lives in the green house and the person who enjoys tennis are not neighbours.
9. The Brit lives in the first house.
10. The person who drinks water keeps the dog.
11. The owner of the horse and the milk drinker live two houses apart.
12. The Swede keeps the rabbit.
13. Whoever lives in the blue house lives in the last house.
14. The cat owner and the tea drinker live in adjacent houses.
15. The person who enjoys golf lives directly to the left of the person who enjoys chess.
16. The teacher lives immediately to the right of the cat owner.
17. The owner of the fish works as the doctor.
18. The lawyer lives immediately to the right of the farmer.
19. The Dane lives next to the dog owner.
20. Whoever lives in the white house lives in the house just left of the one where the person who drinks juice lives.
21. The person in the red house keeps the cat.
22. The person in the yellow house lives in house 3.
23. The owner of the dog lives in the house just left of the one where the doctor lives.
24. There is exactly one house between the cooking enthusiast and the occupant of the white house.

Answer format for this puzzle: {"1": {"<category>": "<value>", ...}, "2": {...}, ...} -- one entry per house number, giving the value of every category.

## Puzzle e4b-g2-03

Grid logic puzzle. Deduce which value of each category belongs to each house. Every value is used exactly once.

There are 6 houses in a row, numbered 1 to 6 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- drink: juice, cocoa, milk, coffee, tea, water
- nationality: Brit, German, Norwegian, Spaniard, Dane, Swede
- pet: dog, cat, horse, fish, bird, rabbit
- color: white, purple, yellow, green, red, blue
- job: farmer, baker, teacher, pilot, lawyer, doctor
- hobby: painting, tennis, hiking, golf, chess, cooking

Clues:
1. The Brit lives in the white house.
2. Whoever lives in the white house works as the teacher.
3. The person in the red house works as the doctor.
4. The person who drinks water lives in the house just left of the one where whoever lives in the white house lives.
5. The baker lives in the green house.
6. The person in the purple house keeps the horse.
7. The person who enjoys golf either works as the farmer or works as the pilot.
8. The owner of the bird and the fish owner are not neighbours.
9. The milk drinker and the Dane are different people.
10. The golf enthusiast lives in the third house.
11. There is exactly one house between the person who drinks cocoa and the Spaniard.
12. The doctor and the person who enjoys tennis are neighbours.
13. The person who enjoys golf lives somewhere to the right of the person who keeps the bird.
14. The Dane lives directly to the left of the farmer.
15. The Brit lives directly to the left of the person in the blue house.
16. The person who keeps the rabbit lives directly to the left of the person who enjoys tennis.
17. The golf enthusiast is the Swede.
18. The German keeps the dog.
19. The person who drinks juice lives in the white house.
20. The coffee drinker and the Norwegian live in adjacent houses.
21. The person who enjoys tennis is the Spaniard.
22. The person who enjoys chess lives in house 2.
23. The teacher lives in a lower-numbered house than the painting enthusiast.
24. The person who enjoys cooking and the person in the yellow house live two houses apart.
25. The person who enjoys tennis lives in the house just left of the one where the cooking enthusiast lives.

Answer format for this puzzle: {"1": {"<category>": "<value>", ...}, "2": {...}, ...} -- one entry per house number, giving the value of every category.

## Puzzle e4b-g2-04

Grid logic puzzle. Deduce which value of each category belongs to each house. Every value is used exactly once.

There are 6 houses in a row, numbered 1 to 6 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- drink: juice, cocoa, milk, coffee, tea, water
- nationality: Brit, German, Norwegian, Spaniard, Dane, Swede
- pet: dog, cat, horse, fish, bird, rabbit
- color: white, purple, yellow, green, red, blue
- job: farmer, baker, teacher, pilot, lawyer, doctor
- hobby: painting, tennis, hiking, golf, chess, cooking

Clues:
1. The Dane lives in the house just left of the one where the farmer lives.
2. The teacher lives in the white house.
3. The tennis enthusiast lives immediately to the right of the rabbit owner.
4. The Dane and the person who drinks milk are different people.
5. The owner of the dog is the German.
6. The person who enjoys golf and the person who enjoys tennis live two houses apart.
7. The Spaniard enjoys tennis.
8. The horse owner lives in the purple house.
9. The bird owner and the fish owner are not neighbours.
10. The person who enjoys golf either works as the farmer or works as the pilot.
11. There is exactly one house between the person who enjoys cooking and the person in the yellow house.
12. The occupant of the blue house lives immediately to the right of the Brit.
13. The baker lives in the green house.
14. The doctor lives next to the person who enjoys tennis.
15. The person who enjoys painting lives somewhere to the right of the teacher.
16. The person in the white house drinks juice.
17. The Brit lives in the white house.
18. The doctor lives in the red house.
19. The cocoa drinker and the Spaniard live two houses apart.
20. The occupant of the white house lives immediately to the right of the water drinker.
21. The chess enthusiast lives in house 2.
22. The cooking enthusiast lives immediately to the right of the tennis enthusiast.
23. The bird owner lives in the second house.
24. The coffee drinker lives next to the Norwegian.
25. The person who enjoys golf is the Swede.

Answer format for this puzzle: {"1": {"<category>": "<value>", ...}, "2": {...}, ...} -- one entry per house number, giving the value of every category.

## Puzzle e4b-g2-00

Grid logic puzzle. Deduce which value of each category belongs to each house. Every value is used exactly once.

There are 6 houses in a row, numbered 1 to 6 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- hobby: chess, golf, tennis, hiking, painting, cooking
- pet: horse, fish, rabbit, cat, bird, dog
- job: teacher, pilot, lawyer, baker, farmer, doctor
- color: yellow, blue, white, purple, green, red
- nationality: Brit, Norwegian, Swede, Spaniard, Dane, German
- drink: juice, milk, cocoa, tea, coffee, water

Clues:
1. The teacher lives immediately to the right of the cat owner.
2. Whoever lives in the white house lives in the house just left of the one where the pilot lives.
3. The person who enjoys cooking and whoever lives in the white house live two houses apart.
4. The person in the green house works as the lawyer.
5. The owner of the fish works as the doctor.
6. Whoever lives in the blue house keeps the rabbit.
7. The horse owner and the person who drinks milk live two houses apart.
8. The person who keeps the horse does not live next to the Swede.
9. The person who enjoys hiking lives immediately to the right of the doctor.
10. The occupant of the blue house lives in one of the two end houses.
11. The doctor lives immediately to the right of the owner of the dog.
12. The owner of the horse and the Norwegian live in adjacent houses.
13. The Brit lives at one end of the row.
14. The occupant of the yellow house lives in house 3.
15. The dog owner drinks water.
16. There is exactly one house between the cocoa drinker and the person who drinks milk.
17. Whoever lives in the green house does not live next to the tennis enthusiast.
18. The golf enthusiast lives at one end of the row.
19. The Dane and the owner of the dog are neighbours.
20. The lawyer lives immediately to the right of the farmer.
21. The occupant of the red house keeps the cat.
22. The person who keeps the cat and the tea drinker are neighbours.
23. The baker keeps the dog.
24. The golf enthusiast lives in the house just left of the one where the chess enthusiast lives.
25. The person who keeps the rabbit is the Swede.
26. The person in the white house lives in the house just left of the one where the juice drinker lives.
27. The person who keeps the fish lives somewhere to the right of the German.
28. Whoever lives in the green house and the Norwegian are neighbours.

Answer format for this puzzle: {"1": {"<category>": "<value>", ...}, "2": {...}, ...} -- one entry per house number, giving the value of every category.
