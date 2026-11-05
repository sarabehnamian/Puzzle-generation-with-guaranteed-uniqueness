# Task: solve logic puzzles

Solve each puzzle below by reasoning. Every puzzle has exactly one solution. Work carefully; you
cannot run code. Give a complete answer for every puzzle even if unsure.

Output: write a single JSON object to the file D:\Puzzle-generation-with-guaranteed-uniqueness\data\llm_tasks\e3_solve\e3_zebra_haiku_003.out.json with this exact structure
{"answers": [{"id": "<puzzle id>", "answer": <answer>}, ...]}
where <answer> has the format stated for each puzzle.

The puzzles follow.


## Puzzle zebra-01049-L1aug

Grid logic puzzle. Deduce which value of each category belongs to each house. Every value is used exactly once.

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- job: teacher, doctor, pilot, baker, lawyer
- drink: juice, cocoa, tea, milk, water
- nationality: Swede, Dane, Brit, Norwegian, German
- color: red, green, yellow, purple, blue

Clues:
1. The doctor lives in the fourth house.
2. Whoever lives in the green house either works as the doctor or works as the teacher.
3. The person in the red house drinks juice.
4. Whoever lives in the green house lives in the fourth house.
5. The person who drinks water is the Norwegian.
6. The German lives in the yellow house.
7. The Norwegian and the teacher live two houses apart.
8. The lawyer lives somewhere to the left of the person who drinks cocoa.
9. The Swede lives next to the tea drinker.
10. The teacher lives somewhere to the right of the person who drinks water.
11. The lawyer lives immediately to the right of the occupant of the blue house.
12. The baker lives in one of the two end houses.
13. The person who drinks cocoa and the Dane are neighbours.
14. The occupant of the blue house and the Brit are neighbours.
15. The person who drinks milk and the person who drinks water are not neighbours.
16. The person who drinks tea lives at one end of the row.
17. The Dane lives in one of the two end houses.
18. The occupant of the purple house drinks tea.
19. The cocoa drinker and the occupant of the yellow house live in adjacent houses.
20. The doctor lives in the house just left of the one where the person in the purple house lives.
21. The milk drinker lives in house 3.
22. The baker lives in the blue house.
23. The Norwegian lives in the first house.

Answer format for this puzzle: {"1": {"<category>": "<value>", ...}, "2": {...}, ...} -- one entry per house number, giving the value of every category.

## Puzzle zebra-00284

Grid logic puzzle. Deduce which value of each category belongs to each house. Every value is used exactly once.

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- hobby: chess, painting, hiking, tennis, cooking
- pet: bird, fish, cat, dog, rabbit
- color: yellow, blue, red, white, purple
- drink: tea, milk, water, coffee, cocoa

Clues:
1. The person who drinks coffee lives next to the person who enjoys tennis.
2. The person who drinks water lives in the leftmost house.
3. The person who keeps the bird and the person who enjoys cooking are neighbours.
4. The owner of the fish drinks tea.
5. Whoever lives in the purple house enjoys hiking.
6. The cocoa drinker and the owner of the rabbit are different people.
7. The owner of the cat and the occupant of the yellow house live in adjacent houses.
8. The person who drinks tea and whoever lives in the yellow house live two houses apart.
9. The occupant of the red house lives in the house just left of the one where the person in the white house lives.
10. The person who keeps the bird lives in one of the two end houses.
11. The person who drinks coffee lives somewhere to the right of the person who enjoys chess.
12. The person who drinks milk and the occupant of the red house live two houses apart.
13. Whoever lives in the purple house drinks water.
14. The person in the blue house lives directly to the left of the coffee drinker.

Answer format for this puzzle: {"1": {"<category>": "<value>", ...}, "2": {...}, ...} -- one entry per house number, giving the value of every category.

## Puzzle zebra-01458

Grid logic puzzle. Deduce which value of each category belongs to each house. Every value is used exactly once.

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- drink: water, coffee, cocoa, tea, juice
- job: baker, lawyer, pilot, doctor, teacher
- hobby: painting, golf, cooking, tennis, hiking
- color: blue, yellow, purple, green, white

Clues:
1. The person who drinks juice lives in the house just left of the one where the cocoa drinker lives.
2. The baker enjoys golf.
3. The person who enjoys tennis and the person in the yellow house live in adjacent houses.
4. The person who enjoys cooking lives in the house just left of the one where the doctor lives.
5. The person who drinks coffee lives in the middle house.
6. The lawyer lives immediately to the right of the cocoa drinker.
7. The person in the blue house lives directly to the left of the teacher.
8. The person who drinks tea either enjoys golf or enjoys painting.
9. The person who enjoys cooking and the teacher live two houses apart.
10. The doctor lives in the house just left of the one where the person in the white house lives.
11. The occupant of the green house is not the lawyer.
12. The cooking enthusiast and the occupant of the yellow house are neighbours.
13. The tea drinker lives in house 4.

Answer format for this puzzle: {"1": {"<category>": "<value>", ...}, "2": {...}, ...} -- one entry per house number, giving the value of every category.

## Puzzle zebra-00388

Grid logic puzzle. Deduce which value of each category belongs to each house. Every value is used exactly once.

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- pet: bird, cat, rabbit, horse, dog
- hobby: cooking, painting, chess, tennis, golf
- drink: juice, cocoa, coffee, milk, tea
- job: pilot, farmer, doctor, baker, teacher

Clues:
1. The farmer and the pilot are neighbours.
2. The person who enjoys painting works as the doctor.
3. The baker and the person who enjoys chess are neighbours.
4. The farmer either enjoys painting or enjoys tennis.
5. The juice drinker either works as the baker or works as the doctor.
6. There is exactly one house between the owner of the cat and the person who drinks cocoa.
7. The owner of the horse lives immediately to the right of the person who drinks tea.
8. The doctor and the dog owner live in adjacent houses.
9. The owner of the horse works as the teacher.
10. The golf enthusiast lives next to the painting enthusiast.
11. The owner of the bird either enjoys chess or enjoys golf.
12. The rabbit owner either works as the baker or works as the doctor.
13. The pilot lives directly to the left of the coffee drinker.

Answer format for this puzzle: {"1": {"<category>": "<value>", ...}, "2": {...}, ...} -- one entry per house number, giving the value of every category.

## Puzzle zebra-01211

Grid logic puzzle. Deduce which value of each category belongs to each house. Every value is used exactly once.

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- job: farmer, baker, doctor, teacher, lawyer
- color: green, yellow, white, purple, blue
- drink: water, coffee, cocoa, milk, juice
- hobby: painting, golf, hiking, tennis, cooking

Clues:
1. The person who enjoys cooking either drinks cocoa or drinks milk.
2. The lawyer lives directly to the left of the doctor.
3. The coffee drinker enjoys golf.
4. Whoever lives in the blue house works as the baker.
5. The farmer drinks milk.
6. The coffee drinker lives next to whoever lives in the yellow house.
7. The person who enjoys tennis lives somewhere to the right of whoever lives in the white house.
8. The person in the blue house lives immediately to the right of the cocoa drinker.
9. The person who drinks juice lives directly to the left of the occupant of the purple house.
10. The person who enjoys hiking works as the teacher.
11. Whoever lives in the purple house lives directly to the left of the person who enjoys cooking.
12. There is exactly one house between the person who enjoys hiking and the person who enjoys tennis.
13. The baker and the water drinker live two houses apart.

Answer format for this puzzle: {"1": {"<category>": "<value>", ...}, "2": {...}, ...} -- one entry per house number, giving the value of every category.
