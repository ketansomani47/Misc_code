from application import application
import pytest
from setup import create_app

# @pytest.fixture()
# def app():
#     app = create_app()
#     app.config.update({
#         "TESTING": True,
#     })
#     yield app
#
# @pytest.fixture()
# def client(app):
#     return app.test_client()
import json
mimetype = 'application/json'
headers = {
    'Content-Type': mimetype,
    'Accept': mimetype
}
def test_add_user():
    response = application.test_client().post('/user/post', data=json.dumps({"Name": "aaa1", "Email": "aa1.aa@nagarro.com", "Age": "2"}), headers=headers)
    print(response.data)
    # application.test_client()
    # assert response.status_code == 201
    assert response.json["message"] == "User Added Successfully"

def test_get_user():
    response = application.test_client().get('/user/get')
    print(response.data)
    assert response.status_code == 200

@pytest.mark.parametrize("id",[6])
def test_update(id):
    rv = application.test_client().put('/user/update/{}'.format(id), data=json.dumps({"Name": "update", "Email": "aa1.update@nagarro.com", "Age": "21"}), headers=headers)
    print(rv.data)
    assert rv.status_code == 200

@pytest.mark.parametrize("id",[5])
def test_delete(id):
    rv = application.test_client().delete('/user/delete/{}'.format(id))
    print(rv.data)
    assert rv.status_code == 200

