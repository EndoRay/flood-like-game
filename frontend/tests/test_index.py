import requests as req


def test_can_connect():
    r = req.get('http://localhost:5000')
    assert r.status_code == 200


def test_homepage_shows():
    r = req.get('http://localhost:5000')
    assert 'Home' in r.text

    
def rooms():
return render_template("templates/rooms.html")
