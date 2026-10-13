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

Output: write a single JSON object to the file /home/user/Puzzle-generation-with-guaranteed-uniqueness/data/llm_tasks/e1_encA/e1_encA_014.out.json with this exact structure
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

## Puzzle paraphrase:zebra-00182

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- pet: fish, cat, horse, dog, bird
- nationality: Swede, Brit, German, Spaniard, Norwegian
- hobby: tennis, golf, hiking, painting, cooking
- color: blue, green, yellow, white, red

Clues:
1. The tennis player lives immediately to the right of the green house.
2. The Brit occupies the leftmost house.
3. House 3 belongs to the cooking enthusiast.
4. The dog's house is immediately to the right of the white house.
5. The cat owner lives next door to the cooking enthusiast.
6. The bird belongs to the Spaniard.
7. The Swede is the one who owns the cat.
8. Hiking is the Spaniard's hobby.
9. One house lies between the blue house and the cooking enthusiast.
10. The tennis player lives in the fifth house.
11. The red house and the white house are not next to each other.
12. The horse owner lives immediately to the left of the Spaniard.
13. The Norwegian and the painting enthusiast live two houses apart.

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

## Puzzle plain:zebra-00060

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- pet: bird, cat, dog, fish, rabbit
- drink: coffee, tea, juice, water, cocoa
- hobby: hiking, tennis, chess, painting, golf
- color: blue, red, white, purple, green

Clues:
1. The person in the purple house lives in the house just left of the one where whoever lives in the red house lives.
2. The person who enjoys hiking and the juice drinker are neighbours.
3. The person in the green house and the person who enjoys tennis are neighbours.
4. The water drinker either keeps the fish or keeps the rabbit.
5. The person in the blue house keeps the rabbit.
6. The owner of the fish enjoys golf.
7. The coffee drinker either keeps the cat or keeps the rabbit.
8. The person who drinks tea lives in the purple house.
9. There is exactly one house between the cat owner and the occupant of the red house.
10. The person in the purple house lives in the third house.
11. The person who drinks water and whoever lives in the white house live in adjacent houses.
12. The owner of the dog and the painting enthusiast live two houses apart.
13. The person who drinks coffee enjoys chess.

## Puzzle hard:zebra_hard-00072

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- pet: rabbit, fish, bird, dog, cat
- nationality: Swede, German, Norwegian, Dane, Spaniard
- job: teacher, farmer, pilot, doctor, lawyer
- hobby: cooking, golf, tennis, hiking, painting

Clues:
1. The doctor and the hiking enthusiast are one and the same person.
2. The Dane and the pilot are one and the same person.
3. Neither the hiking enthusiast nor the person who enjoys painting keeps the dog.
4. One of the neighbours of the cat owner works as the doctor.
5. The left-hand neighbour of the Spaniard enjoys cooking.
6. One of the neighbours of the Norwegian is the Dane.
7. The fish owner lives further to the right than the hiking enthusiast.
8. The cat owner lives somewhere between the person who enjoys cooking and the lawyer.
9. The Norwegian lives somewhere between the painting enthusiast and the person who enjoys tennis.
10. The person who enjoys cooking lives two doors away from the person who enjoys golf.
11. The person who keeps the rabbit and the person who enjoys tennis are one and the same person.
12. The farmer lives two doors away from the Swede.

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

## Puzzle paraphrase:zebra-00196

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- pet: horse, cat, bird, rabbit, fish
- nationality: German, Swede, Dane, Brit, Spaniard
- drink: water, milk, juice, coffee, cocoa
- color: red, white, green, yellow, blue

Clues:
1. The fish owner lives somewhere to the right of the red house's occupant.
2. The green house's resident drinks juice.
3. The milk drinker lives at one end of the row.
4. The Dane and the red house's resident are two houses apart.
5. The bird owner drinks cocoa.
6. The bird owner is either the Brit or the Dane.
7. The fish owner lives immediately to the right of the blue house's resident.
8. The Brit's house is just to the left of the red house.
9. The yellow house is home to the rabbit owner.
10. The cat belongs to the water drinker.
11. The German lives right next to the water drinker.
12. The Spaniard lives immediately to the right of the Swede.
13. The German and the green house's resident are two houses apart.

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

## Puzzle hard:zebra_hard-00055

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- hobby: golf, painting, chess, hiking, tennis
- drink: tea, juice, cocoa, coffee, water
- job: baker, pilot, teacher, lawyer, farmer
- nationality: German, Spaniard, Swede, Dane, Norwegian

Clues:
1. The person who enjoys golf and the person who drinks juice are one and the same person.
2. Exactly one house separates the farmer from the person who enjoys painting.
3. The farmer and the person who drinks tea are one and the same person.
4. The right-hand neighbour of the teacher is the Spaniard.
5. The left-hand neighbour of the lawyer enjoys tennis.
6. The right-hand neighbour of the farmer is the Norwegian.
7. The person who drinks juice does not live to the right of the person who drinks water.
8. The person who enjoys chess is not the same person as the Spaniard.
9. The left-hand neighbour of the Spaniard is the Swede.
10. The person who drinks cocoa and the Dane are one and the same person.
11. The cocoa drinker and the tennis enthusiast are one and the same person.
12. One of the neighbours of the pilot enjoys painting.
