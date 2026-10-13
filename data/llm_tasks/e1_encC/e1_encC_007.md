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

Output: write a single JSON object to the file /home/user/Puzzle-generation-with-guaranteed-uniqueness/data/llm_tasks/e1_encC/e1_encC_007.out.json with this exact structure
{"puzzles": [{"id": "<puzzle id>", "constraints": [{"clue": 1, "expr": "<expression>"}, ...]}, ...]}
One entry per puzzle and exactly one constraint per numbered clue, in order. Use single quotes inside
expressions so the JSON stays valid.

The puzzles follow.


## Puzzle hard:zebra_hard-00057

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- nationality: Brit, Swede, German, Norwegian, Spaniard
- pet: fish, dog, cat, horse, bird
- job: farmer, lawyer, baker, doctor, teacher
- drink: coffee, milk, juice, water, tea

Clues:
1. The tea drinker lives in the fourth house from the right.
2. The owner of the fish lives in the fifth house from the right.
3. The right-hand neighbour of the owner of the horse drinks water.
4. The baker and the Swede are one and the same person.
5. The left-hand neighbour of the person who drinks coffee works as the lawyer.
6. One of the neighbours of the owner of the cat works as the lawyer.
7. The left-hand neighbour of the milk drinker is the Brit.
8. The Norwegian lives in the rightmost house.
9. The baker does not live to the right of the doctor.
10. Exactly 1 house lies to the left of the home of the person who keeps the dog.
11. The Spaniard is not the same person as the tea drinker.
12. The left-hand neighbour of the person who keeps the horse works as the doctor.
13. If the water drinker is not the baker, then that person works as the teacher.

## Puzzle paraphrase:zebra-00191

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- hobby: painting, golf, cooking, chess, tennis
- job: pilot, baker, lawyer, teacher, farmer
- pet: horse, bird, fish, cat, dog
- nationality: Norwegian, Swede, Spaniard, Brit, Dane

Clues:
1. The Dane and the dog owner are next-door neighbours.
2. The horse owner lives immediately to the right of the chess enthusiast.
3. The tennis enthusiast is the pilot.
4. The cat owner lives next door to the Swede.
5. The house directly to the right of the Swede's is the horse owner's.
6. The lawyer is the one who keeps the bird.
7. The teacher lives somewhere to the right of the pilot.
8. The cooking enthusiast is the farmer.
9. The painting enthusiast has the cat.
10. The dog owner's house is immediately to the right of the horse owner's.
11. The Spaniard is the cooking enthusiast.
12. The tennis enthusiast keeps the horse.
13. The Brit is the pilot.

## Puzzle plain:zebra-00092

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- color: white, red, purple, blue, green
- pet: horse, fish, dog, bird, rabbit
- nationality: Dane, German, Swede, Norwegian, Spaniard
- drink: cocoa, juice, milk, tea, water

Clues:
1. The person who keeps the horse lives in the second house.
2. The German lives directly to the left of the person who drinks cocoa.
3. The person who drinks tea lives directly to the left of the person who drinks cocoa.
4. The milk drinker lives in one of the two end houses.
5. The Dane keeps the rabbit.
6. Whoever lives in the purple house drinks juice.
7. The fish owner and the tea drinker are neighbours.
8. The Dane lives immediately to the right of the owner of the dog.
9. The person in the green house and the water drinker live two houses apart.
10. The Spaniard lives immediately to the right of the tea drinker.
11. The bird owner does not live next to the Swede.
12. The person in the red house and the water drinker live in adjacent houses.
13. The Dane lives in the last house.
14. The person in the white house lives directly to the left of the person who drinks juice.
15. The owner of the fish lives in the leftmost house.

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

## Puzzle plain:zebra-00075

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- job: lawyer, doctor, teacher, baker, pilot
- color: yellow, white, red, green, blue
- hobby: golf, painting, tennis, hiking, cooking
- nationality: Brit, Norwegian, Swede, Spaniard, Dane

Clues:
1. The doctor does not live next to whoever lives in the yellow house.
2. The pilot lives immediately to the right of the tennis enthusiast.
3. Whoever lives in the red house lives somewhere to the right of the baker.
4. The golf enthusiast lives in the red house.
5. There is exactly one house between the hiking enthusiast and the lawyer.
6. Whoever lives in the blue house lives in the house just left of the one where the person in the red house lives.
7. The Dane lives in the house just left of the one where the Swede lives.
8. The person who enjoys painting and the person in the white house live in adjacent houses.
9. Whoever lives in the white house either is the Brit or is the Swede.
10. The doctor lives in the house just left of the one where the pilot lives.
11. The baker lives at one end of the row.
12. The Brit lives somewhere to the left of the golf enthusiast.
13. The Norwegian lives directly to the left of the lawyer.
14. The person who enjoys cooking lives directly to the left of the person who enjoys golf.

## Puzzle plain:zebra-00073

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- drink: cocoa, juice, water, milk, tea
- nationality: Norwegian, Swede, Dane, Spaniard, Brit
- hobby: tennis, cooking, painting, chess, hiking
- job: teacher, lawyer, baker, doctor, farmer

Clues:
1. The Norwegian and the Spaniard live two houses apart.
2. The doctor and the Swede live in adjacent houses.
3. The cooking enthusiast lives next to the person who drinks tea.
4. There is exactly one house between the Dane and the person who drinks water.
5. The baker and the hiking enthusiast live two houses apart.
6. The Brit works as the baker.
7. The person who enjoys tennis lives directly to the left of the juice drinker.
8. The Swede and the teacher live two houses apart.
9. The farmer lives in house 4.
10. The Brit lives directly to the left of the Spaniard.
11. The milk drinker enjoys painting.
12. The person who enjoys painting lives in house 5.

## Puzzle paraphrase:zebra-00180

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- drink: tea, coffee, cocoa, water, milk
- pet: dog, bird, horse, fish, rabbit
- color: yellow, red, green, blue, white
- job: farmer, doctor, lawyer, baker, pilot

Clues:
1. Whoever drinks tea is the pilot.
2. The green house stands somewhere to the right of the doctor's house.
3. The dog's keeper drinks water.
4. The horse is kept in the house immediately to the left of the rabbit's house.
5. Tea is drunk in the fourth house.
6. The cocoa drinker is not the one with the rabbit.
7. The baker lives next door to the white house.
8. The cocoa drinker and the lawyer live two houses apart.
9. The fish is kept in the house directly to the left of the red house.
10. The bird lives in house 2.
11. One house separates the white house from the yellow house.
12. The yellow house's occupant drinks coffee.
13. The dog does not live in house 5.
14. The farmer occupies the fifth house.

## Puzzle plain:zebra-00017

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- pet: rabbit, horse, dog, fish, bird
- nationality: Spaniard, German, Norwegian, Dane, Swede
- job: baker, doctor, farmer, pilot, lawyer
- color: yellow, blue, white, green, red

Clues:
1. The horse owner either is the German or is the Spaniard.
2. The owner of the fish lives in the house just left of the one where the dog owner lives.
3. The doctor lives in house 4.
4. The bird owner does not live in the fifth house.
5. Whoever lives in the blue house works as the doctor.
6. The rabbit owner lives directly to the left of the farmer.
7. The lawyer lives in the green house.
8. There is exactly one house between the occupant of the green house and the occupant of the yellow house.
9. The occupant of the red house is not the German.
10. The German lives in the second house.
11. The Norwegian does not live in the third house.
12. The pilot lives next to the Spaniard.
13. The Swede lives in the green house.
14. The baker and the owner of the dog live two houses apart.

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
