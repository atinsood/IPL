import tornado.web
import tornado.ioloop
import playerStats
import json


class PlayerStatsHandler(tornado.web.RequestHandler):

    def initialize(self):
        self.playerSoup = playerStats.parseStatsFile()


    def get(self):
        self.players = playerStats.getPlayerStats(self.playerSoup)
        results = dict(players=self.players)
        self.set_header("Content-Type", "application/json") 
        callback = self.get_argument("callback", "callback")
        super(PlayerStatsHandler, self).write(callback+'(' + json.dumps(results) + ')')
        

application = tornado.web.Application([
    (r"/players", PlayerStatsHandler),
])

if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()

