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

Output: write a single JSON object to the file /home/user/Puzzle-generation-with-guaranteed-uniqueness/data/llm_tasks/e1_encC/e1_encC_028.out.json with this exact structure
{"puzzles": [{"id": "<puzzle id>", "constraints": [{"clue": 1, "expr": "<expression>"}, ...]}, ...]}
One entry per puzzle and exactly one constraint per numbered clue, in order. Use single quotes inside
expressions so the JSON stays valid.

The puzzles follow.


## Puzzle hard:zebra_hard-00049

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- hobby: tennis, chess, golf, hiking, painting
- job: pilot, doctor, baker, lawyer, teacher
- pet: bird, cat, fish, horse, dog
- color: white, yellow, red, purple, blue

Clues:
1. The owner of the dog and the person who enjoys hiking are one and the same person.
2. Exactly 4 houses lie to the left of the home of the fish owner.
3. The bird owner and the person in the yellow house are one and the same person.
4. The right-hand neighbour of the doctor works as the baker.
5. Exactly 2 houses lie to the left of the home of the chess enthusiast.
6. The doctor and the horse owner are one and the same person.
7. If the person who enjoys golf does not live in the blue house, then that person lives in the yellow house.
8. Exactly one house separates the lawyer from whoever lives in the white house.
9. Exactly one house separates the person who enjoys painting from the person in the purple house.
10. Exactly one house separates the lawyer from the teacher.
11. If the teacher does not enjoy chess, then that person enjoys tennis.
12. The person who keeps the cat has only one neighbour.

## Puzzle plain:zebra-00095

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- drink: cocoa, juice, milk, water, coffee
- pet: cat, bird, horse, rabbit, dog
- nationality: German, Swede, Dane, Norwegian, Brit
- hobby: chess, hiking, cooking, golf, painting

Clues:
1. The German and the person who drinks water live in adjacent houses.
2. The cat owner drinks water.
3. There is exactly one house between the Brit and the dog owner.
4. The cocoa drinker and the cooking enthusiast live in adjacent houses.
5. The owner of the cat and the juice drinker are neighbours.
6. The Dane either drinks coffee or drinks water.
7. The golf enthusiast and the Norwegian are neighbours.
8. The juice drinker enjoys painting.
9. The Brit does not live next to the hiking enthusiast.
10. The hiking enthusiast and the person who drinks juice are neighbours.
11. The owner of the bird lives immediately to the right of the rabbit owner.
12. The person who enjoys cooking lives directly to the left of the person who keeps the rabbit.
13. The person who keeps the cat and the person who keeps the rabbit are neighbours.
14. The Brit lives in the house just left of the one where the Dane lives.

## Puzzle plain:zebra-00056

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- pet: dog, bird, horse, cat, fish
- color: blue, purple, red, green, white
- nationality: Dane, German, Norwegian, Swede, Brit
- job: teacher, baker, doctor, farmer, pilot

Clues:
1. There is exactly one house between the Dane and the occupant of the green house.
2. The horse owner lives directly to the left of whoever lives in the white house.
3. The Brit lives directly to the left of the baker.
4. The fish owner and the person in the green house are neighbours.
5. The Swede lives at one end of the row.
6. The German keeps the dog.
7. The fish owner lives next to the person in the red house.
8. The teacher lives in the house just left of the one where the person who keeps the horse lives.
9. The baker lives in the white house.
10. The German lives in the white house.
11. The pilot lives in house 2.
12. Whoever lives in the red house lives in house 2.
13. The fish owner and whoever lives in the purple house live two houses apart.
14. The owner of the cat lives next to the farmer.

## Puzzle paraphrase:zebra-00131

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- hobby: chess, painting, golf, hiking, cooking
- nationality: Swede, Spaniard, Norwegian, Dane, German
- job: doctor, baker, farmer, lawyer, teacher
- drink: milk, cocoa, tea, juice, water

Clues:
1. The cocoa drinker's house is right next to the doctor's.
2. The juice drinker's hobby is either chess or golf.
3. Whoever enjoys painting drinks water.
4. The baker lives directly to the right of the water drinker.
5. The cooking enthusiast is either the farmer or the teacher.
6. The teacher occupies house 1.
7. The tea drinker is either the doctor or the lawyer.
8. The Dane lives directly to the right of the milk drinker.
9. The farmer occupies house 5.
10. The German does not live in house 5.
11. The Spaniard lives somewhere further left than the juice drinker.
12. The tea drinker lives directly to the left of the German.
13. The doctor and the hiking enthusiast live next door to each other.
14. The Norwegian and the water drinker are next-door neighbours.
15. The golf enthusiast is either the lawyer or the teacher.

## Puzzle hard:zebra_hard-00019

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- hobby: painting, tennis, hiking, cooking, chess
- drink: coffee, milk, juice, water, cocoa
- pet: fish, bird, horse, rabbit, dog
- job: doctor, baker, pilot, teacher, lawyer

