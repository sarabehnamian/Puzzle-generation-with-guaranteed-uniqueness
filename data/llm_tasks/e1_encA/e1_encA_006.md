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

Output: write a single JSON object to the file /home/user/Puzzle-generation-with-guaranteed-uniqueness/data/llm_tasks/e1_encA/e1_encA_006.out.json with this exact structure
{"puzzles": [{"id": "<puzzle id>", "constraints": [{"clue": 1, "expr": "<expression>"}, ...]}, ...]}
One entry per puzzle and exactly one constraint per numbered clue, in order. Use single quotes inside
expressions so the JSON stays valid.

The puzzles follow.


## Puzzle plain:zebra-00025

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- pet: cat, horse, dog, bird, rabbit
- color: red, yellow, white, purple, green
- job: teacher, baker, lawyer, farmer, doctor
- hobby: cooking, hiking, golf, painting, tennis

Clues:
1. The person who enjoys painting lives immediately to the right of the teacher.
2. The lawyer either keeps the bird or keeps the cat.
3. The owner of the rabbit lives in the green house.
4. The person who enjoys golf lives somewhere to the left of the farmer.
5. The farmer and the person in the yellow house are neighbours.
6. The horse owner enjoys cooking.
7. The painting enthusiast and the person in the purple house are neighbours.
8. The cooking enthusiast lives in the second house.
9. The doctor and the owner of the rabbit are neighbours.
10. The baker lives immediately to the right of the person who enjoys cooking.
11. The bird owner lives in the house just left of the one where the owner of the rabbit lives.
12. The bird owner lives in the white house.
13. The rabbit owner lives in the house just left of the one where the tennis enthusiast lives.

## Puzzle paraphrase:zebra-00130

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- hobby: chess, golf, hiking, painting, cooking
- drink: water, tea, milk, coffee, cocoa
- pet: rabbit, fish, dog, cat, bird
- job: teacher, pilot, farmer, doctor, baker

Clues:
1. Whoever keeps the dog drinks cocoa.
2. The doctor and the milk drinker are two houses apart.
3. The coffee drinker's house sits immediately to the left of the water drinker's house.
4. The doctor is not a neighbour of the teacher.
5. The baker and the milk drinker live in neighbouring houses.
6. The cat is kept in house 3.
7. The dog's keeper is either the doctor or the teacher.
8. The rabbit owner lives right next door to the pilot, on the pilot's right.
9. The golf enthusiast occupies the leftmost house.
10. The chess player does not live in house 5.
11. Two houses separate the rabbit owner from the teacher.
12. The baker is not the person who owns the bird.
13. The cocoa drinker and the painting enthusiast are two houses apart.
14. The cooking enthusiast lives immediately to the left of the water drinker.

## Puzzle hard:zebra_hard-00070

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- color: purple, blue, yellow, green, white
- nationality: Dane, Brit, Spaniard, Swede, German
- hobby: tennis, painting, golf, chess, hiking
- pet: cat, fish, rabbit, dog, bird

Clues:
1. The dog owner is not the same person as the occupant of the yellow house.
2. The German lives somewhere between the golf enthusiast and the person who enjoys hiking.
3. The tennis enthusiast is not the same person as the occupant of the white house.
4. The occupant of the blue house has only one neighbour.
5. The right-hand neighbour of the owner of the bird is the Brit.
6. If the person who keeps the bird does not enjoy hiking, then that person enjoys tennis.
7. Whoever lives in the green house lives two doors away from the Spaniard.
8. One of the neighbours of the person who keeps the bird keeps the fish.
9. One of the neighbours of the Swede enjoys hiking.
10. The left-hand neighbour of the person who enjoys tennis enjoys hiking.
11. The person who enjoys painting lives somewhere between the owner of the rabbit and the occupant of the yellow house.
12. None of the neighbours of the owner of the fish enjoys chess.
13. One of the neighbours of the occupant of the green house keeps the bird.
14. Whoever lives in the blue house and the Swede are one and the same person.
15. The right-hand neighbour of the person in the yellow house keeps the bird.

## Puzzle plain:zebra-00042

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- color: white, red, yellow, blue, purple
- drink: water, coffee, juice, tea, cocoa
- pet: rabbit, dog, fish, bird, horse
- hobby: tennis, painting, cooking, golf, chess

Clues:
1. The person who enjoys golf does not live in the blue house.
2. The person who enjoys cooking lives next to the fish owner.
3. The cocoa drinker enjoys chess.
4. The person who drinks coffee and the person who enjoys painting are neighbours.
5. The person who drinks tea lives at one end of the row.
6. The person who enjoys cooking and the juice drinker live in adjacent houses.
7. The juice drinker keeps the bird.
8. The person who drinks coffee lives directly to the left of the bird owner.
9. The person in the blue house and the owner of the rabbit live two houses apart.
10. The person who drinks juice lives immediately to the right of whoever lives in the red house.
11. The cooking enthusiast either keeps the horse or keeps the rabbit.
12. The person who enjoys golf lives in the fifth house.
13. The person who drinks juice lives immediately to the right of the dog owner.
14. The person who enjoys cooking lives directly to the left of the person in the yellow house.
15. The person who enjoys painting and whoever lives in the white house live in adjacent houses.

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

## Puzzle hard:zebra_hard-00091

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- hobby: hiking, chess, painting, tennis, golf
- pet: horse, rabbit, cat, dog, fish
- job: farmer, pilot, lawyer, doctor, teacher
- nationality: Dane, Spaniard, Norwegian, Swede, German

Clues:
1. Neither the Norwegian nor the Spaniard enjoys painting.
2. The dog owner lives further to the right than the person who enjoys tennis.
3. The pilot does not live in the third house from the right.
4. The person who keeps the fish and the teacher are one and the same person.
5. The Norwegian lives somewhere between the Dane and the tennis enthusiast.
6. The left-hand neighbour of the person who keeps the fish works as the doctor.
7. The right-hand neighbour of the cat owner works as the lawyer.
8. Exactly 4 houses lie to the left of the home of the rabbit owner.
9. The chess enthusiast and the Spaniard are one and the same person.
10. The person who enjoys hiking lives two doors away from the Norwegian.
11. The person who enjoys golf lives further to the right than the German.
12. Exactly 4 houses lie to the left of the home of the Spaniard.
13. The German and the person who enjoys hiking are one and the same person.
14. The dog owner and the lawyer are one and the same person.

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

## Puzzle paraphrase:zebra-00195

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- color: blue, green, red, white, purple
- drink: tea, coffee, milk, water, juice
- nationality: Brit, German, Swede, Spaniard, Dane
- pet: fish, horse, cat, dog, rabbit

Clues:
1. The Dane is the one with the fish.
2. The tea drinker and the water drinker live next door to each other.
3. The horse is kept in the purple house.
4. The Swede's house has a lower number than the horse owner's.
5. The German drinks either milk or tea.
6. The red house is house 4.
7. The Brit and the dog owner live in adjacent houses.
8. The white house is where the dog owner lives.
9. The blue house is the first house.
10. Exactly one house lies between the milk drinker and the rabbit owner.
11. The Brit occupies the middle house.
12. The coffee drinker lives immediately to the right of the purple house's occupant.
13. The cat owner lives in the first house.
14. The water drinker lives in one of the two end houses.

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
