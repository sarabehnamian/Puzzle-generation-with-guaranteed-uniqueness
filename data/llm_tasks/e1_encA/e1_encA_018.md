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

Output: write a single JSON object to the file D:\Puzzle-generation-with-guaranteed-uniqueness\data\llm_tasks\e1_encA\e1_encA_018.out.json with this exact structure
{"puzzles": [{"id": "<puzzle id>", "constraints": [{"clue": 1, "expr": "<expression>"}, ...]}, ...]}
One entry per puzzle and exactly one constraint per numbered clue, in order. Use single quotes inside
expressions so the JSON stays valid.

The puzzles follow.


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

## Puzzle plain:zebra-00006

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- pet: horse, dog, cat, rabbit, fish
- color: purple, green, yellow, blue, white
- drink: coffee, milk, water, juice, tea
- hobby: chess, hiking, tennis, painting, cooking

Clues:
1. The juice drinker lives in the purple house.
2. There is exactly one house between the fish owner and the person in the green house.
3. The rabbit owner lives in the white house.
4. The person who drinks coffee lives in the blue house.
5. The person who enjoys tennis lives directly to the left of the person who drinks milk.
6. The person who enjoys painting lives in the house just left of the one where the person who enjoys hiking lives.
7. The person who keeps the horse and the person in the white house live two houses apart.
8. Whoever lives in the white house drinks milk.
9. The person in the blue house and whoever lives in the purple house live two houses apart.
10. The painting enthusiast lives next to the tea drinker.
11. The person who enjoys hiking lives somewhere to the right of the person in the white house.
12. The person who drinks juice keeps the cat.
13. The painting enthusiast lives somewhere to the left of the person who keeps the dog.
14. The person who enjoys cooking and the hiking enthusiast are neighbours.

## Puzzle hard:zebra_hard-00068

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- pet: bird, fish, cat, horse, dog
- color: red, blue, yellow, purple, white
- nationality: Dane, Norwegian, Brit, Swede, Spaniard
- drink: coffee, cocoa, juice, tea, water

Clues:
1. One of the neighbours of the Norwegian is the Dane.
2. Exactly 2 houses lie to the left of the home of the owner of the dog.
3. The juice drinker and the occupant of the yellow house are one and the same person.
4. One of the neighbours of the person who keeps the horse drinks coffee.
5. Neither the person who drinks cocoa nor the coffee drinker keeps the bird.
6. The occupant of the blue house has only one neighbour.
7. Exactly 3 houses lie to the left of the home of the Brit.
8. The Norwegian has only one neighbour.
9. The fish owner lives somewhere between the owner of the horse and the Swede.
10. Exactly 0 houses lie to the left of the home of the occupant of the purple house.
11. The left-hand neighbour of the fish owner drinks cocoa.
12. The left-hand neighbour of the owner of the dog lives in the yellow house.
13. The right-hand neighbour of the occupant of the red house is the Swede.
14. Exactly 4 houses lie to the left of the home of the tea drinker.

## Puzzle hard:zebra_hard-00099

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- job: doctor, lawyer, teacher, pilot, farmer
- drink: water, milk, tea, cocoa, juice
- pet: rabbit, cat, horse, dog, fish
- nationality: German, Dane, Norwegian, Spaniard, Swede

Clues:
1. One of the neighbours of the rabbit owner is the Spaniard.
2. One of the neighbours of the Dane is the Spaniard.
3. Exactly 0 houses lie to the left of the home of the dog owner.
4. Exactly one house separates the person who keeps the cat from the person who keeps the rabbit.
5. The doctor lives two doors away from the person who drinks milk.
6. The right-hand neighbour of the cocoa drinker is the German.
7. The person who drinks cocoa lives in the second house from the right.
8. One of the neighbours of the Swede works as the teacher.
9. The farmer lives two doors away from the person who drinks tea.
10. The fish owner and the lawyer are one and the same person.
11. Exactly one house separates the Norwegian from the water drinker.
12. At least one house separates the Norwegian from the Swede.
13. The German and the person who drinks tea are one and the same person.
14. One of the neighbours of the pilot works as the teacher.

## Puzzle hard:zebra_hard-00039

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- pet: bird, rabbit, cat, dog, fish
- nationality: Brit, German, Dane, Norwegian, Swede
- color: green, red, blue, purple, yellow
- drink: water, cocoa, coffee, tea, milk

Clues:
1. The right-hand neighbour of the fish owner keeps the cat.
2. The water drinker lives in the rightmost house.
3. The left-hand neighbour of the fish owner lives in the yellow house.
4. The person who drinks coffee lives somewhere between the occupant of the purple house and the Swede.
5. The person who keeps the rabbit is not the same person as whoever lives in the red house.
6. The dog owner lives two doors away from the milk drinker.
7. The occupant of the purple house and the tea drinker are one and the same person.
8. The left-hand neighbour of the person in the red house is the German.
9. One of the neighbours of the person who keeps the bird is the Brit.
10. The person who keeps the rabbit lives in the rightmost house.
11. The left-hand neighbour of the person in the green house lives in the yellow house.
12. The Dane lives two doors away from the rabbit owner.

