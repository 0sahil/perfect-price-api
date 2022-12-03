# from fastapi import Depends
# from fastapi.security import OAuth2PasswordBearer
# from app.database.models import User
#
# from firebase_admin import auth
#
#
# oauth2_scheme = OAuth2PasswordBearer(tokenUrl='token')
#
#
# async def current_user(token: str = Depends(oauth2_scheme)):
# 	payload = auth.verify_id_token(token)
# 	_email = payload.get('email')
# 	user = await User.get(email=_email)
# 	return user
