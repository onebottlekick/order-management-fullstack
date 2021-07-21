"""empty message

Revision ID: 6897b302bda3
Revises: eb07c602b6f9
Create Date: 2021-07-21 18:34:27.121845

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6897b302bda3'
down_revision = 'eb07c602b6f9'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.create_unique_constraint(batch_op.f('uq_user_phone_number'), ['phone_number'])
        batch_op.create_unique_constraint(batch_op.f('uq_user_username'), ['username'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_constraint(batch_op.f('uq_user_username'), type_='unique')
        batch_op.drop_constraint(batch_op.f('uq_user_phone_number'), type_='unique')

    # ### end Alembic commands ###
