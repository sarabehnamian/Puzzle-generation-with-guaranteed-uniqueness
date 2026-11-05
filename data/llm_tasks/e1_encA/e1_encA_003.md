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

Output: write a single JSON object to the file D:\Puzzle-generation-with-guaranteed-uniqueness\data\llm_tasks\e1_encA\e1_encA_003.out.json with this exact structure
{"puzzles": [{"id": "<puzzle id>", "constraints": [{"clue": 1, "expr": "<expression>"}, ...]}, ...]}
One entry per puzzle and exactly one constraint per numbered clue, in order. Use single quotes inside
expressions so the JSON stays valid.

The puzzles follow.


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

## Puzzle hard:zebra_hard-00043

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- job: doctor, teacher, pilot, baker, lawyer
- hobby: golf, chess, tennis, hiking, cooking
- pet: fish, rabbit, dog, bird, horse
- nationality: Brit, Swede, Spaniard, Norwegian, German

Clues:
1. Exactly 2 houses lie to the left of the home of the bird owner.
2. The right-hand neighbour of the tennis enthusiast enjoys chess.
3. If the teacher does not enjoy chess, then that person enjoys cooking.
4. One of the neighbours of the German works as the doctor.
5. The right-hand neighbour of the teacher is the Brit.
6. The left-hand neighbour of the person who enjoys cooking enjoys chess.
7. Exactly one house separates the fish owner from the person who keeps the horse.
8. Neither the Brit nor the pilot enjoys golf.
9. The Spaniard lives somewhere between the person who keeps the dog and the Norwegian.
10. Exactly 4 houses lie to the left of the home of the German.
11. The horse owner lives somewhere between the person who keeps the dog and the fish owner.
12. The person who keeps the horse and the lawyer are one and the same person.
13. Neither the owner of the bird nor the owner of the horse enjoys tennis.

## Puzzle paraphrase:zebra-00178

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- color: yellow, blue, green, purple, red
- job: farmer, doctor, baker, lawyer, teacher
- drink: juice, coffee, cocoa, milk, tea
- pet: cat, fish, rabbit, bird, horse

Clues:
1. The farmer lives immediately to the left of the cocoa drinker.
2. The doctor lives in house 5.
3. The green house's occupant keeps the horse.
4. The bird owner and the fish keeper live next door to each other.
5. The red house's occupant keeps either the cat or the horse.
6. The teacher lives immediately to the right of the yellow house.
7. The bird keeper lives somewhere to the right of the teacher.
8. The juice drinker does not live next door to the teacher.
9. The yellow house's occupant drinks either coffee or milk.
10. The yellow house is immediately to the left of the coffee drinker.
11. The red house is house 5.
12. The lawyer lives immediately to the left of the bird keeper.
13. The cocoa drinker and the purple house are two houses apart.

## Puzzle paraphrase:zebra-00172

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- pet: rabbit, dog, fish, cat, bird
- job: lawyer, pilot, doctor, baker, teacher
- nationality: Swede, Norwegian, German, Brit, Dane
- color: blue, yellow, white, red, purple

Clues:
1. The yellow house's occupant is the doctor.
2. The German is not next door to the pilot.
3. The cat owner lives in either the blue house or the white house.
4. The red house and the yellow house are two houses apart.
5. The dog owner lives immediately to the left of the yellow house.
6. The bird owner lives somewhere to the left of the Dane.
7. Exactly one house lies between the lawyer and the white house.
8. The teacher lives immediately to the left of the fish owner.
9. One house separates the Brit from the pilot.
10. The lawyer and the Norwegian have exactly one house between them.
11. The Brit and the Dane are not neighbours.
12. The rabbit owner lives in house 2.
13. The Norwegian lives immediately to the left of the purple house.

## Puzzle hard:zebra_hard-00085

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- job: baker, pilot, lawyer, farmer, doctor
- hobby: tennis, cooking, painting, hiking, chess
- color: white, red, blue, yellow, green
- pet: cat, rabbit, horse, fish, bird

Clues:
1. One of the neighbours of the doctor enjoys hiking.
2. The bird owner and the doctor are one and the same person.
3. The person who keeps the horse and the person in the yellow house are one and the same person.
4. The owner of the rabbit is not the same person as whoever lives in the red house.
5. Neither the owner of the rabbit nor the occupant of the yellow house enjoys cooking.
6. Exactly one house separates the farmer from the occupant of the yellow house.
7. The left-hand neighbour of the owner of the cat works as the lawyer.
8. The left-hand neighbour of whoever lives in the white house enjoys chess.
9. Whoever lives in the green house lives somewhere between the cooking enthusiast and the person who keeps the rabbit.
10. If the occupant of the white house is not the farmer, then that person works as the pilot.
11. The pilot lives somewhere between the farmer and the owner of the rabbit.
12. The right-hand neighbour of the bird owner enjoys cooking.
13. One of the neighbours of the tennis enthusiast works as the farmer.

## Puzzle plain:zebra-00051

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- hobby: cooking, tennis, chess, painting, golf
- job: pilot, farmer, baker, lawyer, teacher
- color: yellow, white, purple, red, green
- nationality: Spaniard, Brit, German, Swede, Dane

