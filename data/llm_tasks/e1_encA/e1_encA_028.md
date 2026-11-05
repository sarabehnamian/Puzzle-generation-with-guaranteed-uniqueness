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

Output: write a single JSON object to the file D:\Puzzle-generation-with-guaranteed-uniqueness\data\llm_tasks\e1_encA\e1_encA_028.out.json with this exact structure
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
1. The bird owner and the fish owner are not neighbours.
2. The chess enthusiast and the tea drinker live next door to each other.
3. The Spaniard lives in a lower-numbered house than the water drinker.
4. The dog owner plays tennis.
5. The rabbit owner lives immediately left of the golf enthusiast.
6. The coffee drinker does not live in house 3.
7. The Brit and the Dane do not live next to each other.
8. Two houses separate the German from the rabbit owner.
9. The fish owner lives directly right of the rabbit owner.
10. The coffee drinker keeps either the fish or the horse.
11. The Spaniard is the coffee drinker.
12. Painting is the Brit's hobby.
13. The water drinker is the chess enthusiast.
14. The milk drinker keeps either the dog or the rabbit.
15. The tea drinker lives somewhere to the right of the Brit.
16. The tennis enthusiast lives somewhere left of the fish owner.

## Puzzle paraphrase:zebra-00197

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- pet: fish, bird, horse, dog, cat
- drink: tea, cocoa, juice, milk, coffee
- nationality: Swede, German, Norwegian, Brit, Spaniard
- color: blue, red, purple, yellow, green

Clues:
1. The milk drinker lives in the house immediately left of the bird keeper's.
2. The horse keeper and the milk drinker have exactly one house between them.
3. The cocoa drinker is either the German or the Spaniard.
4. The German is the horse owner.
5. The Brit lives next door to the yellow house's occupant.
6. The cat owner lives immediately to the right of the fish owner.
7. The coffee drinker lives next door to the red house's occupant.
8. The yellow house's occupant drinks juice.
9. The tea drinker lives in house 3.
10. The fish owner lives in the purple house.
11. The tea drinker is either the Brit or the German.
12. The cat owner lives in the green house.
13. The fish owner and the Swede live two houses apart.

## Puzzle paraphrase:zebra-00102

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- hobby: tennis, painting, chess, hiking, golf
- pet: cat, bird, dog, fish, rabbit
- job: doctor, farmer, teacher, lawyer, pilot
- nationality: Dane, German, Spaniard, Norwegian, Swede

Clues:
1. The golf enthusiast is the Norwegian.
2. The fish owner lives somewhere to the left of the pilot.
3. The cat owner and the German live two houses apart.
4. The bird owner lives in the last house.
5. The cat owner's hobby is either golf or hiking.
6. The rabbit owner lives immediately to the left of the doctor.
7. The farmer lives next door to the tennis enthusiast.
8. The Swede is the doctor.
9. The Dane is a lawyer by profession.
10. The Spaniard lives in house 2.
11. The bird owner and the chess enthusiast are neighbours.
12. The German is the farmer.
13. The Swede owns the dog.

## Puzzle paraphrase:zebra-00112

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- hobby: painting, tennis, golf, hiking, chess
- pet: dog, bird, rabbit, cat, horse
- job: farmer, doctor, teacher, pilot, baker
- drink: coffee, milk, tea, juice, water

Clues:
1. The milk drinker lives in house 4.
2. The chess enthusiast is not in house 1.
3. The cat keeper lives somewhere to the right of the baker.
4. The milk drinker is the farmer.
5. The baker and the juice drinker are neighbours.
6. The pilot is the one who keeps the cat.
7. The dog keeper does not live next to the water drinker.
8. The water drinker lives immediately to the right of the golf enthusiast.
9. The horse is kept by the painting enthusiast.
10. The coffee drinker lives next door to the painting enthusiast.
11. The horse owner lives in the third house.
12. The bird owner lives in the house immediately left of the teacher's.
13. The chess enthusiast and the water drinker live two houses apart.
14. The hiking enthusiast lives in a lower-numbered house than the tennis enthusiast.

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

## Puzzle paraphrase:zebra-00186

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- nationality: Dane, German, Brit, Swede, Spaniard
- pet: rabbit, bird, fish, dog, cat
- drink: juice, tea, milk, cocoa, coffee
- hobby: golf, painting, tennis, chess, cooking

Clues:
1. The German does not live beside the painter.
2. The chess player and the Spaniard live two houses apart.
3. The Spaniard has the dog.
4. The juice drinker is the painter.
5. The cooking enthusiast lives in one of the end houses.
6. One house lies between the fish owner and the juice drinker.
7. The dog's owner drinks cocoa.
8. The Swede drinks tea.
9. The juice drinker and the tennis player have exactly one house between them.
10. The bird is in house 2.
11. The German lives at one of the two ends of the row.
12. The milk drinker lives immediately to the left of the juice drinker.
13. The Dane and the tennis player live two houses apart.
14. The rabbit owner lives in a lower-numbered house than the Swede.
15. The chess enthusiast lives somewhere to the right of the Dane.

## Puzzle paraphrase:zebra-00134

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- nationality: Spaniard, Brit, Norwegian, Swede, Dane
- hobby: golf, chess, cooking, painting, tennis
- job: doctor, farmer, baker, lawyer, teacher
- pet: cat, rabbit, horse, bird, fish

Clues:
1. The painting enthusiast lives directly to the right of the golf enthusiast.
2. The cat owner and the teacher live in adjacent houses.
3. The Brit keeps the rabbit.
4. The Dane is the farmer.
5. The baker and the cat owner live two houses apart.
6. The cooking enthusiast lives immediately to the left of the bird owner.
7. The baker lives directly to the right of the farmer.
8. The Spaniard lives directly to the right of the Dane.
9. The rabbit owner's hobby is tennis.
10. The Swede keeps the horse.
11. The rabbit owner lives immediately to the left of the lawyer.
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
5. The white house is directly to the left of the green house.
6. The farmer keeps the dog.
7. The bird owner is the lawyer.
8. The cat owner lives somewhere to the right of the baker.
9. One house lies between the blue house and the rabbit owner.
10. The occupant of the blue house is either the doctor or the farmer.
11. The green house lies somewhere to the left of the farmer.
12. The painting enthusiast lives in the fourth house.
13. The chess enthusiast lives in one of the two end houses.
14. The tennis enthusiast lives directly to the left of the painting enthusiast.
