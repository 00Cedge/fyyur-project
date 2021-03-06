"""empty message

Revision ID: 9588982e4c5d
Revises: 86eb3039f2ba
Create Date: 2021-08-15 14:25:40.938413

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9588982e4c5d'
down_revision = '86eb3039f2ba'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('artist', 'website', new_column_name='website_link')
    op.alter_column('venue', 'website', new_column_name='website_link')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('artist', 'website_link', new_column_name='website')
    op.alter_column('venue', 'website_link', new_column_name='website')
    # ### end Alembic commands ###
