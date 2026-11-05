# Task: rewrite logic-puzzle clues in natural prose

Below are logic-grid puzzles whose clues were produced by a template generator. Rewrite every clue
so it reads like a clue written by a human puzzle author: vary sentence structure, use natural
idioms (neighbours, "next door", "further down the street", ordinals, etc.), and avoid repeating
the template wording. The meaning of every clue must stay EXACTLY the same: do not add, drop, merge
or split information. Keep the numbering one-to-one (clue k becomes rewritten clue k). Keep the
value names exactly as listed in the header so a reader can match them. Houses stay numbered 1..N
from left to right.

Output: write a single JSON object to the file D:\Puzzle-generation-with-guaranteed-uniqueness\data\llm_tasks\e1_para\e1_para_002.out.json with this exact structure
{"puzzles": [{"id": "<puzzle id>", "clues": ["<rewritten clue 1>", "<rewritten clue 2>", ...]}, ...]}

The puzzles follow.


## Puzzle zebra-00120

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- color: green, white, yellow, purple, red
- nationality: Brit, Dane, German, Spaniard, Swede
- job: baker, pilot, doctor, farmer, teacher
- drink: juice, tea, water, coffee, cocoa

Clues:
1. The person in the green house and the Spaniard live in adjacent houses.
2. The Dane works as the pilot.
3. The occupant of the white house lives directly to the left of the Brit.
4. The German drinks tea.
5. Whoever lives in the white house lives in one of the two end houses.
6. The person who drinks coffee works as the farmer.
7. The teacher lives immediately to the right of the German.
8. The water drinker lives in the house just left of the one where the person who drinks juice lives.
9. The person who drinks water is the Brit.
10. The occupant of the red house lives in a lower-numbered house than the baker.
11. The person in the red house either works as the baker or works as the doctor.
12. Whoever lives in the purple house does not live in house 3.

## Puzzle zebra-00121

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- color: white, red, blue, yellow, purple
- hobby: cooking, golf, chess, tennis, hiking
- pet: fish, bird, horse, cat, dog
- nationality: Spaniard, Dane, Brit, Swede, German

Clues:
1. The owner of the dog lives next to the person who keeps the fish.
2. The person who enjoys hiking and the Swede live in adjacent houses.
3. The Brit and the person who enjoys golf live two houses apart.
4. The horse owner lives in the fifth house.
5. The Dane and the person in the yellow house are neighbours.
6. The Swede lives next to the person in the white house.
7. The person who keeps the fish and the golf enthusiast are neighbours.
8. The occupant of the purple house enjoys golf.
9. The person who enjoys chess either is the German or is the Swede.
10. The German lives immediately to the right of the person in the yellow house.
11. The bird owner lives in the blue house.
12. The Spaniard enjoys cooking.
13. The person who enjoys cooking lives in the white house.

## Puzzle zebra-00122

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- color: white, green, blue, purple, red
- drink: tea, cocoa, juice, milk, coffee
- hobby: cooking, tennis, hiking, golf, painting
- pet: rabbit, fish, bird, cat, horse

Clues:
1. The person in the white house lives in a lower-numbered house than whoever lives in the blue house.
2. Whoever lives in the green house drinks tea.
3. The hiking enthusiast lives directly to the left of the painting enthusiast.
4. The person who keeps the cat lives immediately to the right of the person who drinks cocoa.
5. There is exactly one house between the person who drinks cocoa and the cooking enthusiast.
6. The person who drinks juice lives at one end of the row.
7. The person who keeps the fish and the person in the purple house are neighbours.
8. There is exactly one house between whoever lives in the blue house and the occupant of the white house.
9. The horse owner and the owner of the rabbit are neighbours.
10. The milk drinker lives immediately to the right of the person who drinks juice.
11. The person who enjoys cooking drinks tea.
12. The occupant of the red house either keeps the fish or keeps the horse.
13. The golf enthusiast keeps the fish.

## Puzzle zebra-00123

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- drink: water, coffee, juice, milk, tea
- job: pilot, teacher, baker, farmer, lawyer
- nationality: Norwegian, Brit, Swede, German, Spaniard
- pet: cat, dog, bird, horse, rabbit

Clues:
1. The dog owner works as the teacher.
2. The Norwegian lives in the fifth house.
3. The Swede either drinks juice or drinks milk.
4. The Swede works as the pilot.
5. The person who drinks tea keeps the rabbit.
6. The dog owner and the Norwegian live in adjacent houses.
7. The Spaniard drinks milk.
8. There is exactly one house between the milk drinker and the person who drinks water.
9. The dog owner lives in the house just left of the one where the farmer lives.
10. The baker lives next to the person who keeps the cat.
11. The farmer and the owner of the horse live two houses apart.
12. The German lives immediately to the right of the person who keeps the rabbit.

## Puzzle zebra-00124

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- color: white, red, yellow, blue, purple
- pet: rabbit, horse, fish, bird, cat
- drink: juice, cocoa, milk, coffee, tea
- job: farmer, pilot, lawyer, teacher, doctor

Clues:
1. The occupant of the purple house and the teacher live in adjacent houses.
2. The cat owner lives immediately to the right of the owner of the fish.
3. The owner of the bird lives somewhere to the right of the farmer.
4. The pilot either keeps the cat or keeps the fish.
5. The rabbit owner either drinks coffee or drinks tea.
6. The juice drinker and whoever lives in the purple house live in adjacent houses.
7. The pilot and the occupant of the yellow house live in adjacent houses.
8. The farmer lives immediately to the right of the owner of the cat.
9. The coffee drinker lives in the first house.
10. The farmer and the owner of the rabbit live in adjacent houses.
11. There is exactly one house between the person in the blue house and the pilot.
12. The doctor lives somewhere to the right of the cocoa drinker.
13. The owner of the bird and the person in the purple house are not neighbours.
14. Whoever lives in the red house works as the pilot.

