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

Output: write a single JSON object to the file /home/user/Puzzle-generation-with-guaranteed-uniqueness/data/llm_tasks/e1_encC/e1_encC_005.out.json with this exact structure
{"puzzles": [{"id": "<puzzle id>", "constraints": [{"clue": 1, "expr": "<expression>"}, ...]}, ...]}
One entry per puzzle and exactly one constraint per numbered clue, in order. Use single quotes inside
expressions so the JSON stays valid.

The puzzles follow.


## Puzzle paraphrase:zebra-00150

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- nationality: Brit, Dane, German, Spaniard, Swede
- job: pilot, lawyer, doctor, farmer, teacher
- hobby: golf, tennis, cooking, painting, chess
- color: white, purple, green, yellow, blue

Clues:
1. There are exactly two houses between the teacher and the occupant of the yellow house, which is to say they are two doors apart.
2. The Brit and the Spaniard are next-door neighbours.
3. Painting is the Swede's hobby.
4. The tennis player lives in either the green house or the yellow house.
5. The green house is one of the two houses at the ends of the row.
6. The farmer's house lies somewhere to the right of the painter's.
7. The white house sits directly to the left of the lawyer's home.
8. One house separates the Dane from the resident of the purple house.
9. The German and the green house's occupant live two houses apart.
10. The chess player lives immediately to the left of the doctor.
11. The Spaniard's house is the yellow one.
12. The farmer's hobby is chess.
13. The Brit's favourite pastime is golf.

## Puzzle plain:zebra-00061

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- drink: tea, coffee, cocoa, juice, water
- nationality: Norwegian, German, Swede, Spaniard, Dane
- job: baker, teacher, doctor, lawyer, pilot
- hobby: chess, hiking, golf, cooking, painting

Clues:
1. The doctor lives at one end of the row.
2. The juice drinker lives next to the Norwegian.
3. The teacher and the person who drinks water are neighbours.
4. The cocoa drinker lives directly to the left of the person who drinks juice.
5. The Dane and the lawyer live in adjacent houses.
6. The Dane lives directly to the left of the Swede.
7. The doctor lives somewhere to the left of the person who drinks water.
8. The person who enjoys golf and the person who drinks water live in adjacent houses.
9. The cocoa drinker either enjoys chess or enjoys hiking.
10. The Swede lives in the house just left of the one where the painting enthusiast lives.
11. The person who drinks tea either works as the doctor or works as the lawyer.
12. The German lives in a lower-numbered house than the juice drinker.
13. The German either enjoys hiking or enjoys painting.
14. The golf enthusiast and the Swede live two houses apart.
15. The baker lives somewhere to the right of the cocoa drinker.

## Puzzle plain:zebra-00047

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- nationality: Norwegian, Brit, Dane, Spaniard, Swede
- drink: tea, cocoa, juice, water, coffee
- pet: cat, rabbit, fish, horse, dog
- color: red, green, blue, white, yellow

Clues:
1. Whoever lives in the blue house lives in a lower-numbered house than the owner of the rabbit.
2. The Norwegian lives in the house just left of the one where the fish owner lives.
3. The Spaniard does not live next to whoever lives in the white house.
4. The person in the white house lives in house 3.
5. The owner of the dog either is the Dane or is the Swede.
6. The person in the blue house lives in the leftmost house.
7. The person who drinks tea does not live in house 5.
8. The Brit keeps the fish.
9. The person who drinks juice and the occupant of the red house live two houses apart.
10. The person who drinks coffee lives in the house just left of the one where the cat owner lives.
11. The horse owner lives in the white house.
12. The person who drinks tea lives in the yellow house.
13. The cocoa drinker keeps the cat.
14. The Dane either lives in the green house or lives in the red house.
15. The fish owner and whoever lives in the red house live in adjacent houses.

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

## Puzzle plain:zebra-00084

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- color: red, purple, yellow, white, blue
- pet: bird, cat, rabbit, dog, horse
- drink: coffee, juice, milk, cocoa, water
- nationality: Swede, Brit, Dane, German, Spaniard

Clues:
1. The bird owner lives in the fifth house.
2. The cat owner lives in the house just left of the one where the Spaniard lives.
3. The water drinker lives immediately to the right of the dog owner.
4. The dog owner drinks cocoa.
5. The person who drinks milk lives in the red house.
6. The Dane lives in house 2.
7. The juice drinker lives in the house just left of the one where the person in the yellow house lives.
8. The owner of the dog lives next to whoever lives in the yellow house.
9. The person in the yellow house lives in the house just left of the one where the person in the blue house lives.
10. The coffee drinker lives somewhere to the left of the occupant of the purple house.
11. The owner of the bird lives next to the Swede.
12. The owner of the cat does not live next to the milk drinker.
13. The occupant of the yellow house lives immediately to the right of the rabbit owner.
14. The German lives in house 1.

## Puzzle hard:zebra_hard-00092

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- job: doctor, farmer, baker, pilot, lawyer
- color: red, purple, blue, yellow, white
- drink: water, milk, juice, tea, cocoa
- hobby: painting, chess, hiking, golf, tennis

