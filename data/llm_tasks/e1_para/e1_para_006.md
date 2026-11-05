# Task: rewrite logic-puzzle clues in natural prose

Below are logic-grid puzzles whose clues were produced by a template generator. Rewrite every clue
so it reads like a clue written by a human puzzle author: vary sentence structure, use natural
idioms (neighbours, "next door", "further down the street", ordinals, etc.), and avoid repeating
the template wording. The meaning of every clue must stay EXACTLY the same: do not add, drop, merge
or split information. Keep the numbering one-to-one (clue k becomes rewritten clue k). Keep the
value names exactly as listed in the header so a reader can match them. Houses stay numbered 1..N
from left to right.

Output: write a single JSON object to the file D:\Puzzle-generation-with-guaranteed-uniqueness\data\llm_tasks\e1_para\e1_para_006.out.json with this exact structure
{"puzzles": [{"id": "<puzzle id>", "clues": ["<rewritten clue 1>", "<rewritten clue 2>", ...]}, ...]}

The puzzles follow.


## Puzzle zebra-00160

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- pet: bird, dog, cat, rabbit, horse
- job: lawyer, teacher, baker, doctor, farmer
- hobby: chess, cooking, tennis, golf, painting
- drink: juice, water, coffee, cocoa, milk

Clues:
1. The tennis enthusiast drinks juice.
2. The owner of the cat and the person who enjoys painting live in adjacent houses.
3. The person who enjoys golf does not drink milk.
4. The lawyer lives in the middle house.
5. The person who enjoys chess lives in the house just left of the one where the painting enthusiast lives.
6. The person who keeps the bird works as the doctor.
7. The owner of the dog drinks milk.
8. The farmer does not live in the second house.
9. The person who enjoys golf works as the baker.
10. The farmer and the person who drinks water are neighbours.
11. The rabbit owner lives in the first house.
12. The person who drinks cocoa either enjoys painting or enjoys tennis.
13. The person who drinks water lives in the house just left of the one where the person who drinks coffee lives.

## Puzzle zebra-00161

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- drink: tea, cocoa, milk, water, coffee
- job: lawyer, teacher, doctor, farmer, baker
- pet: bird, cat, dog, fish, horse
- hobby: golf, tennis, painting, cooking, hiking

Clues:
1. The cocoa drinker lives in the first house.
2. The person who drinks tea lives next to the teacher.
3. The person who drinks cocoa and the farmer live in adjacent houses.
4. The person who enjoys hiking keeps the bird.
5. The person who drinks coffee either keeps the dog or keeps the fish.
6. The person who keeps the bird lives next to the owner of the fish.
7. The lawyer lives somewhere to the right of the person who enjoys painting.
8. The horse owner works as the farmer.
9. The cat owner lives in the middle house.
10. The milk drinker and the horse owner are different people.
11. The golf enthusiast lives somewhere to the left of the person who drinks milk.
12. The baker enjoys painting.
13. The cooking enthusiast lives next to the person who keeps the dog.
14. The person who drinks tea lives in one of the two end houses.

## Puzzle zebra-00162

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- color: purple, white, yellow, red, green
- hobby: hiking, cooking, painting, golf, tennis
- pet: horse, dog, bird, cat, rabbit
- drink: juice, cocoa, milk, water, coffee

Clues:
1. The person who enjoys hiking and the juice drinker live in adjacent houses.
2. The person who enjoys tennis lives immediately to the right of whoever lives in the green house.
3. Whoever lives in the white house lives in the last house.
4. The person who enjoys hiking lives in the purple house.
5. The hiking enthusiast lives immediately to the right of the person who enjoys cooking.
6. The owner of the rabbit lives in the white house.
7. The owner of the dog and the person who drinks juice are neighbours.
8. The person in the green house and the water drinker are neighbours.
9. Whoever lives in the green house and the person who drinks milk live in adjacent houses.
10. The person who enjoys hiking either keeps the bird or keeps the cat.
11. The tennis enthusiast lives immediately to the right of the cat owner.
12. The golf enthusiast lives in the fifth house.
13. The person who drinks milk lives in a lower-numbered house than the water drinker.
14. The person who drinks cocoa lives next to the person who enjoys hiking.
15. There is exactly one house between whoever lives in the green house and whoever lives in the yellow house.

