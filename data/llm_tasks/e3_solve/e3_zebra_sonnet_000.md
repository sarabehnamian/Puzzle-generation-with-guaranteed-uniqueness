# Task: solve logic puzzles

Solve each puzzle below by reasoning. Every puzzle has exactly one solution. Work carefully; you
cannot run code. Give a complete answer for every puzzle even if unsure.

Output: write a single JSON object to the file /home/user/Puzzle-generation-with-guaranteed-uniqueness/data/llm_tasks/e3_solve/e3_zebra_sonnet_000.out.json with this exact structure
{"answers": [{"id": "<puzzle id>", "answer": <answer>}, ...]}
where <answer> has the format stated for each puzzle.

The puzzles follow.


## Puzzle zebra-01412

Grid logic puzzle. Deduce which value of each category belongs to each house. Every value is used exactly once.

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- nationality: Brit, Norwegian, Swede, German, Spaniard
- drink: cocoa, water, juice, coffee, tea
- pet: rabbit, bird, dog, horse, cat
- hobby: tennis, golf, painting, hiking, chess

Clues:
1. The person who drinks coffee either enjoys golf or enjoys painting.
2. The tennis enthusiast lives immediately to the right of the juice drinker.
3. There is exactly one house between the owner of the dog and the person who enjoys painting.
4. The juice drinker lives directly to the left of the person who keeps the bird.
5. The golf enthusiast is not the Brit.
6. The German drinks tea.
7. The Norwegian lives in the leftmost house.
8. The dog owner and the owner of the rabbit live two houses apart.
9. The Norwegian and the painting enthusiast are neighbours.
10. The cocoa drinker and the owner of the dog are neighbours.
11. The golf enthusiast lives in the house just left of the one where the person who enjoys hiking lives.
12. The German enjoys painting.
13. The owner of the horse and the Spaniard live in adjacent houses.

Answer format for this puzzle: {"1": {"<category>": "<value>", ...}, "2": {...}, ...} -- one entry per house number, giving the value of every category.

## Puzzle zebra-00383

Grid logic puzzle. Deduce which value of each category belongs to each house. Every value is used exactly once.

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- color: purple, green, red, blue, yellow
- drink: tea, juice, milk, coffee, cocoa
- hobby: cooking, painting, hiking, chess, golf
- pet: dog, cat, fish, bird, rabbit

Clues:
1. The fish owner does not live in the red house.
2. The person who keeps the rabbit lives in a lower-numbered house than the golf enthusiast.
3. The cocoa drinker lives next to the rabbit owner.
4. Whoever lives in the blue house does not live next to the person who keeps the cat.
5. The person in the yellow house either keeps the cat or keeps the dog.
6. Whoever lives in the green house lives in a lower-numbered house than the occupant of the red house.
7. The person who enjoys painting lives in the green house.
8. The person who keeps the bird and the tea drinker live two houses apart.
9. The fish owner and the rabbit owner are not neighbours.
10. The chess enthusiast and the cocoa drinker live two houses apart.
11. The person who drinks juice either lives in the blue house or lives in the purple house.
12. The person who drinks milk keeps the cat.
13. The owner of the rabbit lives immediately to the right of the coffee drinker.
14. The person who drinks juice lives directly to the left of the cooking enthusiast.

Answer format for this puzzle: {"1": {"<category>": "<value>", ...}, "2": {...}, ...} -- one entry per house number, giving the value of every category.

## Puzzle zebra-00618

Grid logic puzzle. Deduce which value of each category belongs to each house. Every value is used exactly once.

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- job: lawyer, doctor, baker, teacher, pilot
- drink: juice, milk, tea, water, cocoa
- nationality: Swede, German, Dane, Norwegian, Brit
- pet: dog, rabbit, fish, cat, horse

Clues:
1. The teacher drinks water.
2. The rabbit owner drinks tea.
3. The Norwegian and the Swede live two houses apart.
4. The dog owner lives immediately to the right of the pilot.
5. The milk drinker lives in the house just left of the one where the Swede lives.
6. The owner of the horse lives next to the owner of the rabbit.
7. The owner of the fish lives next to the person who drinks milk.
8. The doctor lives in the middle house.
9. The person who keeps the horse works as the doctor.
10. The Dane works as the lawyer.
11. The juice drinker lives in the third house.
12. The Brit and the person who keeps the horse live two houses apart.
13. The baker lives immediately to the right of the milk drinker.

