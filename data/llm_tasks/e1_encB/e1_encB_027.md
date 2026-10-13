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

Output: write a single JSON object to the file /home/user/Puzzle-generation-with-guaranteed-uniqueness/data/llm_tasks/e1_encB/e1_encB_027.out.json with this exact structure
{"puzzles": [{"id": "<puzzle id>", "constraints": [{"clue": 1, "expr": "<expression>"}, ...]}, ...]}
One entry per puzzle and exactly one constraint per numbered clue, in order. Use single quotes inside
expressions so the JSON stays valid.

The puzzles follow.


## Puzzle paraphrase:zebra-00188

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- job: farmer, baker, teacher, pilot, lawyer
- drink: water, tea, coffee, milk, juice
- nationality: Spaniard, Brit, Swede, Norwegian, Dane
- hobby: tennis, hiking, chess, painting, cooking

Clues:
1. The tennis enthusiast lives in a house with a lower number than the teacher's.
2. The Brit lives immediately to the right of the juice drinker.
3. The Brit and the teacher are next-door neighbours.
4. The Spaniard is the lawyer.
5. Tea is drunk in the last house.
6. The Norwegian does not live in the second house.
7. The Swede is the hiking enthusiast.
8. The Brit and the farmer have one house between them.
9. The lawyer lives immediately to the left of the water drinker.
10. The cooking enthusiast and the Swede live two houses apart.
11. The baker's hobby is tennis.
12. The milk drinker lives immediately to the left of the baker.
13. Chess is the lawyer's hobby.

## Puzzle hard:zebra_hard-00063

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- drink: water, milk, coffee, juice, cocoa
- pet: fish, rabbit, dog, bird, horse
- hobby: chess, tennis, cooking, hiking, golf
- color: red, blue, green, purple, white

Clues:
1. Whoever lives in the white house lives somewhere between the bird owner and the occupant of the purple house.
2. Exactly one house separates the person who keeps the bird from the juice drinker.
3. If the person in the purple house does not keep the bird, then that person keeps the dog.
4. Exactly 3 houses lie to the left of the home of the milk drinker.
5. The cocoa drinker is not the same person as the cooking enthusiast.
6. None of the neighbours of the fish owner drinks juice.
7. The person in the green house lives two doors away from whoever lives in the white house.
8. The person who keeps the bird lives somewhere between the coffee drinker and the juice drinker.
9. The occupant of the white house lives somewhere between the person who drinks cocoa and the golf enthusiast.
10. Exactly 3 houses lie to the left of the home of the tennis enthusiast.
11. The person who enjoys chess lives in the fourth house from the right.
12. One of the neighbours of the person who drinks water lives in the red house.
13. The left-hand neighbour of the owner of the fish lives in the purple house.
14. One of the neighbours of the owner of the horse lives in the green house.

## Puzzle paraphrase:zebra-00159

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- hobby: painting, cooking, golf, chess, hiking
- pet: cat, bird, horse, fish, dog
- drink: juice, milk, water, cocoa, coffee
- color: blue, green, white, purple, red

Clues:
1. The cocoa drinker and the golfer live two houses apart.
2. The milk drinker lives in house 5.
3. The purple house is house 2.
4. The painter drinks either coffee or water.
5. The red house is the third house.
6. The fish keeper and the water drinker live two houses apart.
7. The cat owner lives in the third house.
8. The chess player is the one who keeps the fish.
9. The green house belongs to the dog owner.
10. The cocoa drinker keeps the cat.
11. The fish owner and the white house are two houses apart.
12. The horse owner drinks either cocoa or juice.
13. The cocoa drinker's house number is lower than the cook's.

## Puzzle plain:zebra-00013

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- pet: dog, horse, rabbit, fish, bird
- job: doctor, baker, pilot, teacher, lawyer
- drink: milk, juice, cocoa, water, tea
- color: white, red, blue, yellow, green

