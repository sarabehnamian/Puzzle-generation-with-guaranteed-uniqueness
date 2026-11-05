# Task: solve logic puzzles

Solve each puzzle below by reasoning. Every puzzle has exactly one solution. Work carefully; you
cannot run code. Give a complete answer for every puzzle even if unsure.

Output: write a single JSON object to the file D:\Puzzle-generation-with-guaranteed-uniqueness\data\llm_tasks\e3_solve\e3_zebra_sonnet_004.out.json with this exact structure
{"answers": [{"id": "<puzzle id>", "answer": <answer>}, ...]}
where <answer> has the format stated for each puzzle.

The puzzles follow.


## Puzzle zebra-00230

Grid logic puzzle. Deduce which value of each category belongs to each house. Every value is used exactly once.

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- color: purple, white, green, yellow, red
- job: pilot, baker, doctor, teacher, lawyer
- nationality: Swede, Spaniard, Brit, German, Dane
- hobby: painting, tennis, golf, chess, cooking

Clues:
1. The teacher lives in the fifth house.
2. The Brit and the person in the red house are neighbours.
3. Whoever lives in the green house is not the German.
4. The cooking enthusiast lives directly to the left of the teacher.
5. Whoever lives in the purple house lives directly to the left of the Dane.
6. The Dane enjoys painting.
7. The occupant of the yellow house enjoys chess.
8. The person in the green house lives immediately to the right of the Brit.
9. The Dane and the pilot are not neighbours.
10. The doctor and the Swede live two houses apart.
11. The doctor lives in house 2.
12. The painting enthusiast lives in the last house.
13. The baker lives at one end of the row.
14. The golf enthusiast lives in the leftmost house.

Answer format for this puzzle: {"1": {"<category>": "<value>", ...}, "2": {...}, ...} -- one entry per house number, giving the value of every category.

## Puzzle zebra-01430

Grid logic puzzle. Deduce which value of each category belongs to each house. Every value is used exactly once.

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- drink: water, juice, milk, cocoa, tea
- hobby: hiking, painting, cooking, tennis, chess
- job: teacher, lawyer, farmer, baker, pilot
- nationality: Spaniard, Norwegian, Brit, German, Swede

Clues:
1. The person who drinks juice either enjoys chess or enjoys painting.
2. The teacher lives immediately to the right of the person who drinks milk.
3. The baker lives next to the juice drinker.
4. The Brit and the person who enjoys cooking live two houses apart.
5. The person who drinks tea works as the farmer.
6. The person who drinks water lives in the fifth house.
7. The person who enjoys painting and the person who enjoys tennis are neighbours.
8. The lawyer does not live in house 4.
9. The Spaniard enjoys cooking.
10. The juice drinker and the water drinker live in adjacent houses.
11. The Norwegian lives at one end of the row.
12. The chess enthusiast works as the teacher.
13. The water drinker is the Swede.

Answer format for this puzzle: {"1": {"<category>": "<value>", ...}, "2": {...}, ...} -- one entry per house number, giving the value of every category.

## Puzzle zebra-01240

Grid logic puzzle. Deduce which value of each category belongs to each house. Every value is used exactly once.

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- pet: dog, horse, fish, cat, rabbit
- job: doctor, pilot, teacher, baker, lawyer
- color: purple, green, white, yellow, blue
- nationality: Brit, Dane, Swede, German, Spaniard

Clues:
1. The owner of the horse lives next to the occupant of the purple house.
2. The Dane lives directly to the left of the teacher.
3. The person who keeps the cat and the Swede live in adjacent houses.
4. The owner of the rabbit lives in the house just left of the one where whoever lives in the green house lives.
5. The Brit lives in the yellow house.
6. The person in the purple house lives somewhere to the left of the occupant of the green house.
7. The Brit and the German live two houses apart.
8. The baker and the doctor live in adjacent houses.
9. The owner of the dog lives in the green house.
10. The Dane lives in the house just left of the one where the occupant of the blue house lives.
11. The doctor and the owner of the horse live two houses apart.
12. The Brit lives immediately to the right of the pilot.
13. The Dane and the Spaniard are neighbours.

