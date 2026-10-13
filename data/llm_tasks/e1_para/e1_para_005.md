# Task: rewrite logic-puzzle clues in natural prose

Below are logic-grid puzzles whose clues were produced by a template generator. Rewrite every clue
so it reads like a clue written by a human puzzle author: vary sentence structure, use natural
idioms (neighbours, "next door", "further down the street", ordinals, etc.), and avoid repeating
the template wording. The meaning of every clue must stay EXACTLY the same: do not add, drop, merge
or split information. Keep the numbering one-to-one (clue k becomes rewritten clue k). Keep the
value names exactly as listed in the header so a reader can match them. Houses stay numbered 1..N
from left to right.

Output: write a single JSON object to the file /home/user/Puzzle-generation-with-guaranteed-uniqueness/data/llm_tasks/e1_para/e1_para_005.out.json with this exact structure
{"puzzles": [{"id": "<puzzle id>", "clues": ["<rewritten clue 1>", "<rewritten clue 2>", ...]}, ...]}

The puzzles follow.


## Puzzle zebra-00150

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- nationality: Brit, Dane, German, Spaniard, Swede
- job: pilot, lawyer, doctor, farmer, teacher
- hobby: golf, tennis, cooking, painting, chess
- color: white, purple, green, yellow, blue

Clues:
1. The teacher and whoever lives in the yellow house live two houses apart.
2. The Brit and the Spaniard live in adjacent houses.
3. The Swede enjoys painting.
4. The person who enjoys tennis either lives in the green house or lives in the yellow house.
5. Whoever lives in the green house lives in one of the two end houses.
6. The farmer lives somewhere to the right of the person who enjoys painting.
7. Whoever lives in the white house lives directly to the left of the lawyer.
8. There is exactly one house between the Dane and whoever lives in the purple house.
9. The German and the occupant of the green house live two houses apart.
10. The person who enjoys chess lives directly to the left of the doctor.
11. The Spaniard lives in the yellow house.
12. The farmer enjoys chess.
13. The Brit enjoys golf.

## Puzzle zebra-00151

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- drink: coffee, water, juice, milk, cocoa
- color: red, green, yellow, blue, purple
- nationality: Swede, Spaniard, Brit, Dane, Norwegian
- job: teacher, lawyer, farmer, pilot, baker

Clues:
1. The lawyer lives in the red house.
2. The baker lives somewhere to the right of the Swede.
3. The Brit lives at one end of the row.
4. The Norwegian lives immediately to the right of the milk drinker.
5. The person in the yellow house either works as the farmer or works as the pilot.
6. The Norwegian lives immediately to the right of whoever lives in the green house.
7. The person in the blue house and the Swede live two houses apart.
8. Whoever lives in the blue house is the Spaniard.
9. The Dane works as the baker.
10. There is exactly one house between the farmer and the occupant of the red house.
11. The juice drinker and the person who drinks milk live two houses apart.
12. Whoever lives in the red house lives in the house just left of the one where the juice drinker lives.
13. The teacher lives in a lower-numbered house than the Spaniard.
14. The Norwegian lives somewhere to the left of the water drinker.
15. Whoever lives in the blue house and the person who drinks coffee are not neighbours.

## Puzzle zebra-00152

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- drink: cocoa, tea, juice, water, milk
- job: farmer, teacher, lawyer, doctor, baker
- hobby: cooking, tennis, golf, chess, hiking
- pet: bird, cat, horse, dog, fish

Clues:
1. The person who enjoys cooking lives immediately to the right of the person who keeps the fish.
2. The juice drinker enjoys golf.
3. The person who drinks tea either enjoys chess or enjoys cooking.
4. The person who keeps the bird lives next to the milk drinker.
5. The person who drinks milk either keeps the bird or keeps the dog.
6. The person who drinks juice lives in one of the two end houses.
7. There is exactly one house between the farmer and the person who drinks juice.
8. The lawyer lives in a lower-numbered house than the owner of the dog.
9. The baker drinks water.
10. The person who enjoys hiking either works as the baker or works as the teacher.
11. The person who keeps the cat works as the farmer.
12. The baker and the person who enjoys hiking live two houses apart.
13. The person who enjoys chess lives in a lower-numbered house than the person who enjoys golf.
14. The dog owner and the tennis enthusiast are neighbours.

