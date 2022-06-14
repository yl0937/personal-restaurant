"""empty message

Revision ID: 484f022e2566
Revises: f3c8c8abc0c7
Create Date: 2022-06-14 16:36:20.848339

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '484f022e2566'
down_revision = 'f3c8c8abc0c7'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('poped',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('restaurant_id', sa.Integer(), nullable=False),
    sa.Column('detail_restaurant', sa.String(length=100), nullable=False),
    sa.ForeignKeyConstraint(['restaurant_id'], ['restaurant.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('poped')
    # ### end Alembic commands ###
