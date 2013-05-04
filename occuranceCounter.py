import praw
import json
import time 
 
newCount= {}
storedCount= {}

fname= 'words.json'
THRESH= 5
MINCOMMENTSCORE= 0
subReddit= 'test'

#description of bot
user_agent= 'Calculate the popularity of teams/players based on occurances in comments by /u/amwelch (Testing phase)'

def main():
  r= init()
  subRed= r.get_subreddit(subReddit)
  commentList= subRed.get_comments()
  #commentTree= subRed.get_comments(subRed)
  #commentList= praw.helpers.flatten_tree(commentTree)

  for c in commentList:
    print "Body:\t%s" %(c.body)
    if c.score < MINCOMMENTSCORE:
      continue
    for word in c.body.split():
      word= str(word).lower()
      if word in newCount.keys():
        newCount[word] += 1
      else:
        newCount[word] = 1
  try:
    words= json.load(fname)
  except:
    words= {}

  for w in newCount.keys():
    print "Word:\t%s" % (w)
    if newCount[w] >= THRESH:
      try:
        words[w]['count'] += newCount[w] 
      except:
        words[w]= {}
        words[w]['count'] = newCount[w]
      
      words[w]['Last Modified']= time.time()
  
  json.dump(words, open(fname, 'w'), default=list, indent=2)

def init():
  global user_agent
  global teamStrings
  r= praw.Reddit(user_agent)
  return r

if __name__=="__main__":
    main();