## Puzzle zebra-00153

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- job: lawyer, pilot, farmer, teacher, baker
- nationality: Spaniard, German, Norwegian, Brit, Swede
- hobby: hiking, golf, tennis, painting, chess
- drink: water, milk, tea, cocoa, coffee

Clues:
1. The hiking enthusiast lives in the house just left of the one where the person who drinks milk lives.
2. The farmer lives next to the Norwegian.
3. The person who drinks water lives in house 4.
4. The tennis enthusiast lives in the house just left of the one where the person who enjoys chess lives.
5. The person who drinks coffee enjoys chess.
6. The Brit lives directly to the left of the coffee drinker.
7. The tea drinker works as the baker.
8. The lawyer and the pilot are neighbours.
9. There is exactly one house between the German and the teacher.
10. The painting enthusiast and the person who drinks tea live two houses apart.
11. The milk drinker lives in the house just left of the one where the teacher lives.
12. The Swede lives immediately to the right of the pilot.

## Puzzle zebra-00154

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- hobby: painting, golf, cooking, tennis, hiking
- nationality: Brit, Swede, Norwegian, Dane, Spaniard
- drink: cocoa, water, milk, tea, coffee
- job: farmer, baker, teacher, doctor, lawyer

Clues:
1. The Dane and the Norwegian are not neighbours.
2. The milk drinker lives directly to the left of the tea drinker.
3. The person who enjoys golf lives at one end of the row.
4. The person who enjoys hiking works as the lawyer.
5. The doctor enjoys cooking.
6. The Swede lives at one end of the row.
7. The farmer lives in a lower-numbered house than the lawyer.
8. The baker and the golf enthusiast live in adjacent houses.
9. The person who drinks coffee lives next to the painting enthusiast.
10. The teacher lives in the house just left of the one where the person who drinks tea lives.
11. The coffee drinker and the person who drinks water live in adjacent houses.
12. The Dane either enjoys golf or enjoys tennis.
13. The Spaniard enjoys hiking.
14. The Brit lives in the fourth house.

## Puzzle zebra-00155

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- hobby: cooking, golf, painting, hiking, tennis
- drink: water, milk, coffee, juice, tea
- color: white, yellow, blue, green, purple
- pet: cat, bird, dog, horse, fish

Clues:
1. The person who enjoys hiking drinks coffee.
2. The juice drinker lives in house 4.
3. There is exactly one house between the person in the green house and whoever lives in the purple house.
4. Whoever lives in the blue house and the person who drinks tea are neighbours.
5. The bird owner lives in the house just left of the one where the occupant of the purple house lives.
6. The cooking enthusiast lives next to the water drinker.
7. The golf enthusiast lives next to the tennis enthusiast.
8. The person who enjoys tennis does not keep the dog.
9. There is exactly one house between the owner of the bird and the person in the yellow house.
10. The juice drinker lives somewhere to the right of the person in the yellow house.
11. The golf enthusiast and the person who keeps the horse are not neighbours.
12. The fish owner lives in the house just left of the one where the cat owner lives.
13. The painting enthusiast lives in a lower-numbered house than the hiking enthusiast.
14. The milk drinker and the tennis enthusiast are not neighbours.
15. The person in the white house either enjoys cooking or enjoys painting.
16. The owner of the fish and the water drinker are neighbours.
17. The tennis enthusiast either lives in the green house or lives in the purple house.

## Puzzle zebra-00156

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- drink: cocoa, tea, water, juice, coffee
- color: purple, red, yellow, green, blue
- hobby: golf, hiking, cooking, chess, tennis
- pet: fish, bird, dog, horse, rabbit