## Puzzle zebra-00163

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- job: doctor, lawyer, teacher, baker, farmer
- pet: bird, horse, dog, rabbit, fish
- hobby: painting, hiking, golf, tennis, chess
- drink: cocoa, water, tea, juice, coffee

Clues:
1. The person who enjoys chess lives somewhere to the left of the person who enjoys golf.
2. The golf enthusiast does not live next to the person who drinks water.
3. The doctor enjoys hiking.
4. The cocoa drinker enjoys chess.
5. The rabbit owner lives in the last house.
6. The person who keeps the horse lives at one end of the row.
7. The person who enjoys chess does not keep the fish.
8. The person who enjoys chess lives next to the farmer.
9. The person who enjoys hiking and the horse owner live two houses apart.
10. The person who drinks juice lives directly to the left of the lawyer.
11. The baker and the doctor are not neighbours.
12. The water drinker lives at one end of the row.
13. The owner of the dog lives in the middle house.
14. The owner of the horse lives in the house just left of the one where the person who enjoys chess lives.
15. The person who enjoys tennis works as the baker.
16. The person who drinks coffee and the doctor live two houses apart.

## Puzzle zebra-00164

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- hobby: hiking, painting, chess, golf, tennis
- drink: coffee, milk, water, cocoa, tea
- nationality: Norwegian, Spaniard, Swede, Dane, Brit
- color: blue, purple, red, white, yellow

Clues:
1. The person who enjoys painting lives in the blue house.
2. There is exactly one house between the milk drinker and the Norwegian.
3. The person in the blue house and the person who drinks water live in adjacent houses.
4. The occupant of the purple house drinks tea.
5. The hiking enthusiast lives in a lower-numbered house than the Dane.
6. The Swede lives somewhere to the left of whoever lives in the red house.
7. The person who enjoys tennis lives in the fourth house.
8. The Brit and the cocoa drinker live in adjacent houses.
9. The person in the white house lives in the middle house.
10. The person who drinks water lives directly to the left of the person who enjoys golf.
11. The occupant of the purple house lives next to the Swede.
12. The person who enjoys hiking lives immediately to the right of the Spaniard.

## Puzzle zebra-00165

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- job: farmer, lawyer, teacher, pilot, doctor
- drink: tea, juice, milk, cocoa, coffee
- nationality: Norwegian, German, Swede, Brit, Spaniard
- hobby: chess, hiking, cooking, golf, tennis

Clues:
1. The Norwegian lives in the first house.
2. The person who drinks tea lives in the house just left of the one where the lawyer lives.
3. The German lives directly to the left of the farmer.
4. The milk drinker does not enjoy chess.
5. The person who enjoys golf works as the lawyer.
6. The farmer lives directly to the left of the coffee drinker.
7. There is exactly one house between the Brit and the pilot.
8. The person who drinks cocoa lives in the house just left of the one where the cooking enthusiast lives.
9. The farmer and the Spaniard live in adjacent houses.
10. The doctor either drinks cocoa or drinks juice.
11. The person who drinks milk lives in the house just left of the one where the person who enjoys tennis lives.
12. The person who enjoys cooking and the milk drinker live two houses apart.
13. The cocoa drinker lives next to the doctor.

## Puzzle zebra-00166

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- hobby: golf, cooking, chess, painting, hiking
- job: pilot, farmer, teacher, doctor, baker
- pet: dog, cat, fish, rabbit, horse
- color: yellow, purple, red, blue, green

