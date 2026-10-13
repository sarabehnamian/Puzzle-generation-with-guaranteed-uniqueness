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

Output: write a single JSON object to the file /home/user/Puzzle-generation-with-guaranteed-uniqueness/data/llm_tasks/e1_encA/e1_encA_028.out.json with this exact structure
{"puzzles": [{"id": "<puzzle id>", "constraints": [{"clue": 1, "expr": "<expression>"}, ...]}, ...]}
One entry per puzzle and exactly one constraint per numbered clue, in order. Use single quotes inside
expressions so the JSON stays valid.

The puzzles follow.


## Puzzle plain:zebra-00074

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- nationality: German, Swede, Dane, Brit, Norwegian
- color: purple, green, red, yellow, blue
- job: farmer, teacher, pilot, baker, lawyer
- pet: horse, rabbit, bird, fish, dog

Clues:
1. The pilot lives in the house just left of the one where the person who keeps the horse lives.
2. The owner of the dog and the Swede are not neighbours.
3. The Norwegian lives in one of the two end houses.
4. The farmer keeps the horse.
5. The Swede lives in house 5.
6. The person in the green house works as the baker.
7. Whoever lives in the yellow house keeps the bird.
8. The bird owner and the farmer are neighbours.
9. The Swede keeps the rabbit.
10. The Brit lives in the red house.
11. The pilot lives in the house just left of the one where the German lives.
12. The lawyer does not live next to the person who keeps the rabbit.
13. Whoever lives in the blue house lives in the house just left of the one where the German lives.

## Puzzle paraphrase:zebra-00148

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- hobby: tennis, golf, painting, cooking, chess
- pet: fish, bird, dog, rabbit, horse
- nationality: Spaniard, Dane, Norwegian, Brit, German
- drink: tea, milk, water, juice, coffee

Clues:
1. The bird keeper and the fish keeper do not live next to each other.
2. The chess enthusiast lives next door to the tea drinker.
3. The Spaniard's house has a lower number than the water drinker's.
4. The dog owner plays tennis.
5. The rabbit owner lives immediately left of the golf enthusiast.
6. The coffee drinker does not live in house 3.
7. The Brit and the Dane are not next-door neighbours.
8. The German and the rabbit owner live two houses apart.
9. The fish owner lives directly right of the rabbit keeper.
10. The coffee drinker keeps either the fish or the horse.
11. The Spaniard is the coffee drinker.
12. Painting is the Brit's hobby.
13. The water drinker is the chess enthusiast.
14. The milk drinker keeps either the dog or the rabbit.
15. The tea drinker lives somewhere to the right of the Brit.
16. The tennis enthusiast lives somewhere to the left of the fish owner.

## Puzzle paraphrase:zebra-00197

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- pet: fish, bird, horse, dog, cat
- drink: tea, cocoa, juice, milk, coffee
- nationality: Swede, German, Norwegian, Brit, Spaniard
- color: blue, red, purple, yellow, green

Clues:
1. The bird owner lives in the house immediately to the right of the milk drinker's.
2. Exactly one house lies between the horse owner and the milk drinker.
3. The cocoa drinker is either the German or the Spaniard.
4. The German is the horse owner.
5. The Brit lives next door to the yellow house's resident.
6. The cat owner lives immediately to the right of the fish owner.
7. The coffee drinker lives next door to the red house's resident.
8. The yellow house's occupant drinks juice.
9. The tea drinker lives in house 3.
10. The fish owner lives in the purple house.
11. The tea drinker is either the Brit or the German.
12. The cat owner lives in the green house.
13. The fish owner and the Swede are two houses apart.

## Puzzle paraphrase:zebra-00102

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- hobby: tennis, painting, chess, hiking, golf
- pet: cat, bird, dog, fish, rabbit
- job: doctor, farmer, teacher, lawyer, pilot
- nationality: Dane, German, Spaniard, Norwegian, Swede

Clues:
1. The Norwegian is the one who enjoys golf.
2. The fish keeper lives somewhere to the left of the pilot.
3. The cat owner and the German live two houses apart.
4. The bird owner lives in the last house.
5. The cat owner's hobby is either golf or hiking.
6. The rabbit owner lives immediately to the left of the doctor.
7. The farmer lives next door to the tennis enthusiast.
8. The Swede is the doctor.
9. The lawyer is the Dane.
10. The Spaniard's home is house 2.
11. The bird keeper and the chess enthusiast are neighbours.
12. The farmer is the German.
13. The Swede is the dog owner.

## Puzzle paraphrase:zebra-00112

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- hobby: painting, tennis, golf, hiking, chess
- pet: dog, bird, rabbit, cat, horse
- job: farmer, doctor, teacher, pilot, baker
- drink: coffee, milk, tea, juice, water

Clues:
1. House 4 belongs to the milk drinker.
2. The chess enthusiast is not in house 1.
3. The cat keeper lives somewhere to the right of the baker.
4. The milk drinker is the farmer.
5. The baker and the juice drinker live next door to each other.
6. The pilot is the one who keeps the cat.
7. The dog owner does not live next to the water drinker.
8. The water drinker lives immediately to the right of the golf enthusiast.
9. The painting enthusiast keeps the horse.
10. The coffee drinker lives right beside the painting enthusiast.
11. The horse is kept in the third house.
12. The bird owner lives directly to the left of the teacher.
13. The chess enthusiast and the water drinker have exactly one house between them.
14. The hiking enthusiast lives in a house numbered lower than the tennis enthusiast's.

