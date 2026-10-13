# Task: rewrite logic-puzzle clues in natural prose

Below are logic-grid puzzles whose clues were produced by a template generator. Rewrite every clue
so it reads like a clue written by a human puzzle author: vary sentence structure, use natural
idioms (neighbours, "next door", "further down the street", ordinals, etc.), and avoid repeating
the template wording. The meaning of every clue must stay EXACTLY the same: do not add, drop, merge
or split information. Keep the numbering one-to-one (clue k becomes rewritten clue k). Keep the
value names exactly as listed in the header so a reader can match them. Houses stay numbered 1..N
from left to right.

Output: write a single JSON object to the file /home/user/Puzzle-generation-with-guaranteed-uniqueness/data/llm_tasks/e1_para/e1_para_008.out.json with this exact structure
{"puzzles": [{"id": "<puzzle id>", "clues": ["<rewritten clue 1>", "<rewritten clue 2>", ...]}, ...]}

The puzzles follow.


## Puzzle zebra-00180

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- drink: tea, coffee, cocoa, water, milk
- pet: dog, bird, horse, fish, rabbit
- color: yellow, red, green, blue, white
- job: farmer, doctor, lawyer, baker, pilot

Clues:
1. The tea drinker works as the pilot.
2. The person in the green house lives somewhere to the right of the doctor.
3. The person who keeps the dog drinks water.
4. The person who keeps the horse lives in the house just left of the one where the rabbit owner lives.
5. The person who drinks tea lives in the fourth house.
6. The person who drinks cocoa does not keep the rabbit.
7. The baker and whoever lives in the white house are neighbours.
8. The person who drinks cocoa and the lawyer live two houses apart.
9. The owner of the fish lives directly to the left of the person in the red house.
10. The owner of the bird lives in house 2.
11. There is exactly one house between the occupant of the white house and the occupant of the yellow house.
12. The occupant of the yellow house drinks coffee.
13. The dog owner does not live in house 5.
14. The farmer lives in the fifth house.

## Puzzle zebra-00181

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- nationality: Norwegian, Brit, Dane, Swede, Spaniard
- color: white, green, yellow, blue, purple
- job: doctor, baker, farmer, teacher, lawyer
- pet: cat, dog, rabbit, horse, fish

Clues:
1. Whoever lives in the blue house and the person who keeps the dog are neighbours.
2. The occupant of the yellow house works as the doctor.
3. The Norwegian keeps the rabbit.
4. The doctor does not live in house 5.
5. The Dane lives in house 2.
6. The horse owner lives in the green house.
7. The farmer and the Norwegian are neighbours.
8. Whoever lives in the purple house keeps the dog.
9. The horse owner lives in house 3.
10. The lawyer lives immediately to the right of whoever lives in the blue house.
11. The Spaniard lives in house 4.
12. The Swede lives in the house just left of the one where the baker lives.
13. The fish owner lives next to the Norwegian.

## Puzzle zebra-00182

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- pet: fish, cat, horse, dog, bird
- nationality: Swede, Brit, German, Spaniard, Norwegian
- hobby: tennis, golf, hiking, painting, cooking
- color: blue, green, yellow, white, red

Clues:
1. The person who enjoys tennis lives immediately to the right of the occupant of the green house.
2. The Brit lives in the leftmost house.
3. The cooking enthusiast lives in house 3.
4. The person who keeps the dog lives immediately to the right of whoever lives in the white house.
5. The cat owner and the cooking enthusiast are neighbours.
6. The Spaniard keeps the bird.
7. The owner of the cat is the Swede.
8. The Spaniard enjoys hiking.
9. There is exactly one house between the occupant of the blue house and the cooking enthusiast.
10. The person who enjoys tennis lives in the fifth house.
11. The person in the red house and the person in the white house are not neighbours.
12. The horse owner lives in the house just left of the one where the Spaniard lives.
13. The Norwegian and the painting enthusiast live two houses apart.

## Puzzle zebra-00183

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- hobby: tennis, cooking, painting, golf, chess
- color: green, blue, white, red, yellow
- job: farmer, pilot, baker, teacher, lawyer
- pet: dog, rabbit, bird, horse, cat

Clues:
1. The owner of the dog and the pilot are different people.
2. Whoever lives in the red house either keeps the bird or keeps the rabbit.
3. Whoever lives in the blue house keeps the rabbit.
4. The golf enthusiast and the teacher are different people.
5. The person who enjoys cooking and the pilot live in adjacent houses.
6. The cat owner lives in the green house.
7. The person who enjoys golf either lives in the red house or lives in the white house.
8. There is exactly one house between the lawyer and the teacher.
9. The occupant of the white house lives somewhere to the left of the owner of the horse.
10. The owner of the bird lives somewhere to the right of the teacher.
11. The person who keeps the horse and the tennis enthusiast live two houses apart.
12. Whoever lives in the yellow house lives in one of the two end houses.
13. Whoever lives in the red house lives directly to the left of the person who enjoys painting.
14. The farmer and the painting enthusiast live in adjacent houses.
15. There is exactly one house between the occupant of the green house and the painting enthusiast.
16. The teacher lives somewhere to the left of the owner of the cat.
17. The person who enjoys cooking lives in one of the two end houses.

## Puzzle zebra-00184

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- pet: horse, fish, dog, cat, bird
- color: purple, green, blue, white, red
- nationality: German, Dane, Norwegian, Spaniard, Brit
- drink: milk, water, coffee, cocoa, juice

