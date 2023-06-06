"""Add foreign key to post table

Revision ID: 9c45a3f553bf
Revises: dec0b8f322ad
Create Date: 2023-06-05 16:51:40.842614

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9c45a3f553bf'
down_revision = 'dec0b8f322ad'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts',sa.Column('owner_id',sa.Integer(),nullable=False))
    op.create_foreign_key('post_users_fk',source_table = "posts", referent_table="users", local_cols = ['owner_id'], remote_cols= ['id'], ondelete="CASCADE")


def downgrade() -> None:
    op.drop_constraint('post_users_fk',table_name='posts')
    op.drop_column('posts','owner_id')