## Puzzle hard:zebra_hard-00033

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- drink: water, cocoa, tea, juice, coffee
- color: blue, red, green, white, purple
- hobby: golf, cooking, painting, tennis, chess
- job: lawyer, pilot, teacher, doctor, farmer

Clues:
1. The golf enthusiast and the water drinker are one and the same person.
2. The person who enjoys painting lives two doors away from the pilot.
3. The person who enjoys chess and the occupant of the green house are one and the same person.
4. The person who enjoys tennis lives somewhere between the person who enjoys cooking and the teacher.
5. One of the neighbours of the cocoa drinker lives in the purple house.
6. The doctor lives two doors away from the tennis enthusiast.
7. At least one house separates the lawyer from the teacher.
8. The occupant of the blue house and the doctor are one and the same person.
9. The chess enthusiast and the lawyer are one and the same person.
10. The left-hand neighbour of the person who drinks cocoa enjoys tennis.
11. The doctor is not the same person as the person who enjoys golf.
12. Exactly 3 houses lie to the left of the home of the occupant of the red house.
13. The juice drinker and the person who enjoys tennis are one and the same person.
14. One of the neighbours of the person who drinks coffee enjoys golf.

## Puzzle hard:zebra_hard-00083

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- nationality: Spaniard, Swede, German, Dane, Brit
- color: purple, red, yellow, blue, green
- drink: coffee, water, cocoa, tea, milk
- job: teacher, lawyer, baker, doctor, pilot

Clues:
1. The milk drinker and the Swede are one and the same person.
2. If the doctor does not live in the green house, then that person lives in the red house.
3. The right-hand neighbour of the person who drinks water is the Brit.
4. The German lives somewhere between the Swede and the person in the yellow house.
5. The person who drinks cocoa and the person in the green house are one and the same person.
6. The right-hand neighbour of the cocoa drinker lives in the yellow house.
7. The right-hand neighbour of the baker works as the pilot.
8. The coffee drinker lives two doors away from the Spaniard.
9. One of the neighbours of the lawyer lives in the blue house.
10. Exactly 1 house lies to the left of the home of the occupant of the yellow house.
11. At least one house separates the Dane from the baker.
12. The pilot lives somewhere between the doctor and the person in the yellow house.
13. If the pilot is not the German, then that person is the Spaniard.

## Puzzle paraphrase:zebra-00185

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- job: baker, lawyer, pilot, doctor, farmer
- nationality: Norwegian, Brit, Swede, Spaniard, Dane
- hobby: chess, cooking, hiking, tennis, painting
- drink: tea, juice, water, milk, coffee

Clues:
1. The farmer and the milk drinker have one house between them.
2. Water is drunk in the second house.
3. The doctor's drink is coffee.
4. The Brit lives immediately to the right of the tea drinker.
5. The pilot's hobby is hiking.
6. The Spaniard lives in one of the two end houses.
7. The tennis enthusiast is either the baker or the pilot.
8. The baker lives immediately to the left of the Brit.
9. Painting is the Spaniard's hobby.
10. The Dane drinks either juice or tea.
11. The lawyer lives immediately to the left of the milk drinker.
12. The doctor's hobby is either cooking or hiking.
13. The cooking enthusiast lives next door to the Swede.

## Puzzle paraphrase:zebra-00134

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- nationality: Spaniard, Brit, Norwegian, Swede, Dane
- hobby: golf, chess, cooking, painting, tennis
- job: doctor, farmer, baker, lawyer, teacher
- pet: cat, rabbit, horse, bird, fish

Clues:
1. The painting enthusiast lives directly to the right of the golf enthusiast.
2. The cat owner and the teacher live in adjacent houses.
3. The rabbit belongs to the Brit.
4. The Dane is the farmer.
5. The baker and the cat owner are two houses apart.
6. The cooking enthusiast lives immediately to the left of the bird owner.
7. The baker lives directly to the right of the farmer.
8. The Spaniard lives directly to the right of the Dane.
9. The rabbit owner's hobby is tennis.
10. The Swede is the one with the horse.
11. The rabbit owner lives directly to the left of the lawyer.
12. The Swede is the cooking enthusiast.

## Puzzle paraphrase:zebra-00135

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- hobby: golf, cooking, painting, chess, tennis
- color: blue, red, green, white, yellow
- pet: cat, rabbit, dog, horse, bird
- job: lawyer, farmer, doctor, teacher, baker

Clues:
1. The yellow house is the fourth house.
2. The dog owner lives immediately to the left of the rabbit owner.
3. The baker's hobby is cooking.
4. The bird owner does not live in the first house.
5. The white house is immediately to the left of the green house.
6. The farmer is the one who keeps the dog.
7. The lawyer is the one who owns the bird.
8. The cat owner lives somewhere to the right of the baker.
9. Exactly one house lies between the blue house and the rabbit owner.
10. The occupant of the blue house is either the doctor or the farmer.
11. The green house lies somewhere to the left of the farmer.
12. The painting enthusiast lives in the fourth house.
13. The chess player lives in one of the two end houses.
14. The tennis enthusiast lives immediately to the left of the painting enthusiast.