Clues:
1. The baker lives in the last house.
2. The juice drinker either keeps the bird or keeps the fish.
3. The owner of the fish lives immediately to the right of the rabbit owner.
4. Whoever lives in the green house lives in house 3.
5. Whoever lives in the yellow house drinks juice.
6. The water drinker does not live next to whoever lives in the white house.
7. The teacher keeps the rabbit.
8. The owner of the bird lives somewhere to the right of the horse owner.
9. The person who drinks cocoa does not live in the blue house.
10. The person in the blue house lives in house 1.
11. The bird owner and the water drinker live two houses apart.
12. The person who drinks milk and the person in the white house live two houses apart.
13. The person who keeps the horse works as the lawyer.
14. The doctor and the person in the yellow house live in adjacent houses.

## Puzzle paraphrase:zebra-00187

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- drink: juice, tea, milk, water, coffee
- pet: dog, bird, rabbit, horse, fish
- hobby: painting, chess, tennis, cooking, golf
- color: green, red, yellow, blue, purple

Clues:
1. The green house is immediately to the left of the bird's house.
2. Juice is drunk in the yellow house.
3. The tea drinker's hobby is painting.
4. The rabbit owner and the tea drinker are not neighbours.
5. The tennis enthusiast lives in house 1.
6. The milk drinker and the rabbit owner have exactly one house between them.
7. The yellow house is immediately to the left of the horse's house.
8. The painting enthusiast lives immediately to the left of the blue house.
9. The golf enthusiast lives immediately to the right of the yellow house.
10. The fish is kept somewhere to the right of the green house.
11. The cooking enthusiast keeps either the dog or the rabbit.
12. The red house is the second house.
13. The juice drinker lives immediately to the left of the water drinker.

## Puzzle hard:zebra_hard-00076

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- pet: fish, cat, rabbit, horse, dog
- job: farmer, baker, teacher, doctor, pilot
- hobby: painting, golf, chess, tennis, cooking
- color: red, white, green, blue, purple

Clues:
1. If the person who enjoys golf is not the baker, then that person works as the doctor.
2. The person who enjoys painting lives two doors away from the pilot.
3. One of the neighbours of the person in the green house enjoys chess.
4. None of the neighbours of the owner of the cat keeps the dog.
5. The owner of the cat and the doctor are one and the same person.
6. The person who enjoys chess lives in the second house from the right.
7. The doctor and the person in the red house are one and the same person.
8. The person in the purple house lives further to the right than the person who enjoys cooking.
9. The owner of the cat lives in the third house from the right.
10. The owner of the fish and whoever lives in the white house are one and the same person.
11. The farmer and the person who keeps the horse are one and the same person.
12. The cooking enthusiast lives somewhere between the owner of the fish and the horse owner.
13. If the baker does not keep the fish, then that person keeps the horse.

## Puzzle plain:zebra-00080

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- color: white, red, blue, yellow, green
- hobby: tennis, chess, hiking, cooking, golf
- job: doctor, farmer, pilot, lawyer, teacher
- pet: bird, cat, horse, rabbit, dog

Clues:
1. The owner of the dog enjoys chess.
2. The teacher lives somewhere to the left of the owner of the bird.
3. The person in the blue house lives somewhere to the right of the farmer.
4. The person who keeps the rabbit lives directly to the left of the teacher.
5. The person who enjoys chess either lives in the red house or lives in the yellow house.
6. The person who enjoys hiking and the occupant of the yellow house are neighbours.
7. The lawyer enjoys tennis.
8. Whoever lives in the green house and the person who enjoys hiking live in adjacent houses.
9. The doctor and the rabbit owner live two houses apart.
10. The person who keeps the cat lives in the house just left of the one where the golf enthusiast lives.
11. The person in the red house lives next to whoever lives in the white house.
12. There is exactly one house between the occupant of the blue house and the rabbit owner.
13. The occupant of the green house and the golf enthusiast are different people.
14. The cat owner and the person who enjoys cooking are neighbours.

