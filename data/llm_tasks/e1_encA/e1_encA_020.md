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

Output: write a single JSON object to the file /home/user/Puzzle-generation-with-guaranteed-uniqueness/data/llm_tasks/e1_encA/e1_encA_020.out.json with this exact structure
{"puzzles": [{"id": "<puzzle id>", "constraints": [{"clue": 1, "expr": "<expression>"}, ...]}, ...]}
One entry per puzzle and exactly one constraint per numbered clue, in order. Use single quotes inside
expressions so the JSON stays valid.

The puzzles follow.


## Puzzle plain:zebra-00044

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- nationality: Brit, Dane, Spaniard, Swede, Norwegian
- pet: cat, bird, dog, fish, horse
- drink: milk, cocoa, water, coffee, tea
- color: green, purple, blue, white, yellow

Clues:
1. The person who drinks coffee lives in the third house.
2. The Spaniard either keeps the fish or keeps the horse.
3. The person who keeps the dog and the person who drinks water live in adjacent houses.
4. The person who keeps the dog and the Swede are neighbours.
5. The occupant of the purple house either keeps the fish or keeps the horse.
6. The person in the white house keeps the horse.
7. There is exactly one house between the cocoa drinker and the Dane.
8. The person who keeps the fish lives in the house just left of the one where the cat owner lives.
9. The person who drinks tea lives in the second house.
10. The person in the yellow house lives immediately to the right of the person who keeps the bird.
11. The owner of the cat lives in house 5.
12. The Brit lives in the third house.
13. The owner of the fish lives directly to the left of the person in the green house.

## Puzzle plain:zebra-00004

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- nationality: Spaniard, Brit, German, Swede, Norwegian
- color: purple, green, yellow, blue, white
- pet: rabbit, horse, bird, fish, dog
- job: baker, doctor, teacher, farmer, lawyer

Clues:
1. The farmer is the Brit.
2. The person in the purple house lives directly to the left of the owner of the rabbit.
3. The German lives in the house just left of the one where the dog owner lives.
4. Whoever lives in the yellow house either keeps the fish or keeps the horse.
5. Whoever lives in the green house lives in the fourth house.
6. The person in the blue house and the person who keeps the dog live two houses apart.
7. The baker does not live next to the German.
8. The person who keeps the dog works as the farmer.
9. The fish owner lives in the leftmost house.
10. The Norwegian and the Spaniard are neighbours.
11. The Norwegian does not live next to the person in the yellow house.
12. Whoever lives in the purple house works as the lawyer.
13. The teacher lives in the yellow house.
14. The horse owner lives directly to the left of the person in the green house.

## Puzzle paraphrase:zebra-00173

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- job: doctor, farmer, baker, lawyer, teacher
- pet: rabbit, bird, fish, cat, horse
- drink: cocoa, coffee, tea, water, milk
- nationality: Swede, Spaniard, Norwegian, German, Brit

Clues:
1. The Swede does not occupy house 5.
2. The coffee drinker lives immediately to the right of the German.
3. The doctor and the tea drinker are two houses apart.
4. The farmer and the Spaniard are not the same person.
5. The horse belongs to the Spaniard.
6. The Brit is the doctor.
7. The Norwegian lives immediately to the right of the teacher.
8. The cocoa drinker is the lawyer.
9. The cat owner does not live next door to the fish owner.
10. The water drinker lives immediately to the right of the Norwegian.
11. The bird owner and the cat owner have exactly one house between them.
12. The Norwegian owns the rabbit.
13. The tea drinker lives in house 5.

## Puzzle paraphrase:zebra-00101

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- job: farmer, pilot, doctor, baker, teacher
- drink: water, tea, coffee, juice, milk
- hobby: golf, painting, chess, tennis, cooking
- color: red, white, purple, green, blue

Clues:
1. House 1 is where the teacher lives.
2. The baker lives next door to the water drinker.
3. The resident of the purple house drinks water.
4. The farmer's hobby is either cooking or painting.
5. The teacher's hobby is either chess or golf.
6. The painting enthusiast lives immediately to the left of the chess enthusiast.
7. The tennis enthusiast lives in the white house.
8. The pilot occupies house 4.
9. Exactly one house lies between the coffee drinker and the person in the green house.
10. The milk drinker does not live next door to the pilot.
11. The baker lives in either the green house or the purple house.
12. The doctor and the farmer have exactly one house between them.
13. The juice drinker and the occupant of the red house live in neighbouring houses.
14. The cooking enthusiast lives next door to the tennis enthusiast.

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

## Puzzle plain:zebra-00039

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- drink: cocoa, juice, water, coffee, tea
- nationality: German, Spaniard, Brit, Norwegian, Dane
- job: lawyer, baker, pilot, teacher, doctor
- color: yellow, red, blue, white, green

