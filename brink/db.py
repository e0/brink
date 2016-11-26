import rethinkdb as r


class Connection(object):
    """
    Connection provides an instance of the rethinkdb connection object.
    """

    def setup(self, config):
        """
        Setups the database configuartion and sets the RethinkDB loop type to
        asyncio to be compatible with aiohttp.
        """
        r.set_loop_type("asyncio")
        self.config = config

    async def get(self):
        return await r.connect(
            db=self.config.get("db", "test"),
            port=self.config.get("port", 28015)
        )

conn = Connection()