Clues:
1. Whoever lives in the green house lives directly to the left of the person who enjoys golf.
2. The juice drinker lives next to the person in the yellow house.
3. The person who keeps the fish lives in the house just left of the one where the person who drinks juice lives.
4. Whoever lives in the yellow house lives immediately to the right of the person who keeps the bird.
5. The person who keeps the rabbit enjoys cooking.
6. There is exactly one house between the chess enthusiast and the coffee drinker.
7. The person in the purple house lives somewhere to the right of the hiking enthusiast.
8. The person who drinks cocoa lives in the house just left of the one where the tea drinker lives.
9. There is exactly one house between the hiking enthusiast and the occupant of the red house.
10. The owner of the dog lives in the fourth house.
11. The rabbit owner lives immediately to the right of the person in the yellow house.
12. The person in the yellow house either drinks juice or drinks tea.

## Puzzle zebra-00157

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- hobby: hiking, painting, golf, tennis, cooking
- nationality: Spaniard, Norwegian, Dane, Swede, Brit
- color: red, green, blue, white, purple
- pet: bird, rabbit, cat, dog, fish

Clues:
1. The person who enjoys painting lives immediately to the right of the occupant of the red house.
2. The Dane and whoever lives in the white house live in adjacent houses.
3. The person who keeps the fish lives next to whoever lives in the white house.
4. The person who keeps the fish lives somewhere to the right of the Dane.
5. The rabbit owner and the Swede are not neighbours.
6. Whoever lives in the red house either enjoys painting or enjoys tennis.
7. The dog owner either is the Brit or is the Spaniard.
8. The hiking enthusiast does not live in the blue house.
9. The golf enthusiast is the Swede.
10. The person in the green house and whoever lives in the white house are neighbours.
11. The Brit lives in house 5.
12. Whoever lives in the purple house keeps the rabbit.
13. The person who enjoys painting lives somewhere to the left of the rabbit owner.
14. The bird owner lives in the house just left of the one where the person who keeps the rabbit lives.

## Puzzle zebra-00158

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- hobby: painting, tennis, chess, cooking, hiking
- color: white, green, red, purple, blue
- nationality: Spaniard, Brit, Dane, German, Swede
- pet: dog, fish, rabbit, horse, bird

Clues:
1. The hiking enthusiast keeps the fish.
2. Whoever lives in the green house lives next to the Swede.
3. The German lives in the house just left of the one where the person in the white house lives.
4. The person in the purple house and the rabbit owner are neighbours.
5. The person who enjoys painting lives in the red house.
6. The occupant of the purple house does not enjoy tennis.
7. The cooking enthusiast and the Dane live in adjacent houses.
8. The person who keeps the rabbit enjoys cooking.
9. The owner of the bird lives next to the Swede.
10. The Dane keeps the horse.
11. The person in the blue house is the Brit.
12. The Brit and whoever lives in the red house live two houses apart.
13. The occupant of the red house is the Swede.

## Puzzle zebra-00159

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- hobby: painting, cooking, golf, chess, hiking
- pet: cat, bird, horse, fish, dog
- drink: juice, milk, water, cocoa, coffee
- color: blue, green, white, purple, red

Clues:
1. The person who drinks cocoa and the golf enthusiast live two houses apart.
2. The milk drinker lives in house 5.
3. The occupant of the purple house lives in house 2.
4. The painting enthusiast either drinks coffee or drinks water.
5. The person in the red house lives in the third house.
6. The person who keeps the fish and the person who drinks water live two houses apart.
7. The owner of the cat lives in the third house.
8. The chess enthusiast keeps the fish.
9. The dog owner lives in the green house.
10. The person who drinks cocoa keeps the cat.
11. The owner of the fish and whoever lives in the white house live two houses apart.
12. The horse owner either drinks cocoa or drinks juice.
13. The cocoa drinker lives in a lower-numbered house than the person who enjoys cooking.
