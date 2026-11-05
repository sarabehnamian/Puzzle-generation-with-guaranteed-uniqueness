# Task: solve logic puzzles

Solve each puzzle below by reasoning. Every puzzle has exactly one solution. Work carefully; you
cannot run code. Give a complete answer for every puzzle even if unsure.

Output: write a single JSON object to the file D:\Puzzle-generation-with-guaranteed-uniqueness\data\llm_tasks\e4b_heldout\e4b_heldout_opus_000.out.json with this exact structure
{"answers": [{"id": "<puzzle id>", "answer": <answer>}, ...]}
where <answer> has the format stated for each puzzle.

The puzzles follow.


## Puzzle e4b-g1-12

Grid logic puzzle. Deduce which value of each category belongs to each house. Every value is used exactly once.

There are 6 houses in a row, numbered 1 to 6 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- drink: juice, cocoa, milk, coffee, tea, water
- nationality: Brit, German, Norwegian, Spaniard, Dane, Swede
- pet: dog, cat, horse, fish, bird, rabbit
- color: white, purple, yellow, green, red, blue
- job: farmer, baker, teacher, pilot, lawyer, doctor
- hobby: painting, tennis, hiking, golf, chess, cooking

Clues:
1. The person who keeps the dog is the German.
2. The person who drinks water lives in the house just left of the one where whoever lives in the white house lives.
3. The Brit lives in the white house.
4. The golf enthusiast lives somewhere to the left of the tennis enthusiast.
5. The coffee drinker and the Norwegian are neighbours.
6. The teacher lives immediately to the right of the occupant of the green house.
7. The Dane lives directly to the left of the farmer.
8. There is exactly one house between the person who enjoys cooking and the occupant of the yellow house.
9. The person who drinks cocoa and the Spaniard live two houses apart.
10. The juice drinker lives in the white house.
11. The chess enthusiast does not live in house 1.
12. The Spaniard enjoys tennis.
13. The doctor lives in the red house.
14. Whoever lives in the purple house keeps the horse.
15. The Brit lives in the house just left of the one where the person in the blue house lives.
16. The owner of the bird lives in house 2.
17. The owner of the rabbit lives in the house just left of the one where the tennis enthusiast lives.
18. The Swede enjoys golf.
19. The person who drinks milk is not the Dane.
20. The teacher lives somewhere to the left of the painting enthusiast.
21. The person who keeps the bird does not live next to the fish owner.
22. The doctor and the tennis enthusiast are neighbours.
23. The person who enjoys golf either works as the farmer or works as the pilot.
24. The person in the green house works as the baker.
25. The farmer lives in the fifth house.
26. The person who enjoys tennis lives directly to the left of the cooking enthusiast.
27. The teacher lives in the white house.

Answer format for this puzzle: {"1": {"<category>": "<value>", ...}, "2": {...}, ...} -- one entry per house number, giving the value of every category.
