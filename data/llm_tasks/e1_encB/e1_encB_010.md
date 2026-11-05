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

Output: write a single JSON object to the file D:\Puzzle-generation-with-guaranteed-uniqueness\data\llm_tasks\e1_encB\e1_encB_010.out.json with this exact structure
{"puzzles": [{"id": "<puzzle id>", "constraints": [{"clue": 1, "expr": "<expression>"}, ...]}, ...]}
One entry per puzzle and exactly one constraint per numbered clue, in order. Use single quotes inside
expressions so the JSON stays valid.

The puzzles follow.


## Puzzle plain:zebra-00089

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- job: lawyer, baker, pilot, doctor, farmer
- color: red, blue, green, yellow, white
- drink: tea, cocoa, water, milk, juice
- nationality: Swede, Dane, Brit, Spaniard, German

Clues:
1. Whoever lives in the yellow house either drinks cocoa or drinks tea.
2. The German lives directly to the left of the person in the green house.
3. The farmer and the Spaniard are not neighbours.
4. The baker lives immediately to the right of the pilot.
5. The person who drinks juice lives next to the lawyer.
6. The doctor lives in the blue house.
7. The baker lives in the second house.
8. The person who drinks cocoa lives directly to the left of the person who drinks juice.
9. The German drinks tea.
10. The farmer and the person in the red house are not neighbours.
11. The Dane lives in house 2.
12. The German lives in the house just left of the one where the Brit lives.
13. The German and the person who drinks milk live two houses apart.
14. The occupant of the white house lives in house 1.

## Puzzle paraphrase:zebra-00195

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- color: blue, green, red, white, purple
- drink: tea, coffee, milk, water, juice
- nationality: Brit, German, Swede, Spaniard, Dane
- pet: fish, horse, cat, dog, rabbit

Clues:
1. The Dane is the one who owns the fish.
2. The tea drinker and the water drinker live next door to each other.
3. The purple house's occupant keeps the horse.
4. The Swede lives in a lower-numbered house than the horse owner.
5. The German drinks either milk or tea.
6. The red house is house 4.
7. The Brit lives right beside the dog owner.
8. The dog owner lives in the white house.
9. The blue house is the first house.
10. The milk drinker and the rabbit owner have exactly one house between them.
11. The Brit lives in the middle house.
12. The coffee drinker lives immediately to the right of the purple house.
13. The cat owner lives in the first house.
14. The water drinker lives in one of the two end houses.

## Puzzle paraphrase:zebra-00145

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- hobby: golf, chess, painting, hiking, tennis
- job: doctor, baker, farmer, pilot, teacher
- pet: rabbit, fish, bird, dog, cat
- drink: milk, water, coffee, juice, tea

Clues:
1. The farmer's drink is water.
2. The doctor lives next door to the tea drinker.
3. The juice drinker and the milk drinker are neighbours.
4. The chess enthusiast lives immediately left of the dog owner.
5. The juice drinker lives directly right of the golf enthusiast.
6. The rabbit is kept in house 1.
7. The doctor lives in the fourth house.
8. The fish keeper's hobby is hiking.
9. The pilot lives immediately left of the hiking enthusiast.
10. The teacher lives directly right of the pilot.
11. The chess enthusiast lives directly left of the pilot.
12. The cat owner lives next to the golf enthusiast.
13. The tennis enthusiast is the pilot.

## Puzzle hard:zebra_hard-00040

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- pet: rabbit, cat, fish, horse, dog
- job: pilot, lawyer, baker, doctor, teacher
- nationality: Brit, Dane, German, Norwegian, Swede
- color: red, white, blue, yellow, purple

Clues:
1. The right-hand neighbour of the teacher keeps the rabbit.
2. The Dane lives two doors away from the Swede.
3. The baker lives somewhere between the Brit and the pilot.
4. The Norwegian and the teacher are one and the same person.
5. The right-hand neighbour of the Dane keeps the dog.
6. The German and the person in the purple house are one and the same person.
7. If the fish owner does not live in the purple house, then that person lives in the white house.
8. Exactly one house separates the Brit from the Norwegian.
9. The right-hand neighbour of the Swede lives in the red house.
10. The lawyer has only one neighbour.
11. The owner of the cat lives further to the right than whoever lives in the white house.
12. The teacher and the person in the white house are one and the same person.
13. One of the neighbours of whoever lives in the red house works as the doctor.
14. The left-hand neighbour of the person in the blue house lives in the white house.

## Puzzle hard:zebra_hard-00045

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- color: yellow, red, blue, purple, green
- pet: rabbit, dog, horse, bird, fish
- hobby: painting, cooking, golf, chess, hiking
- job: baker, doctor, farmer, pilot, teacher

Clues:
1. The right-hand neighbour of the farmer lives in the blue house.
2. The farmer lives two doors away from the person who enjoys golf.
3. Exactly 3 houses lie to the left of the home of the person who enjoys cooking.
4. The person who keeps the bird and the person who enjoys hiking are one and the same person.
5. The occupant of the green house lives two doors away from the owner of the horse.
6. One of the neighbours of the baker enjoys chess.
7. One of the neighbours of the hiking enthusiast works as the doctor.
8. The farmer does not live in the third house from the right.
9. Exactly 2 houses lie to the left of the home of the person in the purple house.
10. The owner of the dog does not live in the rightmost house.
11. The left-hand neighbour of the person who enjoys painting works as the pilot.
12. The occupant of the yellow house does not live to the right of the occupant of the green house.
13. If the owner of the dog does not live in the green house, then that person lives in the red house.
14. The right-hand neighbour of the person who keeps the fish lives in the purple house.

