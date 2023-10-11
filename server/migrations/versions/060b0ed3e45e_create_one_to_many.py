"""create one-to-many

Revision ID: 060b0ed3e45e
Revises: f94967fddc40
Create Date: 2023-03-16 08:25:08.489327

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '060b0ed3e45e'
down_revision = 'f94967fddc40'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('articles', schema=None) as batch_op:
        batch_op.add_column(sa.Column('user_id', sa.Integer(), nullable=True))
        batch_op.create_foreign_key(batch_op.f('fk_articles_user_id_users'), 'users', ['user_id'], ['id'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('articles', schema=None) as batch_op:
        batch_op.drop_constraint(batch_op.f('fk_articles_user_id_users'), type_='foreignkey')
        batch_op.drop_column('user_id')

    # ### end Alembic commands ###
