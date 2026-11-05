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

Output: write a single JSON object to the file D:\Puzzle-generation-with-guaranteed-uniqueness\data\llm_tasks\e1_encB\e1_encB_017.out.json with this exact structure
{"puzzles": [{"id": "<puzzle id>", "constraints": [{"clue": 1, "expr": "<expression>"}, ...]}, ...]}
One entry per puzzle and exactly one constraint per numbered clue, in order. Use single quotes inside
expressions so the JSON stays valid.

The puzzles follow.


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

## Puzzle hard:zebra_hard-00094

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- nationality: Spaniard, German, Dane, Brit, Norwegian
- drink: coffee, water, milk, tea, juice
- job: doctor, pilot, teacher, baker, lawyer
- hobby: hiking, tennis, chess, golf, cooking

Clues:
1. One of the neighbours of the German works as the lawyer.
2. Exactly one house separates the milk drinker from the teacher.
3. The baker lives two doors away from the pilot.
4. If the Dane does not enjoy golf, then that person enjoys tennis.
5. The Brit and the person who drinks juice are one and the same person.
6. The person who drinks milk and the Spaniard are one and the same person.
7. The person who enjoys chess lives further to the right than the German.
8. Exactly one house separates the coffee drinker from the golf enthusiast.
9. The milk drinker lives in the fifth house from the right.
10. Exactly 4 houses lie to the left of the home of the person who enjoys tennis.
11. The person who drinks juice lives further to the right than the pilot.
12. One of the neighbours of the water drinker enjoys golf.
13. The person who enjoys hiking lives in the third house from the right.

## Puzzle plain:zebra-00069

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- color: red, green, yellow, blue, white
- job: pilot, baker, doctor, teacher, farmer
- pet: fish, rabbit, bird, horse, dog
- hobby: hiking, tennis, cooking, chess, painting

Clues:
1. The doctor lives directly to the left of the hiking enthusiast.
2. The baker lives immediately to the right of the person who enjoys cooking.
3. The occupant of the blue house works as the baker.
4. The occupant of the yellow house lives in the second house.
5. The tennis enthusiast lives in the third house.
6. The chess enthusiast and the pilot live in adjacent houses.
7. The fish owner lives in a lower-numbered house than the chess enthusiast.
8. The dog owner and the owner of the rabbit are not neighbours.
9. The teacher lives in the white house.
10. The owner of the dog lives immediately to the right of the doctor.
11. The owner of the bird lives in the fourth house.
12. The fish owner either lives in the green house or lives in the yellow house.
13. There is exactly one house between the farmer and the pilot.

## Puzzle paraphrase:zebra-00113

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- job: lawyer, doctor, baker, farmer, teacher
- drink: tea, milk, juice, water, coffee
- nationality: Swede, German, Norwegian, Spaniard, Brit
- color: red, yellow, purple, white, blue

Clues:
1. The blue house's occupant and the teacher are not neighbours.
2. The doctor lives in the fifth house.
3. The coffee drinker lives directly to the left of the teacher.
4. The occupant of the blue house is either the farmer or the lawyer.
5. The juice drinker is not the Norwegian.
6. The occupant of the white house lives in house 1.
7. The Swede is not the doctor.
8. The blue house's occupant lives next door to the yellow house's occupant.
9. The juice drinker and the Spaniard live next to each other.
10. The Spaniard lives immediately to the left of the purple house's occupant.
11. The lawyer is either the Brit or the Spaniard.
12. There is exactly one house between the milk drinker and the Norwegian.
13. The baker lives in the white house.
14. The water drinker is the baker.

## Puzzle hard:zebra_hard-00029

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- hobby: golf, painting, chess, hiking, cooking
- color: purple, yellow, green, red, blue
- pet: dog, bird, fish, cat, horse
- nationality: Spaniard, Dane, Norwegian, Brit, German

Clues:
1. The cooking enthusiast and the owner of the dog are one and the same person.
2. One of the neighbours of the owner of the bird lives in the purple house.
3. If the person in the purple house does not keep the cat, then that person keeps the horse.
4. One of the neighbours of whoever lives in the yellow house keeps the bird.
5. The owner of the dog lives further to the right than the person who enjoys chess.
6. The painting enthusiast and the Spaniard are one and the same person.
7. Exactly one house separates the person who keeps the cat from the German.
8. If the occupant of the green house does not enjoy cooking, then that person enjoys golf.
9. Neither the hiking enthusiast nor the person in the purple house keeps the cat.
10. The hiking enthusiast lives in the second house from the right.
11. One of the neighbours of the person in the purple house lives in the blue house.
12. The person in the yellow house lives somewhere between the Dane and the owner of the fish.
13. One of the neighbours of the cat owner is the Spaniard.
14. At least one house separates the Norwegian from the person in the blue house.
15. The cat owner lives two doors away from the person who enjoys chess.

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