## Puzzle plain:zebra-00027

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- hobby: hiking, painting, chess, tennis, cooking
- nationality: Dane, German, Spaniard, Norwegian, Brit
- color: green, purple, white, yellow, red
- drink: tea, milk, water, cocoa, coffee

Clues:
1. The coffee drinker and the person in the red house are neighbours.
2. The chess enthusiast lives somewhere to the right of whoever lives in the white house.
3. The occupant of the red house lives in the house just left of the one where the cocoa drinker lives.
4. The person who drinks water lives immediately to the right of the person who enjoys hiking.
5. The person in the purple house lives in the fourth house.
6. The person who enjoys painting is the Spaniard.
7. The Dane lives in the leftmost house.
8. Whoever lives in the purple house and the tea drinker are not neighbours.
9. The Brit lives in the house just left of the one where the Spaniard lives.
10. The person who enjoys tennis lives in the house just left of the one where the occupant of the purple house lives.
11. The person who enjoys hiking lives in the house just left of the one where the Norwegian lives.
12. The tennis enthusiast lives next to the occupant of the yellow house.

## Puzzle hard:zebra_hard-00048

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- color: yellow, blue, white, purple, red
- hobby: golf, tennis, chess, painting, hiking
- drink: cocoa, coffee, juice, tea, water
- nationality: German, Swede, Spaniard, Dane, Norwegian

Clues:
1. The left-hand neighbour of the tea drinker enjoys hiking.
2. The person who enjoys golf and the occupant of the white house are one and the same person.
3. One of the neighbours of the Spaniard is the Swede.
4. Exactly one house separates the person who drinks water from whoever lives in the white house.
5. The German lives two doors away from the Spaniard.
6. The person who enjoys hiking lives two doors away from whoever lives in the purple house.
7. The person who enjoys chess lives somewhere between the German and the person in the white house.
8. The right-hand neighbour of the Dane lives in the blue house.
9. The person who enjoys chess and the coffee drinker are one and the same person.
10. The tennis enthusiast and the water drinker are one and the same person.
11. The Swede and whoever lives in the yellow house are one and the same person.
12. The person in the blue house and the person who drinks juice are one and the same person.

## Puzzle hard:zebra_hard-00067

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- drink: cocoa, water, milk, tea, coffee
- nationality: Norwegian, Swede, Brit, Spaniard, Dane
- job: pilot, farmer, doctor, teacher, baker
- hobby: golf, painting, chess, cooking, tennis

Clues:
1. The golf enthusiast and the Norwegian are one and the same person.
2. The Brit and the person who drinks cocoa are one and the same person.
3. The person who enjoys painting is not the same person as the teacher.
4. The chess enthusiast lives further to the right than the farmer.
5. At least one house separates the painting enthusiast from the baker.
6. The milk drinker and the Norwegian are one and the same person.
7. The person who enjoys cooking is not the same person as the teacher.
8. The right-hand neighbour of the teacher enjoys chess.
9. The tennis enthusiast lives further to the right than the milk drinker.
10. The pilot and the Swede are one and the same person.
11. The Swede does not live to the right of the Dane.
12. Exactly one house separates the coffee drinker from the tea drinker.
13. If the person who enjoys tennis does not drink milk, then that person drinks tea.
14. The Norwegian lives somewhere between the Spaniard and the person who drinks tea.
15. Exactly 3 houses lie to the left of the home of the doctor.

## Puzzle plain:zebra-00030

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- nationality: Norwegian, Dane, Brit, Spaniard, Swede
- color: red, yellow, purple, green, white
- pet: bird, cat, dog, rabbit, fish
- drink: juice, water, tea, milk, coffee

Clues:
1. The water drinker lives directly to the left of the person in the green house.
2. The Norwegian drinks tea.
3. The rabbit owner drinks coffee.
4. The Spaniard and the occupant of the yellow house are neighbours.
5. The tea drinker lives directly to the left of the juice drinker.
6. The Swede and the occupant of the white house live in adjacent houses.
7. The occupant of the green house lives directly to the left of the Brit.
8. The Norwegian does not live next to the rabbit owner.
9. The owner of the cat and whoever lives in the white house live two houses apart.
10. The Norwegian keeps the dog.
11. The Dane keeps the fish.
12. The person who drinks juice lives immediately to the right of the person in the white house.
13. The occupant of the red house drinks water.

## Puzzle plain:zebra-00015

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- pet: horse, cat, fish, rabbit, dog
- job: teacher, farmer, pilot, lawyer, baker
- color: purple, green, blue, white, yellow
- nationality: Dane, Brit, Norwegian, Spaniard, German

Clues:
1. The occupant of the white house is the Spaniard.
2. Whoever lives in the blue house and the German live in adjacent houses.
3. The person who keeps the rabbit either lives in the purple house or lives in the white house.
4. The person who keeps the fish and whoever lives in the green house live in adjacent houses.
5. The person who keeps the fish lives somewhere to the right of the Norwegian.
6. The teacher lives somewhere to the left of the person who keeps the horse.
7. The farmer lives next to the Norwegian.
8. The occupant of the white house lives in the house just left of the one where the Dane lives.
9. The person who keeps the horse lives in the house just left of the one where the occupant of the yellow house lives.
10. There is exactly one house between the occupant of the blue house and the Spaniard.
11. The owner of the horse either works as the lawyer or works as the pilot.
12. The farmer keeps the cat.
13. The person in the blue house and the pilot live in adjacent houses.
14. The baker and the Brit live two houses apart.
