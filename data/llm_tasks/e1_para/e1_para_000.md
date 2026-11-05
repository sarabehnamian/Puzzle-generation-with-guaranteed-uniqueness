# Task: rewrite logic-puzzle clues in natural prose

Below are logic-grid puzzles whose clues were produced by a template generator. Rewrite every clue
so it reads like a clue written by a human puzzle author: vary sentence structure, use natural
idioms (neighbours, "next door", "further down the street", ordinals, etc.), and avoid repeating
the template wording. The meaning of every clue must stay EXACTLY the same: do not add, drop, merge
or split information. Keep the numbering one-to-one (clue k becomes rewritten clue k). Keep the
value names exactly as listed in the header so a reader can match them. Houses stay numbered 1..N
from left to right.

Output: write a single JSON object to the file D:\Puzzle-generation-with-guaranteed-uniqueness\data\llm_tasks\e1_para\e1_para_000.out.json with this exact structure
{"puzzles": [{"id": "<puzzle id>", "clues": ["<rewritten clue 1>", "<rewritten clue 2>", ...]}, ...]}

The puzzles follow.


## Puzzle zebra-00100

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- pet: bird, dog, horse, cat, fish
- drink: tea, water, juice, coffee, milk
- hobby: chess, tennis, painting, cooking, hiking
- job: lawyer, pilot, doctor, baker, farmer

Clues:
1. The doctor and the farmer are neighbours.
2. The person who drinks milk lives in the third house.
3. The cat owner lives somewhere to the left of the chess enthusiast.
4. The juice drinker lives in the house just left of the one where the person who enjoys cooking lives.
5. There is exactly one house between the coffee drinker and the farmer.
6. The person who enjoys cooking lives directly to the left of the person who keeps the horse.
7. The doctor lives in a lower-numbered house than the lawyer.
8. The person who keeps the dog lives in the house just left of the one where the tennis enthusiast lives.
9. The owner of the fish and the tea drinker are neighbours.
10. The cooking enthusiast and the person who enjoys hiking live two houses apart.
11. The doctor and the lawyer live two houses apart.
12. The baker lives in house 2.
13. The bird owner enjoys hiking.

## Puzzle zebra-00101

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- job: farmer, pilot, doctor, baker, teacher
- drink: water, tea, coffee, juice, milk
- hobby: golf, painting, chess, tennis, cooking
- color: red, white, purple, green, blue

Clues:
1. The teacher lives in the first house.
2. The baker and the water drinker are neighbours.
3. Whoever lives in the purple house drinks water.
4. The farmer either enjoys cooking or enjoys painting.
5. The teacher either enjoys chess or enjoys golf.
6. The painting enthusiast lives directly to the left of the person who enjoys chess.
7. The person who enjoys tennis lives in the white house.
8. The pilot lives in the fourth house.
9. There is exactly one house between the person who drinks coffee and the person in the green house.
10. The milk drinker and the pilot are not neighbours.
11. The baker either lives in the green house or lives in the purple house.
12. There is exactly one house between the doctor and the farmer.
13. The person who drinks juice and the occupant of the red house live in adjacent houses.
14. The cooking enthusiast and the tennis enthusiast are neighbours.

## Puzzle zebra-00102

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- hobby: tennis, painting, chess, hiking, golf
- pet: cat, bird, dog, fish, rabbit
- job: doctor, farmer, teacher, lawyer, pilot
- nationality: Dane, German, Spaniard, Norwegian, Swede

Clues:
1. The person who enjoys golf is the Norwegian.
2. The person who keeps the fish lives somewhere to the left of the pilot.
3. The owner of the cat and the German live two houses apart.
4. The owner of the bird lives in the last house.
5. The cat owner either enjoys golf or enjoys hiking.
6. The rabbit owner lives in the house just left of the one where the doctor lives.
7. The farmer lives next to the person who enjoys tennis.
8. The doctor is the Swede.
9. The Dane works as the lawyer.
10. The Spaniard lives in house 2.
11. The person who keeps the bird and the person who enjoys chess are neighbours.
12. The German works as the farmer.
13. The dog owner is the Swede.

## Puzzle zebra-00103

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- drink: cocoa, tea, coffee, juice, water
- nationality: Spaniard, German, Brit, Swede, Norwegian
- hobby: hiking, golf, painting, cooking, chess
- color: red, purple, blue, green, white

Clues:
1. The coffee drinker enjoys cooking.
2. The occupant of the purple house is the Brit.
3. The cocoa drinker lives immediately to the right of the person who enjoys hiking.
4. There is exactly one house between the occupant of the blue house and the Norwegian.
5. The person who drinks juice lives in house 2.
6. The cocoa drinker lives somewhere to the right of the Swede.
7. There is exactly one house between the German and the occupant of the purple house.
8. The painting enthusiast lives directly to the left of the Brit.
9. The person in the white house enjoys hiking.
10. The Norwegian does not drink tea.
11. The person in the blue house lives in house 3.
12. Whoever lives in the red house enjoys golf.
13. The person who drinks coffee lives in the leftmost house.

## Puzzle zebra-00104

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- drink: cocoa, coffee, tea, water, milk
- nationality: Swede, Spaniard, Dane, Norwegian, German
- hobby: chess, painting, golf, tennis, cooking
- color: blue, red, yellow, white, purple

