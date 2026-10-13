# Task: make fair logic puzzles harder for language-model solvers

Each puzzle below is a 5-house logic-grid puzzle with a known unique solution. A language-model
solver attempted it; its mistakes are listed. Propose 2 variants of each puzzle that you expect to
be HARDER for a language-model solver, while staying solvable by pure step-by-step deduction.

You edit puzzles with operations on the formal clue list:
- {"op": "remove", "clue": <clue number>}
- {"op": "add", "clue": {"type": <type>, "args": [...]}}
- {"op": "replace", "clue": <clue number>, "with": {"type": <type>, "args": [...]}}
Use 1 to 4 operations per variant. Clue types (a, b, c are value names; k is a house number):
  same(a,b)        a and b belong to the same person
  not_same(a,b)    a and b belong to different people
  at(a,k)          a is in house k            not_at(a,k)     a is not in house k
  left_of(a,b)     a is directly left of b    next_to(a,b)    a and b are neighbours
  not_next_to(a,b) a and b are not neighbours (they may share a house)
  before(a,b)      a is somewhere left of b   gap2(a,b)       exactly one house between a and b
  end(a)           a is in house 1 or house 5
  or(a,b,c)        a is with b or with c (b and c from the same category)
Every clue you add must be TRUE of the stated solution. A program will apply your edits, add a clue
if the result is no longer unique, and reject variants that need guessing, so focus on what makes the
deduction harder to follow (for example: fewer direct position clues, longer chains of inference,
negative and relative clues, information spread across many clues).

Output: write a single JSON object to the file /home/user/Puzzle-generation-with-guaranteed-uniqueness/data/llm_tasks/e4_mut_g1/e4_mut_g1_0.out.json with this structure
{"variants": [{"parent": "<puzzle id>", "ops": [<op>, ...], "idea": "<one short sentence>"}, ...]}
with 2 variants per puzzle.

The puzzles follow.


## Puzzle evo-g0-00

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- hobby: golf, cooking, chess, tennis, hiking
- nationality: Norwegian, Dane, Spaniard, German, Swede
- job: lawyer, baker, farmer, pilot, doctor
- color: yellow, white, purple, red, blue

Formal clues (with their English text):
1. gap2(dane, purple)   "The Dane and the occupant of the purple house live two houses apart."
2. gap2(blue, german)   "The person in the blue house and the German live two houses apart."
3. gap2(red, white)   "There is exactly one house between the occupant of the red house and whoever lives in the white house."
4. left_of(norwegian, white)   "The Norwegian lives directly to the left of the person in the white house."
5. left_of(red, tennis)   "The occupant of the red house lives directly to the left of the tennis enthusiast."
6. same(dane, golf)   "The Dane enjoys golf."
7. at(farmer, 4)   "The farmer lives in the fourth house."
8. at(doctor, 5)   "The doctor lives in the fifth house."
9. next_to(baker, purple)   "The baker and the occupant of the purple house live in adjacent houses."
10. before(yellow, swede)   "Whoever lives in the yellow house lives in a lower-numbered house than the Swede."
11. gap2(hiking, lawyer)   "The person who enjoys hiking and the lawyer live two houses apart."
12. same(chess, purple)   "The person in the purple house enjoys chess."

Solution: house 1: chess, pilot, purple, spaniard; house 2: baker, cooking, german, yellow; house 3: dane, golf, lawyer, red; house 4: blue, farmer, norwegian, tennis; house 5: doctor, hiking, swede, white
Solver mistakes: none - the solver got it fully right
Solver cell accuracy so far: 1.00

## Puzzle evo-g0-06

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- color: purple, blue, red, green, yellow
- hobby: tennis, painting, golf, hiking, cooking
- pet: horse, cat, bird, rabbit, dog
- nationality: Swede, Spaniard, Norwegian, German, Brit

Formal clues (with their English text):
1. same(bird, norwegian)   "The bird owner is the Norwegian."
2. not_next_to(golf, hiking)   "The golf enthusiast and the hiking enthusiast are not neighbours."
3. left_of(purple, dog)   "The owner of the dog lives immediately to the right of the person in the purple house."
4. or(german, cooking, hiking)   "The German either enjoys cooking or enjoys hiking."
5. gap2(cooking, swede)   "The cooking enthusiast and the Swede live two houses apart."
6. left_of(yellow, red)   "Whoever lives in the yellow house lives in the house just left of the one where the occupant of the red house lives."
7. next_to(cooking, painting)   "The cooking enthusiast and the person who enjoys painting are neighbours."
8. gap2(bird, horse)   "The person who keeps the bird and the horse owner live two houses apart."
9. left_of(spaniard, cat)   "The Spaniard lives directly to the left of the cat owner."
10. before(hiking, horse)   "The hiking enthusiast lives somewhere to the left of the owner of the horse."
11. left_of(painting, blue)   "The painting enthusiast lives in the house just left of the one where the occupant of the blue house lives."
12. left_of(german, hiking)   "The person who enjoys hiking lives immediately to the right of the German."

Solution: house 1: green, painting, rabbit, spaniard; house 2: blue, cat, cooking, german; house 3: bird, hiking, norwegian, purple; house 4: dog, swede, tennis, yellow; house 5: brit, golf, horse, red
Solver mistakes: none - the solver got it fully right
Solver cell accuracy so far: 1.00

