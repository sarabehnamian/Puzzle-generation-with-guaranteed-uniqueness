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

Output: write a single JSON object to the file D:\Puzzle-generation-with-guaranteed-uniqueness\data\llm_tasks\e1_encC\e1_encC_016.out.json with this exact structure
{"puzzles": [{"id": "<puzzle id>", "constraints": [{"clue": 1, "expr": "<expression>"}, ...]}, ...]}
One entry per puzzle and exactly one constraint per numbered clue, in order. Use single quotes inside
expressions so the JSON stays valid.

The puzzles follow.


## Puzzle hard:zebra_hard-00058

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- job: teacher, doctor, pilot, lawyer, farmer
- pet: horse, cat, dog, fish, bird
- color: red, yellow, blue, white, green
- drink: tea, water, coffee, juice, milk

Clues:
1. The farmer lives somewhere between the fish owner and the tea drinker.
2. The lawyer and the occupant of the red house are one and the same person.
3. None of the neighbours of the person who keeps the bird keeps the horse.
4. The left-hand neighbour of the cat owner works as the pilot.
5. The right-hand neighbour of the teacher lives in the blue house.
6. The right-hand neighbour of whoever lives in the yellow house lives in the red house.
7. The dog owner lives two doors away from the farmer.
8. The water drinker lives somewhere between the lawyer and the person who drinks tea.
9. The person who keeps the bird lives further to the right than the farmer.
10. The occupant of the yellow house lives somewhere between the person in the red house and the person who drinks water.
11. The person who drinks juice lives two doors away from the lawyer.
12. The occupant of the green house lives two doors away from the occupant of the yellow house.
13. Exactly one house separates the person who keeps the cat from the coffee drinker.

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

## Puzzle plain:zebra-00016

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- job: pilot, lawyer, baker, doctor, farmer
- hobby: cooking, chess, hiking, painting, tennis
- drink: cocoa, milk, juice, water, coffee
- color: red, blue, yellow, purple, green

Clues:
1. The person who enjoys chess and the doctor are not neighbours.
2. The person in the blue house lives immediately to the right of the person who enjoys hiking.
3. There is exactly one house between the occupant of the blue house and the person in the yellow house.
4. The person who enjoys cooking lives in the house just left of the one where the doctor lives.
5. The pilot lives in the fifth house.
6. The person who drinks coffee works as the pilot.
7. Whoever lives in the red house either works as the doctor or works as the lawyer.
8. The occupant of the green house drinks water.
9. The person who drinks cocoa either works as the farmer or works as the pilot.
10. The person in the purple house lives immediately to the right of the baker.
11. The person who drinks milk enjoys painting.
12. Whoever lives in the red house lives in a lower-numbered house than the juice drinker.
13. There is exactly one house between the person in the green house and the pilot.

## Puzzle paraphrase:zebra-00152

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- drink: cocoa, tea, juice, water, milk
- job: farmer, teacher, lawyer, doctor, baker
- hobby: cooking, tennis, golf, chess, hiking
- pet: bird, cat, horse, dog, fish

Clues:
1. The cooking enthusiast lives immediately to the right of the fish keeper.
2. The juice drinker's hobby is golf.
3. The tea drinker's hobby is either chess or cooking.
4. The bird keeper lives next door to the milk drinker.
5. The milk drinker keeps either the bird or the dog.
6. The juice drinker lives in one of the two end houses.
7. Exactly one house separates the farmer from the juice drinker.
8. The lawyer lives in a lower-numbered house than the dog's owner.
9. The baker drinks water.
10. The hiking enthusiast is either the baker or the teacher.
11. The baker and the hiking enthusiast live two houses apart.
12. The cat's keeper is the farmer.
13. The chess player lives in a lower-numbered house than the golfer.
14. The dog owner and the tennis player live next to each other.

## Puzzle plain:zebra-00087

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- drink: water, milk, coffee, tea, cocoa
- hobby: cooking, tennis, hiking, chess, golf
- job: baker, pilot, lawyer, farmer, teacher
- pet: bird, cat, fish, horse, rabbit

Clues:
1. The person who drinks cocoa and the person who drinks water live in adjacent houses.
2. The chess enthusiast lives somewhere to the right of the tennis enthusiast.
3. The pilot keeps the rabbit.
4. The person who keeps the cat lives directly to the left of the owner of the fish.
5. The water drinker either keeps the fish or keeps the rabbit.
6. The cocoa drinker and the person who enjoys tennis are neighbours.
7. The rabbit owner enjoys chess.
8. The lawyer keeps the fish.
9. The coffee drinker either keeps the fish or keeps the horse.
10. The person who enjoys hiking does not keep the fish.
11. The baker and the person who drinks coffee are not neighbours.
12. The person who enjoys cooking lives in house 2.
13. The person who keeps the bird lives immediately to the right of the owner of the horse.
14. The farmer enjoys cooking.
15. The tennis enthusiast lives in a lower-numbered house than the milk drinker.
16. The tennis enthusiast drinks tea.

## Puzzle hard:zebra_hard-00034

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- job: lawyer, farmer, pilot, teacher, baker
- hobby: hiking, chess, golf, cooking, painting
- color: white, purple, blue, yellow, red
- pet: dog, fish, bird, cat, horse

