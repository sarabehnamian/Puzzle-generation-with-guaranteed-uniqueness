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

Output: write a single JSON object to the file /home/user/Puzzle-generation-with-guaranteed-uniqueness/data/llm_tasks/e1_encC/e1_encC_004.out.json with this exact structure
{"puzzles": [{"id": "<puzzle id>", "constraints": [{"clue": 1, "expr": "<expression>"}, ...]}, ...]}
One entry per puzzle and exactly one constraint per numbered clue, in order. Use single quotes inside
expressions so the JSON stays valid.

The puzzles follow.


## Puzzle hard:zebra_hard-00011

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- hobby: tennis, chess, painting, hiking, cooking
- drink: coffee, water, juice, milk, cocoa
- nationality: Norwegian, Brit, German, Swede, Dane
- pet: rabbit, dog, cat, fish, horse

Clues:
1. The person who enjoys tennis lives somewhere between the person who drinks cocoa and the person who enjoys hiking.
2. The person who enjoys painting and the Swede are one and the same person.
3. The person who drinks water lives somewhere between the juice drinker and the milk drinker.
4. The right-hand neighbour of the person who keeps the cat keeps the horse.
5. None of the neighbours of the Brit is the German.
6. The person who keeps the dog lives two doors away from the horse owner.
7. The person who drinks cocoa and the fish owner are one and the same person.
8. The Dane and the person who enjoys tennis are one and the same person.
9. Exactly one house separates the juice drinker from the Swede.
10. Exactly 3 houses lie to the left of the home of the fish owner.
11. If the person who drinks cocoa does not enjoy cooking, then that person enjoys tennis.
12. The person who enjoys chess and the milk drinker are one and the same person.
13. The right-hand neighbour of the rabbit owner is the Brit.

## Puzzle hard:zebra_hard-00006

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- nationality: German, Norwegian, Dane, Swede, Brit
- color: red, white, blue, green, purple
- drink: coffee, water, juice, cocoa, tea
- job: baker, pilot, doctor, farmer, lawyer

Clues:
1. The occupant of the green house and the lawyer are one and the same person.
2. The person who drinks coffee lives somewhere between the German and the juice drinker.
3. The left-hand neighbour of the pilot is the Norwegian.
4. The person in the purple house lives in the third house from the right.
5. The occupant of the green house lives somewhere between the person who drinks cocoa and the German.
6. The person in the blue house and the farmer are one and the same person.
7. Whoever lives in the blue house lives further to the right than the Norwegian.
8. The pilot lives somewhere between the doctor and the farmer.
9. The cocoa drinker and the Swede are one and the same person.
10. The right-hand neighbour of the person who drinks cocoa drinks tea.
11. The right-hand neighbour of the person who drinks juice is the Dane.
12. Exactly one house separates the person in the red house from the Swede.

## Puzzle hard:zebra_hard-00054

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- drink: coffee, water, cocoa, tea, juice
- pet: fish, horse, rabbit, cat, bird
- hobby: chess, cooking, painting, golf, tennis
- nationality: Dane, Brit, Spaniard, German, Swede

Clues:
1. The German lives in the fourth house from the right.
2. Exactly 0 houses lie to the left of the home of the person who drinks cocoa.
3. The left-hand neighbour of the owner of the fish is the Spaniard.
4. The person who enjoys golf and the Swede are one and the same person.
5. The person who enjoys chess and the person who keeps the fish are one and the same person.
6. One of the neighbours of the person who keeps the cat keeps the fish.
7. None of the neighbours of the owner of the rabbit keeps the fish.
8. The owner of the cat and the Dane are one and the same person.
9. The right-hand neighbour of the cooking enthusiast drinks tea.
10. Exactly one house separates the person who enjoys golf from the painting enthusiast.
11. One of the neighbours of the coffee drinker is the Dane.
12. The right-hand neighbour of the person who keeps the cat keeps the horse.
13. Exactly 4 houses lie to the left of the home of the person who drinks juice.

## Puzzle hard:zebra_hard-00093

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- pet: rabbit, cat, dog, horse, bird
- nationality: Brit, Norwegian, Swede, German, Spaniard
- hobby: painting, tennis, cooking, hiking, chess
- job: farmer, teacher, lawyer, pilot, doctor

Clues:
1. The right-hand neighbour of the Norwegian works as the lawyer.
2. Exactly 0 houses lie to the left of the home of the doctor.
3. Exactly 2 houses lie to the left of the home of the German.
4. The teacher has only one neighbour.
5. Exactly one house separates the owner of the dog from the Swede.
6. The cooking enthusiast and the Norwegian are one and the same person.
7. If the pilot does not enjoy hiking, then that person enjoys painting.
8. Exactly one house separates the doctor from the person who keeps the horse.
9. If the person who keeps the bird is not the Brit, then that person is the German.
10. The person who enjoys cooking lives in the fourth house from the right.
11. The painting enthusiast lives two doors away from the Spaniard.
12. The person who keeps the cat lives two doors away from the German.
13. The bird owner lives further to the right than the chess enthusiast.

