"""
Functions and routines associated with Enasis Network Homie Automate.

This file is part of Enasis Network software eco-system. Distribution
is permitted, for more information consult the project license file.
"""



from json import dumps
from json import loads
from threading import Lock
from typing import Optional
from typing import TYPE_CHECKING
from typing import Union

from encommon.times import Time
from encommon.times import unitime

from sqlalchemy import Column
from sqlalchemy import Numeric
from sqlalchemy import String
from sqlalchemy import create_engine
from sqlalchemy.engine import Engine
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Session
from sqlalchemy.orm import sessionmaker

if TYPE_CHECKING:
    from ..homie import Homie



HomiePersistValue = Optional[
    int | float | bool | str]

_PERSIST_VALUE = (
    int, float, bool, str)

HomiePersistExpire = Union[
    int, float, str]



class SQLBase(DeclarativeBase):
    """
    Some additional class that SQLAlchemy requires to work.
    """



class HomiePersistTable(SQLBase):
    """
    Schematic for the database operations using SQLAlchemy.

    .. note::
       Fields are not completely documented for this model.
    """

    unique = Column(
        String,
        primary_key=True,
        nullable=False)

    value = Column(
        String,
        nullable=False)

    expire = Column(
        Numeric,
        nullable=True)

    update = Column(
        Numeric,
        nullable=False)

    __tablename__ = 'persist'



class HomiePersist:
    """
    Store the persistent information in the key value store.

    :param homie: Primary class instance for Homie Automate.
    """

    __connect: str
    __locker: Lock

    __sengine: Engine
    __session: (
        # pylint: disable=unsubscriptable-object
        sessionmaker[Session])


    def __init__(
        self,
        homie: 'Homie',
    ) -> None:
        """
        Initialize instance for class using provided parameters.
        """

        self.__homie = homie

        params = homie.params

        self.__connect = (
            params.database)

        self.__locker = Lock()

        self.__build_engine()


    def __build_engine(
        self,
    ) -> None:
        """
        Construct instances using the configuration parameters.
        """

        path = self.__connect

        sengine = (
            create_engine(path))

        (SQLBase.metadata
         .create_all(sengine))

        session = (
            sessionmaker(sengine))

        self.__sengine = sengine
        self.__session = session


    def insert(
        self,
        unique: str,
        value: HomiePersistValue,
        expire: HomiePersistExpire = '30d',
    ) -> None:
        """
        Insert the value within the persistent key value store.

        .. note::
           This will replace existing record with primary key.

        :param unique: Unique identifier from within the table.
        :param value: Value Which will be stored within record.
        :param expire: Optional time in seconds for expiration.
        """

        expire = unitime(expire)

        assert isinstance(expire, int)

        update = Time().spoch
        expire = update + expire


        if value is None:
            self.delete(unique)
            return None


        sess = self.__session()
        lock = self.__locker

        with lock, sess as session:

            session.merge(
                HomiePersistTable(
                    unique=unique,
                    value=dumps(value),
                    expire=expire,
                    update=update))

            session.commit()


    def select(
        self,
        unique: str,
    ) -> HomiePersistValue:
        """
        Return the value from within persistent key value store.

        :param unique: Unique identifier from within the table.
        :returns: Value from within persistent key value store.
        """

        sess = self.__session()
        lock = self.__locker

        table = HomiePersistTable
        field = table.unique

        self.expire()

        with lock, sess as session:

            query = (
                session.query(table)
                .filter(field == unique))

            record = query.first()

            if record is None:
                return None

            value = str(record.value)

        value = loads(value)

        assert isinstance(
            value, _PERSIST_VALUE)

        return value


    def delete(
        self,
        unique: str,
    ) -> None:
        """
        Delete the value within the persistent key value store.

        :param unique: Unique identifier from within the table.
        """

        sess = self.__session()
        lock = self.__locker

        table = HomiePersistTable
        field = table.unique

        with lock, sess as session:

            query = (
                session.query(table)
                .filter(field == unique))

            record = query.first()

            if record is None:
                return None

            session.delete(record)

            session.commit()


    def expire(
        self,
    ) -> None:
        """
        Remove the expired persistent key values from the table.
        """

        table = HomiePersistTable
        expire = table.expire

        sess = self.__session()
        lock = self.__locker

        with lock, sess as session:

            now = Time().spoch

            (session.query(table)
             .filter(expire < now)
             .delete())

            session.commit()
