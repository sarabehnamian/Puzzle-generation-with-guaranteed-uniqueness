# Task: solve logic puzzles

Solve each puzzle below by reasoning. Every puzzle has exactly one solution. Work carefully; you
cannot run code. Give a complete answer for every puzzle even if unsure.

Output: write a single JSON object to the file D:\Puzzle-generation-with-guaranteed-uniqueness\data\llm_tasks\e4b_heldout\e4b_heldout_sonnet_008.out.json with this exact structure
{"answers": [{"id": "<puzzle id>", "answer": <answer>}, ...]}
where <answer> has the format stated for each puzzle.

The puzzles follow.


## Puzzle e4b-g2-04

Grid logic puzzle. Deduce which value of each category belongs to each house. Every value is used exactly once.

There are 6 houses in a row, numbered 1 to 6 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- job: baker, pilot, lawyer, doctor, teacher, farmer
- hobby: tennis, cooking, hiking, painting, golf, chess
- drink: cocoa, coffee, juice, water, tea, milk
- pet: fish, rabbit, bird, cat, dog, horse
- color: green, purple, blue, yellow, red, white
- nationality: Spaniard, German, Swede, Brit, Norwegian, Dane

Clues:
1. The person who drinks water lives in house 1.
2. The person in the white house drinks juice.
3. The farmer either lives in the purple house or lives in the red house.
4. The person in the white house lives in the house just left of the one where the golf enthusiast lives.
5. The person who enjoys hiking lives somewhere to the right of the milk drinker.
6. The milk drinker keeps the bird.
7. The owner of the fish either is the Spaniard or is the Swede.
8. The cocoa drinker either enjoys chess or enjoys painting.
9. Whoever lives in the blue house is the Spaniard.
10. There is exactly one house between the pilot and the Spaniard.
11. The chess enthusiast keeps the horse.
12. Whoever lives in the red house lives at one end of the row.
13. The Dane works as the pilot.
14. Whoever lives in the yellow house lives somewhere to the left of the teacher.
15. Whoever lives in the yellow house lives in a lower-numbered house than the person who drinks cocoa.
16. The Spaniard lives in the second house.
17. The doctor lives immediately to the right of the tennis enthusiast.
18. The Brit lives in house 3.
19. The Brit and whoever lives in the purple house live two houses apart.
20. There is exactly one house between the baker and the tea drinker.
21. The milk drinker lives next to the person who enjoys tennis.
22. The person who enjoys cooking either works as the baker or works as the lawyer.
23. The German lives in a lower-numbered house than the hiking enthusiast.
24. The person who keeps the cat and the person who drinks coffee are not neighbours.
25. The person who enjoys chess lives in the green house.
26. The occupant of the yellow house keeps the dog.
27. The golf enthusiast does not live in the yellow house.
28. The teacher does not live in house 1.
29. The Dane and the Norwegian live two houses apart.
30. The lawyer is the Swede.

Answer format for this puzzle: {"1": {"<category>": "<value>", ...}, "2": {...}, ...} -- one entry per house number, giving the value of every category.