Clues:
1. The person who enjoys tennis and the farmer are different people.
2. The person who enjoys painting lives directly to the left of the person who enjoys golf.
3. The Swede and the person in the white house live two houses apart.
4. The baker lives in the house just left of the one where the Swede lives.
5. The teacher and the occupant of the yellow house are neighbours.
6. The Dane lives in the green house.
7. The cooking enthusiast lives in the red house.
8. The baker lives directly to the left of the person who enjoys chess.
9. Whoever lives in the white house lives in a lower-numbered house than the person who enjoys chess.
10. The lawyer and the teacher live two houses apart.
11. The teacher lives immediately to the right of the person who enjoys cooking.
12. The occupant of the red house and the Swede live in adjacent houses.
13. The Spaniard and the Swede live in adjacent houses.
14. The German lives in house 3.

## Puzzle plain:zebra-00024

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- color: purple, green, yellow, red, blue
- job: doctor, lawyer, baker, farmer, teacher
- nationality: German, Norwegian, Brit, Dane, Spaniard
- pet: rabbit, dog, cat, horse, fish

Clues:
1. The person in the blue house works as the lawyer.
2. The occupant of the purple house works as the teacher.
3. There is exactly one house between the person in the blue house and the occupant of the red house.
4. The doctor and the Norwegian live two houses apart.
5. The Dane either keeps the dog or keeps the horse.
6. The Brit keeps the rabbit.
7. The horse owner and the occupant of the purple house live in adjacent houses.
8. The Dane lives in one of the two end houses.
9. The Spaniard lives in the third house.
10. The Brit lives next to the occupant of the yellow house.
11. The owner of the cat lives next to the person who keeps the rabbit.
12. The person who keeps the horse lives somewhere to the right of the owner of the cat.
13. The person in the blue house lives in the leftmost house.
14. The baker lives somewhere to the right of the German.
15. The Norwegian lives somewhere to the right of the fish owner.
16. The German lives in a lower-numbered house than the Brit.

## Puzzle paraphrase:zebra-00155

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- hobby: cooking, golf, painting, hiking, tennis
- drink: water, milk, coffee, juice, tea
- color: white, yellow, blue, green, purple
- pet: cat, bird, dog, horse, fish

Clues:
1. The hiker drinks coffee.
2. The juice drinker lives in house 4.
3. Exactly one house lies between the green house and the purple house.
4. The blue house's occupant and the tea drinker are neighbours.
5. The bird owner lives immediately to the left of the purple house's occupant.
6. The cooking enthusiast lives next door to the water drinker.
7. The golfer and the tennis player live next to each other.
8. The tennis player doesn't keep the dog.
9. One house sits between the bird's owner and the yellow house's occupant.
10. The juice drinker lives somewhere to the right of the yellow house.
11. The golfer and the horse keeper are not neighbours.
12. The fish owner lives immediately to the left of the cat owner.
13. The painter lives in a lower-numbered house than the hiker.
14. The milk drinker and the tennis player are not next-door neighbours.
15. The white house's occupant enjoys either cooking or painting.
16. The fish owner and the water drinker live next door to each other.
17. The tennis player lives in either the green house or the purple house.

## Puzzle paraphrase:zebra-00131

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- hobby: chess, painting, golf, hiking, cooking
- nationality: Swede, Spaniard, Norwegian, Dane, German
- job: doctor, baker, farmer, lawyer, teacher
- drink: milk, cocoa, tea, juice, water

Clues:
1. The cocoa drinker lives next door to the doctor.
2. Whoever drinks juice enjoys either chess or golf.
3. The painting enthusiast drinks water.
4. The baker lives directly to the right of the water drinker.
5. The cooking enthusiast is either the farmer or the teacher.
6. The teacher lives in house 1.
7. The tea drinker is either the doctor or the lawyer.
8. The Dane lives directly to the right of the milk drinker.
9. The farmer lives in house 5.
10. The German does not live in house 5.
11. The Spaniard lives somewhere to the left of the juice drinker.
12. The tea drinker lives immediately to the left of the German.
13. The doctor and the hiking enthusiast are next-door neighbours.
14. The Norwegian lives next door to the water drinker.
15. The golf enthusiast is either the lawyer or the teacher.

## Puzzle plain:zebra-00011

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- job: doctor, teacher, baker, pilot, farmer
- nationality: German, Brit, Norwegian, Swede, Spaniard
- hobby: chess, cooking, painting, tennis, golf
- color: red, purple, white, green, yellow

Clues:
1. The German lives somewhere to the left of whoever lives in the yellow house.
2. The painting enthusiast works as the doctor.
3. There is exactly one house between the cooking enthusiast and the occupant of the red house.
4. The occupant of the white house lives somewhere to the left of the person who enjoys tennis.
5. Whoever lives in the green house works as the baker.
6. The Spaniard lives next to the person who enjoys tennis.
7. The Brit and the Swede are neighbours.
8. There is exactly one house between the cooking enthusiast and the Spaniard.
9. The farmer either is the Norwegian or is the Swede.
10. The golf enthusiast and the teacher are neighbours.
11. The baker is the Brit.
12. The German and the person in the purple house live two houses apart.
13. The golf enthusiast lives directly to the left of the baker.