## Puzzle hard:zebra_hard-00052

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- color: blue, yellow, red, purple, white
- hobby: tennis, hiking, painting, golf, cooking
- nationality: Brit, Spaniard, Swede, Dane, German
- pet: cat, dog, rabbit, bird, horse

Clues:
1. Exactly one house separates the person who keeps the bird from the person who enjoys tennis.
2. The hiking enthusiast and the Spaniard are one and the same person.
3. The person who keeps the horse lives further to the right than the cooking enthusiast.
4. Whoever lives in the white house lives in the second house from the right.
5. If the person who enjoys tennis is not the Dane, then that person is the Spaniard.
6. Exactly 2 houses lie to the left of the home of the horse owner.
7. The right-hand neighbour of whoever lives in the red house keeps the cat.
8. The person who enjoys hiking and the person who keeps the rabbit are one and the same person.
9. If the German does not live in the purple house, then that person lives in the white house.
10. The occupant of the purple house lives somewhere between the person who enjoys painting and the occupant of the white house.
11. The cat owner and the person who enjoys painting are one and the same person.
12. If the Brit does not live in the blue house, then that person lives in the purple house.

## Puzzle paraphrase:zebra-00108

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- nationality: Norwegian, German, Spaniard, Dane, Swede
- hobby: hiking, chess, golf, painting, tennis
- job: farmer, teacher, pilot, doctor, lawyer
- pet: rabbit, horse, cat, bird, dog

Clues:
1. The rabbit owner lives in house 3.
2. One house lies between the golf enthusiast and the hiker.
3. The Spaniard lives immediately to the left of the dog owner.
4. The Swede lives in house 2.
5. One house separates the lawyer from the tennis enthusiast.
6. The Dane does not live next to the painting enthusiast.
7. The Dane and the teacher live in adjacent houses.
8. The golf enthusiast and the pilot live next door to each other.
9. The hiker is the lawyer.
10. The doctor lives in house 5.
11. The cat owner lives immediately to the left of the bird owner.
12. The Dane and the Norwegian are neighbours.
13. The horse owner lives in house 1.

## Puzzle hard:zebra_hard-00015

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- hobby: golf, painting, hiking, chess, tennis
- nationality: Spaniard, Norwegian, Dane, Swede, Brit
- color: red, yellow, green, white, purple
- drink: juice, tea, coffee, milk, cocoa

Clues:
1. One of the neighbours of the Swede enjoys painting.
2. If the person who enjoys chess does not drink coffee, then that person drinks tea.
3. The person in the white house lives somewhere between the occupant of the purple house and the Spaniard.
4. The left-hand neighbour of the hiking enthusiast lives in the purple house.
5. The Dane lives somewhere between the person who drinks juice and whoever lives in the white house.
6. One of the neighbours of the occupant of the green house drinks milk.
7. None of the neighbours of the occupant of the yellow house drinks milk.
8. None of the neighbours of the juice drinker drinks tea.
9. The Swede is not the same person as the occupant of the white house.
10. The Brit and the tennis enthusiast are one and the same person.
11. The right-hand neighbour of whoever lives in the yellow house enjoys tennis.
12. One of the neighbours of the cocoa drinker is the Swede.
13. The person in the yellow house lives somewhere between the milk drinker and whoever lives in the purple house.

## Puzzle plain:zebra-00065

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- job: teacher, baker, doctor, farmer, pilot
- pet: cat, bird, horse, fish, dog
- drink: juice, tea, water, milk, cocoa
- color: green, white, purple, blue, yellow

Clues:
1. There is exactly one house between the doctor and the person who drinks tea.
2. The owner of the cat lives directly to the left of the water drinker.
3. The baker lives in a lower-numbered house than the person who keeps the fish.
4. The dog owner lives in house 5.
5. The person who keeps the fish works as the farmer.
6. There is exactly one house between the owner of the dog and the occupant of the green house.
7. The owner of the fish and the person who drinks tea live in adjacent houses.
8. The baker lives next to the owner of the horse.
9. Whoever lives in the white house lives in the first house.
10. The pilot lives in the house just left of the one where the person in the purple house lives.
11. The person who keeps the cat lives in house 1.
12. The occupant of the yellow house is not the pilot.
13. The juice drinker lives directly to the left of the person in the blue house.
14. The person who keeps the cat lives next to the doctor.
15. The person who drinks cocoa lives somewhere to the left of the milk drinker.
