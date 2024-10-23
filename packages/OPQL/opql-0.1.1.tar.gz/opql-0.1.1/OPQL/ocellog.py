import sqlite3
import datetime
import re
import json


class OCELEntity:
    def __init__(self, ocel_id: str, map_type: str, dbconnection):
        self.dbconnection = dbconnection
        self.ocel_id = ocel_id
        self.map_type = map_type


class OCELObject(OCELEntity):
    def __init__(self, ocel_id: str, map_type: str, dbconnection):
        super().__init__(ocel_id, map_type, dbconnection)

    def getType(self) -> str:
        res = self.dbconnection.execute(f"SELECT ocel_type FROM object WHERE ocel_id='{self.ocel_id}'")
        type_str = res.fetchone()[0]
        return type_str

    def getPropertyValue(self, property: str, version: datetime.datetime):
        # TODO: shouldnt this be DESC?
        select_q = f"""
        SELECT {property} FROM object_{self.map_type} 
        WHERE ocel_id='{self.ocel_id}' AND {property} IS NOT NULL AND ocel_time <= '{version.isoformat()}'
        ORDER BY ocel_time ASC LIMIT 1 
        """

        try:
            res = self.dbconnection.execute(select_q)
            value_row = res.fetchone()

            if value_row is None:
                return None

            value = value_row[0]
            return value
        except Exception:
            print("Error: Exception during query: " + select_q)
            print("Exception: " + str(type(Exception)) + " " + str(Exception))
            return None

    def getFullHistory(self):
        select_q = f"""
                SELECT ocel_time FROM object_{self.map_type} 
                WHERE ocel_id='{self.ocel_id}'
                ORDER BY ocel_time ASC
                """

        try:
            res = self.dbconnection.execute(select_q)

            vals = res.fetchall()
            return [row[0] for row in vals]
        except Exception:
            print("Error: Exception during query: " + select_q)
            print("Exception: " + str(type(Exception)) + " " + str(Exception))
            return None

    def getPropertyHistory(self, property: str):
        print("HUGE WARNING: We need to get a stronger grip on how ocel histories are defined in eventlogs")
        # TODO: shouldnt this be DESC?
        select_q = f"""
        SELECT ocel_time FROM object_{self.map_type} 
        WHERE ocel_id='{self.ocel_id}' AND {property} IS NOT NULL AND ocel_changed_field='{property} '
        ORDER BY ocel_time ASC
        """

        try:
            res = self.dbconnection.execute(select_q)
            vals = res.fetchall()
            return [row[0] for row in vals]
        except Exception:
            print("Error: Exception during query: " + select_q)
            print("Exception: " + str(type(Exception)) + " " + str(Exception))
            return None


class OCELEvent(OCELEntity):
    def __init__(self, ocel_id: str, map_type: str, dbconnection):
        super().__init__(ocel_id, map_type, dbconnection)

    def getType(self) -> str:
        res = self.dbconnection.execute(f"SELECT ocel_type FROM event WHERE ocel_id='{self.ocel_id}'")
        type_str = res.fetchone()[0]
        return type_str

    def getPropertyValue(self, property: str):
        type = self.getType()
        typeq = f"SELECT ocel_type_map FROM event_map_type WHERE ocel_type='{type}'"
        nameres = self.dbconnection.execute(typeq)
        map_type_name = nameres.fetchone()[0]

        prop_q = f"SELECT {property} FROM event_{map_type_name} WHERE ocel_id='{self.ocel_id}'"
        res = self.dbconnection.execute(prop_q)
        row = res.fetchone()
        propval = row[0]
        return propval


