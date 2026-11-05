# Task: solve logic puzzles

Solve each puzzle below by reasoning. Every puzzle has exactly one solution. Work carefully; you
cannot run code. Give a complete answer for every puzzle even if unsure.

Output: write a single JSON object to the file D:\Puzzle-generation-with-guaranteed-uniqueness\data\llm_tasks\e3_solve\e3_zebra_opus_005.out.json with this exact structure
{"answers": [{"id": "<puzzle id>", "answer": <answer>}, ...]}
where <answer> has the format stated for each puzzle.

The puzzles follow.


## Puzzle zebra-00518

Grid logic puzzle. Deduce which value of each category belongs to each house. Every value is used exactly once.

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- color: white, red, yellow, blue, green
- pet: horse, cat, dog, rabbit, bird
- hobby: golf, cooking, painting, chess, hiking
- nationality: Brit, Spaniard, Norwegian, Dane, Swede

Clues:
1. The person who keeps the cat and the chess enthusiast are neighbours.
2. The Norwegian lives in the red house.
3. The golf enthusiast does not live next to the person in the red house.
4. The person who keeps the rabbit and the person in the white house live in adjacent houses.
5. The occupant of the blue house enjoys golf.
6. The occupant of the red house keeps the dog.
7. Whoever lives in the green house keeps the horse.
8. The cat owner lives directly to the left of the Spaniard.
9. The person who enjoys painting is the Dane.
10. The person who enjoys painting lives in the house just left of the one where the Swede lives.
11. The horse owner lives immediately to the right of the person who enjoys hiking.
12. Whoever lives in the red house lives immediately to the right of the owner of the rabbit.

Answer format for this puzzle: {"1": {"<category>": "<value>", ...}, "2": {...}, ...} -- one entry per house number, giving the value of every category.

## Puzzle zebra-01391-L1aug

Grid logic puzzle. Deduce which value of each category belongs to each house. Every value is used exactly once.

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- color: purple, blue, red, yellow, green
- drink: water, coffee, milk, tea, cocoa
- nationality: Dane, Spaniard, Swede, Norwegian, German
- job: pilot, doctor, lawyer, teacher, farmer

Clues:
1. The doctor lives in the fourth house.
2. The person in the red house lives in one of the two end houses.
3. The person in the red house lives in the first house.
4. The person who drinks water lives in the first house.
5. The person who drinks water does not live in the yellow house.
6. The occupant of the blue house and whoever lives in the purple house live in adjacent houses.
7. The person who drinks milk lives in one of the two end houses.
8. The occupant of the yellow house lives in the fourth house.
9. The German lives in the fourth house.
10. The Spaniard works as the teacher.
11. The person who drinks cocoa does not live in the yellow house.
12. There is exactly one house between the lawyer and the Spaniard.
13. The person who drinks milk is the Spaniard.
14. The person who drinks cocoa lives in the house just left of the one where the person in the yellow house lives.
15. The person who drinks milk lives immediately to the right of the coffee drinker.
16. The occupant of the blue house does not live in house 5.
17. The cocoa drinker and the German are neighbours.
18. The pilot lives somewhere to the left of the Norwegian.
19. The occupant of the green house and the person who drinks tea are not neighbours.
20. The pilot lives at one end of the row.
21. The person in the red house lives next to the Swede.
22. Whoever lives in the purple house lives directly to the left of the coffee drinker.
23. The pilot and the Swede live in adjacent houses.
24. The farmer lives directly to the left of the cocoa drinker.
25. The Dane and the lawyer are not neighbours.
26. The milk drinker and the person in the red house are different people.
27. The person who drinks coffee and whoever lives in the green house are neighbours.

Answer format for this puzzle: {"1": {"<category>": "<value>", ...}, "2": {...}, ...} -- one entry per house number, giving the value of every category.

## Puzzle zebra-00755

Grid logic puzzle. Deduce which value of each category belongs to each house. Every value is used exactly once.

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- nationality: Dane, Norwegian, Swede, German, Brit
- hobby: golf, hiking, tennis, chess, cooking
- drink: juice, cocoa, tea, milk, water
- job: farmer, lawyer, pilot, baker, teacher

