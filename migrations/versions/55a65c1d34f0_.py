"""empty message

Revision ID: 55a65c1d34f0
Revises: 28c8ae8113a7
Create Date: 2018-04-27 05:16:23.159985

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '55a65c1d34f0'
down_revision = '28c8ae8113a7'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('phonenumber', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'phonenumber')
    # ### end Alembic commands ###