Clues:
1. The baker lives two doors away from the person who enjoys painting.
2. At least one house separates the person who enjoys cooking from the farmer.
3. The person who enjoys golf and the pilot are one and the same person.
4. The right-hand neighbour of the person who keeps the fish keeps the horse.
5. One of the neighbours of the occupant of the blue house lives in the purple house.
6. One of the neighbours of the owner of the bird lives in the purple house.
7. The owner of the cat and the person in the red house are one and the same person.
8. The person who enjoys hiking has only one neighbour.
9. The horse owner is not the same person as the person in the purple house.
10. One of the neighbours of the person who enjoys hiking enjoys golf.
11. The right-hand neighbour of the cooking enthusiast lives in the white house.
12. One of the neighbours of the person who enjoys chess works as the lawyer.
13. The person who enjoys chess does not live in the third house from the right.
14. The right-hand neighbour of the occupant of the white house lives in the red house.
15. If the pilot does not live in the red house, then that person lives in the yellow house.

## Puzzle hard:zebra_hard-00032

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- hobby: painting, tennis, chess, hiking, cooking
- nationality: Spaniard, Norwegian, German, Swede, Brit
- job: farmer, pilot, doctor, teacher, lawyer
- pet: bird, dog, fish, horse, cat

Clues:
1. At least one house separates the doctor from the farmer.
2. The cooking enthusiast lives somewhere between the person who enjoys hiking and the Norwegian.
3. Exactly 3 houses lie to the left of the home of the pilot.
4. The German lives two doors away from the tennis enthusiast.
5. The Swede is not the same person as the teacher.
6. Neither the German nor the Norwegian enjoys hiking.
7. The person who keeps the dog and the lawyer are one and the same person.
8. One of the neighbours of the chess enthusiast works as the pilot.
9. One of the neighbours of the person who keeps the fish enjoys painting.
10. The dog owner has only one neighbour.
11. Exactly 0 houses lie to the left of the home of the farmer.
12. One of the neighbours of the bird owner is the Norwegian.
13. If the pilot is not the Spaniard, then that person is the Swede.
14. Exactly one house separates the owner of the cat from the pilot.
15. The right-hand neighbour of the Norwegian is the Spaniard.

## Puzzle paraphrase:zebra-00180

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- drink: tea, coffee, cocoa, water, milk
- pet: dog, bird, horse, fish, rabbit
- color: yellow, red, green, blue, white
- job: farmer, doctor, lawyer, baker, pilot

Clues:
1. Whoever drinks tea is the pilot.
2. The green house stands somewhere to the right of the doctor's house.
3. The dog's owner drinks water.
4. The horse owner lives right next door to the left of the rabbit owner.
5. The tea drinker is in house 4.
6. The cocoa drinker is not the one who keeps the rabbit.
7. The baker lives next to the white house.
8. The cocoa drinker and the lawyer live two houses apart.
9. The fish owner lives immediately to the left of the red house.
10. The bird is kept in house 2.
11. Exactly one house separates the white house from the yellow house.
12. The yellow house's occupant drinks coffee.
13. The dog owner does not live in house 5.
14. The farmer lives in house 5.

## Puzzle plain:zebra-00082

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- drink: coffee, milk, tea, juice, water
- hobby: hiking, tennis, painting, chess, cooking
- pet: bird, horse, dog, cat, fish
- nationality: Swede, Norwegian, Brit, Spaniard, Dane

Clues:
1. The chess enthusiast and the hiking enthusiast live two houses apart.
2. The cat owner lives immediately to the right of the person who enjoys chess.
3. The person who drinks milk lives next to the Spaniard.
4. The dog owner lives at one end of the row.
5. The cat owner either is the Norwegian or is the Swede.
6. The water drinker either enjoys cooking or enjoys painting.
7. The person who drinks coffee lives in house 1.
8. The coffee drinker keeps the horse.
9. The coffee drinker and the Swede live two houses apart.
10. The Brit does not live next to the Spaniard.
11. The person who enjoys painting lives directly to the left of the person who drinks juice.
12. The Spaniard keeps the fish.
13. The tea drinker lives in one of the two end houses.

## Puzzle plain:zebra-00083

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- hobby: tennis, chess, golf, painting, hiking
- job: lawyer, baker, teacher, farmer, doctor
- nationality: Dane, Spaniard, Brit, Norwegian, German
- color: purple, blue, yellow, red, white

Clues:
1. The German does not live next to the occupant of the red house.
2. The occupant of the blue house enjoys chess.
3. Whoever lives in the purple house is the Dane.
4. The farmer and the person who enjoys tennis are neighbours.
5. Whoever lives in the blue house does not live next to the person in the white house.
6. The Brit and the Norwegian are neighbours.
7. The person in the red house lives directly to the left of the lawyer.
8. The golf enthusiast either works as the doctor or works as the lawyer.
9. Whoever lives in the blue house lives at one end of the row.
10. The Brit lives in the fifth house.
11. The person who enjoys painting and the tennis enthusiast live two houses apart.
12. The baker does not live next to the lawyer.
13. The Dane either enjoys chess or enjoys hiking.
14. The Spaniard lives directly to the left of the tennis enthusiast.
15. The teacher lives in one of the two end houses.
