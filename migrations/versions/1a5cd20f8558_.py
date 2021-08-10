"""empty message

Revision ID: 1a5cd20f8558
Revises: 9d4452bf734c
Create Date: 2021-08-08 15:57:18.684855

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1a5cd20f8558'
down_revision = '9d4452bf734c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('artist', sa.Column('website_link', sa.String(length=120), nullable=True))
    op.add_column('artist', sa.Column('looking_for_venues', sa.Boolean(), nullable=True))
    op.add_column('artist', sa.Column('seeking_description', sa.String(length=500), nullable=True))
    op.add_column('venue', sa.Column('website_link', sa.String(length=120), nullable=True))
    op.add_column('venue', sa.Column('looking_for_talent', sa.Boolean(), nullable=True))
    op.add_column('venue', sa.Column('seeking_description', sa.String(length=500), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('venue', 'seeking_description')
    op.drop_column('venue', 'looking_for_talent')
    op.drop_column('venue', 'website_link')
    op.drop_column('artist', 'seeking_description')
    op.drop_column('artist', 'looking_for_venues')
    op.drop_column('artist', 'website_link')
    # ### end Alembic commands ###