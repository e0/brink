import rethinkdb as r


class Connection(object):

    def __init__(self):
        r.set_loop_type("asyncio")

    def setup(self, config):
        self.config = config

    async def get(self):
        return await r.connect(
            db=self.config.get("DATABASE", "test"),
            port=self.config.get("PORT", 28015)
        )


conn = Connection()

