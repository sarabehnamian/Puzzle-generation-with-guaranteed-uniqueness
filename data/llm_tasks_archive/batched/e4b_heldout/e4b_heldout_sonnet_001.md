# Task: solve logic puzzles

Solve each puzzle below by reasoning. Every puzzle has exactly one solution. Work carefully; you
cannot run code. Give a complete answer for every puzzle even if unsure.

Output: write a single JSON object to the file D:\Puzzle-generation-with-guaranteed-uniqueness\data\llm_tasks\e4b_heldout\e4b_heldout_sonnet_001.out.json with this exact structure
{"answers": [{"id": "<puzzle id>", "answer": <answer>}, ...]}
where <answer> has the format stated for each puzzle.

The puzzles follow.


## Puzzle e4b-g0-02

Grid logic puzzle. Deduce which value of each category belongs to each house. Every value is used exactly once.

There are 6 houses in a row, numbered 1 to 6 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- job: baker, pilot, lawyer, doctor, teacher, farmer
- hobby: tennis, cooking, hiking, painting, golf, chess
- drink: cocoa, coffee, juice, water, tea, milk
- pet: fish, rabbit, bird, cat, dog, horse
- color: green, purple, blue, yellow, red, white
- nationality: Spaniard, German, Swede, Brit, Norwegian, Dane

Clues:
1. The Dane and the Norwegian live two houses apart.
2. The person who enjoys golf does not live in the yellow house.
3. There is exactly one house between the baker and the tea drinker.
4. The water drinker lives in the first house.
5. The German lives somewhere to the left of the hiking enthusiast.
6. The Brit and the person in the purple house live two houses apart.
7. The person in the blue house is the Spaniard.
8. The person who enjoys tennis lives directly to the left of the doctor.
9. The cooking enthusiast either works as the baker or works as the lawyer.
10. The person who drinks milk lives somewhere to the left of the hiking enthusiast.
11. The farmer either lives in the purple house or lives in the red house.
12. The person who keeps the horse enjoys chess.
13. The cocoa drinker either enjoys chess or enjoys painting.
14. The lawyer is the Swede.
15. The pilot lives in house 4.
16. The occupant of the white house lives directly to the left of the golf enthusiast.
17. The occupant of the red house lives in house 1.
18. The occupant of the green house enjoys chess.
19. The juice drinker lives in the white house.
20. The owner of the fish either is the Spaniard or is the Swede.
21. The Spaniard lives in house 2.
22. The owner of the dog lives in the yellow house.
23. The pilot is the Dane.
24. The owner of the cat and the person who drinks coffee are not neighbours.
25. The person who keeps the bird drinks milk.

Answer format for this puzzle: {"1": {"<category>": "<value>", ...}, "2": {...}, ...} -- one entry per house number, giving the value of every category.

## Puzzle e4b-g0-00

Grid logic puzzle. Deduce which value of each category belongs to each house. Every value is used exactly once.

There are 6 houses in a row, numbered 1 to 6 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- drink: cocoa, tea, milk, water, juice, coffee
- color: white, green, purple, yellow, red, blue
- pet: dog, cat, bird, rabbit, horse, fish
- hobby: chess, hiking, tennis, cooking, painting, golf
- job: farmer, lawyer, pilot, baker, doctor, teacher
- nationality: German, Norwegian, Brit, Swede, Spaniard, Dane

Clues:
1. The person who enjoys tennis drinks cocoa.
2. The doctor either is the Brit or is the Norwegian.
3. The person who enjoys hiking lives in the house just left of the one where the person who enjoys golf lives.
4. There is exactly one house between the German and the Swede.
5. The person who enjoys hiking works as the pilot.
6. The person who keeps the cat lives in the second house.
7. There is exactly one house between the person who drinks water and whoever lives in the yellow house.
8. The teacher enjoys tennis.
9. The person who enjoys chess lives next to the juice drinker.
10. The owner of the dog either works as the farmer or works as the pilot.
11. Whoever lives in the red house lives in the house just left of the one where the occupant of the blue house lives.
12. The person in the white house either works as the doctor or works as the lawyer.
13. The Swede drinks coffee.
14. There is exactly one house between the person who keeps the cat and the lawyer.
15. The teacher lives in the blue house.
16. The person who enjoys golf works as the baker.
17. The pilot is the Swede.
18. The Spaniard does not live in house 6.
19. The person who enjoys cooking keeps the horse.
20. The person who enjoys cooking lives next to the water drinker.
21. The owner of the cat lives in the purple house.
22. The chess enthusiast is the Brit.
23. The person who enjoys painting does not keep the fish.
24. Whoever lives in the white house lives at one end of the row.
25. The bird owner lives immediately to the right of the cat owner.
26. The tea drinker lives in a lower-numbered house than the person who drinks milk.

Answer format for this puzzle: {"1": {"<category>": "<value>", ...}, "2": {...}, ...} -- one entry per house number, giving the value of every category.

## Puzzle e4b-g0-06

Grid logic puzzle. Deduce which value of each category belongs to each house. Every value is used exactly once.

There are 6 houses in a row, numbered 1 to 6 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- drink: juice, cocoa, milk, coffee, tea, water
- nationality: Brit, German, Norwegian, Spaniard, Dane, Swede
- pet: dog, cat, horse, fish, bird, rabbit
- color: white, purple, yellow, green, red, blue
- job: farmer, baker, teacher, pilot, lawyer, doctor
- hobby: painting, tennis, hiking, golf, chess, cooking

Clues:
1. The person in the blue house lives immediately to the right of the Brit.
2. The teacher lives in a lower-numbered house than the person who enjoys painting.
3. The cooking enthusiast and whoever lives in the yellow house live two houses apart.
4. The person who drinks juice lives in the white house.
5. The teacher lives in the white house.
6. The Dane lives directly to the left of the farmer.
7. The owner of the horse lives in the purple house.
8. The tennis enthusiast is the Spaniard.
9. The person who keeps the bird and the owner of the fish are not neighbours.
10. The person who enjoys golf either works as the farmer or works as the pilot.
11. The person who drinks coffee and the Norwegian live in adjacent houses.
12. The chess enthusiast lives in house 2.
13. The cocoa drinker and the Spaniard live two houses apart.
14. The tennis enthusiast lives in the house just left of the one where the cooking enthusiast lives.
15. The rabbit owner lives in the house just left of the one where the tennis enthusiast lives.
16. The bird owner lives in house 2.
17. The Dane and the person who drinks milk are different people.
18. The Swede enjoys golf.
19. The occupant of the red house works as the doctor.
20. The Brit lives in the white house.
21. The German keeps the dog.
22. The occupant of the white house lives immediately to the right of the person who drinks water.
23. The baker lives in the green house.
24. The golf enthusiast lives in house 3.
25. The doctor and the person who enjoys tennis live in adjacent houses.

Answer format for this puzzle: {"1": {"<category>": "<value>", ...}, "2": {...}, ...} -- one entry per house number, giving the value of every category.

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
