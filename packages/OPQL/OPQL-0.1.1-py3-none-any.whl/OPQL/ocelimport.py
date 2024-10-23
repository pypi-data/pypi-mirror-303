import datetime
import sqlite3
import re

def loadJSON(path: str, target_db):
    print("Begin loading from json")
    starttime = datetime.datetime.now()
    import json
    # new_db = sqlite3.connect(':memory:', detect_types=sqlite3.PARSE_DECLTYPES, check_same_thread=False)
    target_db.execute("BEGIN TRANSACTION")

    # TODO: i don't think the standart does any concrete definition of this mapping,
    #  except for mentioning it can be the identity function. in the case of the provided example logs however,
    #  it is clearly not just the identity
    def map_type_slug(full_name: str):
        # regex that matches valid sqlite3 column names
        column_name_pattern = r'^[a-zA-Z_][a-zA-Z0-9_]*$'
        if re.match(column_name_pattern, full_name):
            return full_name

        slugged = "".join(re.findall("[a-zA-Z]+", full_name))
        return slugged

    with open(path, "r") as jsonocel_file:
        jsoc = json.load(jsonocel_file)

        print("Generating Table structure")

        # create object_map_type
        omt = "CREATE TABLE \"object_map_type\" (`ocel_type` TEXT, `ocel_type_map` TEXT, PRIMARY KEY(`ocel_type`))"
        target_db.execute(omt)

        # create event_map_type
        emt = "CREATE TABLE \"event_map_type\" (`ocel_type`	TEXT, `ocel_type_map` TEXT, PRIMARY KEY(`ocel_type`))"
        target_db.execute(emt)

        # create event
        ev = """
        CREATE TABLE "event" 
        (`ocel_id`	TEXT, 
        `ocel_type`	TEXT, 
        PRIMARY KEY(`ocel_id`), 
        FOREIGN KEY(`ocel_type`) REFERENCES `event_map_type`(`ocel_type`))
        """
        target_db.execute(ev)

        # create object
        ob = """
        CREATE TABLE "object" 
        (`ocel_id` TEXT, 
        `ocel_type` TEXT, 
        FOREIGN KEY(`ocel_type`) REFERENCES `object_map_type`(`ocel_type`), 
        PRIMARY KEY(`ocel_id`))
        """
        target_db.execute(ob)

        # create eo
        eo = """
        CREATE TABLE "event_object" 
        (`ocel_event_id` TEXT, 
        `ocel_object_id` TEXT, 
        `ocel_qualifier` TEXT, 
        PRIMARY KEY(`ocel_event_id`,`ocel_object_id`,`ocel_qualifier`), 
        FOREIGN KEY(`ocel_event_id`) REFERENCES `event`(`ocel_id`), 
        FOREIGN KEY(`ocel_object_id`) REFERENCES `object`(`ocel_id`))
        """
        target_db.execute(eo)

        # create oo
        oo = """
        CREATE TABLE "object_object" 
        (`ocel_source_id`	TEXT, 
        `ocel_target_id` TEXT, 
        `ocel_qualifier` TEXT, 
        PRIMARY KEY(`ocel_source_id`,`ocel_target_id`,`ocel_qualifier`), 
        FOREIGN KEY(`ocel_source_id`) REFERENCES `object`(`ocel_id`), 
        FOREIGN KEY(`ocel_target_id`) REFERENCES `object`(`ocel_id`))
        """
        target_db.execute(oo)

        JSONOCEL_DATATYPE_STRING = "string"
        JSONOCEL_DATATYPE_TIME = "time"
        JSONOCEL_DATATYPE_INTEGER = "integer"
        JSONOCEL_DATATYPE_FLOAT = "float"
        JSONOCEL_DATATYPE_BOOLEAN = "boolean"
        SQL_DATATYPE_TEXT = "TEXT"
        SQL_DATATYPE_TIMESTAMP = "TIMESTAMP"
        SQL_DATATYPE_INTEGER = "INTEGER"
        SQL_DATATYPE_REAL = "REAL"
        SQL_DATATYPE_BOOLEAN = "INTEGER"
        json_to_sqlite_datatypes = {JSONOCEL_DATATYPE_STRING: SQL_DATATYPE_TEXT,
                                    JSONOCEL_DATATYPE_TIME: SQL_DATATYPE_TIMESTAMP,
                                    JSONOCEL_DATATYPE_INTEGER: SQL_DATATYPE_INTEGER,
                                    JSONOCEL_DATATYPE_FLOAT: SQL_DATATYPE_REAL,
                                    JSONOCEL_DATATYPE_BOOLEAN: SQL_DATATYPE_BOOLEAN}

        def attribute_slag(full_name):
            # TODO: this needs a vastly bigger symbolspace. probably better to just regex match on characters,
            #  numbers and underscores and use only that.
            rmap = {" ": "",
                    "(": "",
                    ")": "",
                    "-": ""}
            rval = full_name
            for k in rmap:
                rval = rval.replace(k, rmap[k])
            return rval

        # store types of attributes here for correct format on insertion later
        event_attribute_type = {}

        # create event_*
        for event in jsoc["eventTypes"]:
            name_slug = map_type_slug(event["name"])

            attrib_map = {}

            for attribute in event["attributes"]:
                attrib_map[attribute["name"]] = json_to_sqlite_datatypes[attribute["type"]]

            event_attribute_type[event["name"]] = attrib_map

            attribs = [f"{attribute_slag(key)} {attrib_map[key]}," for key in attrib_map]
            attrib_str = " \n ".join(attribs)

            event_q = f"""
            CREATE TABLE "event_{name_slug}" 
            (ocel_id TEXT, 
            ocel_time TIMESTAMP, 
            {attrib_str}
            PRIMARY KEY(ocel_id))
            """

            target_db.execute(event_q)

        # store types of attributes here for correct format on insertion later
        object_attribute_type = {}

        # create object_*
        for object in jsoc["objectTypes"]:
            name_slug = map_type_slug(object["name"])

            attrib_map = {}

            for attribute in object["attributes"]:
                attrib_map[attribute["name"]] = json_to_sqlite_datatypes[attribute["type"]]

            object_attribute_type[object["name"]] = attrib_map

            attribs = [f"{attribute_slag(key)} {attrib_map[key]}," for key in attrib_map]
            attrib_str = " \n ".join(attribs)

            # TODO a bit weird that this has a foreign key on ocel_id of object but events have primary key on ocel id in ocel2-p2p,
            # order-management has no keys defined whatsoever, container logistics same as ocel2-p2p
            object_q = f"""
            CREATE TABLE "object_{name_slug}" 
            (ocel_id TEXT, 
            ocel_time TIMESTAMP, 
            {attrib_str}
            ocel_changed_field TEXT, 
            FOREIGN KEY(ocel_id) REFERENCES object(ocel_id))
            """

            target_db.execute(object_q)

        print("Creating object and event types")

        # insert object_map_type
        for object in jsoc["objectTypes"]:
            oname = object["name"]
            oslug = map_type_slug(oname)
            insert_q = f"""
            INSERT INTO object_map_type (ocel_type,ocel_type_map)
            VALUES('{oname}','{oslug}');
            """
            target_db.execute(insert_q)

        # insert event_map_type
        for event in jsoc["eventTypes"]:
            ename = event["name"]
            eslug = map_type_slug(ename)
            insert_q = f"""
            INSERT INTO event_map_type (ocel_type,ocel_type_map)
            VALUES('{ename}','{eslug}');
            """
            target_db.execute(insert_q)

        def ts_to_dt(timestamp: str) -> datetime.datetime:
            return datetime.datetime.strptime(timestamp, "%Y-%m-%dT%H:%M:%S.%f%z")

        TIME_EPOCH_STR = "1970-01-01T00:00:00.000Z"
        invalts = ts_to_dt(TIME_EPOCH_STR)

        num_o = len(jsoc["objects"])
        print(f"Adding {num_o} objects")
        i = 1
        # insert all objects
        for object in jsoc["objects"]:
            print(f"{i}/{num_o}", end='\r')
            i += 1
            ocel_id = object["id"]
            ocel_type = object["type"]

            init_event_q = f"""
            INSERT INTO object (ocel_id, ocel_type)
            VALUES('{ocel_id}', '{ocel_type}');
            """

            target_db.execute(init_event_q)

            # collect all attribute values with timestamp 0 for
            attributes = object["attributes"]

            initial_values = [attr for attr in attributes if invalts == ts_to_dt(attr["time"])]

            col_names = [map_type_slug(attr["name"]) for attr in initial_values]
            col_names += ["ocel_time", "ocel_id"]

            col_name_str = ",".join(col_names)

            typemap = object_attribute_type[ocel_type]

            vals = []
            for attr in initial_values:
                attr_type = typemap[attr["name"]]

                if attr_type == SQL_DATATYPE_TEXT or attr_type == SQL_DATATYPE_TIMESTAMP:
                    vals.append("'" + str(attr["value"]) + "'")
                else:
                    vals.append(str(attr["value"]))

            vals += ["'" + TIME_EPOCH_STR + "'", f"'{ocel_id}'"]

            vals_str = ",".join(vals)

            # insert initialization row
            init_insert_q = f"""
            INSERT INTO object_{map_type_slug(object["type"])} ({col_name_str})
            VALUES({vals_str});
            """

            target_db.execute(init_insert_q)

            # now updated values
            value_updates = [attr for attr in attributes if invalts != ts_to_dt(attr["time"])]

            for val_update in value_updates:
                attr_type = typemap[val_update["name"]]

                col_names = [map_type_slug(val_update["name"]), "ocel_time", "ocel_changed_field"]
                col_names.append("ocel_id")
                col_name_str = ",".join(col_names)

                vals = []

                if attr_type == SQL_DATATYPE_TEXT or attr_type == SQL_DATATYPE_TIMESTAMP:
                    vals.append("'" + str(val_update["value"]) + "'")
                else:
                    vals.append(str(val_update["value"]))

                vals.append("'" + val_update["time"] + "'")
                vals.append("'" + map_type_slug(val_update["name"]) + "'")
                vals.append(f"'{ocel_id}'")

                val_str = ",".join(vals)

                update_q = f"""
                INSERT INTO object_{map_type_slug(object["type"])} ({col_name_str})
                VALUES({val_str});
                """

                target_db.execute(update_q)

        num_e = len(jsoc["events"])
        i = 1
        print(f"Adding {num_e} events and EO relations")
        # insert all events
        for event in jsoc["events"]:
            print(f"{i}/{num_e}", end='\r')
            i += 1

            ocel_id = event["id"]
            ocel_type = event["type"]

            init_event_q = f"""
            INSERT INTO event (ocel_id, ocel_type)
            VALUES('{ocel_id}', '{ocel_type}');
            """

            target_db.execute(init_event_q)

            # collect all attribute values with timestamp 0 for
            attributes = event["attributes"]

            initial_values = [attr for attr in attributes]

            # TODO i guess standard will just fill up not specified columns with null values
            col_names = [map_type_slug(attr["name"]) for attr in initial_values]
            col_names += ["ocel_time", "ocel_id"]

            col_name_str = ",".join(col_names)

            typemap = event_attribute_type[ocel_type]

            vals = []
            for attr in initial_values:
                attr_type = typemap[attr["name"]]

                if attr_type == SQL_DATATYPE_TEXT or attr_type == SQL_DATATYPE_TIMESTAMP:
                    vals.append("'" + attr["value"] + "'")
                else:
                    vals.append(attr["value"])

            vals.append("'" + event["time"] + "'")
            vals.append(f"'{ocel_id}'")

            vals_str = ",".join(vals)

            # insert initialization row
            init_insert_q = f"""
            INSERT INTO event_{map_type_slug(event["type"])} ({col_name_str})
            VALUES({vals_str});
            """

            target_db.execute(init_insert_q)

            # insert eo
            for object_relationship in event["relationships"]:
                object_id = object_relationship["objectId"]
                qualifier = object_relationship["qualifier"]

                vals_str = ",".join([f"'{ocel_id}'", f"'{str(object_id)}'", f"'{qualifier}'"])

                eo_insert_q = f"""
                INSERT INTO event_object (ocel_event_id, ocel_object_id, ocel_qualifier)
                VALUES({vals_str});
                """

                target_db.execute(eo_insert_q)

                # ocel_event_id, ocel_object_id, ocel_qualifier

        print("Adding OO relations")

        # insert oo
        for object in jsoc["objects"]:
            ocel_source_id = object["id"]

            for oo_rel in object["relationships"]:
                ocel_target_id = oo_rel["objectId"]
                ocel_qualifier = oo_rel["qualifier"]

                eo_insert_q = f"""
                INSERT INTO object_object (ocel_source_id, ocel_target_id, ocel_qualifier)
                VALUES('{ocel_source_id}','{ocel_target_id}','{ocel_qualifier}');
                """

                target_db.execute(eo_insert_q)

    target_db.execute("END TRANSACTION")
    print(f"Loading done: {str(datetime.datetime.now() - starttime)}")


