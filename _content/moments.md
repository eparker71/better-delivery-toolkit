<!--
Everyday Moments: small moments in the working day, and what each can teach.

The aim is not to hand over the answer. It's to show the idea underneath and a few different ways teams handle it, so that
people adapt one to their own situation, change it, or invent a way that isn't listed.

To add a moment, copy one of the entries below into the file and edit it. Keep to this shape:

## The moment, in a few words
Event: one of Daily, Planning & refinement, Review & demo, Retro, Board & flow, Estimates & forecasts, Stakeholders & reports, Releases & quality, Team & conflict, Working with AI
You'll notice: what people see or hear (one line)
What's going on: the idea underneath, in plain words: why it happens and what it costs (at most 60 words)
Ways to try:
- A way teams handle it (at most 25 words)
- A different kind of way: change the format, the focus or the channel, not just the wording
- A third way, different again (two to four ways in all)
What if: one question that changes a condition, so people have to adapt the ideas (one line)
Tools: Tool Name, Another Tool Name
Spot it: the short label of an anti-pattern in anti-patterns.html (optional)
Bigger version: the title of a scenario in scenarios.md (optional)
Prompt: the id of a prompt in the Prompt Library (optional)

The ways should differ in kind, not be three versions of one idea. Write for anyone on the team: plain words, no jargon,
and keep it to the team, never an individual. The page adds the closing questions ("Which would fit your team? What would
you change? What's a way nobody here has tried?").
Tool names must match the toolkit's tool titles (see start-here-by-role.html). Then run: python3 _generator/build_all.py
-->

## Stand-up runs long
Event: Daily
You'll notice: People give updates one by one, others check their phones, and it passes 15 minutes.
What's going on: A meeting built around people reporting in turn tells you who did what, not how the work is going. Most updates don't affect most listeners, so attention drops, and the real problems wait until afterwards. The question is what the meeting is for.
Ways to try:
- Walk the board from the right-hand column, asking of each item what would get it finished today.
- Talk only about what's blocked or at risk, and skip anything that's going fine.
- Swap the meeting for a short written update for a week, then see what people missed.
What if: Half the team were in another time zone, or twice as many people came?
Tools: Daily Sync, Kanban Board Design
Spot it: Daily sync is a status report
Prompt: standup

## "It's just a quick change"
Event: Planning & refinement
You'll notice: A small request arrives in chat or at the desk, and it's already half done by the time anyone writes it down.
What's going on: Work that isn't written down can't be counted, so it can't be planned for. Each favour looks free, but together they use the time the team planned for something else. Until the interruptions are visible, the plan quietly stops being true, and nobody knows why.
Ways to try:
- Put every interruption on the board as a card for a week, with who asked and how long it took.
- Agree a weekly allowance of time for requests: say yes while it lasts, and "next week" once it's used.
- Send requests through one place, such as a channel or a form, so they can be seen and put in order.
What if: The person asking is a senior leader, or a customer you can't say no to?
Tools: Buffering & Swarming, Kanban Board Design
Spot it: Unplanned work wrecks plans
Bigger version: Urgent work keeps interrupting the iteration

## A ticket has sat in review for days
Event: Board & flow
You'll notice: A card stays in "In review" or "Waiting" for days, and everyone assumes someone else is on it.
What's going on: Waiting is usually where most of the time goes, and a card's age shows trouble while there's still time to act. People often prefer starting something new to finishing something nearly done, so the reviews wait.
Ways to try:
- Sort the board by age each morning, and swarm on the oldest card before starting anything new.
- Limit how much can wait for review, so that starting something new means clearing something first.
- Agree a time, such as two working days, after which a waiting item is raised with the whole team.
What if: The reviewers are in a different team, or only one person is able to review?
Tools: Ageing WIP & SLE, Blocker Clustering
Spot it: Blocked work goes unnoticed
Bigger version: Lots of work is started but little is finished
Prompt: blockers

## The estimate gets challenged
Event: Estimates & forecasts
You'll notice: "How long will it take?" is answered with a number, then comes a tense "Can't you do it faster?"
What's going on: An estimate is a guess made with the least information you'll ever have, and pushing on it tends to make it padded or false. The useful part is what the guess assumes. Sharing the assumptions turns an argument about the number into a conversation about the work.
Ways to try:
- Give two numbers and one reason, such as "3 to 6 days, depending on whether the data is ready".
- Say what you'd need to know to narrow it, and offer to find that out first.
- Show how long similar work took before, and let the history make the point.
What if: Nothing like this has been done before, so there's no history to point to?
Tools: Estimation, Release Forecast & Burn-up
Spot it: Single-date promises
Bigger version: Leadership wants a single delivery date

## The same actions come up at every retro
Event: Retro
You'll notice: The sticky notes could have been written last month, and last month's actions aren't mentioned.
What's going on: A retro's value lies in what changes afterwards. Actions with no owner, no date and no way of telling whether they worked fade away, and then people stop believing retros matter. A few small changes that get followed up teach more than a long list.
Ways to try:
- Pick one action, give it an owner, and ask about it at the next stand-up before anything else.
- Turn it into a small experiment with a measure and an end date, such as "try this for two weeks".
- Review last time's actions first at the next retro, and add no new ones until you have.
What if: The cause of the problem is outside the team's control?
Tools: Retrospective Kit, 1% Experiment Canvas
Spot it: Same issues at every retro
Bigger version: Retrospectives have gone stale
Prompt: retro-fresh

## The status is green until it's suddenly red
Event: Stakeholders & reports
You'll notice: Reports say green for weeks, then a date is missed with no warning.
What's going on: People hold back bad news until they can bring a fix, and a colour says nothing about trouble building. What shows drift early is the trend and the assumptions behind it. It has to be safe to say "at risk" before it's late.
Ways to try:
- Report where you are against the outcome, the forecast as a range, and the one decision you need.
- Add "what would make this amber?" to every report, and say what would turn it.
- Show the trend across the last few reports, not just a snapshot.
What if: The reader only wants a colour, or reacts badly to amber?
Tools: Outcome Status Report, RAID Log
Spot it: Green until suddenly red
Bigger version: The steering group wants traffic-light status
Prompt: status

## Nobody asks questions at the demo
Event: Review & demo
You'll notice: The team shows what it built, people nod, and the only questions are about the date.
What's going on: A demo that only goes one way gets no feedback, and feedback is the point of the meeting. People ask better questions when they've tried the work and know what you want to learn. A review should change what happens next, not just show what happened.
Ways to try:
- Open with the one question you most want answered, and let a stakeholder use the work while you watch.
- Replace the demo with a hands-on session: stakeholders try it, and the team takes notes.
- Send a short recording beforehand, and use the meeting only for questions and decisions.
What if: The stakeholders are senior, remote, or hard to get hold of?
Tools: Sprint Review, Stakeholder Map
Spot it: Review is a one-way demo
Bigger version: Stakeholders don't come to the review
Prompt: review

## Someone pastes AI output that nobody checked
Event: Working with AI
You'll notice: A confident summary, plan or piece of code appears in the chat or a pull request, and nobody can say where it came from.
What's going on: AI writes fluent text that is sometimes wrong, and fluent text feels trustworthy. When nobody owns checking it, mistakes travel further, and the person who shared it may not be able to explain it. The question is who is accountable for what gets used, and how that shows.
Ways to try:
- Add a line to whatever you share, saying what you checked and what you changed.
- Agree which kinds of work AI can draft, and which always need a second person to read them.
- Ask the AI to show its sources or reasoning, then check the parts that matter most.
What if: The output is code, or a number that goes into a report for leadership?
Tools: AI Working Agreement, AI in Delivery
Bigger version: The team is asked to start using AI tools

## Releasing makes everyone nervous
Event: Releases & quality
You'll notice: Releases are planned for evenings or weekends, and people stand by "just in case".
What's going on: Nervousness about releasing usually means releases are large, rare and hard to undo. Each change waits longer, so the next release is bigger and the worry grows. The way out is to make each release smaller, easier to undo, or less visible to users.
Ways to try:
- Ask "how would we undo this, and have we tried?" before each release, and practise the way back once.
- Release smaller pieces more often, so a failure has fewer places to hide.
- Release behind a switch, so it can go to a few people first and be turned off quickly.
What if: There's a fixed release window you can't change, or a regulator involved?
Tools: Release Readiness & Strategy, Continuous Delivery Health Check
Bigger version: Releases are slow, scary and happen late at night
Prompt: release

## Someone goes quiet after being talked over
Event: Team & conflict
You'll notice: One person stops contributing after being interrupted or having an idea dismissed, and the meeting moves on.
What's going on: When an idea is shut down in public, people learn to keep quiet, and the team loses what they know. It rarely feels like a big moment, but it adds up. How a meeting is run can make it easier or harder for quiet people to contribute.
Ways to try:
- Ask everyone to write their view first, silently, and read the views out before any discussion.
- Go round in turn, and ask the most talkative person to go last.
- Check in privately afterwards with something open, such as "what did you make of that?"
What if: The team is remote, or the person who talks over others is senior?
Tools: Facilitation Techniques, Psychological Safety Check
Spot it: Quiet voices go unheard
Bigger version: Someone was shut down or embarrassed in a meeting

## Tickets get updated just before the stand-up
Event: Daily
You'll notice: The board is quiet all day, then everything moves in the five minutes before the meeting.
What's going on: When the board is updated for the meeting rather than for the work, it records the past instead of guiding the present. The update becomes a chore done for someone else, and people stop trusting what the board says.
Ways to try:
- Use the board during the meeting itself, and update cards live as the team talks.
- Agree the one or two moves that matter, such as "started" and "finished", and drop the rest.
- Ask what the board would need to show for the team to want to use it.
What if: The tool is set up by another team and you can't change it?
Tools: Daily Sync, Jira Cheat Sheet
Bigger version: Developers don't keep Jira up to date

## The stand-up turns into a long discussion
Event: Daily
You'll notice: Two people go deep on a problem while everyone else waits.
What's going on: A short meeting for the whole team is a poor place for a discussion that needs only two people. Everyone pays for it, the other topics get squeezed, and people learn to dread the meeting. The skill is noticing the moment and moving the conversation.
Ways to try:
- Keep a visible "parking lot" list, and agree who stays behind to talk about each item.
- Ask "who needs to be part of this?" and let everyone else leave when they can.
- Set a timer for each card, and ask whether to continue or move on when it rings.
What if: The two people are the most senior ones in the room?
Tools: Daily Sync, Facilitation Techniques
Spot it: Meetings have no clear purpose

## Everyone says there are no blockers
Event: Daily
You'll notice: "No blockers" every day, yet work still waits and dates slip.
What's going on: People often don't call something a blocker until it's serious, or they see waiting as normal. A question like "any blockers?" is easy to answer no to. Asking about work that has stopped moving finds problems earlier.
Ways to try:
- Ask of each card, "when did this last move?", and talk about the ones that haven't.
- Keep a visible list of things slowing work down, whether or not anyone calls them blockers.
- Count the days waiting at the end of each week, and look at the biggest number.
What if: People worry that naming a blocker makes them look weak?
Tools: Impediments Board, Blocker Clustering
Spot it: Blocked work goes unnoticed
Prompt: blockers

## The iteration starts without a goal
Event: Planning & refinement
You'll notice: The plan is a list of items, and nobody can say in one sentence what it's for.
What's going on: Without a goal, every item is equally important, and the team can't make trade-offs when something changes. A goal gives the team a reason to choose, to say no, and to know whether it succeeded. It doesn't have to be grand.
Ways to try:
- Finish the sentence "By the end of this iteration, a user can…" before choosing items.
- Ask what you'd show a stakeholder if you could only show one thing.
- Pick the item that would hurt most if it slipped, and build the goal around it.
What if: The work is mostly support or bug fixing, with no obvious theme?
Tools: Sprint Planning, Backlog Refinement
Spot it: Planning has no goal
Bigger version: The team missed its sprint goal
Prompt: goal

## A story is much bigger than anyone expected
Event: Planning & refinement
You'll notice: A story that looked small has been "nearly done" for a week, and keeps growing.
What's going on: Size hides in what nobody asked about. A story feels small until someone finds the unknown rule, the awkward edge case or the system it touches. Talking through examples before starting brings these out while they're cheap to deal with.
Ways to try:
- Before starting, write three concrete examples of how it should behave, and see what questions they raise.
- Split by the thinnest slice a user could use, not by technical layer.
- Time-box an investigation first, and size the story afterwards.
What if: The work is research, or a new technology nobody has used?
Tools: Story Splitting, Example Mapping
Spot it: Stories keep carrying over
Bigger version: Stories keep turning out bigger than expected
Prompt: split

## Everything is top priority
Event: Planning & refinement
You'll notice: Every request comes marked urgent, and the list has no clear order.
What's going on: If everything is first, nothing is. Without an order, the loudest voice wins and the team can't say no. Choosing needs a shared way of comparing options, such as cost of delay, so that the argument is about value, not volume.
Ways to try:
- Ask for the cost of delay: what does each week of waiting cost, and who is hurt?
- Force a single ranking, with only one item allowed in the top spot.
- Let the requesters rank their items together, in the same room, and watch what changes.
What if: The people asking are your customers, or someone who sets your pay?
Tools: Prioritisation Board, Stakeholder Map
Spot it: Everything is top priority
Bigger version: Nobody can agree what to build next
Prompt: rank

## It's "done", but nobody can use it yet
Event: Review & demo
You'll notice: A story is marked done, then reopened because it wasn't tested, deployed or usable.
What's going on: "Done" can mean "I've finished my part" or "someone can use it". When the word means different things to different people, work comes back and everyone is surprised. A shared definition makes the finish line the same for everyone.
Ways to try:
- Write down what "done" means as a short checklist, and check items against it in the meeting.
- Add the last step as a column on the board, so unfinished work is visible.
- Ask the next person in line what they'd need to call it done, and write that down.
What if: Different parts of the work need different standards, such as a prototype and a live service?
Tools: Backlog Item Anatomy, Team Charter
Spot it: "Done" means dev done

## A stakeholder asks for something new at the review
Event: Review & demo
You'll notice: Right after the demo, someone says "can we also add…?" and the room nods.
What's going on: New ideas at a review show people are engaged, but taking them on without a trade-off quietly adds to the plan. The skill is to welcome the idea and make its cost visible, so the choice is shared rather than assumed.
Ways to try:
- Write it on the backlog on the spot, and say when it will be ranked against everything else.
- Ask what they'd swap out of the current plan to make room for it.
- Ask what problem it would solve, since the answer is sometimes smaller than the request.
What if: The person asking has the authority to simply tell you what to do?
Tools: Sprint Review, Prioritisation Board
Bigger version: Stakeholders keep adding work mid-iteration

## Nobody can say whether the last release helped
Event: Review & demo
You'll notice: Features ship and the team moves on, and later nobody knows whether users noticed.
What's going on: Shipping tells you that something was built, not that anything improved. Without a measure chosen before release, there's nothing to compare against afterwards, and the team can't learn whether its guesses were right.
Ways to try:
- Before building, write down what you expect to change and how you'd see it.
- Pick one number to look at a few weeks after release, and put the date in the calendar.
- Ask five users what changed for them, and compare that with the numbers.
What if: Nothing about the product can be measured directly yet?
Tools: Value Metrics, Product Bet Canvas
Bigger version: Users aren't using what we built

## Only a few people speak at the retro
Event: Retro
You'll notice: The same two or three people fill the board, and the rest wait for the end.
What's going on: A retro only shows what the people who speak are willing to say. Quiet people often see different problems, and they're also the least likely to raise them. How you collect ideas shapes what you get back more than the questions you ask.
Ways to try:
- Write ideas silently on stickies first, then share them, so nobody is swayed before they've written.
- Run a short anonymous check before the retro, and discuss only the result.
- Split into pairs or threes to talk first, then bring the best ideas to the group.
What if: The team is remote, or a manager is in the room?
Tools: Retrospective Kit, Facilitation Techniques
Spot it: Quiet voices go unheard
Bigger version: Retrospectives have gone stale

## The retro turns into a complaint session
Event: Retro
You'll notice: A list of things that annoy people, with no sense of what to do about any of them.
What's going on: Venting feels useful, and sometimes is, but complaints rarely lead to change on their own. Moving from what annoys us to why it happens, and then to what we could try, changes the energy. A cause is something you can act on; a complaint isn't.
Ways to try:
- Pick the top item and ask "why?" five times, to find a cause the team could act on.
- Sort items by who could act: the team, someone else, or nobody. Work on the first group.
- Turn each complaint into a question that begins "how might we…?"
What if: Most of the problems are caused by another team?
Tools: Root Cause Analysis, Retrospective Kit
Prompt: whys

## A problem comes up that the team can't fix
Event: Retro
You'll notice: The same issue appears at every retro, and the answer is always "that's up to someone else".
What's going on: Some problems sit outside the team's control, and carrying them in silence uses up goodwill. The team can still choose what to do: raise it with evidence, change how they work around it, or accept it knowingly. What doesn't help is pretending it isn't there.
Ways to try:
- Count what the problem costs the team each week, and take that number to whoever can act.
- Raise it in a cross-team forum, such as a joint retro, so it's no longer one team's complaint.
- Agree a workaround for now, and write down what would have to change to remove it.
What if: The person who could fix it doesn't think it's a problem?
Tools: Impediments Board, Cross-Team Retro
Bigger version: The same cross-team problem repeats every quarter

## Everyone is busy, but nothing finishes
Event: Board & flow
You'll notice: The board is full, people are working hard, and little reaches done.
What's going on: Starting is easier than finishing, so work in progress grows. Every extra item slows all the others, because people switch between them and things wait. Fewer things in flight at once usually means each finishes sooner, even though it feels slower.
Ways to try:
- Set a limit on how many items can be in progress, and stop starting when you reach it.
- Finish from the right: each day, ask what can move to done before anything new is started.
- Compare how many items are in progress with how many people there are, and discuss the ratio.
What if: Most of the work is waiting on other people?
Tools: Kanban Board Design, Ageing WIP & SLE
Spot it: Too much work in progress
Bigger version: Lots of work is started but little is finished
Prompt: wip

## The board doesn't look like how we work
Event: Board & flow
You'll notice: Cards jump columns, skip steps or sit in "Other", and people explain what they "really" mean.
What's going on: A board that doesn't match the real flow hides the places where work waits. When the columns are a guess, nobody can see the queues or the hand-offs. Drawing the real path, even roughly, shows where the time goes.
Ways to try:
- Follow three finished cards backwards, noting every step and wait, and redraw the columns from what you find.
- Ask each role where work comes in and goes out, and mark those hand-offs on the board.
- Add one column for the place where work waits longest, and see what happens.
What if: Different kinds of work follow different paths?
Tools: Kanban Board Design, Value Stream Map

## Only one person knows how to do that
Event: Board & flow
You'll notice: A task waits until a particular person is free, and everyone says "only they know that part".
What's going on: When knowledge sits with one person, the team's speed depends on their calendar, and their leaving or illness becomes a crisis. It's tiring for them, too. Knowledge spreads when people work on it together, not when it's written down alone.
Ways to try:
- Pair on the next piece of that work, with the expert explaining as they go.
- Make a simple map of who can do what, and look at the gaps together.
- Rotate who takes the hard task, with a more experienced person on call.
What if: The expert is too busy to teach, or doesn't want to share?
Tools: Skills Matrix, Pairing & Mobbing
Spot it: Single point of failure
Bigger version: A key person is leaving

## Velocity is being used as a target
Event: Estimates & forecasts
You'll notice: "Can you go faster this iteration?" or a chart comparing teams' points.
What's going on: Velocity is a team's own way of planning, and it only works when it's honest. Once it's a target, the points get bigger and the number goes up without anything improving. Measures easily turn into goals, and then stop measuring the thing they were meant to.
Ways to try:
- Use velocity only to plan the next iteration, and never show it outside the team.
- Count finished items instead of points, and look at the range over several iterations.
- Ask the person who wants it faster what outcome they're really after.
What if: A manager needs a number to report upwards?
Tools: Estimation, Delivery Metrics at a Glance
Spot it: Velocity as a target

## We keep finishing later than we said
Event: Estimates & forecasts
You'll notice: Dates slip a little each time, and the next forecast is always optimistic.
What's going on: Forecasts based on hopes miss for the same reasons each time: unplanned work, work that grows, and waiting. What actually happened tells you more about the future than the plan does. The pattern in your misses is useful information.
Ways to try:
- Compare the last several forecasts with what happened, and look for the common cause.
- Forecast from how many items the team has really finished per week, as a range.
- Size a buffer from your real unplanned work, instead of a guessed percentage.
What if: The work is different each time, so history is a poor guide?
Tools: Release Forecast & Burn-up, Buffering & Swarming
Bigger version: The deadline has just been moved earlier

## "Are we on track?"
Event: Estimates & forecasts
You'll notice: A simple question that's hard to answer, and each answer gets a different reaction.
What's going on: "On track" depends on what you're tracking against: a date, a scope or an outcome. Different people hear different things in the same answer. Naming what you're measuring against, and showing how confident you are, makes the answer more honest and the conversation more useful.
Ways to try:
- Answer with three things: where we are, the likely finish as a range, and what could change it.
- Show a burn-up chart, so scope and progress are on the same picture.
- Ask what decision the asker needs to make, and answer that.
What if: The asker wants a plain yes or no?
Tools: Release Forecast & Burn-up, Outcome Status Report
Prompt: status

## A senior stakeholder keeps changing the priorities
Event: Stakeholders & reports
You'll notice: A new top priority arrives most weeks, usually after a conversation in the corridor.
What's going on: Changes in priority usually signal something real: a pressure the stakeholder feels, or information the team doesn't have. The cost of each change is often invisible to them. Making the cost visible, and understanding the pressure, tends to help more than resisting.
Ways to try:
- Show what the change displaces, so the trade-off is on the table.
- Ask what's driving it, and see whether a smaller response would meet that need.
- Agree a regular time to review priorities, so changes are gathered instead of arriving daily.
What if: They decide your team's budget?
Tools: Stakeholder Map, Prioritisation Board
Bigger version: A senior stakeholder keeps overriding priorities

## Nobody reads the report
Event: Stakeholders & reports
You'll notice: Reports go out on time and nobody replies, or questions only arrive when something's wrong.
What's going on: A report that nobody acts on is a cost with no benefit. It often answers questions the reader doesn't have, in a form that takes effort to use. The way to change it is to ask what the reader does with it, and write for that.
Ways to try:
- Ask two readers what they do with the report, and cut anything that doesn't support it.
- Open with the decisions you need, and put the detail underneath.
- Replace it for a month with a short conversation, and see what's missed.
What if: The report is required by a process you don't control?
Tools: Outcome Status Report, Stakeholder Map
Prompt: status

## A risk is mentioned in passing
Event: Stakeholders & reports
You'll notice: Someone says "that could be a problem" in a meeting, and it never reaches a list.
What's going on: The people closest to the work notice risks early, but only if there's somewhere to put them. When there isn't, they stay as remarks and are rediscovered later as problems. Writing a risk down turns a worry into something the team can decide about.
Ways to try:
- Capture it on the spot on a shared list, with a name against it and a date to look again.
- Run a short "imagine it has failed" session, and list the reasons people give.
- Ask each person for one worry at the start of every iteration.
What if: People think naming a risk means they'll be blamed for it?
Tools: RAID Log, Pre-mortem
Prompt: premortem

## A bug reaches production
Event: Releases & quality
You'll notice: A user finds a fault the team knew nothing about, and a fix is rushed out.
What's going on: Every escaped bug shows where the team's checks have a gap. The first response is to fix it quickly. The second chance is to ask where it could have been caught earlier, and that question improves the next hundred changes, not just this one.
Ways to try:
- After the fix, ask at which earlier step it could have been caught, and add a check there.
- Write the failing example as a test first, so it can't come back unnoticed.
- Look at the last five escaped bugs together, and see what they have in common.
What if: There's no time to ask, because the fix is urgent?
Tools: Test Strategy, Blameless Incident Review
Bigger version: Bugs keep reaching production
Prompt: tests

## Something breaks and everyone asks who did it
Event: Releases & quality
You'll notice: The first question after a failure is who changed it.
What's going on: Looking for someone to blame ends the learning. People protect themselves, details get softer, and the next failure arrives with less warning. Asking how the system let it happen finds causes that can be fixed, and makes it safer to speak up next time.
Ways to try:
- Write a timeline of what happened and what each person knew at the time, before discussing causes.
- Ask "why did that make sense at the time?" of every decision in the story.
- List what made the mistake easy, and fix one thing in the system.
What if: A customer or a senior leader is demanding a name?
Tools: Blameless Incident Review, Psychological Safety Check
Bigger version: People hide mistakes until it's too late
Prompt: incident

## The same manual steps at every release
Event: Releases & quality
You'll notice: A checklist of fiddly steps that someone follows, carefully, each time.
What's going on: Manual steps are slow and easy to get wrong, and they're often done by the people who know most. They survive because each one is small. Listing them shows which could be automated, removed, or made safe some other way.
Ways to try:
- Time each step at the next release, and automate the one that takes longest or goes wrong most.
- Ask of each step what it protects, and whether something else already does that.
- Swap the order of the steps, or who does them, to find the ones that really matter.
What if: The steps are required by an audit or compliance rule?
Tools: Delivery Pipeline Canvas, Continuous Delivery Health Check
Bigger version: Releases are slow, scary and happen late at night

## Two people disagree and it goes round in circles
Event: Team & conflict
You'll notice: The same argument returns, each side repeating a point, and the others stay quiet.
What's going on: Disagreements often continue because people are arguing about different things: facts, goals or values. Until it's clear what's being argued, repeating the point doesn't help. Slowing down to find what each person is trying to protect often changes the conversation.
Ways to try:
- Ask each person to describe the other's view until both agree it's fair, before replying.
- Write down what each side is trying to achieve, and look for a goal they share.
- Agree what evidence would change each person's mind, and go and get it.
What if: The disagreement is really about who has the final say?
Tools: Levels of Conflict, Facilitation Techniques
Bigger version: Two team members are in open conflict

## A new person asks why we do it this way
Event: Team & conflict
You'll notice: A newcomer asks a simple question, and the honest answer is "I'm not sure".
What's going on: Fresh eyes notice habits the team stopped seeing. Some exist for good reasons, and some are leftovers. The question is a chance to find out which, and to write the reasons down so the next person doesn't have to ask.
Ways to try:
- Say thank you, and find out why together, rather than defending it.
- Keep a list of "things we do, and why", and add to it each time someone asks.
- Ask newcomers for their first-week questions on purpose, and review them at a retro.
What if: The person asking is more senior than you, or rarely speaks up?
Tools: Team Charter, Team Onboarding
Bigger version: A new person joins the team

## "I'll just do it myself"
Event: Team & conflict
You'll notice: Someone takes a task back because explaining it or waiting would take longer.
What's going on: It's often faster to do it yourself today, and slower for the team over time. The task never gets shared, and others don't learn or take ownership. The trade-off is real, so the question is how to make handing over cheaper.
Ways to try:
- Pair with the person for part of the task, then step back for the rest.
- Describe the outcome you want and the limits, and leave the method open.
- Agree which kinds of decisions people can make without asking, and write them down.
What if: The task is urgent, or a mistake would be costly?
Tools: Delegation Board, Pairing & Mobbing
Spot it: Unclear decision rights

## The AI gives a different answer each time
Event: Working with AI
You'll notice: The same question gets a different reply, and people disagree about which to trust.
What's going on: AI tools don't always give the same answer twice, and a confident tone doesn't mean it's right. Treat each reply as one possible answer, not the answer. The differences can help, because they show where the question was vague or the answer depends on assumptions.
Ways to try:
- Ask the same question three different ways, and look at what the answers have in common.
- Ask it to list its assumptions, then check the ones that matter.
- Use it to produce options to choose between, not a single decision.
What if: The answer is going into something that needs to be exact?
Tools: AI Working Agreement, AI in Delivery

## Someone pastes work data into a public AI tool
Event: Working with AI
You'll notice: A screenshot, a customer's name or a piece of code appears in a prompt, and nobody stopped to ask.
What's going on: It's easy to paste things in without thinking about where they go. People usually mean well, and the rules aren't always clear. Agreeing in advance what can and can't be shared, and offering a safe alternative, works better than warnings after the fact.
Ways to try:
- Agree three examples of what's fine to share and three that aren't, and put them where people look.
- Replace names and numbers with placeholders before pasting.
- Find out which approved tool the organisation provides, and make it the easy choice.
What if: There's no approved tool yet, and people have deadlines?
Tools: AI Working Agreement, AI in Delivery
Bigger version: The team is asked to start using AI tools

## AI writes the first draft, and the team stops thinking
Event: Working with AI
You'll notice: The first answer is accepted as the plan, and the discussion that used to shape it doesn't happen.
What's going on: A fast first draft is useful, but it also sets the frame. When people only react to it, they stop generating their own ideas, and the team loses the discussion where understanding is built. AI works better as a challenger than as a replacement.
Ways to try:
- Write your own rough idea first, then ask the AI to improve or challenge it.
- Ask the AI to argue against its own draft, and discuss which points hold.
- Discuss a topic without AI first, then compare the result with what it would have said.
What if: The team is short of time, and the draft looks good enough?
Tools: AI in Delivery, AI Working Agreement
