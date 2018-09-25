# Slido Voter
Sli.do Voter - Every Question Matters. `Ever vote counts more though..`

## What is this?
There is a website called Sli.do (slido.com) where Questions are often asked during events, town halls, etc.

Sometimes it's nice to get a few more votes on something pressing

## How to use this?
It's really simple to use `Slido Voter`.

The script takes four commandline arguments, that is `hash`, `eventId`, `questionId` and `votesCount`

```
python slido_voter.py <TheHash_AsShownInTheURL> <TheEventId> <TheQuestionId> <HowManyTimesYouWantThisVotedFor>
```

Example:
```
$ python slido_voter.py ygfrt3zf 641687 5902547 3
  ...
  Successfully voted 3 times
```
