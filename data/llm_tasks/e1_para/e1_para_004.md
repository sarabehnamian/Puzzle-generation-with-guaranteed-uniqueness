# Task: rewrite logic-puzzle clues in natural prose

Below are logic-grid puzzles whose clues were produced by a template generator. Rewrite every clue
so it reads like a clue written by a human puzzle author: vary sentence structure, use natural
idioms (neighbours, "next door", "further down the street", ordinals, etc.), and avoid repeating
the template wording. The meaning of every clue must stay EXACTLY the same: do not add, drop, merge
or split information. Keep the numbering one-to-one (clue k becomes rewritten clue k). Keep the
value names exactly as listed in the header so a reader can match them. Houses stay numbered 1..N
from left to right.

Output: write a single JSON object to the file D:\Puzzle-generation-with-guaranteed-uniqueness\data\llm_tasks\e1_para\e1_para_004.out.json with this exact structure
{"puzzles": [{"id": "<puzzle id>", "clues": ["<rewritten clue 1>", "<rewritten clue 2>", ...]}, ...]}

The puzzles follow.


## Puzzle zebra-00140

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- hobby: chess, tennis, hiking, painting, golf
- drink: tea, water, milk, cocoa, juice
- color: white, red, green, yellow, purple
- pet: cat, bird, horse, fish, rabbit

Clues:
1. Whoever lives in the yellow house does not enjoy tennis.
2. The cocoa drinker lives in the white house.
3. The water drinker lives in house 2.
4. The owner of the rabbit enjoys hiking.
5. The person who enjoys painting lives in one of the two end houses.
6. The occupant of the red house keeps the horse.
7. The tea drinker and the person who keeps the horse are different people.
8. The person in the purple house and the tennis enthusiast are neighbours.
9. The juice drinker enjoys golf.
10. The person who enjoys chess and the occupant of the yellow house are different people.
11. The cat owner lives immediately to the right of the tennis enthusiast.
12. The person who keeps the bird lives immediately to the right of the person who drinks juice.
13. The occupant of the white house keeps the rabbit.
14. The horse owner lives in house 5.

## Puzzle zebra-00141

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- hobby: cooking, tennis, golf, hiking, chess
- pet: horse, dog, bird, fish, cat
- job: teacher, farmer, lawyer, pilot, doctor
- drink: milk, tea, cocoa, juice, water

Clues:
1. There is exactly one house between the doctor and the lawyer.
2. The cat owner and the tea drinker are neighbours.
3. The person who drinks water lives in the house just left of the one where the farmer lives.
4. The owner of the bird and the person who enjoys tennis are neighbours.
5. The owner of the dog and the person who enjoys hiking live in adjacent houses.
6. The person who drinks juice lives immediately to the right of the owner of the horse.
7. The person who drinks tea lives in a lower-numbered house than the cocoa drinker.
8. The doctor lives directly to the left of the golf enthusiast.
9. The pilot lives directly to the left of the cooking enthusiast.
10. The person who drinks water either enjoys chess or enjoys hiking.
11. The bird owner lives in one of the two end houses.
12. The person who enjoys chess and the person who drinks milk are neighbours.
13. The horse owner lives in the house just left of the one where the farmer lives.

## Puzzle zebra-00142

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- hobby: hiking, cooking, golf, tennis, painting
- job: farmer, pilot, lawyer, teacher, baker
- pet: bird, rabbit, cat, horse, fish
- color: yellow, purple, blue, green, red

