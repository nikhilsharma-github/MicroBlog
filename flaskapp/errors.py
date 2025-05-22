from flask import render_template 
from flaskapp import app, db 

# Using Error Handling pages on showing errors 
# 404 Error Handling Page 
@app.errorhandler(404)
def not_found_error(error):
    return render_template('404.html'), 404


# 500 Error Handling Page 
@app.errorhandler(500)
def internal_error(error):
    db.session.rollback()
    return render_template('500.html'), 500