## Puzzle zebra-00125

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- drink: tea, juice, coffee, water, milk
- pet: rabbit, horse, dog, fish, bird
- color: red, green, blue, yellow, white
- hobby: hiking, golf, cooking, chess, tennis

Clues:
1. The milk drinker keeps the bird.
2. The occupant of the green house lives immediately to the right of the milk drinker.
3. The tea drinker lives somewhere to the left of the person who keeps the dog.
4. The coffee drinker lives directly to the left of the person in the white house.
5. The person in the white house either keeps the dog or keeps the rabbit.
6. The person who enjoys golf keeps the rabbit.
7. The person in the white house enjoys hiking.
8. The cooking enthusiast and the person who enjoys hiking live in adjacent houses.
9. The owner of the rabbit drinks coffee.
10. The occupant of the blue house lives immediately to the right of the occupant of the green house.
11. The person who enjoys tennis lives directly to the left of the rabbit owner.
12. The person in the yellow house and the fish owner are different people.
13. The owner of the fish drinks water.

## Puzzle zebra-00126

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- drink: cocoa, tea, milk, water, coffee
- job: pilot, baker, teacher, lawyer, doctor
- nationality: Spaniard, Norwegian, Dane, German, Swede
- color: blue, white, green, yellow, red

Clues:
1. Whoever lives in the yellow house lives in the first house.
2. The occupant of the blue house does not drink tea.
3. The person who drinks cocoa and the Norwegian are not neighbours.
4. There is exactly one house between the water drinker and the person in the white house.
5. Whoever lives in the blue house and the person who drinks cocoa are different people.
6. The doctor and the person who drinks water live two houses apart.
7. The person in the blue house lives in the house just left of the one where the Dane lives.
8. The person in the red house does not live next to the teacher.
9. The lawyer and the Spaniard live two houses apart.
10. The pilot and the tea drinker are neighbours.
11. There is exactly one house between the cocoa drinker and the Spaniard.
12. The German and the person in the white house live in adjacent houses.
13. The person in the green house lives in the house just left of the one where the cocoa drinker lives.
14. The person who drinks coffee lives in the white house.

## Puzzle zebra-00127

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- drink: cocoa, milk, juice, coffee, tea
- color: blue, red, green, yellow, white
- nationality: Spaniard, Brit, Swede, Dane, German
- pet: fish, bird, horse, cat, rabbit

Clues:
1. The cocoa drinker and the Swede are neighbours.
2. The cat owner does not live next to the Swede.
3. The Spaniard keeps the rabbit.
4. The Dane lives in the house just left of the one where the fish owner lives.
5. The milk drinker lives directly to the left of the fish owner.
6. The German and the person in the green house live two houses apart.
7. The owner of the rabbit lives somewhere to the right of the fish owner.
8. The person who drinks coffee either lives in the blue house or lives in the white house.
9. The German lives in house 4.
10. The juice drinker lives in the blue house.
11. The milk drinker lives in the yellow house.
12. The German and the horse owner are not neighbours.
13. Whoever lives in the blue house lives directly to the left of the Spaniard.
14. The person who keeps the cat lives next to the Spaniard.

## Puzzle zebra-00128

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- job: doctor, teacher, pilot, lawyer, farmer
- nationality: Spaniard, Norwegian, German, Dane, Brit
- color: blue, purple, white, yellow, red
- hobby: tennis, hiking, golf, cooking, painting

Clues:
1. The lawyer is the Norwegian.
2. The person in the blue house lives in the second house.
3. The Dane either enjoys golf or enjoys painting.
4. The pilot lives in the leftmost house.
5. Whoever lives in the white house is the Dane.
6. The person in the red house lives immediately to the right of the teacher.
7. The Spaniard enjoys golf.
8. The person in the white house lives directly to the left of the teacher.
9. The teacher and the tennis enthusiast live two houses apart.
10. The occupant of the blue house either is the Dane or is the German.
11. The person in the red house enjoys hiking.
12. The doctor and the German live two houses apart.
13. Whoever lives in the purple house either enjoys golf or enjoys painting.

## Puzzle zebra-00129

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- drink: milk, cocoa, water, tea, coffee
- hobby: chess, painting, cooking, tennis, golf
- color: purple, blue, yellow, red, green
- job: lawyer, doctor, pilot, farmer, baker

Clues:
1. The doctor lives directly to the left of whoever lives in the red house.
2. The person who drinks tea lives immediately to the right of the milk drinker.
3. The baker lives directly to the left of the occupant of the yellow house.
4. There is exactly one house between the person who drinks coffee and the tennis enthusiast.
5. The coffee drinker does not live next to the golf enthusiast.
6. Whoever lives in the green house lives in the house just left of the one where the occupant of the yellow house lives.
7. The occupant of the yellow house works as the lawyer.
8. The coffee drinker lives somewhere to the left of the occupant of the blue house.
9. The golf enthusiast either lives in the purple house or lives in the yellow house.
10. The pilot lives in a lower-numbered house than the farmer.
11. The person who drinks cocoa and the person who enjoys cooking live in adjacent houses.
12. The person who drinks coffee lives immediately to the right of the person who drinks water.
13. The occupant of the blue house lives at one end of the row.
14. The painting enthusiast lives directly to the left of the person who drinks milk.
