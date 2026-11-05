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

Output: write a single JSON object to the file D:\Puzzle-generation-with-guaranteed-uniqueness\data\llm_tasks\e1_encB\e1_encB_008.out.json with this exact structure
{"puzzles": [{"id": "<puzzle id>", "constraints": [{"clue": 1, "expr": "<expression>"}, ...]}, ...]}
One entry per puzzle and exactly one constraint per numbered clue, in order. Use single quotes inside
expressions so the JSON stays valid.

The puzzles follow.


## Puzzle plain:zebra-00062

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- nationality: Spaniard, Swede, German, Norwegian, Brit
- color: yellow, purple, white, green, red
- pet: dog, cat, horse, rabbit, fish
- drink: juice, water, tea, milk, coffee

Clues:
1. The German lives in the house just left of the one where the occupant of the red house lives.
2. The occupant of the purple house drinks tea.
3. The person who drinks coffee and the German live two houses apart.
4. The owner of the dog and whoever lives in the white house are neighbours.
5. The juice drinker lives directly to the left of the dog owner.
6. The coffee drinker keeps the dog.
7. The person who drinks water lives in the fourth house.
8. The rabbit owner lives in the first house.
9. The cat owner lives in the red house.
10. There is exactly one house between the Brit and the cat owner.
11. The owner of the cat is the Swede.
12. The occupant of the green house and the Norwegian live two houses apart.
13. The person in the purple house keeps the horse.
14. The person who drinks coffee and the Norwegian are different people.

## Puzzle paraphrase:zebra-00176

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- job: baker, farmer, teacher, doctor, lawyer
- nationality: Swede, Spaniard, Dane, Brit, German
- color: red, green, yellow, white, blue
- pet: bird, horse, rabbit, cat, dog

Clues:
1. The German lives somewhere to the right of the blue house.
2. The Swede lives in house 3.
3. The Dane lives in house 4.
4. The green house's occupant keeps the cat.
5. The bird owner is either the German or the Spaniard.
6. The Brit is the farmer.
7. The Brit lives immediately to the left of the teacher.
8. The Dane is the doctor.
9. The horse keeper lives in the yellow house.
10. The white house's occupant keeps the rabbit.
11. The dog owner is not next door to the yellow house.
12. The baker and the blue house are two houses apart.
13. The baker and the teacher are two houses apart.
14. The bird keeper lives right beside the green house.
15. The yellow house lies somewhere to the right of the baker.

## Puzzle hard:zebra_hard-00053

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- hobby: chess, cooking, painting, hiking, tennis
- job: lawyer, pilot, teacher, doctor, baker
- color: blue, purple, green, yellow, red
- pet: horse, bird, fish, rabbit, cat

Clues:
1. The chess enthusiast and the pilot are one and the same person.
2. The person who keeps the cat does not live to the right of the rabbit owner.
3. None of the neighbours of the doctor works as the teacher.
4. The right-hand neighbour of the doctor enjoys cooking.
5. The left-hand neighbour of the person who enjoys painting works as the teacher.
6. Whoever lives in the blue house lives two doors away from the person who keeps the horse.
7. The tennis enthusiast lives somewhere between the person who keeps the rabbit and whoever lives in the yellow house.
8. The person who enjoys chess and the occupant of the red house are one and the same person.
9. The owner of the bird and the person who enjoys hiking are one and the same person.
10. Exactly one house separates whoever lives in the purple house from whoever lives in the red house.
11. Whoever lives in the blue house is not the same person as the owner of the cat.
12. Exactly 1 house lies to the left of the home of the person in the blue house.
13. Whoever lives in the purple house lives two doors away from the teacher.
14. At least one house separates the lawyer from the person who enjoys chess.

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

## Puzzle paraphrase:zebra-00101

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- job: farmer, pilot, doctor, baker, teacher
- drink: water, tea, coffee, juice, milk
- hobby: golf, painting, chess, tennis, cooking
- color: red, white, purple, green, blue

Clues:
1. The teacher occupies the first house.
2. The baker and the water drinker live next door to each other.
3. The resident of the purple house drinks water.
4. The farmer's hobby is either cooking or painting.
5. The teacher's hobby is either chess or golf.
6. The painting enthusiast lives immediately to the left of the chess enthusiast.
7. The tennis enthusiast lives in the white house.
8. The pilot lives in the fourth house.
9. One house lies between the coffee drinker and the green house's occupant.
10. The milk drinker and the pilot do not live next to each other.
11. The baker lives in either the green house or the purple house.
12. One house lies between the doctor and the farmer.
13. The juice drinker and the red house's occupant live in adjacent houses.
14. The cooking enthusiast and the tennis enthusiast live next door to each other.

## Puzzle paraphrase:zebra-00129

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- drink: milk, cocoa, water, tea, coffee
- hobby: chess, painting, cooking, tennis, golf
- color: purple, blue, yellow, red, green
- job: lawyer, doctor, pilot, farmer, baker

Clues:
1. The doctor lives directly to the left of the red house.
2. The tea drinker lives right next door to the milk drinker, on the right.
3. The baker lives directly to the left of the yellow house.
4. One house separates the coffee drinker from the tennis player.
5. The coffee drinker does not live next to the golfer.
6. The green house is immediately to the left of the yellow house.
7. The yellow house's occupant is the lawyer.
8. The coffee drinker lives somewhere to the left of the blue house.
9. The golfer lives in either the purple house or the yellow house.
10. The pilot lives somewhere to the left of the farmer.
11. The cocoa drinker and the cooking enthusiast live in adjacent houses.
12. The coffee drinker lives directly to the right of the water drinker.
13. The blue house is at one end of the row.
14. The painter lives directly to the left of the milk drinker.

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

## Puzzle plain:zebra-00034

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- hobby: painting, chess, hiking, golf, cooking
- nationality: Swede, Brit, German, Spaniard, Dane
- job: lawyer, baker, pilot, teacher, farmer
- color: green, red, purple, yellow, blue

Clues:
1. The German lives in the house just left of the one where the golf enthusiast lives.
2. The farmer either enjoys golf or enjoys hiking.
3. Whoever lives in the blue house lives in the second house.
4. The Brit lives in the fourth house.
5. The baker lives in house 1.
6. The Dane works as the farmer.
7. The German lives in the house just left of the one where the Swede lives.
8. The person who enjoys chess and the person who enjoys hiking are neighbours.
9. There is exactly one house between the German and the occupant of the yellow house.
10. The pilot and the person in the red house live in adjacent houses.
11. The painting enthusiast either is the Brit or is the Spaniard.
12. The teacher lives in one of the two end houses.
13. The person in the green house lives directly to the left of the golf enthusiast.

## Puzzle plain:zebra-00053

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- pet: rabbit, cat, dog, fish, horse
- nationality: Dane, Norwegian, Spaniard, Brit, Swede
- hobby: painting, tennis, golf, hiking, chess
- drink: cocoa, tea, coffee, milk, juice

Clues:
1. The juice drinker enjoys painting.
2. The person who keeps the dog is the Spaniard.
3. The chess enthusiast is the Brit.
4. The person who enjoys hiking lives immediately to the right of the person who enjoys golf.
5. The person who drinks milk lives in the third house.
6. The person who drinks juice lives in house 1.
7. The Brit keeps the cat.
8. There is exactly one house between the person who enjoys chess and the Norwegian.
9. The horse owner drinks tea.
10. The chess enthusiast lives in the house just left of the one where the owner of the rabbit lives.
11. The Dane lives immediately to the right of the owner of the rabbit.
12. The person who drinks coffee either enjoys painting or enjoys tennis.