## Puzzle plain:zebra-00061

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- drink: tea, coffee, cocoa, juice, water
- nationality: Norwegian, German, Swede, Spaniard, Dane
- job: baker, teacher, doctor, lawyer, pilot
- hobby: chess, hiking, golf, cooking, painting

Clues:
1. The doctor lives at one end of the row.
2. The juice drinker lives next to the Norwegian.
3. The teacher and the person who drinks water are neighbours.
4. The cocoa drinker lives directly to the left of the person who drinks juice.
5. The Dane and the lawyer live in adjacent houses.
6. The Dane lives directly to the left of the Swede.
7. The doctor lives somewhere to the left of the person who drinks water.
8. The person who enjoys golf and the person who drinks water live in adjacent houses.
9. The cocoa drinker either enjoys chess or enjoys hiking.
10. The Swede lives in the house just left of the one where the painting enthusiast lives.
11. The person who drinks tea either works as the doctor or works as the lawyer.
12. The German lives in a lower-numbered house than the juice drinker.
13. The German either enjoys hiking or enjoys painting.
14. The golf enthusiast and the Swede live two houses apart.
15. The baker lives somewhere to the right of the cocoa drinker.

## Puzzle paraphrase:zebra-00132

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- job: doctor, baker, teacher, lawyer, pilot
- pet: fish, horse, dog, cat, rabbit
- drink: milk, tea, coffee, water, cocoa
- hobby: chess, golf, hiking, tennis, cooking

Clues:
1. The cooking enthusiast lives next door to the dog owner.
2. The baker's hobby is hiking.
3. The dog owner lives in the fifth house.
4. The milk drinker and the rabbit owner are two houses apart.
5. Exactly one house lies between the hiking enthusiast and the horse owner.
6. The milk drinker lives right next to the tennis enthusiast.
7. The baker and the tea drinker are next-door neighbours.
8. The chess player and the rabbit owner are two houses apart.
9. The cooking enthusiast and the teacher live next to each other.
10. One house stands between the coffee drinker and the tea drinker.
11. One house stands between the doctor and the water drinker.
12. The cat belongs to the lawyer.
13. The tea drinker lives somewhere to the left of the water drinker.
14. The baker lives in one of the two end houses.
15. The pilot and the teacher are not next-door neighbours.

## Puzzle hard:zebra_hard-00017

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- pet: dog, bird, cat, horse, fish
- drink: water, milk, coffee, juice, cocoa
- hobby: hiking, chess, painting, golf, tennis
- color: blue, yellow, green, white, purple

Clues:
1. The person who drinks coffee lives further to the right than the person who enjoys chess.
2. The occupant of the purple house does not live in the fifth house from the right.
3. One of the neighbours of the person in the blue house enjoys hiking.
4. At least one house separates the painting enthusiast from the person who drinks milk.
5. Exactly 3 houses lie to the left of the home of the occupant of the blue house.
6. The owner of the cat and the person who enjoys tennis are one and the same person.
7. The person who drinks juice and whoever lives in the white house are one and the same person.
8. One of the neighbours of the golf enthusiast keeps the horse.
9. If the occupant of the white house does not enjoy golf, then that person enjoys hiking.
10. None of the neighbours of the person who keeps the horse lives in the purple house.
11. One of the neighbours of the person who enjoys tennis drinks water.
12. The coffee drinker and the person in the green house are one and the same person.
13. If the owner of the horse does not drink cocoa, then that person drinks coffee.
14. The person who keeps the bird and the chess enthusiast are one and the same person.
15. Exactly one house separates the golf enthusiast from the person who drinks water.
16. If the person who enjoys tennis does not live in the blue house, then that person lives in the yellow house.
17. If the cocoa drinker does not keep the cat, then that person keeps the dog.
