from fastapi import APIRouter, Query
from schemas.schemas import AccountSchema, ContactSchema
from models.models import AccountModel, ContactModel
from crud.crud import ContactOperations, AccountOperations
import datetime as dt
router = APIRouter()
contacts = {}


@router.get('/')
def home():
    return {'message':'Home'}

@router.get('/get-all-contacts')
def test():
    return {'message':'test'}

@router.post('/create-contact')
def create_contact(contact:ContactSchema):
    c_model = ContactModel()
    c_model.first_name = contact.first_name
    c_model.last_name = contact.last_name
    c_model.email = contact.email
    ops = ContactOperations()
    res = ops.create_contact(c_model)
    return res

@router.delete('/delete-contact')
def delete_contact(contact_id:int):
    ops = ContactOperations()
    res = ops.delete_contact(contact_id)
    return res
    

@router.post('/signin')
def sign_in(account:AccountSchema):
    a_model = AccountModel()
    a_model.email = account.email
    a_model.user_pwd = account.password
    ops = AccountOperations()
    res = ops.sign_in(a_model)
    return res

@router.post('/signup')
def sign_up(account:AccountSchema):
    a_model = AccountModel()
    a_model.email = account.email
    a_model.user_pwd = account.password
    a_model.created_on = dt.datetime.now()
    a_model.last_login = dt.datetime.now()
    a_model.login_attempts = 0
    ops = AccountOperations()
    res = ops.sign_up(a_model)
    return res