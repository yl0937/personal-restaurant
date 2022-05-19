"""empty message

Revision ID: 1d81241c3745
Revises: 157d8be97279
Create Date: 2022-05-18 15:43:23.651981

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1d81241c3745'
down_revision = '157d8be97279'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('reservation', sa.Column('peoplenum', sa.Integer(), server_default='1', nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('reservation', 'peoplenum')
    # ### end Alembic commands ###
