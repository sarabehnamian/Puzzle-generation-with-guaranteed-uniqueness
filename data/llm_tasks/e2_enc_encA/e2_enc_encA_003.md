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

Output: write a single JSON object to the file /home/user/Puzzle-generation-with-guaranteed-uniqueness/data/llm_tasks/e2_enc_encA/e2_enc_encA_003.out.json with this exact structure
{"puzzles": [{"id": "<puzzle id>", "constraints": [{"clue": 1, "expr": "<expression>"}, ...]}, ...]}
One entry per puzzle and exactly one constraint per numbered clue, in order. Use single quotes inside
expressions so the JSON stays valid.

The puzzles follow.


## Puzzle zebra/2/g10

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- race: Dwarf, Gnome, Human, Orc, Elf
- weapon: Axe, Staff, Sword, Spear, Bow
- mount: Boar, Wolf, Horse, Griffin, Bear
- gem: Opal, Pearl, Ruby, Onyx, Jade

Clues:
1. The Human lives in the middle house.
2. The Gnome lives directly left of the Human.
3. The Orc lives next to the Human.
4. The Elf lives somewhere to the right of the Dwarf.
5. The Sword belongs to the Human.
6. The Bow belongs to the Elf.
7. The Spear wielder lives directly left of the Elf.
8. The Gnome does not use the Axe.
9. The Horse rider wields the Sword.
10. The Bear rider wields the Bow.
11. The Griffin rider lives directly left of the Bear rider.
12. The Wolf rider lives next to the Horse rider.
13. The Ruby belongs to the Horse rider.
14. The Onyx belongs to the Orc.
15. The Pearl belongs to the Gnome.
16. The Jade owner lives somewhere to the right of the Onyx owner.

## Puzzle zebra/0/g6

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- flower: rose, tulip, lily, daisy, iris
- gem: ruby, opal, jade, onyx, pearl
- herb: basil, thyme, sage, mint, dill
- tool: saw, drill, hammer, wrench, plane

Clues:
1. The rose is in the middle house.
2. The iris is directly right of the lily.
3. The lily is in house 1 or house 2.
4. The tulip is in one of the two end houses.
5. The jade is in the rose's house.
6. The pearl is in the daisy's house.
7. The opal is in one of the two end houses.
8. The opal is somewhere to the right of the ruby.
9. The onyx is not in house 2.
10. The onyx goes with the mint.
11. The dill is directly right of the mint.
12. The basil goes with the jade.
13. The thyme goes with the opal.
14. The hammer is in the rose's house.
15. The wrench is in the tulip's house.
16. The drill goes with the sage.
17. The saw is directly right of the plane.

## Puzzle zebra/0/g9

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- name: Ravi, Lena, Omar, Greta, Kofi
- city: Oslo, Lima, Cairo, Seoul, Quito
- dish: ramen, tacos, pizza, kebab, paella
- pet: lizard, rabbit, parrot, snail, mouse

Clues:
1. Kofi lives in the middle house.
2. There is exactly one house between Omar and Ravi.
3. Omar lives somewhere to the left of Ravi.
4. Lena does not live next to Omar.
5. The Lima resident is Kofi.
6. The Oslo resident lives directly right of the Lima resident.
7. The Cairo resident lives next to the Lima resident.
8. The Seoul resident lives somewhere to the left of the Quito resident.
9. The tacos fan is from Lima.
10. The kebab fan lives next to the tacos fan but not in Ravi's house.
11. The paella lover lives next to the tacos fan.
12. The pizza fan is not from Seoul.
13. The parrot owner eats tacos.
14. The lizard owner is from Oslo.
15. The mouse owner lives next to the parrot owner.
16. The snail owner lives somewhere to the left of the rabbit owner.

## Puzzle zebra/2/g4

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- flower: Lily, Daisy, Tulip, Orchid, Rose
- bird: Swan, Robin, Finch, Owl, Crow
- tea: Oolong, Mint, Chai, Green tea, Earl Grey
- instrument: Cello, Tuba, Oboe, Lute, Banjo

Clues:
1. The lily is in the house at the far left.
2. The daisy is next to the lily.
3. The tulip is not in either end house.
4. The orchid is directly right of the tulip.
5. The rose is somewhere to the right of the orchid.
6. The crow lives in the house with the rose.
7. The finch lives in the tulip house.
8. The owl lives directly left of the crow.
9. The swan does not live next to the finch.
10. The green tea drinker keeps the owl.
11. Earl Grey is drunk directly right of the green tea.
12. The chai drinker keeps the finch.
13. The mint drinker lives directly left of the chai drinker.
14. The banjo player lives in the rose house.
15. The oboe player drinks chai.
16. The lute player lives directly right of the oboe player.
17. The tuba player drinks mint.
18. There is exactly one house between the swan and the finch.

## Puzzle zebra/2/g1

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- colour: Yellow, Green, Red, White, Blue
- pet: Fish, Dog, Bird, Cat, Horse
- drink: Milk, Tea, Coffee, Water, Juice
- job: Chef, Teacher, Doctor, Pilot, Baker

