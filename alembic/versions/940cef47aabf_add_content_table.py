"""Add content table

Revision ID: 940cef47aabf
Revises: 920075a8f604
Create Date: 2023-06-05 16:34:11.870783

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '940cef47aabf'
down_revision = '920075a8f604'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts',sa.Column('content',sa.String(),nullable=False))


def downgrade() -> None:
    op.drop_column('posts','content')
