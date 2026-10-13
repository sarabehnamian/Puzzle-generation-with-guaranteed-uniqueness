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

Output: write a single JSON object to the file /home/user/Puzzle-generation-with-guaranteed-uniqueness/data/llm_tasks/e1_encC/e1_encC_027.out.json with this exact structure
{"puzzles": [{"id": "<puzzle id>", "constraints": [{"clue": 1, "expr": "<expression>"}, ...]}, ...]}
One entry per puzzle and exactly one constraint per numbered clue, in order. Use single quotes inside
expressions so the JSON stays valid.

The puzzles follow.


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

## Puzzle hard:zebra_hard-00017

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- pet: dog, bird, cat, horse, fish
- drink: water, milk, coffee, juice, cocoa
- hobby: hiking, chess, painting, golf, tennis
- color: blue, yellow, green, white, purple

Clues:
1. The person who drinks coffee lives further to the right than the person who enjoys chess.
2. The occupant of the purple house does not live in the fifth house from the right.
3. One of the neighbours of the person in the blue house enjoys hiking.
4. At least one house separates the painting enthusiast from the person who drinks milk.
5. Exactly 3 houses lie to the left of the home of the occupant of the blue house.
6. The owner of the cat and the person who enjoys tennis are one and the same person.
7. The person who drinks juice and whoever lives in the white house are one and the same person.
8. One of the neighbours of the golf enthusiast keeps the horse.
9. If the occupant of the white house does not enjoy golf, then that person enjoys hiking.
10. None of the neighbours of the person who keeps the horse lives in the purple house.
11. One of the neighbours of the person who enjoys tennis drinks water.
12. The coffee drinker and the person in the green house are one and the same person.
13. If the owner of the horse does not drink cocoa, then that person drinks coffee.
14. The person who keeps the bird and the chess enthusiast are one and the same person.
15. Exactly one house separates the golf enthusiast from the person who drinks water.
16. If the person who enjoys tennis does not live in the blue house, then that person lives in the yellow house.
17. If the cocoa drinker does not keep the cat, then that person keeps the dog.

## Puzzle plain:zebra-00036

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- nationality: Swede, Norwegian, Spaniard, Brit, German
- drink: milk, juice, cocoa, water, tea
- pet: dog, fish, bird, cat, horse
- hobby: chess, hiking, golf, painting, cooking

Clues:
1. The Brit and the chess enthusiast are different people.
2. The person who keeps the bird lives in the leftmost house.
3. The person who enjoys golf either is the Brit or is the German.
4. The painting enthusiast and the Spaniard live in adjacent houses.
5. The owner of the horse lives in the middle house.
6. The chess enthusiast lives somewhere to the left of the German.
7. The person who drinks milk lives in the second house.
8. The German lives in the third house.
9. The painting enthusiast drinks cocoa.
10. The Spaniard lives somewhere to the right of the fish owner.
11. The Brit and the person who enjoys hiking are not neighbours.
12. The owner of the horse either drinks cocoa or drinks water.
13. The person who enjoys hiking lives in one of the two end houses.
14. The cooking enthusiast lives immediately to the right of the person who drinks juice.
15. The Swede keeps the cat.

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

## Puzzle paraphrase:zebra-00144

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- drink: milk, water, tea, juice, coffee
- pet: horse, fish, dog, rabbit, cat
- nationality: Spaniard, Dane, Norwegian, Swede, Brit
- color: green, purple, red, blue, yellow

Clues:
1. The water drinker lives in house 4.
2. The Dane is the one who drinks water.
3. The Spaniard lives in house 5.
4. Two houses separate the Brit from the yellow house's occupant.
5. Water is what the green house's occupant drinks.
6. The rabbit owner and the tea drinker live two houses apart.
7. The juice drinker lives in the yellow house.
8. The purple house and the water drinker's home are two houses apart.
9. The fish keeper lives in one of the two end houses.
10. Exactly one house sits between the coffee drinker and the juice drinker.
11. The cat owner lives somewhere to the right of the fish keeper.
12. The blue house's occupant and the cat owner do not live next to each other.
13. The Norwegian lives at one end of the row.
14. The horse belongs to the occupant of the blue house.
15. The Spaniard is the one in the red house.

## Puzzle hard:zebra_hard-00065

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- job: farmer, teacher, baker, doctor, lawyer
- hobby: hiking, cooking, painting, golf, chess
- nationality: Dane, Brit, Swede, German, Spaniard
- drink: coffee, juice, cocoa, tea, water