Clues:
1. The water drinker is the Norwegian.
2. The person who drinks cocoa lives at one end of the row.
3. The Dane lives directly to the left of the Spaniard.
4. The fish owner lives somewhere to the right of the person who keeps the horse.
5. The occupant of the blue house lives in the house just left of the one where the person who drinks coffee lives.
6. The Spaniard lives in the house just left of the one where the milk drinker lives.
7. There is exactly one house between the coffee drinker and the person in the white house.
8. The person who keeps the bird either is the Brit or is the Dane.
9. The German either drinks coffee or drinks juice.
10. The fish owner drinks coffee.
11. Whoever lives in the red house lives in house 5.
12. There is exactly one house between the cat owner and the occupant of the purple house.
13. The occupant of the green house and the Spaniard live two houses apart.

## Puzzle zebra-00185

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- job: baker, lawyer, pilot, doctor, farmer
- nationality: Norwegian, Brit, Swede, Spaniard, Dane
- hobby: chess, cooking, hiking, tennis, painting
- drink: tea, juice, water, milk, coffee

Clues:
1. There is exactly one house between the farmer and the milk drinker.
2. The person who drinks water lives in the second house.
3. The doctor drinks coffee.
4. The Brit lives immediately to the right of the person who drinks tea.
5. The pilot enjoys hiking.
6. The Spaniard lives in one of the two end houses.
7. The person who enjoys tennis either works as the baker or works as the pilot.
8. The baker lives in the house just left of the one where the Brit lives.
9. The person who enjoys painting is the Spaniard.
10. The Dane either drinks juice or drinks tea.
11. The lawyer lives in the house just left of the one where the milk drinker lives.
12. The doctor either enjoys cooking or enjoys hiking.
13. The person who enjoys cooking and the Swede are neighbours.

## Puzzle zebra-00186

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- nationality: Dane, German, Brit, Swede, Spaniard
- pet: rabbit, bird, fish, dog, cat
- drink: juice, tea, milk, cocoa, coffee
- hobby: golf, painting, tennis, chess, cooking

Clues:
1. The German does not live next to the person who enjoys painting.
2. The chess enthusiast and the Spaniard live two houses apart.
3. The Spaniard keeps the dog.
4. The juice drinker enjoys painting.
5. The person who enjoys cooking lives in one of the two end houses.
6. There is exactly one house between the person who keeps the fish and the juice drinker.
7. The dog owner drinks cocoa.
8. The Swede drinks tea.
9. There is exactly one house between the juice drinker and the tennis enthusiast.
10. The person who keeps the bird lives in house 2.
11. The German lives in one of the two end houses.
12. The milk drinker lives directly to the left of the person who drinks juice.
13. The Dane and the person who enjoys tennis live two houses apart.
14. The rabbit owner lives in a lower-numbered house than the Swede.
15. The person who enjoys chess lives somewhere to the right of the Dane.

## Puzzle zebra-00187

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- drink: juice, tea, milk, water, coffee
- pet: dog, bird, rabbit, horse, fish
- hobby: painting, chess, tennis, cooking, golf
- color: green, red, yellow, blue, purple

Clues:
1. The person in the green house lives directly to the left of the person who keeps the bird.
2. The person in the yellow house drinks juice.
3. The tea drinker enjoys painting.
4. The person who keeps the rabbit and the tea drinker are not neighbours.
5. The tennis enthusiast lives in house 1.
6. There is exactly one house between the milk drinker and the owner of the rabbit.
7. Whoever lives in the yellow house lives directly to the left of the person who keeps the horse.
8. The painting enthusiast lives in the house just left of the one where whoever lives in the blue house lives.
9. The occupant of the yellow house lives in the house just left of the one where the golf enthusiast lives.
10. The person who keeps the fish lives somewhere to the right of the person in the green house.
11. The cooking enthusiast either keeps the dog or keeps the rabbit.
12. Whoever lives in the red house lives in the second house.
13. The juice drinker lives directly to the left of the person who drinks water.

## Puzzle zebra-00188

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- job: farmer, baker, teacher, pilot, lawyer
- drink: water, tea, coffee, milk, juice
- nationality: Spaniard, Brit, Swede, Norwegian, Dane
- hobby: tennis, hiking, chess, painting, cooking

Clues:
1. The tennis enthusiast lives in a lower-numbered house than the teacher.
2. The Brit lives immediately to the right of the person who drinks juice.
3. The Brit lives next to the teacher.
4. The lawyer is the Spaniard.
5. The tea drinker lives in the last house.
6. The Norwegian does not live in the second house.
7. The hiking enthusiast is the Swede.
8. There is exactly one house between the Brit and the farmer.
9. The lawyer lives in the house just left of the one where the person who drinks water lives.
10. The person who enjoys cooking and the Swede live two houses apart.
11. The baker enjoys tennis.
12. The milk drinker lives directly to the left of the baker.
13. The lawyer enjoys chess.

## Puzzle zebra-00189

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- job: lawyer, farmer, teacher, doctor, baker
- hobby: painting, tennis, cooking, hiking, golf
- pet: horse, rabbit, fish, dog, bird
- nationality: German, Dane, Swede, Spaniard, Brit

Clues:
1. The owner of the rabbit and the person who enjoys tennis live two houses apart.
2. The painting enthusiast is the Spaniard.
3. The owner of the bird lives directly to the left of the doctor.
4. The Dane and the farmer live in adjacent houses.
5. The Spaniard lives immediately to the right of the person who keeps the fish.
6. The person who enjoys golf lives in the house just left of the one where the owner of the dog lives.
7. The lawyer lives in the fourth house.
8. There is exactly one house between the Swede and the teacher.
9. The German lives in the house just left of the one where the owner of the dog lives.
10. The Swede lives somewhere to the left of the Spaniard.
11. The painting enthusiast does not live in house 5.
12. The Dane and the horse owner live two houses apart.
13. The person who enjoys cooking works as the farmer.
