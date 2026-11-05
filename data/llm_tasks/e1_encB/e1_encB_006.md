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

Output: write a single JSON object to the file D:\Puzzle-generation-with-guaranteed-uniqueness\data\llm_tasks\e1_encB\e1_encB_006.out.json with this exact structure
{"puzzles": [{"id": "<puzzle id>", "constraints": [{"clue": 1, "expr": "<expression>"}, ...]}, ...]}
One entry per puzzle and exactly one constraint per numbered clue, in order. Use single quotes inside
expressions so the JSON stays valid.

The puzzles follow.


## Puzzle plain:zebra-00094

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- hobby: hiking, chess, golf, painting, tennis
- color: green, yellow, purple, blue, red
- nationality: Dane, Swede, Spaniard, Brit, Norwegian
- drink: milk, water, coffee, cocoa, tea

Clues:
1. The occupant of the red house either drinks cocoa or drinks milk.
2. Whoever lives in the red house enjoys tennis.
3. The painting enthusiast is the Swede.
4. The Brit lives immediately to the right of whoever lives in the green house.
5. The Spaniard either drinks milk or drinks water.
6. The Dane lives in house 5.
7. The person who enjoys hiking lives next to the person in the yellow house.
8. The golf enthusiast lives directly to the left of the Norwegian.
9. The coffee drinker either is the Dane or is the Norwegian.
10. The Swede lives in the house just left of the one where the person in the red house lives.
11. The hiking enthusiast drinks cocoa.
12. The occupant of the blue house lives in house 1.

## Puzzle paraphrase:zebra-00126

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- drink: cocoa, tea, milk, water, coffee
- job: pilot, baker, teacher, lawyer, doctor
- nationality: Spaniard, Norwegian, Dane, German, Swede
- color: blue, white, green, yellow, red

Clues:
1. The yellow house is house number 1.
2. The blue house's occupant does not drink tea.
3. The cocoa drinker and the Norwegian do not live next to each other.
4. One house lies between the water drinker and the white house.
5. The blue house's occupant is not the cocoa drinker.
6. The doctor and the water drinker live two houses apart.
7. The blue house is immediately to the left of the Dane's house.
8. The red house is not next door to the teacher.
9. The lawyer and the Spaniard live two houses apart.
10. The pilot lives next door to the tea drinker.
11. There is one house between the cocoa drinker and the Spaniard.
12. The German and the white house's occupant are neighbours.
13. The green house is directly left of the cocoa drinker's house.
14. The coffee drinker lives in the white house.

## Puzzle plain:zebra-00031

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- hobby: cooking, tennis, painting, chess, hiking
- job: doctor, pilot, lawyer, teacher, baker
- nationality: Dane, Norwegian, Swede, Spaniard, German
- color: purple, yellow, white, green, blue

Clues:
1. The pilot lives in the house just left of the one where the teacher lives.
2. The baker and the hiking enthusiast live two houses apart.
3. The Swede lives at one end of the row.
4. The Swede works as the lawyer.
5. There is exactly one house between the chess enthusiast and the Norwegian.
6. The person who enjoys painting lives in the second house.
7. The Dane lives next to the occupant of the yellow house.
8. The Spaniard lives immediately to the right of the cooking enthusiast.
9. The chess enthusiast lives at one end of the row.
10. The doctor either lives in the blue house or lives in the yellow house.
11. The doctor lives in the house just left of the one where the cooking enthusiast lives.
12. Whoever lives in the green house either enjoys cooking or enjoys hiking.
13. The painting enthusiast and the person in the purple house live in adjacent houses.
14. The person in the yellow house lives directly to the left of the person in the blue house.

## Puzzle paraphrase:zebra-00153

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- job: lawyer, pilot, farmer, teacher, baker
- nationality: Spaniard, German, Norwegian, Brit, Swede
- hobby: hiking, golf, tennis, painting, chess
- drink: water, milk, tea, cocoa, coffee

Clues:
1. The hiker lives immediately to the left of the milk drinker.
2. The farmer lives next door to the Norwegian.
3. The water drinker lives in house 4.
4. The tennis enthusiast lives immediately to the left of the chess player.
5. The coffee drinker's hobby is chess.
6. The Brit lives directly to the left of the coffee drinker.
7. The tea drinker is the baker.
8. The lawyer and the pilot live next door to each other.
9. Exactly one house lies between the German and the teacher.
10. The painter and the tea drinker live two houses apart.
11. The milk drinker lives immediately to the left of the teacher.
12. The Swede lives immediately to the right of the pilot.

## Puzzle plain:zebra-00032

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- drink: water, juice, cocoa, coffee, milk
- pet: cat, horse, fish, bird, rabbit
- job: lawyer, doctor, teacher, pilot, farmer
- nationality: Dane, Spaniard, Brit, German, Norwegian

