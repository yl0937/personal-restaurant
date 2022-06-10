"""empty message

Revision ID: 7a96d22536c3
Revises: 0bcb18cf80c1
Create Date: 2022-06-10 21:09:09.403893

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7a96d22536c3'
down_revision = '0bcb18cf80c1'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('pop', sa.Column('pop_restaurant_id', sa.Integer(), nullable=False))
    op.drop_constraint(None, 'pop', type_='foreignkey')
    op.create_foreign_key(None, 'pop', 'restaurant', ['pop_restaurant_id'], ['id'], ondelete='CASCADE')
    op.drop_column('pop', 'restaurant_id')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('pop', sa.Column('restaurant_id', sa.INTEGER(), nullable=False))
    op.drop_constraint(None, 'pop', type_='foreignkey')
    op.create_foreign_key(None, 'pop', 'restaurant', ['restaurant_id'], ['id'], ondelete='CASCADE')
    op.drop_column('pop', 'pop_restaurant_id')
    # ### end Alembic commands ###