Clues:
1. The baker lives somewhere between the juice drinker and the teacher.
2. If the German does not enjoy cooking, then that person enjoys golf.
3. Neither the golf enthusiast nor the Spaniard works as the lawyer.
4. Exactly one house separates the baker from the Spaniard.
5. The baker and the person who enjoys golf are one and the same person.
6. The chess enthusiast lives in the fifth house from the right.
7. The right-hand neighbour of the person who enjoys painting drinks water.
8. The right-hand neighbour of the Brit is the German.
9. The left-hand neighbour of the coffee drinker enjoys golf.
10. Exactly 0 houses lie to the left of the home of the farmer.
11. The person who drinks coffee and the German are one and the same person.
12. The left-hand neighbour of the person who drinks cocoa is the Dane.
13. The left-hand neighbour of the juice drinker drinks tea.

## Puzzle paraphrase:zebra-00141

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- hobby: cooking, tennis, golf, hiking, chess
- pet: horse, dog, bird, fish, cat
- job: teacher, farmer, lawyer, pilot, doctor
- drink: milk, tea, cocoa, juice, water

Clues:
1. The doctor and the lawyer have a single house between them.
2. The cat owner lives next door to the tea drinker.
3. The farmer lives in the house immediately right of the water drinker.
4. The bird owner and the tennis enthusiast are neighbours.
5. The dog owner and the hiking enthusiast live in adjoining houses.
6. The owner of the horse lives directly left of the juice drinker.
7. The tea drinker's house has a lower number than the cocoa drinker's.
8. The golf enthusiast lives immediately right of the doctor.
9. The cooking enthusiast lives immediately right of the pilot.
10. The water drinker's hobby is either chess or hiking.
11. The bird owner occupies one of the two end houses.
12. The chess enthusiast and the milk drinker are next-door neighbours.
13. The farmer lives immediately right of the horse owner.

## Puzzle hard:zebra_hard-00095

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- nationality: Swede, German, Brit, Dane, Spaniard
- color: white, purple, green, yellow, red
- pet: cat, dog, horse, bird, fish
- drink: tea, milk, coffee, cocoa, water

Clues:
1. None of the neighbours of the milk drinker keeps the cat.
2. The right-hand neighbour of the Spaniard drinks water.
3. The person who keeps the cat and the Spaniard are one and the same person.
4. The occupant of the green house and the milk drinker are one and the same person.
5. The person who keeps the horse and whoever lives in the yellow house are one and the same person.
6. The German has only one neighbour.
7. Exactly one house separates the person who keeps the bird from whoever lives in the green house.
8. The milk drinker lives somewhere between the Brit and the person who keeps the fish.
9. The left-hand neighbour of the cocoa drinker keeps the dog.
10. None of the neighbours of the tea drinker keeps the fish.
11. The left-hand neighbour of the Swede keeps the horse.
12. The person who drinks coffee lives two doors away from the person who keeps the dog.
13. One of the neighbours of the occupant of the white house is the Brit.
14. The left-hand neighbour of whoever lives in the purple house keeps the dog.

## Puzzle plain:zebra-00020

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- pet: fish, horse, rabbit, cat, bird
- job: doctor, teacher, lawyer, farmer, pilot
- color: purple, blue, yellow, red, green
- hobby: painting, hiking, golf, cooking, chess

Clues:
1. The person who enjoys golf lives in one of the two end houses.
2. The person who keeps the bird lives immediately to the right of the lawyer.
3. The owner of the cat enjoys cooking.
4. The person in the green house lives directly to the left of the owner of the bird.
5. The person in the yellow house lives in the house just left of the one where the painting enthusiast lives.
6. Whoever lives in the blue house lives in the third house.
7. The cooking enthusiast works as the doctor.
8. The pilot keeps the fish.
9. The chess enthusiast either keeps the fish or keeps the rabbit.
10. There is exactly one house between the farmer and the occupant of the purple house.
11. The doctor lives in the house just left of the one where whoever lives in the red house lives.
12. The person who enjoys painting lives in the house just left of the one where the chess enthusiast lives.

## Puzzle paraphrase:zebra-00118

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- hobby: tennis, chess, cooking, hiking, painting
- job: pilot, teacher, lawyer, doctor, farmer
- color: blue, white, yellow, red, green
- pet: dog, fish, horse, cat, bird

Clues:
1. The cat lives in the yellow house.
2. The hiking enthusiast is either the lawyer or the pilot.
3. The bird owner lives right next to the white house.
4. The fish owner lives directly to the left of the hiking enthusiast.
5. The farmer is the cooking enthusiast.
6. The chess enthusiast and the green house's occupant have exactly one house between them.
7. The painting enthusiast and the teacher live in adjacent houses.
8. The cooking enthusiast lives in one of the two end houses.
9. The horse is kept in the blue house.
10. The tennis enthusiast lives in either the blue house or the red house.
11. The dog owner and the horse owner live in adjacent houses.
12. The hiking enthusiast and the lawyer live in neighbouring houses.
13. The painting enthusiast lives immediately to the left of the cat owner.
14. Exactly one house lies between the blue house and the fish owner.
