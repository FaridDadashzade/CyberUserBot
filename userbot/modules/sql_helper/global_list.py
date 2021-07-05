import threading

from sqlalchemy import Column, String, UnicodeText, distinct, func

from . import BASE, SESSION


class CyberGloballist(BASE):
    __tablename__ = "cyberglobal_list"
    keywoard = Column(UnicodeText, primary_key=True)
    group_id = Column(String, primary_key=True, nullable=False)

    def __init__(self, keywoard, group_id):
        self.keywoard = keywoard
        self.group_id = str(group_id)

    def __repr__(self):
        return "<Cyber global values '%s' for %s>" % (self.group_id, self.keywoard)

    def __eq__(self, other):
        return bool(
            isinstance(other, CyberGloballist)
            and self.keywoard == other.keywoard
            and self.group_id == other.group_id
        )


CyberGloballist.__table__.create(checkfirst=True)

CYBERGLOBALLIST_INSERTION_LOCK = threading.RLock()


class GLOBALLIST_SQL:
    def __init__(self):
        self.GLOBALLIST_VALUES = {}


GLOBALLIST_SQL_ = GLOBALLIST_SQL()


def add_to_list(keywoard, group_id):
    with CYBERGLOBALLIST_INSERTION_LOCK:
        broadcast_group = CyberGloballist(keywoard, str(group_id))
        SESSION.merge(broadcast_group)
        SESSION.commit()
        GLOBALLIST_SQL_.GLOBALLIST_VALUES.setdefault(keywoard, set()).add(str(group_id))


def rm_from_list(keywoard, group_id):
    with CYBERGLOBALLIST_INSERTION_LOCK:
        broadcast_group = SESSION.query(CyberGloballist).get((keywoard, str(group_id)))
        if broadcast_group:
            if str(group_id) in GLOBALLIST_SQL_.GLOBALLIST_VALUES.get(keywoard, set()):
                GLOBALLIST_SQL_.GLOBALLIST_VALUES.get(keywoard, set()).remove(
                    str(group_id)
                )

            SESSION.delete(broadcast_group)
            SESSION.commit()
            return True
        SESSION.close()
        return False


def is_in_list(keywoard, group_id):
    with CYBERGLOBALLIST_INSERTION_LOCK:
        broadcast_group = SESSION.query(CyberGloballist).get((keywoard, str(group_id)))
        return bool(broadcast_group)


def del_keyword_list(keywoard):
    with CYBERGLOBALLIST_INSERTION_LOCK:
        broadcast_group = (
            SESSION.query(CyberGloballist.keywoard)
            .filter(CyberGloballist.keywoard == keywoard)
            .delete()
        )
        GLOBALLIST_SQL_.GLOBALLIST_VALUES.pop(keywoard)
        SESSION.commit()


def get_collection_list(keywoard):
    return GLOBALLIST_SQL_.GLOBALLIST_VALUES.get(keywoard, set())


def get_list_keywords():
    try:
        chats = SESSION.query(CyberGloballist.keywoard).distinct().all()
        return [i[0] for i in chats]
    finally:
        SESSION.close()


def num_list():
    try:
        return SESSION.query(CyberGloballist).count()
    finally:
        SESSION.close()


def num_list_keyword(keywoard):
    try:
        return (
            SESSION.query(CyberGloballist.keywoard)
            .filter(CyberGloballist.keywoard == keywoard)
            .count()
        )
    finally:
        SESSION.close()


def num_list_keywords():
    try:
        return SESSION.query(func.count(distinct(CyberGloballist.keywoard))).scalar()
    finally:
        SESSION.close()


def __load_chat_lists():
    try:
        chats = SESSION.query(CyberGloballist.keywoard).distinct().all()
        for (keywoard,) in chats:
            GLOBALLIST_SQL_.GLOBALLIST_VALUES[keywoard] = []

        all_groups = SESSION.query(CyberGloballist).all()
        for x in all_groups:
            GLOBALLIST_SQL_.GLOBALLIST_VALUES[x.keywoard] += [x.group_id]

        GLOBALLIST_SQL_.GLOBALLIST_VALUES = {
            x: set(y) for x, y in GLOBALLIST_SQL_.GLOBALLIST_VALUES.items()
        }

    finally:
        SESSION.close()


__load_chat_lists()