Clues:
1. The owner of the cat lives in the middle house.
2. The Norwegian lives immediately to the right of the doctor.
3. The person who drinks coffee lives directly to the left of the pilot.
4. The lawyer drinks juice.
5. The person who keeps the horse lives in the house just left of the one where the doctor lives.
6. The person who drinks milk lives directly to the left of the lawyer.
7. The person who drinks coffee keeps the fish.
8. The German does not live next to the owner of the rabbit.
9. The Spaniard lives next to the person who drinks water.
10. The pilot lives in the house just left of the one where the German lives.
11. There is exactly one house between the Brit and the farmer.

## Puzzle paraphrase:zebra-00183

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- hobby: tennis, cooking, painting, golf, chess
- color: green, blue, white, red, yellow
- job: farmer, pilot, baker, teacher, lawyer
- pet: dog, rabbit, bird, horse, cat

Clues:
1. The dog owner is not the pilot.
2. The red house's occupant has either the bird or the rabbit.
3. The rabbit lives in the blue house.
4. The golfer is not the teacher.
5. The cooking enthusiast and the pilot live in neighbouring houses.
6. The green house is where the cat lives.
7. The golfer lives in either the red house or the white house.
8. The lawyer and the teacher have exactly one house between them.
9. The white house is somewhere to the left of the horse owner.
10. The bird owner lives somewhere to the right of the teacher.
11. The horse owner and the tennis player live two houses apart.
12. The yellow house is at one of the two ends of the row.
13. The red house is immediately to the left of the painting enthusiast.
14. The farmer and the painter live next door to each other.
15. One house separates the green house from the painter.
16. The teacher lives somewhere to the left of the cat owner.
17. The cooking enthusiast lives in one of the end houses.

## Puzzle plain:zebra-00099

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- drink: juice, water, cocoa, coffee, tea
- job: pilot, farmer, lawyer, teacher, baker
- color: red, purple, white, blue, yellow
- hobby: golf, hiking, tennis, painting, chess

Clues:
1. The tea drinker lives in the house just left of the one where the occupant of the yellow house lives.
2. The person who drinks coffee lives next to the person who enjoys painting.
3. Whoever lives in the blue house and whoever lives in the red house are neighbours.
4. The water drinker enjoys chess.
5. The person in the purple house lives in a lower-numbered house than the painting enthusiast.
6. The person in the yellow house works as the farmer.
7. The baker and the cocoa drinker live in adjacent houses.
8. The person who drinks cocoa and the teacher live two houses apart.
9. The tennis enthusiast lives in the second house.
10. The cocoa drinker lives in the fourth house.
11. The person in the red house either drinks cocoa or drinks juice.
12. The lawyer drinks cocoa.
13. The person who enjoys chess and the tea drinker are not neighbours.
14. The hiking enthusiast and the water drinker live two houses apart.
15. The farmer and the person in the purple house live two houses apart.

## Puzzle plain:zebra-00059

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- color: purple, green, yellow, white, blue
- hobby: chess, hiking, tennis, cooking, painting
- nationality: German, Spaniard, Swede, Brit, Dane
- pet: dog, cat, rabbit, bird, fish

Clues:
1. The person who keeps the rabbit is the German.
2. The person who enjoys chess and the Swede are not neighbours.
3. Whoever lives in the blue house and the Swede live in adjacent houses.
4. The fish owner lives immediately to the right of the German.
5. The occupant of the purple house lives immediately to the right of the Spaniard.
6. The hiking enthusiast lives in the house just left of the one where whoever lives in the purple house lives.
7. The painting enthusiast lives in house 2.
8. The person who keeps the cat lives in the yellow house.
9. The person who keeps the dog and the hiking enthusiast are neighbours.
10. The cooking enthusiast lives in the house just left of the one where the Swede lives.
11. The chess enthusiast lives in the middle house.
12. The Brit lives in the green house.

## Puzzle hard:zebra_hard-00026

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- color: green, blue, white, purple, yellow
- job: lawyer, teacher, doctor, farmer, pilot
- drink: coffee, tea, cocoa, milk, water
- hobby: cooking, chess, hiking, tennis, golf

Clues:
1. If the occupant of the yellow house does not enjoy golf, then that person enjoys hiking.
2. Whoever lives in the green house lives somewhere between the coffee drinker and the golf enthusiast.
3. The milk drinker lives somewhere between the coffee drinker and the lawyer.
4. The left-hand neighbour of the lawyer drinks water.
5. One of the neighbours of the pilot lives in the blue house.
6. Whoever lives in the blue house and the cocoa drinker are one and the same person.
7. The pilot and the occupant of the purple house are one and the same person.
8. The chess enthusiast and whoever lives in the green house are one and the same person.
9. The person in the blue house and the golf enthusiast are one and the same person.
10. None of the neighbours of the person who drinks cocoa enjoys cooking.
11. The milk drinker lives somewhere between the farmer and the lawyer.
12. The teacher and whoever lives in the white house are one and the same person.
13. One of the neighbours of the occupant of the purple house lives in the yellow house.

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
