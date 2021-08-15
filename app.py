#----------------------------------------------------------------------------#
# Imports
#----------------------------------------------------------------------------#

import sys
import json
import dateutil.parser
import babel
from flask import Flask, render_template, request, Response, redirect, url_for, flash
import logging
from logging import Formatter, FileHandler
from flask_wtf import FlaskForm
from forms import *
from models import *


#----------------------------------------------------------------------------#
# Filters.
#----------------------------------------------------------------------------#

def format_datetime(value, format='medium'):
  date = dateutil.parser.parse(value)
  if format == 'full':
      format="EEEE MMMM, d, y 'at' h:mma"
  elif format == 'medium':
      format="EE MM, dd, y h:mma"
  return babel.dates.format_datetime(date, format, locale='en')

app.jinja_env.filters['datetime'] = format_datetime

#----------------------------------------------------------------------------#
# Controllers.
#----------------------------------------------------------------------------#

@app.route('/')
def index():
  return render_template('pages/home.html')

#  Venues
#  ----------------------------------------------------------------

@app.route('/venues')
def venues():  
  venues = Venue.query.all()
  return render_template('pages/venues.html', areas=venues);

@app.route('/venues/search', methods=['POST'])
def search_venues():
  search = request.form.get('search_term')
  response = Venue.query.filter(Venue.name.ilike(f'%{search}%'))

  return render_template('pages/search_venues.html', results=response, search_term=request.form.get('search_term', ''))

@app.route('/venues/<int:venue_id>')
def show_venue(venue_id):
  shows = Show.query.filter_by(venue_id=venue_id).all()
  venue = Venue.query.get(venue_id)
  data = []
  past_shows = []
  upcoming_shows = []
  for show in shows:
      temp_show = {
          'artist_id': show.artist_id,
          'artist_name': show.artist.name,
          'artist_image_link': show.artist.image_link,
          'start_time': str(show.start_time),
      }
      if show.start_time <= datetime.now():
          past_shows.append(temp_show)
      else:
          upcoming_shows.append(temp_show)
      data.append(temp_show)

  data = {
    'id': venue.id,
    'name': venue.name,
    'city': venue.city,
    'phone': venue.phone,
    'genres':venue.genres,
    'facebook_link':venue.facebook_link,
    'website_link':venue.website_link,
    'image_link': venue.image_link,
    'seeking_talent':venue.seeking_talent,
    'seeking_description':venue.seeking_description,
    'upcoming_shows':upcoming_shows,
    'past_shows':past_shows,
    'past_shows_count': len(past_shows),
    'upcoming_shows_count': len(upcoming_shows)
}

  print(data)

  return render_template('pages/show_venue.html', venue=data)

#  Create Venue
#  ----------------------------------------------------------------

@app.route('/venues/create', methods=['GET'])
def create_venue_form():
  form = VenueForm()
  return render_template('forms/new_venue.html', form=form)

@app.route('/venues/create', methods=['POST'])
def create_venue_submission():
  
  try:
    form = VenueForm(request.form)
    print(form.name)
    print(form.city)
    print(form.genres)
    venueform = Venue(
      name=form.name.data,
      city=form.city.data,
      state=form.state.data,
      address=form.address.data,
      phone=form.phone.data,
      image_link=form.image_link.data,
      genres=form.genres.data,
      facebook_link=form.facebook_link.data,
      website_link=form.website_link.data,
      seeking_talent=form.seeking_talent.data,
      seeking_description=form.seeking_description.data,
    )
    db.session.add(venueform)
    db.session.commit()
    flash('Venue ' + request.form['name'] + ' was successfully listed!')
  except: 
    db.session.rollback()
    flash('An error occurred. Venue ' + request.form['name'] + ' could not be listed.')
    print(sys.exc_info())
  finally:
    db.session.close()
  return render_template('pages/home.html')

@app.route('/venues/<venue_id>', methods=['POST'])
def delete_venue(venue_id):
    try:
        venue = Venue.query.filter_by(id=venue_id).first_or_404()
        db.session.delete(venue)
        db.session.commit()
        flash('The venue has been removed together with all of its shows.')
        return render_template('pages/home.html')
    except ValueError:
        db.session.rollback()
        print(sys.exc_info())
        flash('It was not possible to delete this Venue')
    finally:
        db.session.close()
    return redirect(url_for('venues'))

#  Artists
#  ----------------------------------------------------------------

@app.route('/artists')
def artists():
  data = Artist.query.all()
  return render_template('pages/artists.html', artists=data)

@app.route('/artists/search', methods=['POST'])
def search_artists():
  search = request.form.get('search_term')
  response = Artist.query.filter(Artist.name.ilike(f'%{search}%'))

  return render_template('pages/search_artists.html', results=response, search_term=request.form.get('search_term', ''))

@app.route('/artists/<int:artist_id>')
def show_artist(artist_id):
  shows = Show.query.all()
  artist = Artist.query.get(artist_id)
  data = []
  past_shows = []
  upcoming_shows = []
  for show in shows:
      temp_show = {
          'venue_id': show.venue_id,
          'venue_name': show.venue.name,
          'venue_image_link': show.venue.image_link,
          'start_time': str(show.start_time),
      }
      if show.start_time <= datetime.now():
          past_shows.append(temp_show)
      else:
          upcoming_shows.append(temp_show)
      data.append(temp_show)
  data = {
    'id': artist.id,
    'name': artist.name,
    'city': artist.city,
    'state': artist.state,
    'phone': artist.phone,
    'genres':artist.genres,
    'facebook_link':artist.facebook_link,
    'website_link':artist.website_link,
    'image_link': artist.image_link,
    'seeking_venue':artist.seeking_venue,
    'seeking_description':artist.seeking_description,
    'upcoming_shows':upcoming_shows,
    'past_shows':past_shows,
    'past_shows_count': len(past_shows),
    'upcoming_shows_count': len(upcoming_shows)
}
  return render_template('pages/show_artist.html', artist=data)


