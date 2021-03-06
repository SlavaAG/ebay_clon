"""added email to user

Revision ID: 007cf100de9a
Revises: d706b0e9f0d3
Create Date: 2019-04-18 19:56:54.140613

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '007cf100de9a'
down_revision = 'd706b0e9f0d3'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('email', sa.String(length=40), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'email')
    # ### end Alembic commands ###
