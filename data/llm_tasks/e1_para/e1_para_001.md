# Task: rewrite logic-puzzle clues in natural prose

Below are logic-grid puzzles whose clues were produced by a template generator. Rewrite every clue
so it reads like a clue written by a human puzzle author: vary sentence structure, use natural
idioms (neighbours, "next door", "further down the street", ordinals, etc.), and avoid repeating
the template wording. The meaning of every clue must stay EXACTLY the same: do not add, drop, merge
or split information. Keep the numbering one-to-one (clue k becomes rewritten clue k). Keep the
value names exactly as listed in the header so a reader can match them. Houses stay numbered 1..N
from left to right.

Output: write a single JSON object to the file /home/user/Puzzle-generation-with-guaranteed-uniqueness/data/llm_tasks/e1_para/e1_para_001.out.json with this exact structure
{"puzzles": [{"id": "<puzzle id>", "clues": ["<rewritten clue 1>", "<rewritten clue 2>", ...]}, ...]}

The puzzles follow.


## Puzzle zebra-00110

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- hobby: chess, hiking, cooking, golf, tennis
- pet: horse, rabbit, fish, bird, dog
- drink: milk, cocoa, tea, coffee, juice
- nationality: Dane, Swede, Spaniard, Norwegian, Brit

Clues:
1. The juice drinker enjoys golf.
2. The Brit and the person who keeps the rabbit live two houses apart.
3. The cocoa drinker lives in the house just left of the one where the Dane lives.
4. The cooking enthusiast keeps the horse.
5. The rabbit owner lives in house 5.
6. The person who drinks coffee lives somewhere to the right of the Dane.
7. The person who enjoys tennis lives directly to the left of the chess enthusiast.
8. The person who keeps the dog drinks juice.
9. The hiking enthusiast lives directly to the left of the dog owner.
10. The Swede lives in the leftmost house.
11. The Norwegian lives immediately to the right of the golf enthusiast.
12. The owner of the fish and the milk drinker are neighbours.

## Puzzle zebra-00111

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- drink: tea, coffee, water, juice, milk
- hobby: tennis, cooking, hiking, painting, golf
- color: white, blue, purple, green, red
- job: doctor, pilot, farmer, teacher, baker

Clues:
1. The farmer lives next to the pilot.
2. The person who drinks tea lives in the green house.
3. The person in the white house either enjoys cooking or enjoys tennis.
4. The person who drinks coffee lives in the purple house.
5. The baker either lives in the blue house or lives in the purple house.
6. The person who enjoys hiking does not live in the fourth house.
7. The farmer lives next to the painting enthusiast.
8. The baker and the occupant of the purple house are neighbours.
9. The milk drinker and the teacher live two houses apart.
10. The person who enjoys tennis lives in the third house.
11. The cooking enthusiast lives in one of the two end houses.
12. The person in the red house drinks water.
13. The hiking enthusiast lives immediately to the right of the pilot.
14. The person who enjoys cooking lives directly to the left of whoever lives in the green house.
15. The farmer either enjoys golf or enjoys hiking.

## Puzzle zebra-00112

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- hobby: painting, tennis, golf, hiking, chess
- pet: dog, bird, rabbit, cat, horse
- job: farmer, doctor, teacher, pilot, baker
- drink: coffee, milk, tea, juice, water

Clues:
1. The milk drinker lives in house 4.
2. The person who enjoys chess does not live in house 1.
3. The person who keeps the cat lives somewhere to the right of the baker.
4. The person who drinks milk works as the farmer.
5. The baker and the person who drinks juice are neighbours.
6. The pilot keeps the cat.
7. The person who keeps the dog does not live next to the water drinker.
8. The person who drinks water lives immediately to the right of the person who enjoys golf.
9. The painting enthusiast keeps the horse.
10. The person who drinks coffee lives next to the painting enthusiast.
11. The horse owner lives in the third house.
12. The owner of the bird lives in the house just left of the one where the teacher lives.
13. The chess enthusiast and the water drinker live two houses apart.
14. The person who enjoys hiking lives in a lower-numbered house than the tennis enthusiast.

## Puzzle zebra-00113

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- job: lawyer, doctor, baker, farmer, teacher
- drink: tea, milk, juice, water, coffee
- nationality: Swede, German, Norwegian, Spaniard, Brit
- color: red, yellow, purple, white, blue

Clues:
1. The person in the blue house and the teacher are not neighbours.
2. The doctor lives in the fifth house.
3. The coffee drinker lives directly to the left of the teacher.
4. The person in the blue house either works as the farmer or works as the lawyer.
5. The person who drinks juice is not the Norwegian.
6. The occupant of the white house lives in house 1.
7. The Swede and the doctor are different people.
8. Whoever lives in the blue house lives next to whoever lives in the yellow house.
9. The juice drinker and the Spaniard are neighbours.
10. The Spaniard lives in the house just left of the one where whoever lives in the purple house lives.
11. The lawyer either is the Brit or is the Spaniard.
12. There is exactly one house between the person who drinks milk and the Norwegian.
13. The baker lives in the white house.
14. The water drinker works as the baker.

## Puzzle zebra-00114

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- pet: bird, fish, cat, rabbit, horse
- nationality: Brit, Dane, Spaniard, Swede, Norwegian
- drink: coffee, tea, water, cocoa, juice
- job: lawyer, baker, farmer, teacher, doctor