Clues:
1. The juice drinker either is the German or is the Spaniard.
2. The cocoa drinker is the Brit.
3. The occupant of the red house lives at one end of the row.
4. The occupant of the white house lives in the house just left of the one where the doctor lives.
5. The teacher and the person who drinks water are neighbours.
6. The Norwegian drinks tea.
7. The Brit and whoever lives in the red house live two houses apart.
8. The lawyer lives in the white house.
9. The person in the red house is not the baker.
10. There is exactly one house between the Brit and the Dane.
11. The Spaniard lives in the blue house.
12. The teacher drinks juice.
13. The Dane lives in a lower-numbered house than the Norwegian.
14. The person in the green house and the person who drinks juice are not neighbours.
15. The German either lives in the blue house or lives in the white house.

## Puzzle hard:zebra_hard-00010

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- nationality: Dane, Brit, German, Swede, Spaniard
- hobby: golf, painting, cooking, tennis, chess
- drink: juice, water, coffee, tea, cocoa
- job: doctor, baker, farmer, teacher, lawyer

Clues:
1. The baker lives somewhere between the doctor and the German.
2. At least one house separates the farmer from the teacher.
3. The person who enjoys painting and the teacher are one and the same person.
4. The baker and the person who enjoys tennis are one and the same person.
5. The left-hand neighbour of the Swede is the Spaniard.
6. The person who enjoys cooking lives further to the right than the farmer.
7. One of the neighbours of the water drinker drinks coffee.
8. The person who enjoys cooking and the lawyer are one and the same person.
9. The coffee drinker and the golf enthusiast are one and the same person.
10. The teacher lives somewhere between the Brit and the person who enjoys chess.
11. The person who drinks cocoa and the Swede are one and the same person.
12. The water drinker lives somewhere between the farmer and the lawyer.
13. The baker and the juice drinker are one and the same person.

## Puzzle paraphrase:zebra-00183

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- hobby: tennis, cooking, painting, golf, chess
- color: green, blue, white, red, yellow
- job: farmer, pilot, baker, teacher, lawyer
- pet: dog, rabbit, bird, horse, cat

Clues:
1. The dog owner is not the pilot.
2. The red house's occupant has either the bird or the rabbit.
3. The rabbit belongs to the occupant of the blue house.
4. The golf enthusiast is not the teacher.
5. The cooking enthusiast and the pilot live in neighbouring houses.
6. The green house is home to the cat.
7. The golf enthusiast lives in either the red house or the white house.
8. The lawyer and the teacher have exactly one house between them.
9. The white house lies somewhere to the left of the horse owner.
10. The bird's owner lives somewhere to the right of the teacher.
11. The horse owner and the tennis enthusiast live two houses apart.
12. The yellow house is one of the two end houses.
13. The red house is immediately to the left of the painting enthusiast.
14. The farmer and the painting enthusiast are next-door neighbours.
15. One house separates the green house from the painting enthusiast.
16. The teacher lives somewhere to the left of the cat owner.
17. The cooking enthusiast lives in one of the two end houses.

## Puzzle paraphrase:zebra-00184

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- pet: horse, fish, dog, cat, bird
- color: purple, green, blue, white, red
- nationality: German, Dane, Norwegian, Spaniard, Brit
- drink: milk, water, coffee, cocoa, juice

Clues:
1. The Norwegian is the one who drinks water.
2. Cocoa is drunk at one end of the row.
3. The Dane lives immediately to the left of the Spaniard.
4. The fish is kept somewhere to the right of the horse.
5. The blue house is immediately to the left of the coffee drinker's house.
6. The Spaniard's house is immediately to the left of the milk drinker's house.
7. One house lies between the coffee drinker and the white house.
8. The bird's owner is either the Brit or the Dane.
9. The German drinks either coffee or juice.
10. Coffee is what the fish owner drinks.
11. The red house is house 5.
12. The cat owner and the purple house have exactly one house between them.
13. The green house and the Spaniard are two houses apart.

## Puzzle hard:zebra_hard-00005

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- job: teacher, doctor, lawyer, pilot, baker
- hobby: chess, golf, painting, tennis, hiking
- color: green, white, red, purple, blue
- pet: dog, rabbit, horse, bird, cat

Clues:
1. Exactly one house separates the owner of the bird from the person who enjoys chess.
2. The right-hand neighbour of the occupant of the blue house keeps the dog.
3. The lawyer and the occupant of the white house are one and the same person.
4. The occupant of the purple house and the teacher are one and the same person.
5. The pilot lives somewhere between the baker and the bird owner.
6. If the person who enjoys painting does not keep the cat, then that person keeps the dog.
7. If the painting enthusiast does not live in the blue house, then that person lives in the white house.
8. The left-hand neighbour of whoever lives in the red house enjoys golf.
9. Whoever lives in the white house lives further to the right than the teacher.
10. If the doctor does not enjoy golf, then that person enjoys tennis.
11. If the doctor does not keep the dog, then that person keeps the horse.
12. The lawyer does not live in the second house from the right.
13. The right-hand neighbour of the person who enjoys painting lives in the purple house.
