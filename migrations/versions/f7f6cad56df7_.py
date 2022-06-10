"""empty message

Revision ID: f7f6cad56df7
Revises: 7926893f7d6e
Create Date: 2022-06-10 21:17:47.246170

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f7f6cad56df7'
down_revision = '7926893f7d6e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('pop', 'pop_restaurant_id',
               existing_type=sa.INTEGER(),
               nullable=True)
    op.drop_constraint(None, 'pop', type_='foreignkey')
    op.create_foreign_key(None, 'pop', 'restaurant', ['pop_restaurant_id'], ['id'], ondelete='CASCADE')
    op.drop_column('pop', 'restaurant_id')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('pop', sa.Column('restaurant_id', sa.INTEGER(), nullable=False))
    op.drop_constraint(None, 'pop', type_='foreignkey')
    op.create_foreign_key(None, 'pop', 'restaurant', ['restaurant_id'], ['id'], ondelete='CASCADE')
    op.alter_column('pop', 'pop_restaurant_id',
               existing_type=sa.INTEGER(),
               nullable=False)
    # ### end Alembic commands ###