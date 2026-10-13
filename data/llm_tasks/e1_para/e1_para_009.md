# Task: rewrite logic-puzzle clues in natural prose

Below are logic-grid puzzles whose clues were produced by a template generator. Rewrite every clue
so it reads like a clue written by a human puzzle author: vary sentence structure, use natural
idioms (neighbours, "next door", "further down the street", ordinals, etc.), and avoid repeating
the template wording. The meaning of every clue must stay EXACTLY the same: do not add, drop, merge
or split information. Keep the numbering one-to-one (clue k becomes rewritten clue k). Keep the
value names exactly as listed in the header so a reader can match them. Houses stay numbered 1..N
from left to right.

Output: write a single JSON object to the file /home/user/Puzzle-generation-with-guaranteed-uniqueness/data/llm_tasks/e1_para/e1_para_009.out.json with this exact structure
{"puzzles": [{"id": "<puzzle id>", "clues": ["<rewritten clue 1>", "<rewritten clue 2>", ...]}, ...]}

The puzzles follow.


## Puzzle zebra-00190

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- nationality: Swede, German, Brit, Norwegian, Dane
- hobby: hiking, painting, cooking, chess, tennis
- drink: milk, juice, cocoa, tea, water
- pet: fish, dog, rabbit, horse, cat

Clues:
1. The person who enjoys chess keeps the rabbit.
2. The person who drinks cocoa lives somewhere to the left of the person who drinks juice.
3. The Dane either keeps the dog or keeps the fish.
4. The person who enjoys cooking lives in house 1.
5. There is exactly one house between the cat owner and the painting enthusiast.
6. The tea drinker is the German.
7. The person who enjoys hiking lives in house 4.
8. The cooking enthusiast and the person who drinks milk live two houses apart.
9. The tennis enthusiast lives immediately to the right of the chess enthusiast.
10. The horse owner either drinks milk or drinks water.
11. The Swede lives directly to the left of the water drinker.
12. The dog owner either drinks juice or drinks water.
13. The Brit lives immediately to the right of the Norwegian.

## Puzzle zebra-00191

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- hobby: painting, golf, cooking, chess, tennis
- job: pilot, baker, lawyer, teacher, farmer
- pet: horse, bird, fish, cat, dog
- nationality: Norwegian, Swede, Spaniard, Brit, Dane

Clues:
1. The Dane and the owner of the dog live in adjacent houses.
2. The person who keeps the horse lives immediately to the right of the person who enjoys chess.
3. The person who enjoys tennis works as the pilot.
4. The cat owner lives next to the Swede.
5. The Swede lives in the house just left of the one where the horse owner lives.
6. The bird owner works as the lawyer.
7. The teacher lives somewhere to the right of the pilot.
8. The person who enjoys cooking works as the farmer.
9. The person who enjoys painting keeps the cat.
10. The horse owner lives in the house just left of the one where the dog owner lives.
11. The cooking enthusiast is the Spaniard.
12. The person who enjoys tennis keeps the horse.
13. The pilot is the Brit.

## Puzzle zebra-00192

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- drink: tea, juice, milk, coffee, cocoa
- job: lawyer, baker, teacher, farmer, pilot
- hobby: tennis, golf, hiking, painting, chess
- pet: horse, fish, cat, bird, dog

Clues:
1. The baker does not live next to the owner of the fish.
2. The owner of the cat lives directly to the left of the person who drinks milk.
3. The person who enjoys painting lives in the leftmost house.
4. The owner of the horse and the teacher live two houses apart.
5. The cat owner and the person who enjoys hiking live two houses apart.
6. The person who enjoys hiking lives next to the person who keeps the horse.
7. The dog owner either works as the farmer or works as the lawyer.
8. The pilot either enjoys chess or enjoys tennis.
9. The owner of the dog lives in the house just left of the one where the person who drinks tea lives.
10. There is exactly one house between the lawyer and the person who drinks tea.
11. The person who enjoys hiking lives somewhere to the right of the farmer.
12. The owner of the cat lives directly to the left of the chess enthusiast.
13. The fish owner lives in a lower-numbered house than the horse owner.
14. There is exactly one house between the lawyer and the pilot.
15. The hiking enthusiast either drinks cocoa or drinks milk.
16. The person who drinks coffee lives in house 1.

## Puzzle zebra-00193

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- nationality: Swede, German, Brit, Spaniard, Dane
- job: baker, doctor, teacher, farmer, pilot
- pet: fish, dog, cat, rabbit, horse
- color: green, blue, yellow, white, red

Clues:
1. Whoever lives in the white house and the person in the yellow house live in adjacent houses.
2. The doctor is the Dane.
3. The person who keeps the cat lives immediately to the right of the Swede.
4. Whoever lives in the green house either keeps the cat or keeps the dog.
5. The German and whoever lives in the red house are not neighbours.
6. The Brit and the farmer live in adjacent houses.
7. The Swede works as the pilot.
8. The Dane and whoever lives in the yellow house live two houses apart.
9. The German and the pilot live in adjacent houses.
10. The person in the blue house lives directly to the left of whoever lives in the yellow house.
11. The person who keeps the dog lives somewhere to the right of the German.
12. The teacher lives somewhere to the right of the Brit.
13. The owner of the rabbit either works as the doctor or works as the pilot.
14. The person who keeps the fish works as the teacher.

## Puzzle zebra-00194

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- job: doctor, farmer, baker, teacher, lawyer
- pet: horse, dog, cat, bird, rabbit
- nationality: Dane, German, Norwegian, Brit, Swede
- color: green, white, red, blue, yellow

