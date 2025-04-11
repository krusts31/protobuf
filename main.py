import sys 
import account_pb2 as account_pb

def account():
	return account_pb.Account(
		id=42,
		name='Linus_Torvals',
		is_verified=True,
		follow_ids=[0,1]
	)
	

if __name__ == '__main__':
	fns = {
		'account': account	
	}
	if len(sys.argv) != 2:
		print(f'Usage: main.py [{"|".join(fns)}]')
		sys.exit()
	fn = fns.get(sys.argv[1], None)
	if not fn:
		print(f'Unkown functions: \"{sys.argv[1]}\"')
		sys.exit()
	print(fn())