Answer format for this puzzle: {"1": {"<category>": "<value>", ...}, "2": {...}, ...} -- one entry per house number, giving the value of every category.

## Puzzle zebra-01380-L1aug

Grid logic puzzle. Deduce which value of each category belongs to each house. Every value is used exactly once.

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- color: red, yellow, blue, white, green
- hobby: hiking, golf, tennis, painting, cooking
- job: pilot, teacher, doctor, farmer, baker
- pet: rabbit, cat, dog, bird, horse

Clues:
1. The owner of the bird lives somewhere to the left of whoever lives in the green house.
2. The dog owner enjoys tennis.
3. Whoever lives in the green house does not live next to the occupant of the yellow house.
4. The person who enjoys golf lives in one of the two end houses.
5. The occupant of the blue house enjoys tennis.
6. The owner of the rabbit does not live in the fifth house.
7. The doctor lives directly to the left of the person in the green house.
8. The farmer and the person in the red house live two houses apart.
9. The person who enjoys painting lives somewhere to the right of the golf enthusiast.
10. The farmer lives in the house just left of the one where the person who enjoys cooking lives.
11. The occupant of the yellow house is not the pilot.
12. The cat owner does not live next to the painting enthusiast.
13. The baker lives in the house just left of the one where the person who enjoys painting lives.
14. The teacher lives in the fourth house.
15. The person who keeps the dog works as the pilot.
16. The cooking enthusiast does not live in the first house.
17. There is exactly one house between the doctor and the person who enjoys tennis.
18. The doctor and the person in the yellow house are not neighbours.
19. The hiking enthusiast lives in the fourth house.
20. The teacher either enjoys hiking or enjoys tennis.
21. The occupant of the green house enjoys hiking.
22. The person in the green house works as the teacher.
23. Whoever lives in the blue house and the rabbit owner live two houses apart.
24. The owner of the rabbit lives in house 3.
25. The bird owner lives in the white house.
26. The person who enjoys cooking lives in the house just left of the one where the doctor lives.
27. The farmer either keeps the cat or keeps the dog.

Answer format for this puzzle: {"1": {"<category>": "<value>", ...}, "2": {...}, ...} -- one entry per house number, giving the value of every category.

## Puzzle zebra-00414-L1aug

Grid logic puzzle. Deduce which value of each category belongs to each house. Every value is used exactly once.

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- job: lawyer, farmer, doctor, pilot, baker
- hobby: tennis, painting, cooking, hiking, golf
- color: red, blue, white, green, yellow
- nationality: Spaniard, Swede, German, Dane, Brit

Clues:
1. The Dane lives in the house just left of the one where the Swede lives.
2. The Dane and the farmer live in adjacent houses.
3. The occupant of the yellow house does not live in the third house.
4. The person in the blue house and whoever lives in the white house are not neighbours.
5. The occupant of the green house lives at one end of the row.
6. The person who enjoys painting lives in the yellow house.
7. The person who enjoys cooking either is the German or is the Swede.
8. The occupant of the green house enjoys cooking.
9. The Swede and the occupant of the yellow house are neighbours.
10. The baker and the painting enthusiast live in adjacent houses.
11. The Brit enjoys hiking.
12. The lawyer and the Spaniard live two houses apart.
13. The occupant of the white house lives directly to the left of the pilot.
14. The pilot lives somewhere to the right of whoever lives in the green house.
15. The Spaniard lives in the yellow house.
16. The pilot and the Swede live in adjacent houses.
17. The pilot lives in house 5.
18. The Dane is not the doctor.
19. Whoever lives in the blue house lives immediately to the right of the person who enjoys cooking.
20. Whoever lives in the white house enjoys tennis.
21. The pilot lives somewhere to the right of the Dane.
22. The Spaniard does not live in house 3.

Answer format for this puzzle: {"1": {"<category>": "<value>", ...}, "2": {...}, ...} -- one entry per house number, giving the value of every category.
