# Task: encode logic-grid puzzles as solver constraints

Translate each puzzle below into constraints in a small Python DSL. A program will check your
constraints with a SAT/SMT solver, so they must say exactly what each clue says - no more, no less.

The DSL:
- pos('value') is the house number (an integer from 1 to N) of the given value. Use the value names
  exactly as they appear in the puzzle header (case does not matter).
- The basic rules (every value is in exactly one house; values of the same category are in different
  houses) are added automatically. Do not encode them.
- Encode each numbered clue as ONE Python boolean expression using pos(...), integer constants,
  == != < <= > >= + -, and the functions Abs(x), And(a, b, ...), Or(a, b, ...), Not(a), Implies(a, b).
- Do not use Python's and/or/not/in, chained comparisons such as 1 < x < 3, or abs().

Examples (from other puzzles):
- "The baker keeps the parrot."            ->  pos('baker') == pos('parrot')
- "The violinist lives in the fourth house." ->  pos('violinist') == 4
- "The person who reads poetry lives next to the person who drinks lemonade."
                                            ->  Abs(pos('poetry') - pos('lemonade')) == 1

Output: write a single JSON object to the file /home/user/Puzzle-generation-with-guaranteed-uniqueness/data/llm_tasks/e1_encA/e1_encA_021.out.json with this exact structure
{"puzzles": [{"id": "<puzzle id>", "constraints": [{"clue": 1, "expr": "<expression>"}, ...]}, ...]}
One entry per puzzle and exactly one constraint per numbered clue, in order. Use single quotes inside
expressions so the JSON stays valid.

The puzzles follow.


## Puzzle hard:zebra_hard-00001

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- job: doctor, baker, farmer, lawyer, teacher
- nationality: Brit, Swede, Spaniard, German, Dane
- drink: milk, juice, water, tea, cocoa
- pet: bird, horse, rabbit, dog, cat

Clues:
1. Neither the cat owner nor the milk drinker works as the doctor.
2. The right-hand neighbour of the German is the Brit.
3. The left-hand neighbour of the baker keeps the horse.
4. The person who drinks cocoa and the doctor are one and the same person.
5. The person who keeps the rabbit lives somewhere between the bird owner and the farmer.
6. The owner of the bird and the teacher are one and the same person.
7. The left-hand neighbour of the Spaniard drinks tea.
8. One of the neighbours of the person who drinks juice keeps the cat.
9. The Dane lives in the fifth house from the right.
10. One of the neighbours of the person who drinks water keeps the bird.
11. The right-hand neighbour of the person who keeps the cat drinks tea.
12. The baker and the water drinker are one and the same person.

## Puzzle hard:zebra_hard-00000

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- job: lawyer, baker, pilot, teacher, doctor
- color: white, red, blue, purple, yellow
- hobby: hiking, painting, chess, tennis, golf
- drink: juice, tea, milk, cocoa, water

Clues:
1. The person in the yellow house lives somewhere between whoever lives in the blue house and the water drinker.
2. Exactly one house separates the chess enthusiast from the golf enthusiast.
3. The cocoa drinker lives in the second house from the right.
4. The right-hand neighbour of the milk drinker works as the pilot.
5. One of the neighbours of whoever lives in the white house lives in the blue house.
6. The right-hand neighbour of the doctor lives in the blue house.
7. The teacher lives somewhere between the lawyer and the person who drinks milk.
8. If the chess enthusiast does not live in the blue house, then that person lives in the white house.
9. The left-hand neighbour of whoever lives in the red house works as the pilot.
10. The golf enthusiast lives further to the right than the person who drinks juice.
11. The right-hand neighbour of the tennis enthusiast enjoys hiking.
12. The person who enjoys golf and the pilot are one and the same person.

## Puzzle hard:zebra_hard-00082

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- job: teacher, lawyer, doctor, farmer, pilot
- color: yellow, blue, white, green, purple
- pet: dog, bird, fish, cat, horse
- drink: cocoa, water, coffee, milk, tea

