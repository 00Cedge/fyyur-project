"""empty message

Revision ID: 2f840f350539
Revises: 5aa8a31d7434
Create Date: 2021-08-10 12:33:37.405635

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2f840f350539'
down_revision = '5aa8a31d7434'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('artist_genres')
    op.drop_table('venue_genres')
    op.drop_table('genre')
    op.add_column('artist', sa.Column('genres', sa.ARRAY(sa.String()), nullable=True))
    op.alter_column('artist', 'looking_for_venues', new_column_name='seeking_venues')
    op.add_column('venue', sa.Column('genres', sa.ARRAY(sa.String()), nullable=True))
    op.alter_column('venue', 'looking_for_talent', new_column_name='seeking_talent')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('venue', 'seeking_talent', new_column_name='looking_for_talent')
    op.drop_column('venue', 'genres')
    op.alter_column('artist', 'seeking_venue', new_column_name='looking_for_venues')
    op.drop_column('artist', 'genres')
    op.create_table('venue_genres',
    sa.Column('venue_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('genre_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['genre_id'], ['genre.id'], name='venue_genres_genre_id_fkey'),
    sa.ForeignKeyConstraint(['venue_id'], ['venue.id'], name='venue_genres_venue_id_fkey'),
    sa.PrimaryKeyConstraint('venue_id', 'genre_id', name='venue_genres_pkey')
    )
    op.create_table('artist_genres',
    sa.Column('artist_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('genre_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['artist_id'], ['artist.id'], name='Artist_genres_Artist_id_fkey'),
    sa.ForeignKeyConstraint(['genre_id'], ['genre.id'], name='Artist_genres_Genre_id_fkey'),
    sa.PrimaryKeyConstraint('artist_id', 'genre_id', name='Artist_genres_pkey')
    )
    op.create_table('genre',
    sa.Column('id', sa.INTEGER(), server_default=sa.text('nextval(\'"Genre_id_seq"\'::regclass)'), autoincrement=True, nullable=False),
    sa.Column('genre', sa.VARCHAR(length=50), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id', name='Genre_pkey')
    )
    # ### end Alembic commands ###
