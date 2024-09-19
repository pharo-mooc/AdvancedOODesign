{ 
"title" : "Test-Driven Development",
"subtitle" : "",
"slidesid" : "M2S3" 
} 
 
 
# Outline 
- TDD \(Test-Driven Development\) 
- An example of TDD 
- Rethinking it 
 
# Write tests first 
- Write test **first**! Yes, yes, yes 
- "Whenever you are tempted to type something into a print statement or a debugger expression, **write it as a test instead**" - Martin Fowler 
 
# TDD is about the flow 
![](figures/TDD-workflow.pdf width=42) 
# TDD: Write your test 
- Imagine we just created the class `Counter` 
- Write a test about setting and getting a counter value 
 
``` 
CounterTest >> testCount
	| c |
	c := Counter new.
	c count: 10.
	self assert: c count equals: 10 
``` 
 
# TDD: Run your test! 
- It is red \(the test produces an error\) 
  - This is normal since we did not define the methods `count` and `count:` 
- So far so good! 
- If it is already green this is a bonus but maybe your test is not good 
- Work until your test gets green! 
 
# TDD: Rerun *all* the tests 
- **Rerun all your tests**! \(side effects, ...\) 
- Fix the broken tests 
  - Either a test is now **wrong** 
  - Or you broke something else 
  - In both cases, you should fix them 
 
# TDD: When all the tests are green 
- Commit and take a break ;-\) 
- Then, it is a good time to 
  - **Clean** and **refactor** your code if necessary 
  - and then, rerun **all** the tests 
 
# Why writing test first? 
- You specify **what** you want to get in tests \(executable specification\) 
- You think **how to build/assemble** to get the functionnality 
- You are your first client: strengthen your APIs 
- You get a **clear** context 
- You can debug on the spot 
 
# Conclusion 
- TDD is powerful 
  - Solid code base 
  - Fewer regressions 
  - Cleaner API 
- Do not miss the next lecture on XTDD 
- XTDD = **TDD on steroids**, it is gorgeous! 