# taken and adapted from webpy who, as it seems, had the same problem with pythons sqlite3 datetime conversions being buggy
# TODO: give these some more graceful and expressive error handling in case a timestamp does not correspond to expected format
# TODO: there is potential merit in converting these to utility functions
def adapt_datetime_iso(date_time: datetime.datetime) -> str:
    """
    Convert a Python datetime.datetime into a ISO 8601 date string. Also works with timezone-aware datetime!
    >>> adapt_datetime_iso(datetime.datetime(2023, 4, 5, 6, 7, 8, 9))
    '2023-04-05T06:07:08.000009'
    """
    return date_time.isoformat()


def convert_timestamp(time_stamp: bytes) -> datetime:
    """
    Convert an ISO 8601 formatted bytestring to a datetime.datetime object.
    >>> convert_timestamp(b'2023-04-05T06:07:08.000009Z')
    datetime.datetime(2023, 4, 5, 6, 7, 8, 9)
    """
    return datetime.datetime.strptime(time_stamp.decode("utf-8"), "%Y-%m-%dT%H:%M:%S.%f%z")


sqlite3.register_adapter(datetime, adapt_datetime_iso)
sqlite3.register_converter("timestamp", convert_timestamp)


def loadSQLITE(path: str, target_db):
    # PARSE_DECLTYPES should make sure we get actual datetime object back when querying for such
    # HOWEVER, we dont do this. python sqlite3 datetime converters are FUBR.
    # using them will raise errors because it cannot correctly handle stuff like timezones etc
    # while https://bugs.python.org/issue43831 states it has been fixed, it crashed with the same
    # value error in python 3.12, so this is probably a regression and the converters are deprecated
    # so no future fix is to be expected


    print(f"Opening {path}")
    old_db = sqlite3.connect(path, detect_types=sqlite3.PARSE_DECLTYPES,)
    print("Creating replication query")
    query = "".join(line for line in old_db.iterdump())

    # Dump old database in the new one.
    print("Dumping to in memory db with same thread check deactivated")
    target_db.executescript(query)