Clues:
1. The person who enjoys golf lives in the house just left of the one where whoever lives in the blue house lives.
2. There is exactly one house between the pilot and the person who keeps the rabbit.
3. The painting enthusiast lives in the fourth house.
4. The cooking enthusiast lives in house 2.
5. The owner of the bird lives in the house just left of the one where whoever lives in the purple house lives.
6. The occupant of the red house works as the teacher.
7. The baker lives in the second house.
8. The occupant of the blue house lives next to the person who enjoys tennis.
9. The farmer does not live next to the person who keeps the rabbit.
10. The person who keeps the fish and the rabbit owner are neighbours.
11. There is exactly one house between the occupant of the blue house and the occupant of the green house.
12. The person who enjoys tennis either works as the farmer or works as the lawyer.
13. The person in the blue house lives next to the fish owner.
14. The person who keeps the bird lives next to the horse owner.
15. The teacher lives in the middle house.

## Puzzle zebra-00143

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- hobby: hiking, cooking, chess, tennis, painting
- color: yellow, blue, green, red, white
- job: doctor, baker, pilot, farmer, lawyer
- drink: tea, coffee, water, juice, milk

Clues:
1. The juice drinker and the person who enjoys tennis live two houses apart.
2. The chess enthusiast lives next to the hiking enthusiast.
3. The occupant of the red house lives in the house just left of the one where whoever lives in the blue house lives.
4. The person who drinks coffee lives immediately to the right of the pilot.
5. The juice drinker lives in the third house.
6. The baker lives in house 2.
7. The chess enthusiast lives immediately to the right of the pilot.
8. The chess enthusiast and the person who drinks water live two houses apart.
9. The occupant of the green house lives next to the person who drinks tea.
10. The pilot lives somewhere to the right of the lawyer.
11. The pilot either lives in the green house or lives in the white house.
12. The milk drinker enjoys hiking.
13. The person who enjoys painting lives directly to the left of the farmer.

## Puzzle zebra-00144

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- drink: milk, water, tea, juice, coffee
- pet: horse, fish, dog, rabbit, cat
- nationality: Spaniard, Dane, Norwegian, Swede, Brit
- color: green, purple, red, blue, yellow

Clues:
1. The person who drinks water lives in house 4.
2. The Dane drinks water.
3. The Spaniard lives in house 5.
4. The Brit and the occupant of the yellow house live two houses apart.
5. The occupant of the green house drinks water.
6. The rabbit owner and the tea drinker live two houses apart.
7. The person who drinks juice lives in the yellow house.
8. The occupant of the purple house and the person who drinks water live two houses apart.
9. The person who keeps the fish lives in one of the two end houses.
10. There is exactly one house between the person who drinks coffee and the person who drinks juice.
11. The owner of the cat lives somewhere to the right of the person who keeps the fish.
12. Whoever lives in the blue house and the person who keeps the cat are not neighbours.
13. The Norwegian lives at one end of the row.
14. The occupant of the blue house keeps the horse.
15. The person in the red house is the Spaniard.

## Puzzle zebra-00145

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- hobby: golf, chess, painting, hiking, tennis
- job: doctor, baker, farmer, pilot, teacher
- pet: rabbit, fish, bird, dog, cat
- drink: milk, water, coffee, juice, tea

Clues:
1. The farmer drinks water.
2. The doctor and the tea drinker live in adjacent houses.
3. The juice drinker lives next to the person who drinks milk.
4. The person who enjoys chess lives in the house just left of the one where the dog owner lives.
5. The person who drinks juice lives immediately to the right of the person who enjoys golf.
6. The owner of the rabbit lives in house 1.
7. The doctor lives in the fourth house.
8. The person who keeps the fish enjoys hiking.
9. The pilot lives directly to the left of the person who enjoys hiking.
10. The pilot lives in the house just left of the one where the teacher lives.
11. The pilot lives immediately to the right of the person who enjoys chess.
12. The person who keeps the cat lives next to the golf enthusiast.
13. The tennis enthusiast works as the pilot.

## Puzzle zebra-00146

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- nationality: Swede, Brit, Dane, Spaniard, Norwegian
- job: teacher, baker, pilot, doctor, lawyer
- hobby: cooking, hiking, golf, chess, tennis
- drink: cocoa, coffee, tea, juice, water