Clues:
1. The farmer lives in one of the two end houses.
2. The lawyer keeps the horse.
3. Whoever lives in the yellow house lives in the house just left of the one where the cat owner lives.
4. The person who keeps the bird and the lawyer are neighbours.
5. There is exactly one house between the baker and the Swede.
6. The Swede either lives in the blue house or lives in the green house.
7. The horse owner either lives in the blue house or lives in the white house.
8. Whoever lives in the red house either works as the lawyer or works as the teacher.
9. The baker and the Brit live in adjacent houses.
10. The German lives in the leftmost house.
11. The Norwegian keeps the rabbit.
12. The Dane lives next to the teacher.
13. Whoever lives in the red house keeps the dog.
14. The occupant of the green house and the occupant of the red house are not neighbours.

## Puzzle zebra-00195

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- color: blue, green, red, white, purple
- drink: tea, coffee, milk, water, juice
- nationality: Brit, German, Swede, Spaniard, Dane
- pet: fish, horse, cat, dog, rabbit

Clues:
1. The fish owner is the Dane.
2. The person who drinks tea and the water drinker are neighbours.
3. The occupant of the purple house keeps the horse.
4. The Swede lives in a lower-numbered house than the owner of the horse.
5. The German either drinks milk or drinks tea.
6. Whoever lives in the red house lives in house 4.
7. The Brit and the person who keeps the dog live in adjacent houses.
8. The dog owner lives in the white house.
9. The person in the blue house lives in the first house.
10. There is exactly one house between the person who drinks milk and the rabbit owner.
11. The Brit lives in the middle house.
12. The person who drinks coffee lives immediately to the right of the occupant of the purple house.
13. The owner of the cat lives in the first house.
14. The person who drinks water lives in one of the two end houses.

## Puzzle zebra-00196

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- pet: horse, cat, bird, rabbit, fish
- nationality: German, Swede, Dane, Brit, Spaniard
- drink: water, milk, juice, coffee, cocoa
- color: red, white, green, yellow, blue

Clues:
1. The fish owner lives somewhere to the right of the occupant of the red house.
2. Whoever lives in the green house drinks juice.
3. The person who drinks milk lives at one end of the row.
4. The Dane and the person in the red house live two houses apart.
5. The person who keeps the bird drinks cocoa.
6. The person who keeps the bird either is the Brit or is the Dane.
7. The fish owner lives immediately to the right of whoever lives in the blue house.
8. The Brit lives in the house just left of the one where the person in the red house lives.
9. The rabbit owner lives in the yellow house.
10. The water drinker keeps the cat.
11. The German lives next to the water drinker.
12. The Spaniard lives immediately to the right of the Swede.
13. The German and the person in the green house live two houses apart.

## Puzzle zebra-00197

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- pet: fish, bird, horse, dog, cat
- drink: tea, cocoa, juice, milk, coffee
- nationality: Swede, German, Norwegian, Brit, Spaniard
- color: blue, red, purple, yellow, green

Clues:
1. The person who drinks milk lives in the house just left of the one where the person who keeps the bird lives.
2. There is exactly one house between the person who keeps the horse and the person who drinks milk.
3. The cocoa drinker either is the German or is the Spaniard.
4. The horse owner is the German.
5. The Brit lives next to whoever lives in the yellow house.
6. The cat owner lives immediately to the right of the owner of the fish.
7. The coffee drinker lives next to the person in the red house.
8. The occupant of the yellow house drinks juice.
9. The person who drinks tea lives in house 3.
10. The owner of the fish lives in the purple house.
11. The tea drinker either is the Brit or is the German.
12. The owner of the cat lives in the green house.
13. The fish owner and the Swede live two houses apart.

## Puzzle zebra-00198

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- drink: juice, tea, milk, coffee, cocoa
- color: red, green, yellow, blue, purple
- hobby: painting, tennis, chess, cooking, hiking
- job: baker, lawyer, teacher, pilot, farmer

Clues:
1. The person who drinks tea lives in the house just left of the one where the person in the blue house lives.
2. The baker lives in the house just left of the one where the coffee drinker lives.
3. The juice drinker works as the farmer.
4. The milk drinker lives somewhere to the left of the hiking enthusiast.
5. The farmer and the person who enjoys tennis live two houses apart.
6. The pilot lives immediately to the right of the milk drinker.
7. The person who enjoys hiking and the occupant of the purple house live in adjacent houses.
8. The person who enjoys chess lives in house 5.
9. The lawyer and the occupant of the yellow house are neighbours.
10. The person in the purple house lives immediately to the right of the person who drinks juice.
11. The pilot does not enjoy painting.
12. The cooking enthusiast lives directly to the left of the person in the green house.

## Puzzle zebra-00199

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- job: lawyer, pilot, baker, farmer, doctor
- drink: milk, tea, coffee, juice, cocoa
- hobby: chess, painting, tennis, cooking, hiking
- nationality: Brit, Dane, German, Norwegian, Spaniard

Clues:
1. The milk drinker is not the doctor.
2. The baker lives immediately to the right of the pilot.
3. The person who enjoys chess lives directly to the left of the Brit.
4. The farmer lives in the house just left of the one where the pilot lives.
5. The painting enthusiast lives immediately to the right of the Brit.
6. The Dane drinks tea.
7. The tea drinker lives next to the person who enjoys tennis.
8. The person who enjoys chess drinks coffee.
9. There is exactly one house between the Brit and the farmer.
10. The Norwegian lives immediately to the right of the cooking enthusiast.
11. The juice drinker lives next to the Norwegian.
12. The lawyer is the Spaniard.
13. The farmer lives immediately to the right of the doctor.
