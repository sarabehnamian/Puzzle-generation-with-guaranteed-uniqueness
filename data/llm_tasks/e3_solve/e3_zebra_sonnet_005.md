# Task: solve logic puzzles

Solve each puzzle below by reasoning. Every puzzle has exactly one solution. Work carefully; you
cannot run code. Give a complete answer for every puzzle even if unsure.

Output: write a single JSON object to the file D:\Puzzle-generation-with-guaranteed-uniqueness\data\llm_tasks\e3_solve\e3_zebra_sonnet_005.out.json with this exact structure
{"answers": [{"id": "<puzzle id>", "answer": <answer>}, ...]}
where <answer> has the format stated for each puzzle.

The puzzles follow.


## Puzzle zebra-00478

Grid logic puzzle. Deduce which value of each category belongs to each house. Every value is used exactly once.

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- nationality: Norwegian, Spaniard, German, Brit, Swede
- drink: cocoa, tea, juice, milk, coffee
- pet: rabbit, cat, horse, bird, fish
- job: teacher, pilot, baker, farmer, lawyer

Clues:
1. The Spaniard lives in house 5.
2. The Brit and the pilot are not neighbours.
3. The person who drinks juice lives in house 4.
4. The person who keeps the bird lives somewhere to the right of the Swede.
5. The Swede and the tea drinker live two houses apart.
6. The Brit either drinks cocoa or drinks milk.
7. The Brit does not keep the horse.
8. The bird owner works as the baker.
9. The owner of the fish lives in the house just left of the one where the horse owner lives.
10. The German lives immediately to the right of the lawyer.
11. The pilot drinks cocoa.
12. The person who keeps the cat works as the teacher.
13. The juice drinker and the milk drinker live two houses apart.
14. The horse owner and the teacher live two houses apart.
15. The person who drinks juice and the German are different people.

Answer format for this puzzle: {"1": {"<category>": "<value>", ...}, "2": {...}, ...} -- one entry per house number, giving the value of every category.