class OCELLog:
    def __init__(self, dbconnection):
        self.dbpath = ""
        self.dbconnection = dbconnection

    def numObjects(self) -> int:
        res = self.dbconnection.execute("SELECT COUNT(*) FROM object")
        num_objects = res.fetchone()[0]
        return num_objects

    def numEvents(self) -> int:
        res = self.dbconnection.execute("SELECT COUNT(*) FROM event")
        num_events = res.fetchone()[0]
        return num_events

    def types(self, type: str):
        res = self.dbconnection.execute(f"SELECT ocel_type, FROM {type}_map_type")
        return [entry for entry in res]

    def objectTypes(self):
        return self.types("object")

    def eventTypes(self):
        return self.types("event")

    # only here to avoid copy pasta
    def mapType(self, type: str):
        res = self.dbconnection.execute(f"SELECT ocel_type, ocel_type_map FROM {type}_map_type")
        resultmap: dict[str, str] = dict()
        for entry in res:
            resultmap[entry[0]] = entry[1]

        return resultmap

    def objectMapType(self) -> dict[str, str]:
        return self.mapType("object")

    def eventMapType(self) -> dict[str, str]:
        return self.mapType("event")

    def getObjectType(self, ocel_id) -> str:
        res = self.dbconnection.execute(f"SELECT ocel_type FROM object WHERE ocel_id='{ocel_id}'")
        row = res.fetchone()

        if not row:
            return None

        return row[0]

    def getEventType(self, ocel_id) -> str:
        q = f"SELECT ocel_type FROM event WHERE ocel_id='{ocel_id}'"
        res = self.dbconnection.execute(q)
        row = res.fetchone()
        if row is not None:
            return row[0]
        return None

    def objectExists(self, ocel_id: str):
        ex_q = f"""SELECT EXISTS(SELECT 1 FROM object WHERE ocel_id='{ocel_id}');"""
        res = self.dbconnection.execute(ex_q)
        row = res.fetchone()
        if row[0] == 1:
            return True

        return False

    def eventExists(self, ocel_id: str):
        ex_q = f"""SELECT EXISTS(SELECT 1 FROM event WHERE ocel_id='{ocel_id}');"""
        res = self.dbconnection.execute(ex_q)
        row = res.fetchone()
        if row[0] == 1:
            return True

        return False

    def getObject(self, ocel_id: str) -> OCELObject:
        omt = self.objectMapType()
        ot = self.getObjectType(ocel_id)
        map_type = omt[ot]
        return OCELObject(ocel_id, map_type, self.dbconnection)

    def getEvent(self, ocel_id: str) -> OCELEvent:
        emt = self.eventMapType()
        et = self.getEventType(ocel_id)
        map_type = emt[et]
        return OCELEvent(ocel_id, map_type, self.dbconnection)

    def getEventIdsByType(self, ocel_type: str) -> list[str]:
        query = f"SELECT ocel_id FROM event WHERE ocel_type='{ocel_type}'"
        res = self.dbconnection.execute(query)
        rval = res.fetchall()
        return [row[0] for row in rval]

    def getObjectIdsByType(self, ocel_type: str) -> list[str]:
        query = f"SELECT ocel_id FROM object WHERE ocel_type='{ocel_type}'"
        res = self.dbconnection.execute(query)
        rval = res.fetchall()
        return [row[0] for row in rval]

    def getEventIds(self) -> list[str]:
        query = f"SELECT ocel_id FROM event"
        res = self.dbconnection.execute(query)
        rval = res.fetchall()
        return [row[0] for row in rval]

    def getObjectIds(self) -> list[str]:
        query = f"SELECT ocel_id FROM object"
        res = self.dbconnection.execute(query)
        rval = res.fetchall()
        return [row[0] for row in rval]

    def getOORelations(self,
                       source_id: str | None, source_type: str | None,
                       target_id: str | None, target_type: str | None,
                       qualifier: str | None) -> list[(str, str, str, str, str)]:
        q = """
        SELECT ocel_source_id, toB.ocel_type AS ocel_source_type, 
        ocel_target_id, toA.ocel_type AS ocel_target_type, 
        ocel_qualifier
        FROM object_object tOO
        INNER JOIN object toA on tOO.ocel_target_id = toA.ocel_id
        INNER JOIN object toB on tOO.ocel_source_id = toB.ocel_id
        """

        if source_id or target_id or qualifier:
            q += " WHERE "

            # keeps track if anything has been written before and an AND must be written between predicates
            running = False

            if source_id:
                q += f"ocel_source_id='{source_id}'"
                running = True
            if source_type:
                if running:
                    q += " AND "
                q += f"ocel_source_type='{source_type}'"
                running = True
            if target_id:
                if running:
                    q += " AND "
                q += f"ocel_target_id='{target_id}'"
                running = True
            if target_type:
                if running:
                    q += " AND "
                q += f"ocel_target_type='{target_type}'"
                running = True
            if qualifier:
                if running:
                    q += " AND "
                q += f"ocel_qualifier='{qualifier}'"

        res = self.dbconnection.execute(q)
        rval = res.fetchall()

        return [(row[0], row[1], row[2], row[3], row[4]) for row in rval]

    def getEORelations(self,
                       event_id: str | None, event_type: str | None,
                       object_id: str | None, object_type: str | None,
                       qualifier: str | None) -> list[(str, str, str, str, str)]:
        q = """
        SELECT ocel_event_id, tEv.ocel_type AS ocel_event_type, 
        ocel_object_id, tOb.ocel_type AS ocel_object_type, 
        ocel_qualifier
        FROM event_object tEO
        INNER JOIN event tEv on tEO.ocel_event_id = tEv.ocel_id
        INNER JOIN object tOb on tEO.ocel_object_id = tOb.ocel_id
        """

        # q = "SELECT ocel_event_id, ocel_object_id, ocel_qualifier from event_object"
        if event_id or object_id or qualifier:
            q += " WHERE "

            # keeps track if anything has been written before and an AND must be written between predicates
            running = False

            if event_id:
                q += f"ocel_event_id='{event_id}'"
                running = True
            if event_type:
                if running:
                    q += " AND "
                q += f"ocel_event_type='{event_type}'"
                running = True
            if object_id:
                if running:
                    q += " AND "
                q += f"ocel_object_id='{object_id}'"
                running = True
            if object_type:
                if running:
                    q += " AND "
                q += f"ocel_object_type='{object_type}'"
                running = True
            if qualifier:
                if running:
                    q += " AND "
                q += f"ocel_qualifier='{qualifier}'"

        res = self.dbconnection.execute(q)
        rval = res.fetchall()

        return [(row[0], row[1], row[2], row[3], row[4]) for row in rval]

    def deleteObject(self, object_id: str):
        if not self.objectExists(object_id):
            return

        # delete object from object_<typemap>
        obj = self.getObject(object_id)
        type = obj.getType()
        map_type = self.objectMapType()
        tablename = "object_" + map_type[type]

        delete_attributes_query = f"DELETE FROM {tablename} WHERE ocel_id='{object_id}'"
        self.dbconnection.execute(delete_attributes_query)

        # delete object from eo relations
        self.deleteEORelation(None, object_id, None)

        # delete object from oo relations
        self.deleteOORelation(object_id, None, None)
        self.deleteOORelation(None, object_id, None)

        # delete object from object table
        delete_object_query = f"DELETE FROM object WHERE ocel_id='{object_id}'"
        self.dbconnection.execute(delete_object_query)

    def deleteEvent(self, event_id: str):
        if not self.eventExists(event_id):
            return

        ev = self.getEvent(event_id)
        type = ev.getType()
        map_type = self.eventMapType()
        tablename = "event_" + map_type[type]

        delete_attributes_query = f"DELETE FROM {tablename} WHERE ocel_id='{event_id}'"
        self.dbconnection.execute(delete_attributes_query)

        # delete object from eo relations
        self.deleteEORelation(event_id, None, None)

        # delete object from object table
        delete_event_query = f"DELETE FROM event WHERE ocel_id='{event_id}'"
        self.dbconnection.execute(delete_event_query)

    def deleteEORelation(self, event_id: str | None, object_id: str | None, qualifier: str | None):
        q = """DELETE FROM event_object"""

        if event_id or object_id or qualifier:
            q += " WHERE "

            # keeps track if anything has been written before and an AND must be written between predicates
            running = False

            if event_id:
                q += f"ocel_event_id='{event_id}'"
                running = True
            if object_id:
                if running:
                    q += " AND "
                q += f"ocel_object_id='{object_id}'"
                running = True
            if qualifier:
                if running:
                    q += " AND "
                q += f"ocel_qualifier='{qualifier}'"

        self.dbconnection.execute(q)

    def deleteOORelation(self, source_id: str | None, target_id: str | None, qualifier: str | None):
        q = """DELETE FROM object_object"""

        if source_id or target_id or qualifier:
            q += " WHERE "

            # keeps track if anything has been written before and an AND must be written between predicates
            running = False

            if source_id:
                q += f"ocel_event_id='{source_id}'"
                running = True
            if target_id:
                if running:
                    q += " AND "
                q += f"ocel_object_id='{target_id}'"
                running = True
            if qualifier:
                if running:
                    q += " AND "
                q += f"ocel_qualifier='{qualifier}'"

        self.dbconnection.execute(q)

    # returns id of next/previous event w.r.t object id
    def olaglead(self,
                 event_id: str | None,
                 object_id: str | None,
                 lag: bool = True,
                 offset: int = 0,
                 etype: None | str = None):

        if event_id is None or object_id is None:
            return None

        event = self.getEvent(event_id)

        ev_timestamp = event.getPropertyValue("ocel_time")

        q = f"""
        SELECT ocel_event_id
        FROM event_object tEO
        WHERE tEO.ocel_object_id == '{object_id}'
        """

        res = self.dbconnection.execute(q)
        rval = res.fetchall()

        def get_event_ts(event_id):
            ev = self.getEvent(event_id)
            return ev.getPropertyValue("ocel_time")

        # we do this because outer joining on all the spread out event tables is hell.
        # it would have been really nice to have ocel_time as a column in the event table,
        # especially since it is a property every single event has.
        events_w_dates = [(event_id[0], get_event_ts(event_id[0])) for event_id in rval]

        if lag:
            events_w_dates = [ev_tuple for ev_tuple in events_w_dates if ev_tuple[1] < ev_timestamp]
        else:
            events_w_dates = [ev_tuple for ev_tuple in events_w_dates if ev_tuple[1] > ev_timestamp]

        events_w_dates.sort(reverse=lag)

        if etype:
            events_w_dates = [ev_tuple for ev_tuple in events_w_dates if self.getEventType(ev_tuple[0]) == etype]

        if not events_w_dates:
            return None

        # offset goes into nirvana
        if offset >= len(events_w_dates):
            return None

        return events_w_dates[offset][0]
