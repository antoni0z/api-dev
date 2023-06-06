"""create posts table

Revision ID: 920075a8f604
Revises: 
Create Date: 2023-06-05 16:06:32.220070

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '920075a8f604'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('posts', sa.Column('id',sa.Integer(),nullable=False,primary_key=True), sa.Column('title',sa.String(),nullable=False))


def downgrade() -> None:
    op.drop_table('posts')
