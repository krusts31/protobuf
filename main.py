import sys 
import account_pb2 as account_pb
import user_pb2 as user_pb
import product_pb2 as product_pb
import phone_book_pb2 as phone_book_pb
import login_pb2 as login_pb
import google.protobuf.duration_pb2 as duration_pb
import google.protobuf.timestamp_pb2 as timestamp_pb
import google.protobuf.field_mask_pb2 as field_mask_pb
import google.protobuf.wrappers_pb2 as wrappers_pb
from google.protobuf import json_format
import datetime

def durration():
	return duration_pb.Duration(
		seconds=3,
		nanos=0
	)

def durration2():
	td = datetime.timedelta(days=3, minutes=3, microseconds=15)
	d = duration_pb.Duration()
	d.FromTimedelta(td)
	return d
	

def login_error():
	return login_pb.LoginResult(
		error="Ther username is incorect"
	)

def login_success():
	return login_pb.LoginResult(
		token=login_pb.Token()
	)

def phone_book():
	return phone_book_pb.PhoneBook(
		phones={
			'Linux Tox': '12341234234',
			'Testing': '12341234234'
		}
	)

def phone_book2():
	book = phone_book_pb.PhoneBook()
	book.phones['Linux Tox'] = "21341234";
	book.phones['Dudes'] = "123412342134123";
	return book

def account():
	return account_pb.Account(
		id=42,
		name='Linus_Torvals',
		is_verified=True,
		follow_ids=[0,1]
	)

def product():
	return product_pb.Product(
		id=42,
		type=product_pb.ProductType.PANTS,# you can also use the tag = 1;
	)

def user():
	return user_pb.User(
		id=42,
		name='Linus_Torvals',
		follows=[
			user_pb.User(id=0, name="Linux Foundation"),
			user_pb.User(id=1, name="Dude Nukem"),
		]
	)

def user2():
	u = user_pb.User()
	u.id = 42
	u.name = 'Linux Tox'
	u.follows.add(id=0, name="Linux Foundation")
	u.follows.add(id=1, name="Dan Blizzard")
	return u

def timestamp():
	t = timestamp_pb.Timestamp()
	t.GetCurrentTime()
	return t

def field_mask():
	acc = account()
	fm = field_mask_pb.FieldMask(
		paths=[
			'id',
			'is_verified'
		]
	)
	iiv = account_pb.Account()
	fm.MergeMessage(acc, iiv)
	return iiv

def field_mask2():
	mask = field_mask_pb.FieldMask()
	mask.FromJsonString('id,name')
	mask2 = field_mask_pb.FieldMask()
	mask2.FromJsonString('id,isVerified')
	mask3 = field_mask_pb.FieldMask()
	mask3.Union(mask, mask2)
	acc = account()
	iniv = account_pb.Account()
	mask3.MergeMessage(acc, iniv)
	return iniv

def wrapper():
	return [
		wrappers_pb.BoolValue(value=True),
		wrappers_pb.BytesValue(value=b'these are bytes'),
		wrappers_pb.FloatValue(value=42.0),
	]

def file():
	acc = account()
	path = 'account.bin'
	print('--Write to file--')
	print(acc)
	with open(path, 'wb') as f:
		bytes_str = acc.SerializeToString()
		f.write(bytes_str)
	print('--Read From file--')
	with open(path, 'rb') as f:
		acc = account_pb.Account().FromString(f.read())
	print(acc)

def to_json(message):
	return json_format.MessageToJson(
		message,
		indent=None,
		preserving_proto_field_name=True
	)

def from_json(json_str, type):
	return json_format.Parse(
		json_str,
		type(),
		ignore_unknown_fields=True
	)
	
def json():
	acc = account()
	json_str = to_json(acc)
	print(json_str)
	print('------------')
	print(from_json(json_str, account_pb.Account))
	print('------------')
	print(from_json('{"id": 42, "lolol": "lol"}', account_pb.Account))

if __name__ == '__main__':
	fns = {
		'account': account,
		'user': user,
		'user2': user2,
		'product': product,
		'phone': phone_book,
		'phone2': phone_book2,
		'login_error': login_error,
		'login_token': login_success,
		'durration': durration,
		'durration2': durration2,
		'timestamp': timestamp,
		'field_mask': field_mask,
		'field_mask2': field_mask2,
		'wrapper': wrapper,
		'file': file,
		'json': json,
	}
	if len(sys.argv) != 2:
		print(f'Usage: main.py [{"|".join(fns)}]')
		sys.exit()
	fn = fns.get(sys.argv[1], None)
	if not fn:
		print(f'Unkown functions: \"{sys.argv[1]}\"')
		sys.exit()
	print(fn())
