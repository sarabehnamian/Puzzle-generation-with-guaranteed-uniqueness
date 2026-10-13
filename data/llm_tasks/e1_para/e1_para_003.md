# Task: rewrite logic-puzzle clues in natural prose

Below are logic-grid puzzles whose clues were produced by a template generator. Rewrite every clue
so it reads like a clue written by a human puzzle author: vary sentence structure, use natural
idioms (neighbours, "next door", "further down the street", ordinals, etc.), and avoid repeating
the template wording. The meaning of every clue must stay EXACTLY the same: do not add, drop, merge
or split information. Keep the numbering one-to-one (clue k becomes rewritten clue k). Keep the
value names exactly as listed in the header so a reader can match them. Houses stay numbered 1..N
from left to right.

Output: write a single JSON object to the file /home/user/Puzzle-generation-with-guaranteed-uniqueness/data/llm_tasks/e1_para/e1_para_003.out.json with this exact structure
{"puzzles": [{"id": "<puzzle id>", "clues": ["<rewritten clue 1>", "<rewritten clue 2>", ...]}, ...]}

The puzzles follow.


## Puzzle zebra-00130

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- hobby: chess, golf, hiking, painting, cooking
- drink: water, tea, milk, coffee, cocoa
- pet: rabbit, fish, dog, cat, bird
- job: teacher, pilot, farmer, doctor, baker

Clues:
1. The dog owner drinks cocoa.
2. The doctor and the person who drinks milk live two houses apart.
3. The coffee drinker lives in the house just left of the one where the water drinker lives.
4. The doctor does not live next to the teacher.
5. The baker and the person who drinks milk live in adjacent houses.
6. The person who keeps the cat lives in house 3.
7. The person who keeps the dog either works as the doctor or works as the teacher.
8. The rabbit owner lives immediately to the right of the pilot.
9. The golf enthusiast lives in the leftmost house.
10. The person who enjoys chess does not live in house 5.
11. The person who keeps the rabbit and the teacher live two houses apart.
12. The baker and the owner of the bird are different people.
13. The cocoa drinker and the person who enjoys painting live two houses apart.
14. The person who enjoys cooking lives in the house just left of the one where the water drinker lives.

## Puzzle zebra-00131

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- hobby: chess, painting, golf, hiking, cooking
- nationality: Swede, Spaniard, Norwegian, Dane, German
- job: doctor, baker, farmer, lawyer, teacher
- drink: milk, cocoa, tea, juice, water

Clues:
1. The cocoa drinker lives next to the doctor.
2. The juice drinker either enjoys chess or enjoys golf.
3. The painting enthusiast drinks water.
4. The baker lives immediately to the right of the person who drinks water.
5. The person who enjoys cooking either works as the farmer or works as the teacher.
6. The teacher lives in house 1.
7. The tea drinker either works as the doctor or works as the lawyer.
8. The Dane lives immediately to the right of the milk drinker.
9. The farmer lives in house 5.
10. The German does not live in house 5.
11. The Spaniard lives somewhere to the left of the juice drinker.
12. The person who drinks tea lives directly to the left of the German.
13. The doctor and the hiking enthusiast are neighbours.
14. The Norwegian and the water drinker are neighbours.
15. The person who enjoys golf either works as the lawyer or works as the teacher.

## Puzzle zebra-00132

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- job: doctor, baker, teacher, lawyer, pilot
- pet: fish, horse, dog, cat, rabbit
- drink: milk, tea, coffee, water, cocoa
- hobby: chess, golf, hiking, tennis, cooking