@app.route('/artist/<artist_id>', methods=['POST'])
def delete_artist(artist_id):
    try:
        artist = Artist.query.filter_by(id=artist_id).first_or_404()
        db.session.delete(artist)
        db.session.commit()
        flash('The artist has been removed together with all of its shows.')
        return render_template('pages/home.html')
    except ValueError:
        db.session.rollback()
        print(sys.exc_info())
        flash('It was not possible to delete this Artist')
    finally:
        db.session.close()
    return redirect(url_for('artists'))


#  Update
#  ----------------------------------------------------------------
@app.route('/artists/<int:artist_id>/edit', methods=['GET'])
def edit_artist(artist_id):
  form = ArtistForm(request.form)
  artist = Artist.query.filter_by(id=artist_id).first_or_404()
  form = ArtistForm(obj=artist)
  return render_template('forms/edit_artist.html', form=form, artist=artist)


@app.route('/artists/<int:artist_id>/edit', methods=['POST'])
def edit_artist_submission(artist_id):
  artist = Artist.query.get(artist_id)
  form = ArtistForm(request.form)
  try:
    form.populate_obj(artist)
    db.session.commit()
    print("Print value!!!!!!", request.form['seeking_venue'])
    flash('Artist ' + request.form['name'] + ' was successfully edited!')
  except:
    db.session.rollback()
    flash('An error occurred. Artist ' + request.form['name'] + ' could not be updated.')
    print(sys.exc_info())
  finally:
    db.session.close()
  return redirect(url_for('show_artist', artist_id=artist_id))


@app.route('/venues/<int:venue_id>/edit', methods=['GET'])
def edit_venue(venue_id):
  form = VenueForm(request.form)
  venue = Venue.query.filter_by(id=venue_id).first_or_404()
  form = VenueForm(obj=venue)
  return render_template('forms/edit_venue.html', form=form, venue=venue)


@app.route('/venues/<int:venue_id>/edit', methods=['POST'])
def edit_venue_submission(venue_id):
  venue = Venue.query.get(venue_id)
  form = VenueForm(request.form)
  try:
    form.populate_obj(venue)
    db.session.commit()
    flash('Venue ' + request.form['name'] + ' was successfully edited!')
  except:
    db.session.rollback()
    flash('An error occurred. Venue ' + request.form['name'] + ' could not be updated.')
    print(sys.exc_info())

  finally:
    db.session.close()
  return redirect(url_for('show_venue', venue_id=venue_id))

#  Create Artist
#  ----------------------------------------------------------------

@app.route('/artists/create', methods=['GET'])
def create_artist_form():
  form = ArtistForm()
  return render_template('forms/new_artist.html', form=form)

@app.route('/artists/create', methods=['POST'])
def create_artist_submission():
  try:
    form = ArtistForm(request.form)
    artistform = Artist(
      name=form.name.data,
      city=form.city.data,
      state=form.state.data,
      phone=form.phone.data,
      image_link=form.image_link.data,
      genres=form.genres.data,
      facebook_link=form.facebook_link.data,
      website_link=form.website_link.data,
      seeking_venue=form.seeking_venue.data,
      seeking_description=form.seeking_description.data,
    )
    db.session.add(artistform)
    db.session.commit()
    flash('Artist ' + request.form['name'] + ' was successfully listed!')
  except: 
    db.session.rollback()
    flash('An error occurred. Artist ' + request.form['name'] + ' could not be listed.')
    print(sys.exc_info())
  finally:
    db.session.close()
  return render_template('pages/home.html')


#  Shows
#  ----------------------------------------------------------------

@app.route('/shows')
def shows():
  data = []
  shows = Show.query.all()
  for show in shows:
    showObj = {"venue_id": show.venue_id,
    "venue_name": show.venue.name,
    "artist_id": show.artist_id,
    "artist_name": show.artist.name,
    "artist_image_link": show.artist.image_link,
    "start_time": str(show.start_time)
    }
    data.append(showObj)
  return render_template('pages/shows.html', shows=data)


@app.route('/shows/create')
def create_shows():
  # renders form. do not touch.
  form = ShowForm()
  return render_template('forms/new_show.html', form=form)


@app.route('/shows/create', methods=['POST'])
def create_show_submission():
  try:
    form = ShowForm(request.form)
    showform = Show(
      artist_id=form.artist_id.data,
      venue_id=form.venue_id.data,
      start_time=form.start_time.data,
    )
    db.session.add(showform)
    db.session.commit()
    flash('Show was successfully listed!')
  except: 
    db.session.rollback()
    flash('An error occurred. Show could not be listed.')
    print(sys.exc_info())
  finally:
    db.session.close()
  return render_template('pages/home.html')


@app.errorhandler(404)
def not_found_error(error):
    return render_template('errors/404.html'), 404


@app.errorhandler(500)
def server_error(error):
    return render_template('errors/500.html'), 500


if not app.debug:
    file_handler = FileHandler('error.log')
    file_handler.setFormatter(
        Formatter('%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]')
    )
    app.logger.setLevel(logging.INFO)
    file_handler.setLevel(logging.INFO)
    app.logger.addHandler(file_handler)
    app.logger.info('errors')

#----------------------------------------------------------------------------#
# Launch.
#----------------------------------------------------------------------------#

# Default port:
if __name__ == '__main__':
    app.run()

# Or specify port manually:
'''
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
'''
