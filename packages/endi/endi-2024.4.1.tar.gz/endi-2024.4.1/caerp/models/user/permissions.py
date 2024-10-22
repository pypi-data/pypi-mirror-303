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
)

from caerp_base.models.base import (
    DBBASE,
    default_table_args,
)
from caerp.forms import (
    EXCLUDED,
)

logger = logging.getLogger(__name__)


role_permission = Table(
    "role_permission",
    DBBASE.metadata,
    Column("role_id", Integer, ForeignKey("role.id")),
    Column("permission_id", Integer, ForeignKey("permission.id")),
    mysql_charset=default_table_args["mysql_charset"],
    mysql_engine=default_table_args["mysql_engine"],
)


class Permission(DBBASE):
    """
    Permissions for enDI
    """

    __tablename__ = "permission"
    __table_args__ = default_table_args

    id = Column(Integer, primary_key=True, info={"colanderalchemy": EXCLUDED})
    name = Column(
        String(30),
        nullable=False,
        info={"colanderalchemy": {"title": "Nom"}},
        unique=True,
    )
    context_related = Column(
        Boolean(),
        default=False,
        info={
            "colanderalchemy": {
                "title": "Permission relative au contexte (ne sera utilisée que dans le calcul dynamique des ACEs)?"
            }
        },
    )
    roles = relationship(
        "Role", secondary="role_permission", back_populates="permissions"
    )

    def __json__(self, request):
        return dict(id=self.id, name=self.name, context_related=self.context_related)


class Role(DBBASE):
    """
    Roles used in enDI
    """

    __tablename__ = "role"
    __table_args__ = default_table_args

    id = Column(Integer, primary_key=True, info={"colanderalchemy": EXCLUDED})
    name = Column(
        String(30),
        nullable=False,
        info={"colanderalchemy": {"title": "Nom"}},
        unique=True,
    )
    permissions = relationship(
        "Permission", secondary="role_permission", back_populates="roles"
    )

    def __json__(self, request):
        return dict(id=self.id, name=self.name)
