import time, sys
import re

status =''
S = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
l = len(S)

#Functions
def validate_status():
	m = input('Please Enter the mode | 0 For Encrypt / 1 for Decrypt ')
	if m == '0' :
		st = 'encrypt'
	elif  m == '1' :
		st = 'decrypt'
	else :
		m = input('Invalid Value, again | Type: 0 For Encrypt / Type: 1 for Decrypt ')
	return st

def checkKey(k):
	kl = list(k)
	kl.sort()
	sl = list(S)
	sl.sort()
	if not (kl == sl):
		sys.exit('!! There is an problem in the key or symbols list !!')


def subs_enc(msg, k, S):
	msg_encypted = ''
	for c in msg:
		if c.upper() in S: # Only characters in 'S' 
			c_index = S.index(c.upper()) # Character's index
			if c.isupper():
				msg_encypted += k[c_index].upper()
			else:
				msg_encypted += k[c_index].lower()
		else :
			msg_encypted += c 
	return msg_encypted

def subs_dec(msg, k, S):
	msg_decypted = ''
	k, S = S, k
	for c in msg:
		if c.upper() in S: # Only characters in 'S' 
			c_index = S.index(c.upper()) # Character's index
			if c.isupper():
				msg_decypted += k[c_index].upper()
			else:
				msg_decypted += k[c_index].lower()
		else :
			msg_decypted += c 
	return msg_decypted

def subs_cipher(msg, k, st):
	if st == 'encrypt':
		res = subs_enc(msg, k, S)
	elif st == 'decrypt':
		res = subs_dec(msg, k, S)
	return res


#Main

def Main():
	print("********* THE SUBSTITUTION CIPHER || Encypting & Decrypting **********")
	print('++++++++++++++++++++++++++++ How it works ? ++++++++++++++++++++++++++')
	print('+++ The Key must contain letters that are in the symbols list ++++++++')
	print('+++ In this script, I used English letters with length = 26 ++++++++++')
	print('+++ So, the Key must contains all the English letters and its length = 26 ++++++')
	status = validate_status() # Encypting or Decrypting
	print('\n')
	key = input('Please Enter your Key ')
	print('\n')
	checkKey(key)
	msg = input('Please Enter your Message : ')
	print('\n')
	# Infos
	print('-------------All in All------------------')
	print('List of symbols : %s ' %S )
	print('\n')
	print('Mode is : %s ' %status )
	print('\n')
	print('Key is : %s ' %key )
	print('\n')
	print('Your message is : %s ' %msg )
	print('\n')
	print('------------------------------------------')
	print('\n')
	# Continue ?
	print('You want to continue ? (Y)es or (N)o ?')
	response = input('> ')
	if not response.lower().startswith('y'):
		sys.exit()
	#
	print('Processing now ...' )
	timer = time.time()
	r = subs_cipher(msg, key, status)
	t = round(time.time() - timer, 2)
	print('The result is : %s' %r)
	print('\n')
	print('------------- SUMMARY ---------------------')
	print('List of symbols : %s ' %S )
	print('\n')
	print('Mode is : %s ' %status )
	print('\n')
	print('Key is : %s ' %key )
	print('\n')
	print('Your message is : %s ' %msg )
	print('\n')
	print('The result is : %s ' %r )
	print('\n')
	print('Process time : %s ' %t )
	print('\n')
	print('-------------------------------------------')
	
if __name__ == '__main__':
 	Main()