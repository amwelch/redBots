import praw
#data structures for storing search strings
teamStrings= {}
playerStrings= {}

#data structures for storing # seen for search strings
playerCount= {}
teamCount= {}

#description of bot
user_agent= 'This is a test bot!'
subReddit= 'test'

MINCOMMENTSCORE = 0

def main():
  r= init()
  #sub= r.get_submission(submission_id= 'TODO')
  subRed= r.get_subreddit(subReddit)
  commentTree= get_comments(subRed)
  commentList= praw.helpers.flatten_tree(commentTree)
  for c in commentList:
    if c.score < MINCOMMENTSCORE:
      continue
  
    for team in teamStrings.keys():
      for string in teamStrings[team]:
        if string.lowercase() in c.lowercase():
          teamCount[team] += 1
          print "One for %s" % (team)
          print comment.body
    
    for player in playerStrings.keys():
      for string in playerStrings[team]:
        if string.lowercase() in c.lowercase():
          playerCount[player] += 1
          print "One for %s" % (team)
          print comment.body

def init():
  global user_agent
  global teamStrings
  r= praw.Reddit(user_agent)

  teamStrings['Liverpoolfc']= ['liverpool', 'lfc', 'liverpoolfc', 'liverpool fc', 'liverpool football club', 'liverpool f c']
  teamStrings['Manchester United']= ['manchester united', 'manu', 'mufc', 'mu fc', 'man u', 'manchester u']
  teamStrings['Manchester City']= ['manchester city', 'mcfc', 'mc fc', 'mc']
  teamStrings['Chelsea']= ['chelsea', 'chelski', 'cfc']
  teamStrings['Spurs']= ['spurs', 'spur', 'tottenham']
  teamStrings['Arsenal']= ['gooners', 'afc', 'arsenal']
  teamStrings['Everton']= ['everton', 'evertonfc']
  teamStrings['Fulham']= ['fulhamfc', 'fulham']
  teamStrings['West Bromwhich Albion']= ['wba', 'wbafc', 'west brom']
  teamStrings['Stoke City']= ['stoke', 'stoke city']
  teamStrings['Wigan']= ['lattics', 'wigan', 'wiganfc']
  teamStrings['Aston Villa']= ['avfc', ' av ', 'aston villa', 'villa', ' villans ']
  teamStrings['Swansea']= ['swansea']
  teamStrings['Queens Park Rangers']= ['qpr', 'queens park', 'queen park ranger']
  teamStrings['Reading']= ['reading', 'readingfc']
  teamStrings['Southhampton']= ['saints', 'southhampton']
  teamStrings['Norwhich']= ['canaries', 'norwhich']
  teamStrings['West Ham']= ['whu', 'west ham', 'hammers']
  teamStrings['Cardiff']= ['cardiff']

  playerStrings['Luis Suarez']= ['suarez']
  playerStrings['Robin Van Persie']= ['rvp', 'van persie', 'robinvp', 'robin vp']
  playerStrings['Gareth Bale']= ['bale', 'gareth bale']

  for player in playerStrings.keys():
    playerCount[player]= 0

  for team in teamStrings.keys():
    teamCount[team]= 0

  return r

if __name__=="__main__":
    main();
