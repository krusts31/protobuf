import sys 
import account_pb2 as account_pb
import user_pb2 as user_pb

def account():
	return account_pb.Account(
		id=42,
		name='Linus_Torvals',
		is_verified=True,
		follow_ids=[0,1]
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
	

if __name__ == '__main__':
	fns = {
		'account': account,
		'user': user,
		'user2': user2,
	}
	if len(sys.argv) != 2:
		print(f'Usage: main.py [{"|".join(fns)}]')
		sys.exit()
	fn = fns.get(sys.argv[1], None)
	if not fn:
		print(f'Unkown functions: \"{sys.argv[1]}\"')
		sys.exit()
	print(fn())
