import logging

from sqlalchemy import (
    Table,
    Column,
    Integer,
    String,
    ForeignKey,
    Boolean,
)
from sqlalchemy.orm import (
    relationship,
    deferred,
)

from caerp_base.models.base import (
    DBBASE,
    DBSESSION,
    default_table_args,
)
from caerp.forms import (
    EXCLUDED,
)

logger = logging.getLogger(__name__)


USER_GROUPS = Table(
    "user_groups",
    DBBASE.metadata,
    Column("login_id", Integer, ForeignKey("login.id")),
    Column("group_id", Integer, ForeignKey("groups.id")),
    mysql_charset=default_table_args["mysql_charset"],
    mysql_engine=default_table_args["mysql_engine"],
)


class Group(DBBASE):
    """
    Available groups used in enDI
    """

    __tablename__ = "groups"
    __table_args__ = default_table_args
    id = Column(Integer, primary_key=True, info={"colanderalchemy": EXCLUDED})
    name = Column(
        String(30), nullable=False, info={"colanderalchemy": {"title": "Nom du groupe"}}
    )
    label = deferred(
        Column(
            String(255),
            nullable=False,
            info={"colanderalchemy": {"title": "Libellé"}},
        ),
        group="edit",
    )
    primary = deferred(
        Column(
            Boolean(),
            default=False,
            info={"colanderalchemy": {"exclude": True}},
        )
    )
    editable = deferred(
        Column(
            Boolean(),
            default=False,
            info={"colanderalchemy": {"exclude": True}},
        )
    )
    users = relationship(
        "Login",
        secondary=USER_GROUPS,
        back_populates="_groups",
    )

    @classmethod
    def _find_one(cls, name_or_id):
        """
        Used as a creator for the initialization proxy
        """
        with DBSESSION.no_autoflush:
            res = DBSESSION.query(cls).get(name_or_id)
            if res is None:
                # We try with the id
                res = DBSESSION.query(cls).filter(cls.name == name_or_id).one()

        return res

    def __json__(self, request):
        return dict(name=self.name, label=self.label)
