from Crypto.Cipher import AES
import os

def encrypt_file(key, in_filename, out_filename=None, chunksize=64*1024):
    if not out_filename:
        out_filename = in_filename + '.enc'
    iv = os.urandom(16)
    encryptor = AES.new(key, AES.MODE_CBC, iv)
    filesize = os.path.getsize(in_filename)
    with open(in_filename, 'rb') as infile:
        with open(out_filename, 'wb') as outfile:
            outfile.write(filesize.to_bytes(8, byteorder='big'))
            outfile.write(iv)
            while True:
                chunk = infile.read(chunksize)
                if len(chunk) == 0:
                    break
                elif len(chunk) % 16 != 0:
                    chunk += b' ' * (16 - len(chunk) % 16)
                outfile.write(encryptor.encrypt(chunk))

def decrypt_file(key, in_filename, out_filename=None, chunksize=24*1024):
    if not out_filename:
        out_filename = os.path.splitext(in_filename)[0]
    with open(in_filename, 'rb') as infile:
        filesize = int.from_bytes(infile.read(8), byteorder='big')
        iv = infile.read(16)
        decryptor = AES.new(key, AES.MODE_CBC, iv)
        with open(out_filename, 'wb') as outfile:
            while True:
                chunk = infile.read(chunksize)
                if len(chunk) == 0:
                    break
                outfile.write(decryptor.decrypt(chunk))
            outfile.truncate(filesize)

def create_directory(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)
def copy_file(source_file, destination_file):
    with open(source_file, 'rb') as fsrc:
        with open(destination_file, 'wb') as fdst:
            while True:
                buf = fsrc.read(1024 * 1024)
                if not buf:
                    break
                fdst.write(buf)

def delete_file(filename):
    os.remove(filename)
key = b'Dake'
create_directory('data')
copy_file('test.txt', 'data/test.txt')
encrypt_file(key, 'data/test.txt', 'data/test.txt.enc')

delete_file('data/test.txt')