## Puzzle hard:zebra_hard-00061

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- pet: fish, cat, bird, dog, horse
- hobby: tennis, golf, hiking, cooking, chess
- color: green, blue, red, yellow, white
- drink: water, coffee, juice, milk, tea

Clues:
1. Exactly 1 house lies to the left of the home of the person who drinks tea.
2. The person who enjoys golf lives somewhere between the person who drinks coffee and the horse owner.
3. The person in the blue house and the juice drinker are one and the same person.
4. One of the neighbours of the person who keeps the cat enjoys chess.
5. Whoever lives in the blue house and the person who enjoys cooking are one and the same person.
6. One of the neighbours of the person who enjoys cooking lives in the white house.
7. The person who enjoys hiking lives two doors away from the occupant of the red house.
8. One of the neighbours of the occupant of the white house drinks milk.
9. The left-hand neighbour of the chess enthusiast drinks water.
10. The owner of the cat and whoever lives in the red house are one and the same person.
11. Exactly one house separates the person who keeps the fish from the person in the green house.
12. One of the neighbours of the owner of the dog enjoys chess.

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

## Puzzle hard:zebra_hard-00078

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- color: white, green, red, purple, yellow
- pet: fish, dog, bird, horse, rabbit
- nationality: Norwegian, Dane, German, Brit, Swede
- job: teacher, farmer, baker, doctor, lawyer

Clues:
1. The right-hand neighbour of the person who keeps the dog is the German.
2. Exactly 1 house lies to the left of the home of the occupant of the red house.
3. Neither the person who keeps the rabbit nor the occupant of the white house works as the teacher.
4. One of the neighbours of the occupant of the yellow house keeps the bird.
5. The person who keeps the bird and whoever lives in the white house are one and the same person.
6. Exactly one house separates the doctor from the person in the white house.
7. If the Brit is not the doctor, then that person works as the lawyer.
8. The Swede lives further to the right than the fish owner.
9. One of the neighbours of the farmer keeps the fish.
10. The Dane lives somewhere between the German and whoever lives in the green house.
11. The baker and the person who keeps the rabbit are one and the same person.
12. The German and whoever lives in the red house are one and the same person.
13. One of the neighbours of the German keeps the rabbit.

## Puzzle paraphrase:zebra-00128

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- job: doctor, teacher, pilot, lawyer, farmer
- nationality: Spaniard, Norwegian, German, Dane, Brit
- color: blue, purple, white, yellow, red
- hobby: tennis, hiking, golf, cooking, painting

Clues:
1. The lawyer is the Norwegian.
2. The blue house is the second house.
3. The Dane enjoys either golf or painting.
4. The pilot lives in the leftmost house.
5. The white house's occupant is the Dane.
6. The red house stands immediately to the right of the teacher.
7. The Spaniard enjoys golf.
8. The white house stands directly to the left of the teacher.
9. The teacher and the tennis enthusiast live two houses apart.
10. The blue house's occupant is either the Dane or the German.
11. The occupant of the red house enjoys hiking.
12. The doctor and the German live two houses apart.
13. The occupant of the purple house enjoys either golf or painting.

## Puzzle paraphrase:zebra-00160

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- pet: bird, dog, cat, rabbit, horse
- job: lawyer, teacher, baker, doctor, farmer
- hobby: chess, cooking, tennis, golf, painting
- drink: juice, water, coffee, cocoa, milk

Clues:
1. Whoever plays tennis for fun is the juice drinker.
2. The cat's owner and the painting enthusiast occupy neighbouring houses.
3. The golfer never drinks milk.
4. The lawyer's home is the one in the centre of the row.
5. The chess player lives directly to the left of the painter.
6. The doctor is the one who keeps the bird.
7. Milk is what the dog owner drinks.
8. The farmer's home is not house number 2.
9. The golfer is also the baker.
10. The farmer lives next door to the water drinker.
11. House 1 belongs to the rabbit owner.
12. The cocoa drinker's hobby is either painting or tennis.
13. The water drinker lives immediately to the left of the coffee drinker.

## Puzzle plain:zebra-00059

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- color: purple, green, yellow, white, blue
- hobby: chess, hiking, tennis, cooking, painting
- nationality: German, Spaniard, Swede, Brit, Dane
- pet: dog, cat, rabbit, bird, fish

Clues:
1. The person who keeps the rabbit is the German.
2. The person who enjoys chess and the Swede are not neighbours.
3. Whoever lives in the blue house and the Swede live in adjacent houses.
4. The fish owner lives immediately to the right of the German.
5. The occupant of the purple house lives immediately to the right of the Spaniard.
6. The hiking enthusiast lives in the house just left of the one where whoever lives in the purple house lives.
7. The painting enthusiast lives in house 2.
8. The person who keeps the cat lives in the yellow house.
9. The person who keeps the dog and the hiking enthusiast are neighbours.
10. The cooking enthusiast lives in the house just left of the one where the Swede lives.
11. The chess enthusiast lives in the middle house.
12. The Brit lives in the green house.