Clues:
1. If the person who keeps the fish does not drink cocoa, then that person drinks coffee.
2. The cocoa drinker lives further to the right than the pilot.
3. The right-hand neighbour of the farmer drinks water.
4. The person who keeps the horse lives in the third house from the right.
5. The farmer and whoever lives in the purple house are one and the same person.
6. The doctor has only one neighbour.
7. The doctor and the occupant of the green house are one and the same person.
8. Exactly 0 houses lie to the left of the home of whoever lives in the blue house.
9. The left-hand neighbour of the teacher keeps the bird.
10. The cocoa drinker and the farmer are one and the same person.
11. The cat owner and the person in the white house are one and the same person.
12. None of the neighbours of the farmer keeps the dog.
13. The occupant of the blue house and the person who drinks tea are one and the same person.

## Puzzle plain:zebra-00078

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- drink: milk, coffee, cocoa, juice, water
- hobby: golf, tennis, chess, painting, cooking
- color: white, yellow, red, green, blue
- nationality: Norwegian, Swede, Spaniard, German, Dane

Clues:
1. The person in the blue house and the juice drinker live in adjacent houses.
2. The occupant of the green house lives directly to the left of the golf enthusiast.
3. The occupant of the green house and whoever lives in the yellow house live two houses apart.
4. The German lives next to the person who enjoys golf.
5. The person in the yellow house is the Swede.
6. The person who drinks coffee lives immediately to the right of the person who drinks milk.
7. The painting enthusiast lives directly to the left of the occupant of the white house.
8. Whoever lives in the green house either enjoys chess or enjoys painting.
9. The Dane enjoys painting.
10. The German drinks milk.
11. The water drinker lives in house 2.
12. The person who drinks juice enjoys tennis.
13. The occupant of the yellow house lives immediately to the right of the Norwegian.

## Puzzle hard:zebra_hard-00089

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- drink: milk, coffee, juice, water, tea
- pet: rabbit, cat, horse, bird, dog
- job: farmer, teacher, doctor, lawyer, pilot
- hobby: tennis, painting, hiking, cooking, chess

Clues:
1. The juice drinker lives somewhere between the cooking enthusiast and the horse owner.
2. The right-hand neighbour of the rabbit owner works as the teacher.
3. The right-hand neighbour of the doctor enjoys cooking.
4. The right-hand neighbour of the lawyer works as the doctor.
5. The farmer and the person who drinks juice are one and the same person.
6. The owner of the cat and the teacher are one and the same person.
7. The left-hand neighbour of the milk drinker enjoys painting.
8. The coffee drinker lives in the fifth house from the right.
9. The person who enjoys tennis lives somewhere between the person who drinks milk and the tea drinker.
10. The tennis enthusiast lives somewhere between the owner of the dog and the owner of the horse.
11. The left-hand neighbour of the hiking enthusiast enjoys painting.

## Puzzle plain:zebra-00010

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- job: baker, doctor, farmer, pilot, teacher
- drink: cocoa, milk, tea, water, coffee
- pet: bird, fish, horse, rabbit, dog
- nationality: German, Brit, Swede, Dane, Norwegian

Clues:
1. The Dane and the German live two houses apart.
2. There is exactly one house between the Norwegian and the teacher.
3. The owner of the fish lives next to the German.
4. The farmer lives next to the Norwegian.
5. The owner of the rabbit either works as the farmer or works as the pilot.
6. The owner of the horse lives directly to the left of the person who keeps the fish.
7. The bird owner works as the doctor.
8. The teacher lives in the house just left of the one where the coffee drinker lives.
9. The German lives next to the person who drinks tea.
10. The tea drinker either is the Brit or is the Norwegian.
11. The person who keeps the fish drinks cocoa.
12. The Brit lives next to the person who drinks milk.
13. The Swede is not the doctor.
14. The pilot lives directly to the left of the owner of the bird.
15. The milk drinker lives in house 2.

## Puzzle plain:zebra-00003

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- hobby: chess, hiking, cooking, tennis, golf
- nationality: Dane, Norwegian, Brit, Spaniard, Swede
- pet: bird, fish, horse, rabbit, dog
- job: farmer, baker, doctor, lawyer, pilot

