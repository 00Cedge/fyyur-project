"""empty message

Revision ID: 86eb3039f2ba
Revises: ae1db0713b55
Create Date: 2021-08-14 15:33:55.159484

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '86eb3039f2ba'
down_revision = 'ae1db0713b55'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('show', 'artist_id',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.alter_column('show', 'venue_id',
               existing_type=sa.INTEGER(),
               nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('show', 'venue_id',
               existing_type=sa.INTEGER(),
               nullable=True)
    op.alter_column('show', 'artist_id',
               existing_type=sa.INTEGER(),
               nullable=True)
    # ### end Alembic commands ###