Clues:
1. The person who enjoys painting lives somewhere between the person who enjoys chess and the milk drinker.
2. The person who drinks coffee lives somewhere between the baker and the fish owner.
3. The water drinker lives further to the right than the baker.
4. The doctor lives somewhere between the person who keeps the bird and the chess enthusiast.
5. Exactly one house separates the doctor from the person who drinks milk.
6. The bird owner does not live in the fifth house from the right.
7. If the teacher does not enjoy cooking, then that person enjoys painting.
8. One of the neighbours of the painting enthusiast works as the baker.
9. The cocoa drinker and the lawyer are one and the same person.
10. The lawyer and the rabbit owner are one and the same person.
11. If the person who keeps the bird does not enjoy hiking, then that person enjoys painting.
12. The cooking enthusiast lives two doors away from the person who enjoys tennis.
13. The lawyer lives further to the right than the person who drinks coffee.
14. At least one house separates the person who drinks water from the person who enjoys hiking.
15. Neither the painting enthusiast nor the water drinker works as the teacher.
16. If the horse owner does not drink coffee, then that person drinks water.

## Puzzle hard:zebra_hard-00096

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- nationality: Dane, German, Swede, Spaniard, Norwegian
- job: baker, pilot, teacher, farmer, doctor
- pet: fish, horse, bird, cat, rabbit
- color: red, white, blue, yellow, purple

Clues:
1. The right-hand neighbour of the person who keeps the fish works as the doctor.
2. The left-hand neighbour of the German lives in the yellow house.
3. The occupant of the blue house and the German are one and the same person.
4. One of the neighbours of the Dane works as the teacher.
5. The occupant of the white house does not live in the fifth house from the right.
6. The person who keeps the horse and the Norwegian are one and the same person.
7. Exactly one house separates the occupant of the blue house from the rabbit owner.
8. Exactly one house separates the occupant of the purple house from whoever lives in the white house.
9. The right-hand neighbour of the horse owner is the German.
10. Exactly 0 houses lie to the left of the home of the Dane.
11. One of the neighbours of the person in the red house is the Swede.
12. The pilot lives somewhere between the person who keeps the bird and the German.
13. The rabbit owner lives further to the right than the farmer.

## Puzzle hard:zebra_hard-00016

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- pet: horse, dog, cat, fish, rabbit
- drink: milk, juice, water, tea, coffee
- hobby: painting, golf, tennis, cooking, hiking
- color: yellow, white, blue, purple, green

Clues:
1. One of the neighbours of the person in the purple house enjoys golf.
2. The right-hand neighbour of whoever lives in the purple house lives in the white house.
3. One of the neighbours of the person who keeps the dog lives in the yellow house.
4. The occupant of the blue house has only one neighbour.
5. If the owner of the fish does not enjoy cooking, then that person enjoys painting.
6. The person who enjoys tennis lives somewhere between the tea drinker and the person who drinks water.
7. One of the neighbours of the person who drinks water lives in the green house.
8. The milk drinker and the tennis enthusiast are one and the same person.
9. The cat owner and the cooking enthusiast are one and the same person.
10. One of the neighbours of the tea drinker keeps the cat.
11. Exactly 0 houses lie to the left of the home of the juice drinker.
12. Exactly 1 house lies to the left of the home of the person who keeps the horse.
13. One of the neighbours of the person who enjoys painting lives in the yellow house.
14. The person who enjoys cooking lives in the fifth house from the right.

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

## Puzzle plain:zebra-00048

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- nationality: Spaniard, Dane, German, Brit, Swede
- hobby: painting, chess, golf, hiking, tennis
- color: blue, red, white, purple, yellow
- job: farmer, pilot, doctor, baker, lawyer

Clues:
1. The Spaniard does not live in the fifth house.
2. The doctor lives in the second house.
3. The pilot lives somewhere to the right of the hiking enthusiast.
4. The person in the red house lives somewhere to the right of the person who enjoys tennis.
5. The German enjoys hiking.
6. The chess enthusiast lives in the white house.
7. The Swede works as the lawyer.
8. There is exactly one house between the person who enjoys chess and the German.
9. The farmer lives somewhere to the left of the occupant of the purple house.
10. The baker does not live in house 1.
11. The golf enthusiast is the Swede.
12. The Dane and the occupant of the yellow house live two houses apart.
13. The lawyer does not live in house 5.
14. The chess enthusiast lives in house 4.
15. The baker either lives in the blue house or lives in the purple house.
16. The person who enjoys chess is the Dane.

## Puzzle paraphrase:zebra-00158

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- hobby: painting, tennis, chess, cooking, hiking
- color: white, green, red, purple, blue
- nationality: Spaniard, Brit, Dane, German, Swede
- pet: dog, fish, rabbit, horse, bird

Clues:
1. The hiker keeps the fish.
2. The green house is right next to the Swede.
3. The German lives immediately to the left of the white house.
4. The purple house and the rabbit owner are neighbours.
5. The painter lives in the red house.
6. The purple house's occupant is not the tennis player.
7. The cook and the Dane live in neighbouring houses.
8. The rabbit keeper's hobby is cooking.
9. The bird owner lives right next to the Swede.
10. The horse belongs to the Dane.
11. The Brit is the one in the blue house.
12. The Brit and the red house are two houses apart.
13. The Swede lives in the red house.