Clues:
1. The pilot and the person in the purple house are one and the same person.
2. The person who enjoys chess lives two doors away from the person who drinks cocoa.
3. One of the neighbours of the hiking enthusiast works as the lawyer.
4. The right-hand neighbour of the person who enjoys painting drinks juice.
5. The right-hand neighbour of the person who drinks tea works as the doctor.
6. The baker lives somewhere between the occupant of the purple house and the tennis enthusiast.
7. The right-hand neighbour of the tennis enthusiast lives in the blue house.
8. The baker and the milk drinker are one and the same person.
9. The right-hand neighbour of the person in the white house drinks cocoa.
10. The person in the yellow house lives somewhere between whoever lives in the blue house and the person who drinks milk.
11. The right-hand neighbour of the person who drinks water drinks juice.

## Puzzle paraphrase:zebra-00174

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- drink: juice, milk, tea, water, coffee
- job: teacher, pilot, baker, farmer, doctor
- nationality: Dane, German, Swede, Norwegian, Brit
- color: blue, yellow, white, green, red

Clues:
1. The coffee drinker lives immediately to the right of the German.
2. One house sits between the doctor and the juice drinker.
3. The green house is immediately to the right of the teacher's house.
4. The blue house and the coffee drinker's house are adjacent.
5. The water drinker is not in house 1.
6. The farmer lives immediately to the right of the tea drinker.
7. The Brit is the one drinking juice.
8. The occupant of the blue house and the Swede are two houses apart.
9. The teacher is the coffee drinker.
10. The pilot lives immediately to the right of the Dane.
11. The farmer lives in the white house.
12. The German works as either the baker or the pilot.
13. The red house and the white house are next to each other.

## Puzzle plain:zebra-00085

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- drink: coffee, juice, cocoa, tea, milk
- job: farmer, pilot, teacher, baker, lawyer
- nationality: Dane, German, Brit, Swede, Spaniard
- color: green, purple, yellow, white, blue

Clues:
1. There is exactly one house between the Brit and the farmer.
2. The person who drinks coffee lives in a lower-numbered house than the Spaniard.
3. The coffee drinker and the pilot live in adjacent houses.
4. The milk drinker lives at one end of the row.
5. The person who drinks cocoa lives in the leftmost house.
6. The person who drinks tea lives directly to the left of the Dane.
7. The lawyer lives next to the occupant of the white house.
8. The occupant of the blue house lives at one end of the row.
9. Whoever lives in the yellow house lives in the house just left of the one where the occupant of the white house lives.
10. The baker drinks coffee.
11. The Swede lives in the white house.
12. The person who drinks milk and whoever lives in the purple house live two houses apart.
13. The person in the purple house works as the baker.
14. The farmer lives immediately to the right of the lawyer.

## Puzzle hard:zebra_hard-00046

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- pet: bird, cat, rabbit, fish, horse
- drink: juice, water, tea, coffee, milk
- job: lawyer, farmer, teacher, pilot, baker
- hobby: cooking, tennis, hiking, chess, painting

Clues:
1. The person who keeps the bird has only one neighbour.
2. The lawyer and the owner of the rabbit are one and the same person.
3. The left-hand neighbour of the person who drinks tea works as the lawyer.
4. The right-hand neighbour of the pilot drinks coffee.
5. If the person who enjoys tennis does not drink coffee, then that person drinks water.
6. One of the neighbours of the chess enthusiast enjoys tennis.
7. The coffee drinker lives in the third house from the right.
8. The person who keeps the cat lives somewhere between the person who enjoys chess and the hiking enthusiast.
9. The person who drinks juice and the painting enthusiast are one and the same person.
10. Neither the owner of the bird nor the person who drinks milk works as the baker.
11. If the person who keeps the fish does not enjoy chess, then that person enjoys cooking.
12. The tennis enthusiast lives somewhere between the milk drinker and the teacher.
13. One of the neighbours of the painting enthusiast works as the farmer.
14. The person who enjoys hiking lives two doors away from the pilot.

## Puzzle paraphrase:zebra-00176

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- job: baker, farmer, teacher, doctor, lawyer
- nationality: Swede, Spaniard, Dane, Brit, German
- color: red, green, yellow, white, blue
- pet: bird, horse, rabbit, cat, dog

Clues:
1. The German lives somewhere to the right of the blue house's occupant.
2. The Swede lives in house 3.
3. The Dane lives in house 4.
4. The cat belongs to the occupant of the green house.
5. The bird belongs to either the German or the Spaniard.
6. The Brit is the farmer.
7. The teacher lives immediately to the right of the Brit.
8. The Dane is the doctor.
9. The horse is kept in the yellow house.
10. The white house's occupant keeps the rabbit.
11. The dog owner and the yellow house's occupant do not live next to each other.
12. The baker and the occupant of the blue house are two houses apart.
13. Two houses separate the baker from the teacher.
14. The bird owner is a neighbour of whoever is in the green house.
15. The yellow house lies somewhere to the right of the baker.
