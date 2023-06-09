"""Add phone number to the Users table

Revision ID: 4935319c1631
Revises: 4dc48237a0e6
Create Date: 2023-06-05 17:34:35.616492

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4935319c1631'
down_revision = '4dc48237a0e6'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('phone_number', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'phone_number')
    # ### end Alembic commands ###
