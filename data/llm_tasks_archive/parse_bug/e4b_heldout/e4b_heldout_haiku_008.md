# Task: solve logic puzzles

Solve each puzzle below by reasoning. Every puzzle has exactly one solution. Work carefully; you
cannot run code. Give a complete answer for every puzzle even if unsure.

Output: write a single JSON object to the file D:\Puzzle-generation-with-guaranteed-uniqueness\data\llm_tasks\e4b_heldout\e4b_heldout_haiku_008.out.json with this exact structure
{"answers": [{"id": "<puzzle id>", "answer": <answer>}, ...]}
where <answer> has the format stated for each puzzle.

The puzzles follow.


## Puzzle e4b-g1-02

Grid logic puzzle. Deduce which value of each category belongs to each house. Every value is used exactly once.

There are 6 houses in a row, numbered 1 to 6 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- hobby: chess, golf, tennis, hiking, painting, cooking
- pet: horse, fish, rabbit, cat, bird, dog
- job: teacher, pilot, lawyer, baker, farmer, doctor
- color: yellow, blue, white, purple, green, red
- nationality: Brit, Norwegian, Swede, Spaniard, Dane, German
- drink: juice, milk, cocoa, tea, coffee, water

Clues:
1. The horse owner either drinks cocoa or drinks water.
2. The farmer lives in the house just left of the one where the lawyer lives.
3. The occupant of the green house and the person who enjoys tennis are not neighbours.
4. The person in the green house works as the lawyer.
5. The Dane and the owner of the dog are neighbours.
6. There is exactly one house between the person who enjoys cooking and whoever lives in the white house.
7. There is exactly one house between the person who keeps the horse and the milk drinker.
8. The person who enjoys hiking lives immediately to the right of the doctor.
9. The cat owner lives in the house just left of the one where the teacher lives.
10. The baker keeps the dog.
11. The doctor lives immediately to the right of the dog owner.
12. The person who drinks water keeps the dog.
13. The person who enjoys golf lives directly to the left of the person who enjoys chess.
14. The person in the blue house lives in house 6.
15. The person who drinks cocoa and the person who drinks milk live two houses apart.
16. The owner of the cat and the tea drinker are neighbours.
17. Whoever lives in the green house and the Norwegian are neighbours.
18. The golf enthusiast lives at one end of the row.
19. The fish owner lives somewhere to the right of the German.
20. The occupant of the white house lives directly to the left of the juice drinker.
21. The person who drinks water lives in the yellow house.
22. The person who keeps the bird lives in the leftmost house.
23. The fish owner works as the doctor.
24. The cat owner lives in the red house.
25. The owner of the rabbit is the Swede.
26. The person in the yellow house and the person in the blue house are not neighbours.
27. The Brit lives at one end of the row.

Answer format for this puzzle: {"1": {"<category>": "<value>", ...}, "2": {...}, ...} -- one entry per house number, giving the value of every category.
