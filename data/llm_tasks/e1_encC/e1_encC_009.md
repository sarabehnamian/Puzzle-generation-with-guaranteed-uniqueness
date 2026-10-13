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

Output: write a single JSON object to the file /home/user/Puzzle-generation-with-guaranteed-uniqueness/data/llm_tasks/e1_encC/e1_encC_009.out.json with this exact structure
{"puzzles": [{"id": "<puzzle id>", "constraints": [{"clue": 1, "expr": "<expression>"}, ...]}, ...]}
One entry per puzzle and exactly one constraint per numbered clue, in order. Use single quotes inside
expressions so the JSON stays valid.

The puzzles follow.


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

## Puzzle plain:zebra-00030

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- nationality: Norwegian, Dane, Brit, Spaniard, Swede
- color: red, yellow, purple, green, white
- pet: bird, cat, dog, rabbit, fish
- drink: juice, water, tea, milk, coffee

Clues:
1. The water drinker lives directly to the left of the person in the green house.
2. The Norwegian drinks tea.
3. The rabbit owner drinks coffee.
4. The Spaniard and the occupant of the yellow house are neighbours.
5. The tea drinker lives directly to the left of the juice drinker.
6. The Swede and the occupant of the white house live in adjacent houses.
7. The occupant of the green house lives directly to the left of the Brit.
8. The Norwegian does not live next to the rabbit owner.
9. The owner of the cat and whoever lives in the white house live two houses apart.
10. The Norwegian keeps the dog.
11. The Dane keeps the fish.
12. The person who drinks juice lives immediately to the right of the person in the white house.
13. The occupant of the red house drinks water.

## Puzzle hard:zebra_hard-00059

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- hobby: tennis, cooking, painting, chess, golf
- nationality: Swede, German, Brit, Dane, Norwegian
- drink: cocoa, water, juice, milk, tea
- job: baker, doctor, pilot, teacher, lawyer

Clues:
1. The pilot and the person who drinks tea are one and the same person.
2. If the doctor does not enjoy painting, then that person enjoys tennis.
3. The person who drinks milk lives somewhere between the baker and the person who drinks water.
4. The left-hand neighbour of the person who drinks juice is the Dane.
5. Neither the Norwegian nor the person who drinks water works as the doctor.
6. The right-hand neighbour of the painting enthusiast works as the teacher.
7. The German and the teacher are one and the same person.
8. Neither the doctor nor the person who drinks juice is the Swede.
9. The left-hand neighbour of the German drinks juice.
10. The cooking enthusiast lives two doors away from the pilot.
11. One of the neighbours of the German enjoys chess.
12. If the person who enjoys chess is not the Brit, then that person is the Dane.

## Puzzle hard:zebra_hard-00080

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- pet: bird, cat, rabbit, horse, dog
- nationality: Brit, German, Swede, Norwegian, Dane
- drink: tea, coffee, juice, water, milk
- hobby: cooking, painting, chess, tennis, hiking

Clues:
1. If the person who drinks water does not keep the dog, then that person keeps the horse.
2. One of the neighbours of the person who drinks juice keeps the dog.
3. If the Swede does not enjoy cooking, then that person enjoys painting.
4. The right-hand neighbour of the Norwegian keeps the dog.
5. If the German does not drink milk, then that person drinks water.
6. The Brit lives two doors away from the rabbit owner.
7. The person who enjoys hiking has only one neighbour.
8. One of the neighbours of the owner of the horse enjoys tennis.
9. The tea drinker lives in the fourth house from the right.
10. One of the neighbours of the person who enjoys cooking drinks milk.
11. Exactly 0 houses lie to the left of the home of the person who drinks milk.
12. The left-hand neighbour of the owner of the cat is the Swede.
13. Exactly 4 houses lie to the left of the home of the Brit.
14. Exactly 4 houses lie to the left of the home of the owner of the dog.

## Puzzle hard:zebra_hard-00090

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- nationality: Norwegian, Dane, Swede, German, Spaniard
- color: yellow, green, blue, red, white
- job: farmer, pilot, teacher, lawyer, baker
- drink: water, coffee, milk, juice, cocoa

Clues:
1. The pilot lives somewhere between the juice drinker and the lawyer.
2. One of the neighbours of the occupant of the red house drinks coffee.
3. The left-hand neighbour of the German drinks water.
4. Neither the person in the blue house nor the cocoa drinker works as the baker.
5. If the cocoa drinker is not the German, then that person is the Norwegian.
6. One of the neighbours of the cocoa drinker drinks coffee.
7. The right-hand neighbour of the Norwegian is the Swede.
8. Whoever lives in the green house and the teacher are one and the same person.
9. The occupant of the green house does not live in the second house from the right.
10. The right-hand neighbour of the coffee drinker is the Norwegian.
11. Exactly 4 houses lie to the left of the home of the lawyer.
12. Neither the baker nor the person in the green house is the Spaniard.
13. The right-hand neighbour of the baker drinks water.
14. The German and the person in the white house are one and the same person.

## Puzzle paraphrase:zebra-00167

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- job: lawyer, doctor, farmer, pilot, baker
- drink: juice, coffee, tea, cocoa, milk
- color: red, green, purple, yellow, white
- pet: fish, cat, horse, dog, bird

