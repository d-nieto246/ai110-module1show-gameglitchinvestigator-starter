# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the secret number kept changing" or "the hints were backwards").

When I first ran the game, it appeared as a basic Streamlit app gas a "guessing number" game, but it contained multiple bugs that made it unplayable. The difficulty ranges were backwards, with Normal set to 1-100 and Hard to 1-50, instead of the expected Normal being 1-50 and Hard 1-100 (this is not technically a bug, but the programmer just had it backwards). During gameplay, the hints were completely wrong; for instance, guessing 40 in a 1-50 range prompted me to go lower, yet the secret number turned out to be 41 after several attempts. The New Game button failed to reset the game properly, always keeping the range at 1-100 regardless of difficulty selection and not updating the attempt limits, making every offered setting ineffective to use.

Gitch found: A normal difficulty uses 1-100, a larger range while Hard uses 1-50, which feels counterintuitive since Hard should be harder with a bigger range. The underlying logic was that it was set incorrectly in app.py's "get-range-for-difficulty" function, the ranges are set backwards for Normal and Hard, but also includes an unnecessary return statement returning a default of a range from 1, 100 at the end of the function.

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

I used Copilot about 95% of the time and Claude for the remaining handful of questions; Copilot helped me fix the core game logic so that when I guessed a number the game correctly told me whether I was too low or too high and it respected the chosen difficulty range rather than sending me out-of-bounds. One thing I got wrong at first was the attempt counter: the app still only decremented “Attempts left” after the second guess instead of immediately on the first guess, and we verified that by actually playing the game and watching the counter not drop until after the second input.
---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

I decided a bug was really fixed by verifying the behavior both in code (via pytest) and in the running Streamlit app; if the behavior matched the intended rules (correct hints, correct range, attempts counting down properly) then it was fixed. One test I ran was the pytest suite that checks "check_guess()" returns the right outcome and hint message, which proved the core game logic was correct, and I also played the game in the UI to confirm the attempt counter and range were behaving as expected. AI helped me design the unit tests by suggesting the key cases to cover (win/too high/too low) and pointing out that the function should return a tuple of (outcome, message), which guided how I wrote the assertions.

---

## 4. What did you learn about Streamlit and state?

- In your own words, explain why the secret number kept changing in the original app.
- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
- What change did you make that finally gave the game a stable secret number?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