Clues:
1. The hiking enthusiast lives next to the person who keeps the rabbit.
2. Whoever lives in the red house keeps the cat.
3. The doctor keeps the fish.
4. The golf enthusiast and the person who keeps the horse live in adjacent houses.
5. The occupant of the yellow house works as the baker.
6. There is exactly one house between the horse owner and the owner of the rabbit.
7. The baker enjoys cooking.
8. The occupant of the blue house and the owner of the fish live in adjacent houses.
9. The owner of the fish lives in one of the two end houses.
10. There is exactly one house between the horse owner and whoever lives in the yellow house.
11. The farmer lives in a lower-numbered house than the teacher.
12. The occupant of the green house lives immediately to the right of the person in the blue house.
13. There is exactly one house between the pilot and the person in the purple house.
14. There is exactly one house between the horse owner and the painting enthusiast.

## Puzzle zebra-00167

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- job: lawyer, doctor, farmer, pilot, baker
- drink: juice, coffee, tea, cocoa, milk
- color: red, green, purple, yellow, white
- pet: fish, cat, horse, dog, bird

Clues:
1. The fish owner and the lawyer live two houses apart.
2. Whoever lives in the purple house lives directly to the left of the person who drinks tea.
3. The coffee drinker lives next to the dog owner.
4. The person who drinks juice and the person in the white house live in adjacent houses.
5. The person who drinks milk lives in one of the two end houses.
6. Whoever lives in the purple house lives immediately to the right of the occupant of the white house.
7. The coffee drinker keeps the bird.
8. The dog owner lives in the purple house.
9. The baker keeps the cat.
10. The doctor and the owner of the dog live in adjacent houses.
11. There is exactly one house between the person in the green house and the occupant of the red house.
12. The farmer lives directly to the left of the person in the purple house.
13. The occupant of the green house lives in the middle house.
14. Whoever lives in the green house and the owner of the horse live two houses apart.

## Puzzle zebra-00168

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- pet: dog, fish, horse, bird, cat
- drink: cocoa, coffee, juice, milk, water
- job: pilot, doctor, lawyer, farmer, baker
- nationality: Dane, Brit, Norwegian, Swede, German

Clues:
1. There is exactly one house between the owner of the bird and the German.
2. The bird owner lives in a lower-numbered house than the pilot.
3. The lawyer lives in the house just left of the one where the baker lives.
4. The person who drinks cocoa lives in the house just left of the one where the baker lives.
5. The pilot lives in the house just left of the one where the Swede lives.
6. The person who keeps the horse lives in house 4.
7. The coffee drinker is the Dane.
8. The Brit lives directly to the left of the Dane.
9. The owner of the cat lives directly to the left of the water drinker.
10. The pilot keeps the fish.
11. The farmer keeps the horse.
12. The owner of the horse lives next to the person who drinks juice.

## Puzzle zebra-00169

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- pet: fish, cat, horse, bird, rabbit
- job: baker, lawyer, teacher, doctor, farmer
- drink: cocoa, juice, coffee, milk, water
- nationality: Norwegian, Spaniard, Swede, Dane, Brit

Clues:
1. The baker lives next to the rabbit owner.
2. The person who drinks coffee lives immediately to the right of the person who drinks water.
3. The cocoa drinker lives in house 5.
4. There is exactly one house between the Dane and the doctor.
5. There is exactly one house between the Norwegian and the Swede.
6. The owner of the cat and the fish owner live in adjacent houses.
7. The person who keeps the cat lives immediately to the right of the farmer.
8. The Dane and the person who keeps the rabbit live in adjacent houses.
9. The person who drinks cocoa and the farmer are neighbours.
10. The Spaniard either keeps the cat or keeps the horse.
11. The teacher drinks water.
12. There is exactly one house between the person who keeps the bird and the cat owner.
13. The person who drinks cocoa lives somewhere to the right of the doctor.
14. The owner of the rabbit is the Swede.
15. The doctor and the milk drinker live in adjacent houses.