Clues:
1. The fish owner and the lawyer live two doors apart.
2. The purple house is immediately to the left of the tea drinker's house.
3. The coffee drinker lives next door to the dog owner.
4. The juice drinker and the white house's occupant live in neighbouring houses.
5. Milk is drunk by someone living in one of the two end houses.
6. The purple house is directly to the right of the white house.
7. The bird belongs to the coffee drinker.
8. The purple house is where the dog owner lives.
9. The cat is owned by the baker.
10. The doctor lives right beside the dog owner.
11. The green house and the red house have exactly one house between them.
12. The farmer lives immediately to the left of the purple house's occupant.
13. The green house is the middle one.
14. The green house's occupant and the horse owner are two houses apart.

## Puzzle paraphrase:zebra-00186

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- nationality: Dane, German, Brit, Swede, Spaniard
- pet: rabbit, bird, fish, dog, cat
- drink: juice, tea, milk, cocoa, coffee
- hobby: golf, painting, tennis, chess, cooking

Clues:
1. The German does not live next door to the painting enthusiast.
2. The chess enthusiast and the Spaniard live two houses apart.
3. The dog belongs to the Spaniard.
4. Painting is the hobby of the juice drinker.
5. The cooking enthusiast lives in one of the two end houses.
6. One house sits between the fish owner and the juice drinker.
7. Cocoa is what the dog owner drinks.
8. The Swede drinks tea.
9. The juice drinker and the tennis enthusiast have exactly one house between them.
10. The bird lives in house 2.
11. The German lives in one of the two end houses.
12. The milk drinker lives immediately to the left of the juice drinker.
13. The Dane and the tennis enthusiast live two houses apart.
14. The rabbit owner lives in a house with a lower number than the Swede's.
15. The chess enthusiast lives somewhere to the right of the Dane.

## Puzzle hard:zebra_hard-00074

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- job: farmer, pilot, lawyer, teacher, doctor
- pet: dog, fish, rabbit, cat, horse
- drink: coffee, milk, water, juice, tea
- nationality: Swede, Spaniard, Brit, Dane, German

Clues:
1. The lawyer and the water drinker are one and the same person.
2. The person who keeps the horse and the pilot are one and the same person.
3. The Brit and the farmer are one and the same person.
4. One of the neighbours of the teacher keeps the horse.
5. The lawyer and the Swede are one and the same person.
6. The right-hand neighbour of the person who keeps the dog keeps the rabbit.
7. One of the neighbours of the lawyer is the Spaniard.
8. One of the neighbours of the owner of the dog drinks coffee.
9. The person who keeps the cat and the coffee drinker are one and the same person.
10. One of the neighbours of the person who keeps the horse drinks coffee.
11. The farmer lives in the third house from the right.
12. The Dane and the person who drinks tea are one and the same person.
13. The pilot lives somewhere between the person who drinks juice and the person who keeps the rabbit.
14. The person who drinks milk does not live in the rightmost house.

## Puzzle plain:zebra-00097

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- hobby: cooking, golf, tennis, hiking, painting
- pet: bird, rabbit, horse, dog, fish
- nationality: Spaniard, Brit, Swede, Norwegian, German
- color: green, purple, blue, white, red

Clues:
1. The person who enjoys cooking lives in the house just left of the one where the owner of the fish lives.
2. The Brit lives in the purple house.
3. The Swede lives immediately to the right of the painting enthusiast.
4. The person who keeps the rabbit and the tennis enthusiast are not neighbours.
5. The person who keeps the bird lives somewhere to the right of the Spaniard.
6. The person who keeps the fish lives somewhere to the right of the rabbit owner.
7. The golf enthusiast either keeps the dog or keeps the fish.
8. The person in the red house lives directly to the left of the Brit.
9. The Spaniard keeps the horse.
10. The German lives in house 2.
11. The person who enjoys cooking and the person who enjoys tennis live in adjacent houses.
12. The owner of the dog lives immediately to the right of the person in the purple house.
13. The occupant of the white house lives in the house just left of the one where the cooking enthusiast lives.
14. The Norwegian lives in the green house.

## Puzzle plain:zebra-00040

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- drink: milk, coffee, cocoa, water, tea
- hobby: golf, tennis, chess, hiking, painting
- job: farmer, baker, lawyer, pilot, teacher
- nationality: Dane, German, Brit, Norwegian, Swede

Clues:
1. There is exactly one house between the Dane and the teacher.
2. The person who drinks cocoa enjoys painting.
3. The farmer and the tea drinker live in adjacent houses.
4. The Brit lives in house 2.
5. The pilot and the person who drinks tea are not neighbours.
6. The farmer enjoys chess.
7. The person who drinks cocoa is the Norwegian.
8. The Dane and the farmer live in adjacent houses.
9. The Dane lives in house 4.
10. The milk drinker lives in the house just left of the one where the person who enjoys golf lives.
11. The farmer and the lawyer live two houses apart.
12. The tea drinker lives next to the water drinker.
13. The German lives immediately to the right of the person who enjoys tennis.
14. The Norwegian lives in house 5.
15. The pilot lives in one of the two end houses.