Answer format for this puzzle: {"1": {"<category>": "<value>", ...}, "2": {...}, ...} -- one entry per house number, giving the value of every category.

## Puzzle zebra-01256

Grid logic puzzle. Deduce which value of each category belongs to each house. Every value is used exactly once.

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- hobby: golf, cooking, hiking, tennis, painting
- nationality: Swede, Spaniard, German, Norwegian, Dane
- color: white, purple, red, green, yellow
- job: pilot, lawyer, doctor, baker, farmer

Clues:
1. There is exactly one house between the person who enjoys cooking and the pilot.
2. The person in the red house either enjoys hiking or enjoys painting.
3. The Dane lives somewhere to the left of whoever lives in the red house.
4. The lawyer and the Spaniard live two houses apart.
5. The doctor lives in the purple house.
6. The Swede does not live in the fifth house.
7. The hiking enthusiast works as the lawyer.
8. The Dane and the German are neighbours.
9. The doctor lives immediately to the right of the occupant of the yellow house.
10. The farmer lives directly to the left of the German.
11. The German lives immediately to the right of the person who enjoys tennis.
12. The occupant of the green house lives in the house just left of the one where the lawyer lives.
13. The lawyer and the painting enthusiast live in adjacent houses.
14. Whoever lives in the yellow house is the Dane.

Answer format for this puzzle: {"1": {"<category>": "<value>", ...}, "2": {...}, ...} -- one entry per house number, giving the value of every category.

## Puzzle zebra-00885-L1aug

Grid logic puzzle. Deduce which value of each category belongs to each house. Every value is used exactly once.

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- nationality: German, Norwegian, Brit, Dane, Spaniard
- job: lawyer, pilot, farmer, doctor, teacher
- hobby: cooking, tennis, painting, hiking, golf
- pet: fish, horse, cat, rabbit, dog

Clues:
1. The person who keeps the rabbit and the Spaniard are neighbours.
2. The doctor and the golf enthusiast are not neighbours.
3. The painting enthusiast is not the Spaniard.
4. The dog owner lives in house 4.
5. The farmer lives somewhere to the left of the German.
6. The farmer keeps the rabbit.
7. The Dane and the tennis enthusiast live in adjacent houses.
8. The Norwegian and the owner of the rabbit live in adjacent houses.
9. The person who enjoys hiking lives in house 3.
10. The Spaniard lives directly to the left of the farmer.
11. The doctor lives directly to the left of the person who enjoys tennis.
12. The hiking enthusiast either works as the pilot or works as the teacher.
13. The cooking enthusiast lives next to the teacher.
14. The doctor and the Norwegian are neighbours.
15. The cooking enthusiast lives immediately to the right of the Norwegian.
16. The tennis enthusiast works as the pilot.
17. The owner of the cat and the person who keeps the rabbit are neighbours.
18. The Dane and the fish owner live in adjacent houses.
19. The Brit and the person who enjoys hiking live in adjacent houses.
20. The golf enthusiast does not live next to the Norwegian.
21. The Brit does not live next to the dog owner.
22. The Spaniard keeps the cat.
23. The teacher keeps the horse.
24. The owner of the horse either enjoys cooking or enjoys hiking.
25. The farmer does not live in the first house.
26. The painting enthusiast lives in the second house.
27. The person who keeps the horse and the lawyer are not neighbours.
28. The doctor lives in the fourth house.
29. The rabbit owner does not live in the fifth house.
30. The person who enjoys painting does not keep the fish.
31. The dog owner and the pilot are neighbours.
32. The person who keeps the rabbit lives next to the teacher.
33. The painting enthusiast does not live in house 1.
34. The Spaniard and the horse owner are different people.
35. There is exactly one house between the Brit and the dog owner.
36. The Spaniard and the hiking enthusiast are different people.

Answer format for this puzzle: {"1": {"<category>": "<value>", ...}, "2": {...}, ...} -- one entry per house number, giving the value of every category.
