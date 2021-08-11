"""empty message

Revision ID: 450fd63efe40
Revises: 30c6226237ce
Create Date: 2021-08-10 16:25:37.612100

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '450fd63efe40'
down_revision = '30c6226237ce'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('show', 'date', new_column_name='start_time')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
   op.alter_column('show', 'start_time', new_column_name='date')
    # ### end Alembic commands ###