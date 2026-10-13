# Task: solve logic puzzles

Solve each puzzle below by reasoning. Every puzzle has exactly one solution. Work carefully; you
cannot run code. Give a complete answer for every puzzle even if unsure.

Output: write a single JSON object to the file /home/user/Puzzle-generation-with-guaranteed-uniqueness/data/llm_tasks/e3_solve/e3_zebra_haiku_002.out.json with this exact structure
{"answers": [{"id": "<puzzle id>", "answer": <answer>}, ...]}
where <answer> has the format stated for each puzzle.

The puzzles follow.


## Puzzle zebra-00668

Grid logic puzzle. Deduce which value of each category belongs to each house. Every value is used exactly once.

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- color: red, purple, green, blue, yellow
- hobby: chess, hiking, cooking, golf, painting
- pet: bird, horse, fish, cat, dog
- drink: cocoa, coffee, juice, milk, tea

Clues:
1. The dog owner and the person in the yellow house live two houses apart.
2. Whoever lives in the red house and the person who drinks tea live two houses apart.
3. The cocoa drinker lives in one of the two end houses.
4. The person who drinks juice keeps the fish.
5. The occupant of the yellow house enjoys painting.
6. The cocoa drinker does not live next to the person who enjoys cooking.
7. There is exactly one house between the occupant of the red house and the occupant of the yellow house.
8. The occupant of the red house lives immediately to the right of the person who keeps the bird.
9. The cat owner drinks milk.
10. Whoever lives in the blue house enjoys hiking.
11. The owner of the cat lives in the green house.
12. The owner of the fish enjoys chess.
13. The coffee drinker either enjoys cooking or enjoys painting.

Answer format for this puzzle: {"1": {"<category>": "<value>", ...}, "2": {...}, ...} -- one entry per house number, giving the value of every category.

## Puzzle zebra-01132

Grid logic puzzle. Deduce which value of each category belongs to each house. Every value is used exactly once.

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- color: white, green, blue, red, yellow
- job: baker, doctor, teacher, farmer, pilot
- nationality: Norwegian, Brit, Dane, Spaniard, German
- hobby: painting, hiking, chess, golf, tennis

Clues:
1. The hiking enthusiast either works as the baker or works as the farmer.
2. The person who enjoys golf is the Norwegian.
3. There is exactly one house between the person who enjoys golf and the person who enjoys painting.
4. The person in the green house works as the teacher.
5. The chess enthusiast lives in the leftmost house.
6. The person who enjoys hiking is the Dane.
7. The person in the yellow house works as the pilot.
8. The Spaniard lives in house 4.
9. The German is not the doctor.
10. The person in the green house either is the Brit or is the Dane.
11. Whoever lives in the red house lives next to the occupant of the yellow house.
12. The farmer lives in the middle house.
13. The person in the white house lives immediately to the right of whoever lives in the blue house.
14. The painting enthusiast lives in one of the two end houses.
15. The Norwegian lives somewhere to the right of the occupant of the green house.

Answer format for this puzzle: {"1": {"<category>": "<value>", ...}, "2": {...}, ...} -- one entry per house number, giving the value of every category.

## Puzzle zebra-00647

Grid logic puzzle. Deduce which value of each category belongs to each house. Every value is used exactly once.

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- job: farmer, teacher, doctor, baker, pilot
- drink: tea, coffee, juice, milk, cocoa
- hobby: cooking, golf, tennis, chess, hiking
- pet: bird, fish, horse, dog, rabbit

Clues:
1. The baker lives in the house just left of the one where the pilot lives.
2. The person who drinks cocoa lives in the second house.
3. The juice drinker and the pilot are different people.
4. The farmer and the milk drinker are neighbours.
5. The doctor and the person who enjoys hiking live in adjacent houses.
6. The teacher lives in the last house.
7. The person who drinks tea lives directly to the left of the person who enjoys golf.
8. The juice drinker lives in house 4.
9. The person who drinks juice lives directly to the left of the cooking enthusiast.
10. The person who keeps the bird lives immediately to the right of the pilot.
11. The doctor keeps the fish.
12. The pilot lives next to the person who keeps the rabbit.
13. The chess enthusiast either works as the doctor or works as the teacher.
14. The person who keeps the horse does not enjoy tennis.

Answer format for this puzzle: {"1": {"<category>": "<value>", ...}, "2": {...}, ...} -- one entry per house number, giving the value of every category.

## Puzzle zebra-01137

Grid logic puzzle. Deduce which value of each category belongs to each house. Every value is used exactly once.

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- hobby: cooking, chess, painting, hiking, tennis
- job: teacher, farmer, doctor, baker, lawyer
- nationality: Swede, Brit, Dane, Spaniard, Norwegian
- pet: horse, dog, bird, rabbit, cat

Clues:
1. The person who keeps the bird lives in the house just left of the one where the owner of the cat lives.
2. The farmer lives directly to the left of the baker.
3. The Brit and the teacher are not neighbours.
4. The Swede and the tennis enthusiast are neighbours.
5. The chess enthusiast keeps the rabbit.
6. The person who enjoys cooking is the Swede.
7. The person who enjoys painting works as the lawyer.
8. The person who keeps the dog lives in one of the two end houses.
9. The person who keeps the horse lives in the house just left of the one where the Spaniard lives.
10. The person who enjoys chess either works as the baker or works as the teacher.
11. The Norwegian lives in the fifth house.
12. The painting enthusiast lives in house 3.
13. The bird owner lives in the house just left of the one where the tennis enthusiast lives.

Answer format for this puzzle: {"1": {"<category>": "<value>", ...}, "2": {...}, ...} -- one entry per house number, giving the value of every category.

## Puzzle zebra-01459

Grid logic puzzle. Deduce which value of each category belongs to each house. Every value is used exactly once.

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- color: green, white, red, blue, yellow
- job: lawyer, doctor, teacher, pilot, baker
- nationality: Spaniard, Dane, German, Brit, Norwegian
- pet: horse, rabbit, bird, cat, dog

Clues:
1. The person in the red house lives in one of the two end houses.
2. The person who keeps the rabbit lives in the house just left of the one where the German lives.
3. The person who keeps the bird and the person in the yellow house live in adjacent houses.
4. The lawyer lives immediately to the right of the dog owner.
5. The pilot and the teacher live in adjacent houses.
6. The person who keeps the cat lives in house 3.
7. The pilot is not the Brit.
8. The Brit lives directly to the left of whoever lives in the yellow house.
9. The Dane lives somewhere to the left of the Brit.
10. The baker lives in house 3.
11. Whoever lives in the blue house and the teacher are not neighbours.
12. The Spaniard lives directly to the left of the baker.
13. The Spaniard and the person in the white house live two houses apart.

Answer format for this puzzle: {"1": {"<category>": "<value>", ...}, "2": {...}, ...} -- one entry per house number, giving the value of every category.