## Puzzle plain:zebra-00049

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- pet: bird, horse, cat, dog, fish
- hobby: hiking, golf, chess, painting, tennis
- job: farmer, baker, lawyer, doctor, teacher
- nationality: Swede, Brit, German, Norwegian, Spaniard

Clues:
1. The owner of the cat lives in a lower-numbered house than the Norwegian.
2. The cat owner lives in the house just left of the one where the person who keeps the horse lives.
3. The person who enjoys painting lives in the house just left of the one where the golf enthusiast lives.
4. The person who keeps the dog lives somewhere to the right of the owner of the cat.
5. The baker and the hiking enthusiast are not neighbours.
6. The owner of the bird works as the doctor.
7. The owner of the cat either is the German or is the Swede.
8. The Brit and the doctor live in adjacent houses.
9. The person who keeps the cat and the teacher are neighbours.
10. The owner of the cat enjoys chess.
11. The person who enjoys painting works as the farmer.
12. The owner of the horse is the German.
13. The baker and the bird owner live two houses apart.
14. The lawyer and the Norwegian are neighbours.

## Puzzle hard:zebra_hard-00036

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- drink: coffee, juice, cocoa, tea, water
- job: teacher, lawyer, pilot, farmer, baker
- color: purple, blue, green, red, white
- pet: dog, fish, bird, cat, rabbit

Clues:
1. The baker lives somewhere between the person who keeps the cat and the lawyer.
2. Neither the fish owner nor the person who drinks water lives in the green house.
3. The person who keeps the dog lives in the second house from the right.
4. The teacher and the water drinker are one and the same person.
5. Exactly one house separates the person who drinks juice from whoever lives in the red house.
6. If the person in the white house does not keep the bird, then that person keeps the rabbit.
7. The bird owner lives two doors away from the farmer.
8. The bird owner and the teacher are one and the same person.
9. Exactly one house separates the person who keeps the cat from whoever lives in the red house.
10. Exactly one house separates the coffee drinker from the person in the white house.
11. The owner of the fish and the person who drinks juice are one and the same person.
12. Whoever lives in the purple house lives two doors away from the teacher.
13. The person who keeps the bird lives in the fourth house from the right.
14. The person who drinks tea lives further to the right than whoever lives in the red house.

## Puzzle hard:zebra_hard-00088

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- hobby: chess, hiking, painting, cooking, golf
- nationality: Spaniard, Brit, German, Swede, Dane
- color: blue, red, white, yellow, green
- pet: fish, bird, horse, cat, rabbit

Clues:
1. If the occupant of the white house does not keep the cat, then that person keeps the horse.
2. The owner of the horse and whoever lives in the yellow house are one and the same person.
3. Exactly 4 houses lie to the left of the home of the owner of the cat.
4. The right-hand neighbour of the person who keeps the fish is the Swede.
5. The Brit lives somewhere between the person in the red house and the occupant of the yellow house.
6. The hiking enthusiast and the person in the white house are one and the same person.
7. The Spaniard lives in the fifth house from the right.
8. One of the neighbours of the person in the green house keeps the cat.
9. The right-hand neighbour of the person who keeps the bird enjoys chess.
10. The left-hand neighbour of whoever lives in the yellow house enjoys painting.
11. The German and the person who enjoys golf are one and the same person.

## Puzzle paraphrase:zebra-00121

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- color: white, red, blue, yellow, purple
- hobby: cooking, golf, chess, tennis, hiking
- pet: fish, bird, horse, cat, dog
- nationality: Spaniard, Dane, Brit, Swede, German

Clues:
1. The dog owner and the fish keeper live next door to each other.
2. The hiking fan and the Swede are neighbours.
3. The Brit and the golfer live two houses apart.
4. The horse is kept in house 5.
5. The Dane is a neighbour of the person in the yellow house.
6. The Swede lives next to the white house.
7. The fish keeper and the golf enthusiast are neighbours.
8. The golf lover lives in the purple house.
9. The chess player is either the German or the Swede.
10. The German lives directly to the right of the yellow house.
11. The bird lives in the blue house.
12. The Spaniard's hobby is cooking.
13. The cooking enthusiast lives in the white house.

## Puzzle paraphrase:zebra-00199

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- job: lawyer, pilot, baker, farmer, doctor
- drink: milk, tea, coffee, juice, cocoa
- hobby: chess, painting, tennis, cooking, hiking
- nationality: Brit, Dane, German, Norwegian, Spaniard

Clues:
1. The doctor does not drink milk.
2. The baker lives immediately to the right of the pilot.
3. The chess enthusiast lives directly to the left of the Brit.
4. The farmer lives just left of the pilot.
5. The painting enthusiast lives immediately to the right of the Brit.
6. The Dane drinks tea.
7. The tea drinker lives next door to the tennis enthusiast.
8. The chess enthusiast drinks coffee.
9. The Brit and the farmer have exactly one house between them.
10. The Norwegian lives immediately to the right of the cooking enthusiast.
11. The juice drinker lives next door to the Norwegian.
12. The Spaniard is the lawyer.
13. The farmer lives immediately to the right of the doctor.
