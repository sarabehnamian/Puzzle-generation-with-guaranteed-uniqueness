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

Output: write a single JSON object to the file /home/user/Puzzle-generation-with-guaranteed-uniqueness/data/llm_tasks/e4_mut_g0/e4_mut_g0_1.out.json with this structure
{"variants": [{"parent": "<puzzle id>", "ops": [<op>, ...], "idea": "<one short sentence>"}, ...]}
with 2 variants per puzzle.

The puzzles follow.


## Puzzle evo-g0-04

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- job: lawyer, doctor, pilot, teacher, baker
- pet: cat, dog, bird, horse, fish
- hobby: chess, golf, cooking, tennis, hiking
- color: white, yellow, purple, red, green

Formal clues (with their English text):
1. left_of(horse, cat)   "The cat owner lives immediately to the right of the owner of the horse."
2. same(chess, red)   "The person who enjoys chess lives in the red house."
3. at(yellow, 5)   "The person in the yellow house lives in the fifth house."
4. at(baker, 4)   "The baker lives in house 4."
5. next_to(bird, lawyer)   "The owner of the bird and the lawyer are neighbours."
6. same(bird, hiking)   "The bird owner enjoys hiking."
7. left_of(pilot, cat)   "The pilot lives directly to the left of the person who keeps the cat."
8. end(cooking)   "The person who enjoys cooking lives at one end of the row."
9. gap2(chess, doctor)   "There is exactly one house between the chess enthusiast and the doctor."
10. or(purple, hiking, tennis)   "Whoever lives in the purple house either enjoys hiking or enjoys tennis."
11. next_to(purple, white)   "Whoever lives in the purple house and the person in the white house are neighbours."
12. before(cooking, cat)   "The person who keeps the cat lives somewhere to the right of the person who enjoys cooking."
13. next_to(horse, tennis)   "The horse owner lives next to the person who enjoys tennis."
14. or(dog, cooking, hiking)   "The person who keeps the dog either enjoys cooking or enjoys hiking."

Solution: house 1: cooking, dog, lawyer, white; house 2: bird, hiking, purple, teacher; house 3: chess, horse, pilot, red; house 4: baker, cat, green, tennis; house 5: doctor, fish, golf, yellow
Solver mistakes: none - the solver got it fully right
Solver cell accuracy so far: 1.00

## Puzzle evo-g0-05

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- hobby: golf, painting, tennis, cooking, hiking
- nationality: Norwegian, Swede, German, Spaniard, Dane
- color: red, green, blue, yellow, white
- drink: cocoa, water, tea, milk, juice

Formal clues (with their English text):
1. left_of(cocoa, red)   "The person who drinks cocoa lives directly to the left of whoever lives in the red house."
2. next_to(dane, german)   "The Dane lives next to the German."
3. or(tea, red, white)   "The tea drinker either lives in the red house or lives in the white house."
4. left_of(swede, milk)   "The Swede lives in the house just left of the one where the milk drinker lives."
5. same(golf, water)   "The golf enthusiast drinks water."
6. next_to(german, red)   "The German and the occupant of the red house are neighbours."
7. left_of(dane, yellow)   "The Dane lives in the house just left of the one where the person in the yellow house lives."
8. same(painting, swede)   "The Swede enjoys painting."
9. not_next_to(golf, juice)   "The person who enjoys golf does not live next to the juice drinker."
10. same(norwegian, tennis)   "The Norwegian enjoys tennis."
11. left_of(blue, yellow)   "The person in the blue house lives directly to the left of whoever lives in the yellow house."
12. before(white, hiking)   "Whoever lives in the white house lives somewhere to the left of the person who enjoys hiking."
13. left_of(painting, cooking)   "The painting enthusiast lives in the house just left of the one where the person who enjoys cooking lives."
14. next_to(german, painting)   "The German and the painting enthusiast are neighbours."

Solution: house 1: norwegian, tea, tennis, white; house 2: blue, dane, golf, water; house 3: cocoa, german, hiking, yellow; house 4: juice, painting, red, swede; house 5: cooking, green, milk, spaniard
Solver mistakes: none - the solver got it fully right
Solver cell accuracy so far: 1.00

## Puzzle evo-g0-07

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- drink: coffee, water, milk, cocoa, juice
- pet: cat, horse, bird, dog, fish
- hobby: tennis, painting, cooking, hiking, chess
- color: red, purple, green, blue, white

Formal clues (with their English text):
1. left_of(purple, tennis)   "Whoever lives in the purple house lives directly to the left of the tennis enthusiast."
2. gap2(bird, fish)   "There is exactly one house between the owner of the bird and the fish owner."
3. not_next_to(milk, painting)   "The person who drinks milk does not live next to the person who enjoys painting."
4. before(tennis, dog)   "The owner of the dog lives somewhere to the right of the person who enjoys tennis."
5. gap2(bird, red)   "There is exactly one house between the owner of the bird and the occupant of the red house."
6. at(green, 4)   "Whoever lives in the green house lives in house 4."
7. gap2(horse, white)   "The owner of the horse and the occupant of the white house live two houses apart."
8. before(cat, coffee)   "The person who drinks coffee lives somewhere to the right of the cat owner."
9. at(cooking, 5)   "The cooking enthusiast lives in the last house."
10. at(juice, 2)   "The juice drinker lives in the second house."
11. end(coffee)   "The coffee drinker lives in one of the two end houses."
12. same(blue, cocoa)   "The cocoa drinker lives in the blue house."
13. same(bird, chess)   "The owner of the bird enjoys chess."
14. left_of(hiking, fish)   "The person who enjoys hiking lives directly to the left of the fish owner."

Solution: house 1: cat, hiking, milk, purple; house 2: fish, juice, red, tennis; house 3: blue, cocoa, horse, painting; house 4: bird, chess, green, water; house 5: coffee, cooking, dog, white
Solver mistakes: none - the solver got it fully right
Solver cell accuracy so far: 1.00
