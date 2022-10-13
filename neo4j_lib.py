from neo4j import GraphDatabase


class NeoApp:
    def __init__(self, uri, user, password):
        self.driver = GraphDatabase.driver(uri, auth=(user, password))

    def close(self):
        self.driver.close()

    def query(self, query, parameters=None, db=None):
        session = None
        response = None
        try:
            session = (
                self.driver.session(database=db)
                if db is not None
                else self.driver.session()
            )
            r = session.run(query, parameters)
            response = [ dict(i) for i in r]
        except Exception as e:
            print("Query failed:", e)
        finally:
            if session is not None:
                session.close()
        return response