Clues:
1. The person who enjoys cooking lives next to the person who keeps the dog.
2. The baker enjoys hiking.
3. The person who keeps the dog lives in the fifth house.
4. The milk drinker and the rabbit owner live two houses apart.
5. There is exactly one house between the hiking enthusiast and the person who keeps the horse.
6. The milk drinker lives next to the tennis enthusiast.
7. The baker and the person who drinks tea are neighbours.
8. The person who enjoys chess and the rabbit owner live two houses apart.
9. The cooking enthusiast and the teacher are neighbours.
10. There is exactly one house between the person who drinks coffee and the tea drinker.
11. There is exactly one house between the doctor and the person who drinks water.
12. The lawyer keeps the cat.
13. The tea drinker lives somewhere to the left of the water drinker.
14. The baker lives at one end of the row.
15. The pilot and the teacher are not neighbours.

## Puzzle zebra-00133

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- nationality: Norwegian, Spaniard, Swede, German, Dane
- drink: tea, water, juice, milk, cocoa
- pet: horse, rabbit, dog, cat, bird
- job: doctor, lawyer, farmer, teacher, baker

Clues:
1. The Swede keeps the dog.
2. The baker lives directly to the left of the horse owner.
3. The milk drinker is the Swede.
4. The owner of the bird and the Swede live in adjacent houses.
5. The owner of the bird works as the lawyer.
6. The doctor either is the Dane or is the Swede.
7. The farmer lives in the house just left of the one where the owner of the dog lives.
8. The lawyer lives somewhere to the left of the cocoa drinker.
9. The German lives directly to the left of the person who drinks juice.
10. There is exactly one house between the Norwegian and the Swede.
11. The doctor lives in the fifth house.
12. The farmer drinks water.
13. The person who keeps the cat works as the baker.

## Puzzle zebra-00134

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- nationality: Spaniard, Brit, Norwegian, Swede, Dane
- hobby: golf, chess, cooking, painting, tennis
- job: doctor, farmer, baker, lawyer, teacher
- pet: cat, rabbit, horse, bird, fish

Clues:
1. The person who enjoys painting lives immediately to the right of the golf enthusiast.
2. The owner of the cat and the teacher live in adjacent houses.
3. The Brit keeps the rabbit.
4. The farmer is the Dane.
5. The baker and the owner of the cat live two houses apart.
6. The person who enjoys cooking lives in the house just left of the one where the bird owner lives.
7. The baker lives immediately to the right of the farmer.
8. The Spaniard lives immediately to the right of the Dane.
9. The rabbit owner enjoys tennis.
10. The Swede keeps the horse.
11. The person who keeps the rabbit lives directly to the left of the lawyer.
12. The cooking enthusiast is the Swede.

## Puzzle zebra-00135

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- hobby: golf, cooking, painting, chess, tennis
- color: blue, red, green, white, yellow
- pet: cat, rabbit, dog, horse, bird
- job: lawyer, farmer, doctor, teacher, baker

Clues:
1. Whoever lives in the yellow house lives in the fourth house.
2. The person who keeps the dog lives in the house just left of the one where the person who keeps the rabbit lives.
3. The baker enjoys cooking.
4. The bird owner does not live in the first house.
5. The occupant of the white house lives in the house just left of the one where the person in the green house lives.
6. The farmer keeps the dog.
7. The owner of the bird works as the lawyer.
8. The person who keeps the cat lives somewhere to the right of the baker.
9. There is exactly one house between whoever lives in the blue house and the rabbit owner.
10. Whoever lives in the blue house either works as the doctor or works as the farmer.
11. Whoever lives in the green house lives somewhere to the left of the farmer.
12. The painting enthusiast lives in the fourth house.
13. The person who enjoys chess lives in one of the two end houses.
14. The tennis enthusiast lives in the house just left of the one where the painting enthusiast lives.

## Puzzle zebra-00136

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- drink: milk, cocoa, juice, coffee, tea
- job: lawyer, baker, pilot, farmer, doctor
- color: red, purple, white, yellow, green
- pet: fish, bird, dog, rabbit, horse