Clues:
1. The teacher either enjoys golf or enjoys hiking.
2. The pilot lives in one of the two end houses.
3. The tennis enthusiast lives in house 2.
4. The baker lives in the fourth house.
5. The baker lives immediately to the right of the tea drinker.
6. There is exactly one house between the lawyer and the Swede.
7. The water drinker is the Dane.
8. The milk drinker is the Brit.
9. The Norwegian and the Swede are neighbours.
10. The Dane lives somewhere to the left of the pilot.
11. The Swede lives immediately to the right of the baker.
12. The Brit and the person who enjoys cooking live in adjacent houses.
13. The chess enthusiast lives next to the Swede.
14. The juice drinker is the Norwegian.
15. The hiking enthusiast lives somewhere to the left of the person who drinks juice.

Answer format for this puzzle: {"1": {"<category>": "<value>", ...}, "2": {...}, ...} -- one entry per house number, giving the value of every category.

## Puzzle zebra-00790

Grid logic puzzle. Deduce which value of each category belongs to each house. Every value is used exactly once.

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- hobby: hiking, painting, golf, tennis, cooking
- job: doctor, teacher, farmer, baker, pilot
- drink: tea, coffee, juice, cocoa, water
- color: blue, yellow, green, white, red

Clues:
1. The person in the green house lives in the fifth house.
2. The person who enjoys cooking and the water drinker live in adjacent houses.
3. The person who drinks water lives in the house just left of the one where the occupant of the white house lives.
4. The tennis enthusiast lives directly to the left of the golf enthusiast.
5. Whoever lives in the blue house and whoever lives in the yellow house live two houses apart.
6. The tea drinker lives in the house just left of the one where whoever lives in the yellow house lives.
7. There is exactly one house between the person who drinks coffee and the person who drinks water.
8. The teacher lives in house 4.
9. The water drinker lives immediately to the right of the baker.
10. The doctor lives in the last house.
11. The person who enjoys golf lives in house 5.
12. The pilot drinks juice.
13. The farmer and the person who enjoys hiking live two houses apart.

Answer format for this puzzle: {"1": {"<category>": "<value>", ...}, "2": {...}, ...} -- one entry per house number, giving the value of every category.

## Puzzle zebra-00551-L1aug

Grid logic puzzle. Deduce which value of each category belongs to each house. Every value is used exactly once.

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- nationality: Norwegian, German, Brit, Spaniard, Swede
- color: white, green, red, purple, yellow
- pet: horse, dog, cat, rabbit, fish
- job: doctor, lawyer, teacher, pilot, farmer

Clues:
1. The German lives in the fourth house.
2. The Norwegian lives in the third house.
3. The German works as the farmer.
4. The doctor and the pilot live in adjacent houses.
5. The owner of the dog lives directly to the left of the person who keeps the rabbit.
6. The person who keeps the dog and the pilot are neighbours.
7. There is exactly one house between the Brit and the German.
8. There is exactly one house between the person who keeps the fish and the pilot.
9. The rabbit owner lives in the second house.
10. The Norwegian lives immediately to the right of the Brit.
11. The person who keeps the dog lives directly to the left of the person in the white house.
12. The farmer either is the German or is the Norwegian.
13. The Brit and the owner of the dog are different people.
14. There is exactly one house between the cat owner and the occupant of the green house.
15. The Brit either works as the pilot or works as the teacher.
16. The doctor lives in the house just left of the one where whoever lives in the yellow house lives.
17. The teacher keeps the horse.
18. The Swede lives in house 5.
19. The person in the purple house lives in house 1.
20. The Spaniard and the doctor are different people.
21. The dog owner lives in the first house.
22. The person who keeps the horse either lives in the green house or lives in the yellow house.
23. The Brit lives next to the lawyer.
24. Whoever lives in the red house lives in the house just left of the one where the farmer lives.
25. The person in the white house lives somewhere to the left of the German.

Answer format for this puzzle: {"1": {"<category>": "<value>", ...}, "2": {...}, ...} -- one entry per house number, giving the value of every category.
