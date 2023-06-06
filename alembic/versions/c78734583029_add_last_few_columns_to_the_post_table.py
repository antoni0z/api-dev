"""Add last few columns to the post table

Revision ID: c78734583029
Revises: 9c45a3f553bf
Create Date: 2023-06-05 16:56:30.137228

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c78734583029'
down_revision = '9c45a3f553bf'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts',
    sa.Column('published',sa.Boolean(),nullable=False, server_default='TRUE'),)
    op.add_column('posts',sa.Column('created_at',sa.TIMESTAMP(timezone=True),nullable=False, server_default=sa.text('NOW()')))



def downgrade() -> None:
    op.drop_column('posts','published')
    op.drop_column('posts','created_at')