Clues:
1. The Dane lives in the leftmost house.
2. The person who enjoys cooking either is the Brit or is the Dane.
3. The Dane enjoys golf.
4. The baker and the person who enjoys chess live in adjacent houses.
5. The person who enjoys hiking lives in the second house.
6. The doctor drinks coffee.
7. The person who drinks coffee and the Spaniard are neighbours.
8. The baker and the water drinker live in adjacent houses.
9. The person who drinks coffee and the tea drinker live two houses apart.
10. The Norwegian lives next to the person who enjoys tennis.
11. There is exactly one house between the person who enjoys hiking and the lawyer.
12. The person who enjoys tennis works as the pilot.
13. The Norwegian drinks cocoa.

## Puzzle zebra-00147

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- hobby: cooking, golf, hiking, tennis, chess
- nationality: German, Swede, Norwegian, Spaniard, Dane
- pet: horse, fish, dog, bird, cat
- color: purple, green, yellow, blue, white

Clues:
1. The owner of the fish lives in the yellow house.
2. The bird owner enjoys chess.
3. The Dane lives directly to the left of the person who keeps the horse.
4. The Norwegian lives somewhere to the right of whoever lives in the green house.
5. The cooking enthusiast lives somewhere to the right of the person who keeps the bird.
6. The owner of the cat and the Norwegian are different people.
7. The dog owner lives directly to the left of the Swede.
8. The person who keeps the horse and the person in the white house are neighbours.
9. The Norwegian and the person in the yellow house are neighbours.
10. The person who enjoys hiking lives next to whoever lives in the purple house.
11. The German lives directly to the left of the person who keeps the fish.
12. The Spaniard enjoys cooking.
13. The person who enjoys tennis lives in the third house.

## Puzzle zebra-00148

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- hobby: tennis, golf, painting, cooking, chess
- pet: fish, bird, dog, rabbit, horse
- nationality: Spaniard, Dane, Norwegian, Brit, German
- drink: tea, milk, water, juice, coffee

Clues:
1. The person who keeps the bird and the person who keeps the fish are not neighbours.
2. The chess enthusiast and the tea drinker are neighbours.
3. The Spaniard lives in a lower-numbered house than the water drinker.
4. The owner of the dog enjoys tennis.
5. The owner of the rabbit lives directly to the left of the person who enjoys golf.
6. The coffee drinker does not live in the third house.
7. The Brit and the Dane are not neighbours.
8. The German and the person who keeps the rabbit live two houses apart.
9. The fish owner lives immediately to the right of the person who keeps the rabbit.
10. The coffee drinker either keeps the fish or keeps the horse.
11. The coffee drinker is the Spaniard.
12. The Brit enjoys painting.
13. The person who drinks water enjoys chess.
14. The person who drinks milk either keeps the dog or keeps the rabbit.
15. The tea drinker lives somewhere to the right of the Brit.
16. The person who enjoys tennis lives somewhere to the left of the owner of the fish.

## Puzzle zebra-00149

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- hobby: cooking, golf, hiking, tennis, painting
- job: teacher, baker, pilot, farmer, doctor
- nationality: Swede, Dane, Norwegian, Spaniard, German
- drink: juice, water, tea, cocoa, milk

Clues:
1. The pilot enjoys cooking.
2. The golf enthusiast lives immediately to the right of the Swede.
3. The farmer is the Dane.
4. The person who drinks water is not the farmer.
5. The person who drinks tea is the Spaniard.
6. The painting enthusiast drinks milk.
7. The teacher enjoys golf.
8. The German lives in house 5.
9. The hiking enthusiast lives next to the person who drinks milk.
10. The doctor and the person who drinks milk are different people.
11. The water drinker lives in the second house.
12. The doctor lives somewhere to the right of the person who enjoys tennis.
13. The farmer lives directly to the left of the doctor.
14. The person who drinks juice lives directly to the left of the baker.