Clues:
1. The owner of the horse enjoys chess.
2. The Swede either works as the farmer or works as the lawyer.
3. The Swede lives in the third house.
4. The Spaniard lives immediately to the right of the pilot.
5. The owner of the fish and the person who enjoys golf live two houses apart.
6. The Dane is not the farmer.
7. The person who keeps the horse lives somewhere to the left of the hiking enthusiast.
8. The person who keeps the fish lives in a lower-numbered house than the person who enjoys hiking.
9. The person who enjoys cooking works as the pilot.
10. The Norwegian keeps the rabbit.
11. The chess enthusiast either works as the lawyer or works as the pilot.
12. The Brit lives in one of the two end houses.
13. The baker lives immediately to the right of the Norwegian.
14. The owner of the rabbit lives next to the tennis enthusiast.
15. There is exactly one house between the bird owner and the owner of the horse.

## Puzzle plain:zebra-00020

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- pet: fish, horse, rabbit, cat, bird
- job: doctor, teacher, lawyer, farmer, pilot
- color: purple, blue, yellow, red, green
- hobby: painting, hiking, golf, cooking, chess

Clues:
1. The person who enjoys golf lives in one of the two end houses.
2. The person who keeps the bird lives immediately to the right of the lawyer.
3. The owner of the cat enjoys cooking.
4. The person in the green house lives directly to the left of the owner of the bird.
5. The person in the yellow house lives in the house just left of the one where the painting enthusiast lives.
6. Whoever lives in the blue house lives in the third house.
7. The cooking enthusiast works as the doctor.
8. The pilot keeps the fish.
9. The chess enthusiast either keeps the fish or keeps the rabbit.
10. There is exactly one house between the farmer and the occupant of the purple house.
11. The doctor lives in the house just left of the one where whoever lives in the red house lives.
12. The person who enjoys painting lives in the house just left of the one where the chess enthusiast lives.

## Puzzle paraphrase:zebra-00142

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- hobby: hiking, cooking, golf, tennis, painting
- job: farmer, pilot, lawyer, teacher, baker
- pet: bird, rabbit, cat, horse, fish
- color: yellow, purple, blue, green, red

Clues:
1. The golf enthusiast lives immediately left of the blue house's occupant.
2. The pilot and the rabbit owner are separated by exactly one house.
3. The painting enthusiast lives in house 4.
4. House 2 is home to the cooking enthusiast.
5. The bird owner lives immediately left of the purple house's occupant.
6. The red house's occupant is the teacher.
7. The baker lives in house 2.
8. The tennis enthusiast lives next door to the occupant of the blue house.
9. The farmer is not a neighbour of the rabbit owner.
10. The fish keeper and the rabbit owner live next to each other.
11. Exactly one house lies between the blue house and the green house.
12. The tennis enthusiast is either the farmer or the lawyer.
13. The fish owner lives next door to the person in the blue house.
14. The bird keeper lives next door to the horse owner.
15. The teacher lives in the middle house.

## Puzzle plain:zebra-00021

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- nationality: German, Brit, Spaniard, Norwegian, Swede
- job: farmer, baker, doctor, pilot, lawyer
- pet: fish, rabbit, dog, cat, horse
- color: yellow, blue, green, white, red

Clues:
1. The occupant of the white house works as the farmer.
2. The occupant of the white house lives at one end of the row.
3. The fish owner either is the Norwegian or is the Spaniard.
4. Whoever lives in the blue house and the fish owner are neighbours.
5. The cat owner lives in the second house.
6. The pilot is the Swede.
7. The person who keeps the dog lives directly to the left of the cat owner.
8. The German keeps the horse.
9. The doctor lives in the last house.
10. The fish owner lives next to the Spaniard.
11. The owner of the fish either lives in the blue house or lives in the green house.
12. There is exactly one house between the German and the lawyer.
13. Whoever lives in the red house lives in the house just left of the one where the baker lives.