Clues:
1. The person in the red house and the Spaniard live in adjacent houses.
2. The person who drinks milk and whoever lives in the white house live two houses apart.
3. The Norwegian lives immediately to the right of the Spaniard.
4. The person who enjoys cooking lives next to the German.
5. The German lives in the house just left of the one where the person who drinks coffee lives.
6. The coffee drinker does not live next to the water drinker.
7. The person who drinks coffee and the person who enjoys golf are not neighbours.
8. The Norwegian lives in the fifth house.
9. The milk drinker either enjoys chess or enjoys cooking.
10. The Dane lives directly to the left of the person in the blue house.
11. The person who drinks cocoa lives in the leftmost house.
12. The person in the yellow house enjoys painting.
13. The painting enthusiast lives directly to the left of the person who drinks water.
14. The occupant of the red house drinks water.

## Puzzle zebra-00105

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- pet: dog, horse, rabbit, bird, cat
- job: lawyer, farmer, teacher, pilot, doctor
- drink: juice, tea, milk, water, coffee
- color: green, blue, white, red, purple

Clues:
1. Whoever lives in the green house works as the lawyer.
2. The coffee drinker lives in the fourth house.
3. The person in the red house lives somewhere to the right of the occupant of the blue house.
4. The owner of the cat lives immediately to the right of the dog owner.
5. The owner of the bird and the doctor live in adjacent houses.
6. The person who drinks tea lives immediately to the right of the rabbit owner.
7. The farmer lives in the red house.
8. The person who drinks juice lives directly to the left of the person in the purple house.
9. There is exactly one house between the person who drinks coffee and the doctor.
10. The person who drinks coffee and the pilot live in adjacent houses.
11. The occupant of the blue house keeps the horse.
12. The lawyer lives immediately to the right of the person who drinks water.

## Puzzle zebra-00106

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- hobby: cooking, painting, golf, tennis, chess
- color: yellow, red, green, blue, purple
- job: pilot, doctor, baker, lawyer, teacher
- nationality: Dane, Norwegian, German, Spaniard, Swede

Clues:
1. The Spaniard lives in the second house.
2. The person who enjoys cooking either works as the lawyer or works as the pilot.
3. The Swede lives immediately to the right of the person in the green house.
4. There is exactly one house between the person who enjoys golf and the pilot.
5. The doctor lives immediately to the right of the Norwegian.
6. The lawyer lives directly to the left of the person who enjoys tennis.
7. The teacher lives in house 2.
8. The Dane lives in the house just left of the one where the person in the red house lives.
9. The person who enjoys golf lives in the purple house.
10. The person who enjoys chess lives in the blue house.
11. The Norwegian lives somewhere to the left of whoever lives in the yellow house.
12. The person who enjoys tennis lives in the fourth house.

## Puzzle zebra-00107

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- hobby: chess, golf, hiking, tennis, cooking
- pet: bird, dog, fish, rabbit, cat
- nationality: German, Dane, Brit, Swede, Spaniard
- job: lawyer, teacher, doctor, pilot, baker

Clues:
1. The teacher is the Brit.
2. The Dane lives next to the Spaniard.
3. The Swede lives in the house just left of the one where the fish owner lives.
4. The hiking enthusiast lives in the last house.
5. The fish owner lives next to the lawyer.
6. The person who enjoys golf lives immediately to the right of the cooking enthusiast.
7. There is exactly one house between the owner of the cat and the hiking enthusiast.
8. There is exactly one house between the pilot and the person who enjoys tennis.
9. The person who enjoys hiking lives next to the Spaniard.
10. The doctor lives directly to the left of the lawyer.
11. The Dane keeps the bird.
12. The person who enjoys chess lives in the fourth house.
13. The doctor and the person who keeps the rabbit are neighbours.

## Puzzle zebra-00108

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- nationality: Norwegian, German, Spaniard, Dane, Swede
- hobby: hiking, chess, golf, painting, tennis
- job: farmer, teacher, pilot, doctor, lawyer
- pet: rabbit, horse, cat, bird, dog

Clues:
1. The rabbit owner lives in house 3.
2. There is exactly one house between the golf enthusiast and the person who enjoys hiking.
3. The Spaniard lives in the house just left of the one where the owner of the dog lives.
4. The Swede lives in house 2.
5. There is exactly one house between the lawyer and the tennis enthusiast.
6. The Dane does not live next to the painting enthusiast.
7. The Dane and the teacher live in adjacent houses.
8. The person who enjoys golf and the pilot are neighbours.
9. The hiking enthusiast works as the lawyer.
10. The doctor lives in house 5.
11. The owner of the cat lives directly to the left of the bird owner.
12. The Dane and the Norwegian are neighbours.
13. The owner of the horse lives in house 1.

## Puzzle zebra-00109

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- nationality: Brit, Norwegian, Swede, Spaniard, German
- job: doctor, baker, lawyer, farmer, pilot
- hobby: golf, hiking, painting, cooking, chess
- pet: fish, dog, cat, rabbit, horse

Clues:
1. The person who enjoys chess lives in house 4.
2. The doctor enjoys cooking.
3. The painting enthusiast lives directly to the left of the hiking enthusiast.
4. The Brit and the Spaniard are neighbours.
5. The owner of the rabbit works as the farmer.
6. The pilot lives immediately to the right of the baker.
7. There is exactly one house between the farmer and the Norwegian.
8. The baker lives somewhere to the left of the owner of the horse.
9. The hiking enthusiast keeps the dog.
10. The fish owner lives in the house just left of the one where the baker lives.
11. The lawyer lives directly to the left of the German.
12. The owner of the fish is not the Spaniard.