## Puzzle evo-g0-03

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- color: blue, white, purple, green, yellow
- drink: water, cocoa, milk, coffee, tea
- nationality: Swede, German, Brit, Norwegian, Dane
- hobby: cooking, painting, chess, golf, tennis

Formal clues (with their English text):
1. same(coffee, purple)   "Whoever lives in the purple house drinks coffee."
2. left_of(yellow, cooking)   "The person who enjoys cooking lives immediately to the right of the occupant of the yellow house."
3. end(dane)   "The Dane lives at one end of the row."
4. left_of(cooking, water)   "The person who enjoys cooking lives in the house just left of the one where the water drinker lives."
5. or(chess, german, swede)   "The person who enjoys chess either is the German or is the Swede."
6. or(water, dane, swede)   "The person who drinks water either is the Dane or is the Swede."
7. at(tea, 1)   "The tea drinker lives in the leftmost house."
8. same(blue, german)   "The occupant of the blue house is the German."
9. next_to(cocoa, norwegian)   "The person who drinks cocoa and the Norwegian live in adjacent houses."
10. left_of(german, norwegian)   "The German lives in the house just left of the one where the Norwegian lives."
11. same(golf, white)   "The person who enjoys golf lives in the white house."
12. left_of(tennis, german)   "The German lives immediately to the right of the person who enjoys tennis."
13. not_next_to(coffee, milk)   "The person who drinks coffee and the milk drinker are not neighbours."

Solution: house 1: dane, painting, tea, yellow; house 2: brit, coffee, cooking, purple; house 3: green, swede, tennis, water; house 4: blue, chess, cocoa, german; house 5: golf, milk, norwegian, white
Solver mistakes: none - the solver got it fully right
Solver cell accuracy so far: 1.00

## Puzzle evo-g1-02

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- color: purple, blue, red, green, yellow
- hobby: tennis, painting, golf, hiking, cooking
- pet: horse, cat, bird, rabbit, dog
- nationality: Swede, Spaniard, Norwegian, German, Brit

Formal clues (with their English text):
1. before(hiking, horse)   "The horse owner lives somewhere to the right of the person who enjoys hiking."
2. left_of(purple, dog)   "Whoever lives in the purple house lives in the house just left of the one where the person who keeps the dog lives."
3. next_to(cooking, painting)   "The person who enjoys cooking lives next to the person who enjoys painting."
4. not_same(painting, purple)   "The person in the purple house and the person who enjoys painting are different people."
5. gap2(cooking, swede)   "There is exactly one house between the cooking enthusiast and the Swede."
6. gap2(bird, horse)   "There is exactly one house between the owner of the bird and the person who keeps the horse."
7. next_to(painting, blue)   "The painting enthusiast and the occupant of the blue house are neighbours."
8. same(bird, norwegian)   "The person who keeps the bird is the Norwegian."
9. next_to(spaniard, cat)   "The Spaniard and the cat owner live in adjacent houses."
10. left_of(german, hiking)   "The person who enjoys hiking lives immediately to the right of the German."
11. or(german, cooking, hiking)   "The German either enjoys cooking or enjoys hiking."
12. left_of(yellow, red)   "Whoever lives in the yellow house lives in the house just left of the one where the person in the red house lives."
13. not_next_to(golf, hiking)   "The person who enjoys golf does not live next to the person who enjoys hiking."

Solution: house 1: green, painting, rabbit, spaniard; house 2: blue, cat, cooking, german; house 3: bird, hiking, norwegian, purple; house 4: dog, swede, tennis, yellow; house 5: brit, golf, horse, red
Solver mistakes: none - the solver got it fully right
Solver cell accuracy so far: 1.00

## Puzzle evo-g0-01

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- pet: bird, dog, cat, rabbit, horse
- job: lawyer, pilot, doctor, teacher, baker
- color: yellow, white, blue, green, purple
- hobby: painting, hiking, tennis, golf, chess

Formal clues (with their English text):
1. gap2(pilot, white)   "There is exactly one house between the pilot and the person in the white house."
2. next_to(horse, white)   "The person who keeps the horse lives next to whoever lives in the white house."
3. same(horse, teacher)   "The horse owner works as the teacher."
4. at(bird, 1)   "The bird owner lives in house 1."
5. same(lawyer, tennis)   "The tennis enthusiast works as the lawyer."
6. gap2(green, hiking)   "There is exactly one house between whoever lives in the green house and the hiking enthusiast."
7. end(golf)   "The golf enthusiast lives in one of the two end houses."
8. or(yellow, baker, pilot)   "Whoever lives in the yellow house either works as the baker or works as the pilot."
9. or(rabbit, white, yellow)   "The owner of the rabbit either lives in the white house or lives in the yellow house."
10. same(golf, rabbit)   "The person who enjoys golf keeps the rabbit."
11. or(doctor, blue, purple)   "The doctor either lives in the blue house or lives in the purple house."
12. gap2(cat, painting)   "There is exactly one house between the person who keeps the cat and the painting enthusiast."
13. not_next_to(blue, white)   "The person in the blue house does not live next to the person in the white house."
14. gap2(blue, purple)   "There is exactly one house between whoever lives in the blue house and whoever lives in the purple house."

Solution: house 1: bird, green, lawyer, tennis; house 2: blue, cat, chess, doctor; house 3: dog, hiking, pilot, yellow; house 4: horse, painting, purple, teacher; house 5: baker, golf, rabbit, white
Solver mistakes: none - the solver got it fully right
Solver cell accuracy so far: 1.00
