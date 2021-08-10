"""empty message

Revision ID: 32344f3d6805
Revises: d185c53de535
Create Date: 2021-08-10 16:49:06.893920

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '32344f3d6805'
down_revision = 'd185c53de535'
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