Clues:
1. The person in the white house and the baker are different people.
2. Whoever lives in the green house lives next to the occupant of the red house.
3. The person who keeps the fish lives immediately to the right of the cocoa drinker.
4. There is exactly one house between the person who keeps the dog and whoever lives in the purple house.
5. There is exactly one house between the doctor and the pilot.
6. The coffee drinker lives in house 1.
7. The person who keeps the horse lives in the house just left of the one where the doctor lives.
8. Whoever lives in the purple house and the tea drinker are neighbours.
9. The horse owner works as the lawyer.
10. The occupant of the green house lives somewhere to the right of the doctor.
11. The owner of the rabbit lives in the house just left of the one where the farmer lives.
12. The dog owner and the lawyer are not neighbours.
13. The person in the green house lives immediately to the right of the cocoa drinker.
14. The doctor and the owner of the rabbit are different people.
15. There is exactly one house between the occupant of the green house and the milk drinker.

## Puzzle zebra-00137

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- nationality: Swede, Spaniard, Brit, Norwegian, German
- drink: milk, juice, coffee, cocoa, water
- hobby: cooking, golf, tennis, hiking, painting
- pet: horse, rabbit, fish, bird, cat

Clues:
1. The juice drinker lives directly to the left of the Swede.
2. The Norwegian drinks coffee.
3. The German lives directly to the left of the person who enjoys hiking.
4. The person who enjoys cooking and the hiking enthusiast live two houses apart.
5. The owner of the bird lives in the second house.
6. The person who drinks water lives immediately to the right of the German.
7. The person who keeps the rabbit either is the Brit or is the Spaniard.
8. The cat owner lives somewhere to the right of the Spaniard.
9. The hiking enthusiast and the horse owner are neighbours.
10. The person who enjoys tennis lives in the second house.
11. The person who drinks milk lives next to the Spaniard.
12. The Spaniard either keeps the fish or keeps the rabbit.
13. The golf enthusiast is the Swede.

## Puzzle zebra-00138

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- color: purple, blue, yellow, white, green
- hobby: tennis, painting, cooking, chess, golf
- job: lawyer, baker, doctor, pilot, teacher
- drink: juice, cocoa, milk, water, coffee

Clues:
1. The painting enthusiast and the occupant of the purple house are neighbours.
2. The person in the blue house lives directly to the left of the teacher.
3. The lawyer lives at one end of the row.
4. The person who enjoys chess and the milk drinker are neighbours.
5. The person who enjoys cooking drinks water.
6. Whoever lives in the blue house lives in a lower-numbered house than the person in the white house.
7. The doctor lives in a lower-numbered house than the person who drinks coffee.
8. The pilot lives directly to the left of the doctor.
9. The tennis enthusiast works as the teacher.
10. The person who drinks water lives in the purple house.
11. The golf enthusiast and the teacher live two houses apart.
12. The person who drinks cocoa lives in one of the two end houses.
13. The person who drinks coffee lives next to the person who drinks milk.
14. The person who enjoys chess lives directly to the left of whoever lives in the green house.
15. Whoever lives in the green house either works as the doctor or works as the teacher.

## Puzzle zebra-00139

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- color: yellow, purple, red, white, blue
- pet: bird, rabbit, dog, horse, cat
- hobby: golf, chess, painting, tennis, cooking
- nationality: Brit, Spaniard, Dane, Norwegian, Swede

Clues:
1. The person in the blue house either is the Brit or is the Spaniard.
2. The Spaniard enjoys tennis.
3. The dog owner lives immediately to the right of the occupant of the white house.
4. The owner of the horse is the Brit.
5. The person in the white house lives directly to the left of the cooking enthusiast.
6. The Norwegian lives directly to the left of the person who enjoys chess.
7. The Norwegian and the Spaniard live in adjacent houses.
8. The owner of the bird and the occupant of the yellow house are neighbours.
9. The Norwegian and the person in the red house are neighbours.
10. The cooking enthusiast lives in the house just left of the one where the Dane lives.
11. The painting enthusiast lives somewhere to the right of the rabbit owner.
12. The cooking enthusiast lives somewhere to the right of whoever lives in the yellow house.
13. The rabbit owner lives in a lower-numbered house than the cooking enthusiast.
