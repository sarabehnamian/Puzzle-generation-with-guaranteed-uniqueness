# Task: solve logic puzzles

Solve each puzzle below by reasoning. Every puzzle has exactly one solution. Work carefully; you
cannot run code. Give a complete answer for every puzzle even if unsure.

Output: write a single JSON object to the file D:\Puzzle-generation-with-guaranteed-uniqueness\data\llm_tasks\e4b_eval_g1\e4b_eval_g1_haiku_002.out.json with this exact structure
{"answers": [{"id": "<puzzle id>", "answer": <answer>}, ...]}
where <answer> has the format stated for each puzzle.

The puzzles follow.


## Puzzle e4b-g1-06

Grid logic puzzle. Deduce which value of each category belongs to each house. Every value is used exactly once.

There are 6 houses in a row, numbered 1 to 6 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- color: green, purple, red, yellow, blue, white
- hobby: golf, tennis, cooking, hiking, painting, chess
- job: teacher, doctor, pilot, lawyer, farmer, baker
- nationality: Norwegian, Brit, German, Spaniard, Dane, Swede
- pet: bird, fish, dog, rabbit, horse, cat
- drink: coffee, juice, cocoa, water, milk, tea

Clues:
1. The coffee drinker either enjoys cooking or enjoys tennis.
2. The horse owner lives in the house just left of the one where the person who keeps the bird lives.
3. The farmer lives in the house just left of the one where the coffee drinker lives.
4. The teacher lives next to the pilot.
5. The lawyer lives immediately to the right of the person who keeps the rabbit.
6. The baker and the person who drinks cocoa live in adjacent houses.
7. The Norwegian and whoever lives in the green house are different people.
8. The person who keeps the fish lives directly to the left of whoever lives in the yellow house.
9. The doctor and the horse owner are neighbours.
10. The person in the blue house and the person who drinks milk live two houses apart.
11. The Brit lives directly to the left of the person who drinks tea.
12. The Spaniard lives in house 3.
13. The occupant of the purple house lives in house 5.
14. The owner of the dog either works as the doctor or works as the pilot.
15. The person who enjoys hiking keeps the dog.
16. The occupant of the yellow house lives in the house just left of the one where the person who enjoys hiking lives.
17. The person who enjoys tennis lives in the house just left of the one where the Dane lives.
18. The German lives in the house just left of the one where the Swede lives.
19. The person who enjoys painting lives in the white house.
20. The golf enthusiast works as the baker.
21. The tennis enthusiast lives somewhere to the right of the painting enthusiast.
22. The milk drinker lives immediately to the right of the Swede.
23. The doctor does not live next to the person who drinks milk.
24. The person in the blue house either drinks juice or drinks tea.
25. The coffee drinker lives in the green house.
26. The person who drinks cocoa lives in a lower-numbered house than the person who keeps the horse.

Answer format for this puzzle: {"1": {"<category>": "<value>", ...}, "2": {...}, ...} -- one entry per house number, giving the value of every category.

## Puzzle e4b-g1-03

Grid logic puzzle. Deduce which value of each category belongs to each house. Every value is used exactly once.

There are 6 houses in a row, numbered 1 to 6 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- drink: water, milk, juice, cocoa, tea, coffee
- color: purple, white, red, yellow, blue, green
- nationality: German, Dane, Swede, Norwegian, Spaniard, Brit
- hobby: cooking, golf, hiking, chess, painting, tennis
- job: pilot, baker, teacher, doctor, lawyer, farmer
- pet: horse, rabbit, cat, fish, bird, dog

Clues:
1. The coffee drinker lives next to the cocoa drinker.
2. The person who enjoys cooking is the German.
3. The tea drinker works as the baker.
4. The person who drinks water enjoys painting.
5. The Norwegian lives directly to the left of the owner of the fish.
6. The occupant of the white house is the Brit.
7. Whoever lives in the yellow house works as the pilot.
8. The Dane lives in the third house.
9. The owner of the bird and the lawyer live two houses apart.
10. The Spaniard lives somewhere to the right of the occupant of the red house.
11. The Brit and whoever lives in the purple house are neighbours.
12. The person who drinks milk lives immediately to the right of the baker.
13. The lawyer and the person who drinks milk live two houses apart.
14. The occupant of the blue house lives in the house just left of the one where the Brit lives.
15. The person who enjoys chess and the doctor are neighbours.
16. The occupant of the red house lives in a lower-numbered house than the person who keeps the rabbit.
17. The person who drinks juice either keeps the horse or keeps the rabbit.
18. The teacher lives directly to the left of the occupant of the blue house.
19. The person who enjoys tennis drinks milk.
20. The person who keeps the fish and the owner of the horse are neighbours.
21. The Spaniard enjoys golf.
22. The lawyer either drinks milk or drinks water.
23. The cocoa drinker lives in house 5.
24. The dog owner drinks water.
25. The person who keeps the cat lives in a lower-numbered house than the owner of the fish.

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
