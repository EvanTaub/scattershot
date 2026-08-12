"""baseline

Revision ID: 3e57e401e0e0
Revises:
Create Date: 2026-08-11 20:21:24.927041

"""

from collections.abc import Sequence

# revision identifiers, used by Alembic.
revision: str = "3e57e401e0e0"
down_revision: str | Sequence[str] | None = None
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