Clues:
1. The red house is in the middle of the row.
2. The green house is directly left of the red house.
3. The blue house is next to the white house.
4. The white house is somewhere to the left of the blue house.
5. The fish owner lives in the yellow house.
6. The bird owner lives in the red house.
7. The dog owner lives directly left of the bird owner.
8. The horse owner lives in the blue house.
9. The coffee drinker lives in the red house.
10. The tea drinker owns the dog.
11. The milk drinker owns the fish.
12. The water drinker lives directly left of the juice drinker.
13. The doctor drinks coffee.
14. The pilot owns the cat.
15. The baker drinks juice.
16. The teacher lives somewhere to the right of the chef.

## Puzzle zebra/3/g3

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- name: Alice, Bob, Carol, Dave, Eve
- flower: rose, tulip, lily, daisy, orchid
- instrument: piano, violin, flute, drums, guitar
- drink: tea, coffee, cocoa, soda, juice

Clues:
1. Alice lives in the middle house.
2. Bob lives at one end of the row.
3. Carol lives somewhere left of Alice.
4. Dave lives directly right of Alice.
5. There is exactly one house between Eve and Dave.
6. Alice grows daisies.
7. The orchid grower lives directly right of the daisy grower.
8. Bob grows lilies.
9. The tulip grower lives somewhere left of the rose grower.
10. The flute player grows lilies.
11. The violin player grows daisies.
12. The guitarist lives next to the flute player.
13. The drummer does not live next to the violin player.
14. The juice drinker plays the violin.
15. The coffee drinker plays the flute.
16. The orchid grower drinks soda.
17. The tea drinker is not the drummer.

## Puzzle zebra/0/g8

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- colour: ivory, navy, coral, mauve, khaki
- pet: ferret, goat, owl, gecko, pony
- music: jazz, rock, folk, blues, punk
- drink: mocha, kefir, sake, punch, broth

Clues:
1. The ivory house is directly left of the khaki house.
2. The navy house is directly right of the khaki house.
3. The coral house is not next to the mauve house.
4. The coral house is somewhere to the left of the mauve house.
5. The ferret lives in the khaki house.
6. The pony lives next to the ferret.
7. The pony does not live in the ivory house.
8. The gecko lives next to the owl.
9. The owl lives somewhere to the left of the gecko.
10. The folk fan keeps the ferret.
11. The rock fan lives directly right of the folk fan.
12. The jazz fan keeps the gecko.
13. The punk fan lives somewhere to the left of the blues fan.
14. The mocha drinker likes folk.
15. The broth drinker lives in the navy house.
16. The punch drinker likes jazz.
17. The sake drinker does not live in the coral house.

## Puzzle zebra/3/g10

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- name: Abe, Bea, Cid, Dot, Eli
- instrument: banjo, cello, harp, oboe, sitar
- snack: bagel, donut, muffin, scone, waffle
- color: azure, crimson, ebony, ivory, violet

Clues:
1. Eli lives in the middle house.
2. Bea and Dot live at opposite ends of the row.
3. Abe lives directly right of Dot.
4. Cid's house is crimson.
5. The violet house is at one end of the row, but it is not Dot's.
6. The azure house is directly right of the ivory house.
7. Abe's house is not ivory.
8. The cellist lives in the crimson house.
9. The sitar player lives in Abe's house.
10. The harpist lives at one end of the row.
11. The harpist lives somewhere left of the banjo player.
12. Bea does not play the banjo.
13. The donut is eaten by the cellist.
14. The muffin is eaten in the violet house.
15. The bagel is eaten by the sitar player.
16. The scone is not eaten by the banjo player.

## Puzzle zebra/3/g2

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- nationality: Brit, Dane, Finn, German, Swede
- car: Audi, Fiat, Mazda, Saab, Volvo
- hobby: chess, golf, rowing, tennis, fencing
- snack: nuts, chips, olives, popcorn, pretzels

Clues:
1. The Brit lives in the middle house.
2. The Dane lives at one end of the row.
3. The Swede lives next to the Brit.
4. The German does not live next to the Brit.
5. The Finn lives directly right of the Brit.
6. The Dane lives somewhere left of the German.
7. The Saab owner is the Finn.
8. The Mazda owner lives directly right of the Saab owner.
9. The Audi owner lives in the middle house.
10. The Swede does not drive the Fiat.
11. The golfer drives the Fiat.
12. The Finn is a rower.
13. The tennis player lives directly left of the rower.
14. The fencer lives next to the rower.
15. The chips eater is the tennis player.
16. The olives eater lives at one end of the row.
17. The olives eater lives somewhere left of the nuts eater.
18. The popcorn eater is the Finn.
19. The pretzels eater is not the chess player.

## Puzzle zebra/0/g3

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- name: Alice, Ben, Cara, Dev, Eve
- hobby: chess, knitting, gardening, painting, cycling
- drink: cocoa, lemonade, cider, tea, soda
- pet: parrot, rabbit, turtle, hamster, cat

Clues:
1. There is exactly one house between Cara and Eve.
2. Cara lives somewhere to the left of Eve.
3. Ben lives directly left of Eve.
4. Eve lives somewhere to the left of Alice.
5. Alice lives somewhere to the left of Dev.
6. Eve's hobby is knitting.
7. Alice plays chess.
8. The gardener lives directly right of the cyclist.
9. The knitter drinks soda.
10. The chess player drinks cider.
11. The cocoa drinker is the gardener.
12. The cyclist does not drink lemonade.
13. The parrot's owner drinks soda.
14. The turtle's owner drinks cider.
15. The cat lives next to the rabbit.
16. The rabbit's owner drinks tea.
