import scrapy
import json

class LaliganineteenSpider(scrapy.Spider):
    name='laligarounds'
    allowed_domains=['api.sofascore.com']
    # start_urls=['https://api.sofascore.com/api/v1/unique-tournament/8/season/24127/events/last/1']
    c=0

    def start_requests(self):
        for i in range(1,39):
            yield scrapy.Request(url='https://api.sofascore.com/api/v1/unique-tournament/8/season/32501/events/round/{}'.format(i),callback=self.parse)



    def parse(self,response):
        dic=json.loads(response.body)
        
        for match in dic.get('events'): 
                yield scrapy.Request(url='https://api.sofascore.com/api/v1/event/{}/lineups'.format(match.get('id')),callback=self.parseid,meta={'Home':match.get('homeTeam').get('name'),'Away':match.get('awayTeam').get('name')})


    def parseid(self,response):
        players=json.loads(response.body)
        home=response.request.meta['Home']
        away=response.request.meta['Away']
        
        hplayers = players.get('home').get('players')
        aplayers=players.get('away').get('players')
        players=hplayers+aplayers
        c=0
        for player in players:
            c+=1
            
            if c<=len(hplayers):
                
                yield {'Name':player.get('player').get('shortName'),
                    'Position':player.get('player').get('position'),
                    'Total Pass': player.get('statistics').get('totalPass',0),
                    'Accurate Pass': player.get('statistics').get('accuratePass',0),
                    'Total Long Balls': player.get('statistics').get('totalLongBalls',0),
                    'Accurate Long Balls': player.get('statistics').get('accurateLongBalls',0),
                    'Total Cross':player.get('statistics').get('totalCross',0),
                    'Accurate Cross':player.get('statistics').get('accurateCross',0),
                    'Aerial Won':player.get('statistics').get('aerialWon',0),
                    'Aerial Lost':player.get('statistics').get('aerialLost',0),
                    'Duel Lost':player.get('statistics').get('duelLost',0),
                    'Duel Won':player.get('statistics').get('duelWon',0),
                    'Total Dribbles':player.get('statistics').get('totalContest',0),
                    'Successful Dribbles':player.get('statistics').get('wonContest',0),
                    'Big Chance Created':player.get('statistics').get('bigChanceCreated',0),
                    'Big Chance Missed':player.get('statistics').get('bigChanceMissed',0),
                    'Interception Won':player.get('statistics').get('interceptionWon',0),
                    'Dribbled Past':player.get('statistics').get('challengeLost',0),
                    'Dispossessed':player.get('statistics').get('dispossessed',0),
                    'Error Lead To Shot':player.get('statistics').get('errorLeadToAShot',0),
                    'Total Tackle':player.get('statistics').get('totalTackle',0),
                    'Fouls':player.get('statistics').get('fouls',0),
                    'Was Fouled':player.get('statistics').get('wasFouled',0),
                    'Total Clearance':player.get('statistics').get('totalClearance',0),
                    'Key Pass':player.get('statistics').get('keyPass',0),
                    'Shots On Target':player.get('statistics').get('onTargetScoringAttempt',0),
                    'Shots Off Target':player.get('statistics').get('shotOffTarget',0),
                    'Goal Assist': player.get('statistics').get('goalAssist',0),
                    'Goals':player.get('statistics').get('goals',0),
                    'Woodwork':player.get('statistics').get('hitWoodwork',0),
                    'Saves':player.get('statistics').get('saves',0),
                    'Punches':player.get('statistics').get('puches',0),
                    'Save From Inside The Box':player.get('statistics').get('savedShotsFromInsideTheBox',0),
                    'Last Man Tackle':player.get('statistics').get('lastManTackle',0),
                    'Shots Blocked':player.get('statistics').get('blockedScoringAttempt',0),
                    'Blocked Shots':player.get('statistics').get('outfielderBlock',0),
                    'Total Keeper Sweeper':player.get('statistics').get('totalKeeperSweeper',0),
                    'Accurate Keeper Sweeper':player.get('statistics').get('accurateKeeperSweeper',0),
                    'Touches':player.get('statistics').get('touches',0),
                    'Total OffSide':player.get('statistics').get('totalOffside',0),
                    'Possession Lost Ctrl':player.get('statistics').get('possessionLostCtrl',0),
                    'Own Goals':player.get('statistics').get('ownGoals',0),
                    'MinutesPlayed':player.get('statistics').get('minutesPlayed',0),
                    'place':'Home',
                    'Team':home,
                    'SofaScore Rating':player.get('statistics').get('rating',0)
                    }
            else:
                yield {'Name':player.get('player').get('shortName'),
                    'Position':player.get('player').get('position'),
                    'Total Pass': player.get('statistics').get('totalPass',0),
                    'Accurate Pass': player.get('statistics').get('accuratePass',0),
                    'Total Long Balls': player.get('statistics').get('totalLongBalls',0),
                    'Accurate Long Balls': player.get('statistics').get('accurateLongBalls',0),
                    'Total Cross':player.get('statistics').get('totalCross',0),
                    'Accurate Cross':player.get('statistics').get('accurateCross',0),
                    'Aerial Won':player.get('statistics').get('aerialWon',0),
                    'Aerial Lost':player.get('statistics').get('aerialLost',0),
                    'Duel Lost':player.get('statistics').get('duelLost',0),
                    'Duel Won':player.get('statistics').get('duelWon',0),
                    'Total Dribbles':player.get('statistics').get('totalContest',0),
                    'Successful Dribbles':player.get('statistics').get('wonContest',0),
                    'Big Chance Created':player.get('statistics').get('bigChanceCreated',0),
                    'Big Chance Missed':player.get('statistics').get('bigChanceMissed',0),
                    'Interception Won':player.get('statistics').get('interceptionWon',0),
                    'Dribbled Past':player.get('statistics').get('challengeLost',0),
                    'Dispossessed':player.get('statistics').get('dispossessed',0),
                    'Error Lead To Shot':player.get('statistics').get('errorLeadToAShot',0),
                    'Total Tackle':player.get('statistics').get('totalTackle',0),
                    'Fouls':player.get('statistics').get('fouls',0),
                    'Was Fouled':player.get('statistics').get('wasFouled',0),
                    'Total Clearance':player.get('statistics').get('totalClearance',0),
                    'Key Pass':player.get('statistics').get('keyPass',0),
                    'Shots On Target':player.get('statistics').get('onTargetScoringAttempt',0),
                    'Shots Off Target':player.get('statistics').get('shotOffTarget',0),
                    'Goal Assist': player.get('statistics').get('goalAssist',0),
                    'Goals':player.get('statistics').get('goals',0),
                    'Woodwork':player.get('statistics').get('hitWoodwork',0),
                    'Saves':player.get('statistics').get('saves',0),
                    'Punches':player.get('statistics').get('puches',0),
                    'Save From Inside The Box':player.get('statistics').get('savedShotsFromInsideTheBox',0),
                    'Last Man Tackle':player.get('statistics').get('lastManTackle',0),
                    'Shots Blocked':player.get('statistics').get('blockedScoringAttempt',0),
                    'Blocked Shots':player.get('statistics').get('outfielderBlock',0),
                    'Total Keeper Sweeper':player.get('statistics').get('totalKeeperSweeper',0),
                    'Accurate Keeper Sweeper':player.get('statistics').get('accurateKeeperSweeper',0),
                    'Touches':player.get('statistics').get('touches',0),
                    'Total OffSide':player.get('statistics').get('totalOffside',0),
                    'Possession Lost Ctrl':player.get('statistics').get('possessionLostCtrl',0),
                    'Own Goals':player.get('statistics').get('ownGoals',0),
                    'MinutesPlayed':player.get('statistics').get('minutesPlayed',0),
                    'place':'Away',
                    'Team':away,
                    'SofaScore Rating':player.get('statistics').get('rating',0)
                    }
        