Clues:
1. The cocoa drinker lives next to the Spaniard.
2. The person who drinks water lives in a lower-numbered house than the person who drinks tea.
3. The person who keeps the fish drinks cocoa.
4. The cocoa drinker does not live next to the juice drinker.
5. The Brit does not live next to the cat owner.
6. There is exactly one house between the Dane and the Spaniard.
7. The bird owner lives next to the farmer.
8. The Dane lives immediately to the right of the Norwegian.
9. The person who keeps the horse lives in the house just left of the one where the doctor lives.
10. The Swede drinks water.
11. The lawyer either keeps the bird or keeps the horse.
12. The person who keeps the cat lives in the fifth house.
13. The cocoa drinker works as the teacher.
14. The Brit lives next to the farmer.
15. The tea drinker works as the farmer.

## Puzzle zebra-00115

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- nationality: Spaniard, Brit, Dane, Swede, Norwegian
- drink: coffee, tea, cocoa, water, milk
- color: blue, yellow, purple, red, green
- job: doctor, teacher, pilot, lawyer, farmer

Clues:
1. The Norwegian lives directly to the left of the milk drinker.
2. The person in the red house lives directly to the left of whoever lives in the blue house.
3. The farmer drinks coffee.
4. The Brit either lives in the green house or lives in the red house.
5. The Dane lives in the fifth house.
6. There is exactly one house between the cocoa drinker and the person in the purple house.
7. There is exactly one house between the Brit and the Norwegian.
8. The Spaniard lives immediately to the right of the person in the green house.
9. The farmer lives next to the teacher.
10. The occupant of the yellow house lives immediately to the right of the Spaniard.
11. The doctor drinks water.
12. The farmer lives in the yellow house.
13. There is exactly one house between the farmer and the pilot.

## Puzzle zebra-00116

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- color: purple, red, green, white, yellow
- nationality: Brit, Spaniard, Dane, Swede, German
- hobby: golf, tennis, chess, cooking, hiking
- job: baker, lawyer, pilot, doctor, teacher

Clues:
1. The person who enjoys golf either is the Brit or is the Spaniard.
2. The doctor lives next to the golf enthusiast.
3. The cooking enthusiast lives next to the occupant of the purple house.
4. The Swede lives somewhere to the right of the person who enjoys tennis.
5. The Swede works as the teacher.
6. Whoever lives in the white house and whoever lives in the yellow house live two houses apart.
7. The baker and the pilot are neighbours.
8. The lawyer and the occupant of the yellow house live in adjacent houses.
9. The person who enjoys chess lives in the red house.
10. The Brit works as the lawyer.
11. The Dane does not live in the fourth house.
12. The occupant of the purple house lives directly to the left of the pilot.
13. The person in the purple house is the German.
14. The person who enjoys hiking lives immediately to the right of the person in the red house.

## Puzzle zebra-00117

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- drink: tea, cocoa, water, juice, coffee
- pet: rabbit, dog, bird, cat, fish
- hobby: hiking, painting, chess, cooking, tennis
- job: lawyer, pilot, teacher, baker, farmer

Clues:
1. The person who enjoys chess lives in house 5.
2. The baker drinks tea.
3. The cooking enthusiast lives immediately to the right of the cocoa drinker.
4. The owner of the bird either drinks coffee or drinks water.
5. The person who keeps the cat and the pilot live two houses apart.
6. The bird owner lives immediately to the right of the owner of the fish.
7. The farmer either drinks coffee or drinks juice.
8. The fish owner lives immediately to the right of the person who keeps the dog.
9. The coffee drinker and the person who enjoys hiking live two houses apart.
10. The lawyer lives directly to the left of the pilot.
11. The tennis enthusiast works as the baker.
12. The teacher does not live in the third house.
13. The owner of the bird enjoys hiking.

## Puzzle zebra-00118

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- hobby: tennis, chess, cooking, hiking, painting
- job: pilot, teacher, lawyer, doctor, farmer
- color: blue, white, yellow, red, green
- pet: dog, fish, horse, cat, bird

Clues:
1. The cat owner lives in the yellow house.
2. The hiking enthusiast either works as the lawyer or works as the pilot.
3. The bird owner lives next to the person in the white house.
4. The owner of the fish lives directly to the left of the person who enjoys hiking.
5. The farmer enjoys cooking.
6. There is exactly one house between the chess enthusiast and the person in the green house.
7. The painting enthusiast and the teacher live in adjacent houses.
8. The person who enjoys cooking lives in one of the two end houses.
9. The person who keeps the horse lives in the blue house.
10. The tennis enthusiast either lives in the blue house or lives in the red house.
11. The owner of the dog and the horse owner live in adjacent houses.
12. The person who enjoys hiking and the lawyer live in adjacent houses.
13. The painting enthusiast lives in the house just left of the one where the cat owner lives.
14. There is exactly one house between whoever lives in the blue house and the fish owner.

## Puzzle zebra-00119

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- job: lawyer, doctor, pilot, baker, farmer
- color: green, white, blue, red, yellow
- hobby: cooking, tennis, chess, hiking, painting
- pet: horse, dog, cat, bird, rabbit

Clues:
1. The occupant of the white house lives somewhere to the left of the owner of the bird.
2. The occupant of the yellow house lives in house 5.
3. The person who enjoys tennis works as the lawyer.
4. The person who keeps the rabbit lives in the leftmost house.
5. The person who enjoys cooking and the lawyer live two houses apart.
6. Whoever lives in the blue house enjoys chess.
7. There is exactly one house between the owner of the horse and the occupant of the red house.
8. Whoever lives in the blue house and the doctor are different people.
9. The person who enjoys cooking and the occupant of the white house live two houses apart.
10. The horse owner enjoys hiking.
11. The baker lives in house 2.
12. The pilot either enjoys painting or enjoys tennis.
13. The person who enjoys chess and the person in the white house are not neighbours.
14. The dog owner works as the pilot.
