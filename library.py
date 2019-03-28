"""A set of libraries that are useful to both the proxy and regular servers."""

# This code uses Python 2.7. These imports make the 2.7 code feel a lot closer
# to Python 3. (They're also good changes to the language!)
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

# THe Python socket API is based closely on the Berkeley sockets API which
# was originally written for the C programming language.
#
# https://en.wikipedia.org/wiki/Berkeley_sockets
#
# The API is more flexible than you need, and it does some quirky things to
# provide that flexibility. I recommend tutorials instead of complete
# descriptions because those can skip the archaic bits. (The API was released
# more than 35 years ago!)
import socket
import time

# Read this many bytes at a time of a command. Each socket holds a buffer of
# data that comes in. If the buffer fills up before you can read it then TCP
# will slow down transmission so you can keep up. We expect that most commands
# will be shorter than this.
COMMAND_BUFFER_SIZE = 256


def CreateServerSocket(port):

  s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  s.bind(('', port))
  print("Listening to server: ")
  s.listen(10)

  return s;

def ConnectClientToServer(server_sock):
  print("Connecting Client To Server!")
  conn, (addr, port) = server_sock.accept()
  return conn, (addr, port)



def CreateClientSocket(server_addr, port):

  print("Creating Client Socket")
  s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  s.connect((server_addr, port))

  return s;


def ReadCommand(sock):

  command = ''

  while not command or command[-1] != '\n':
    command += sock.recv(COMMAND_BUFFER_SIZE);

  return command.strip()



def ParseCommand(command):

  args = command.strip().split(' ')
  command = None
  if args:
    command = args[0]
  arg1 = None
  if len(args) > 1:
    arg1 = args[1]
  remainder = None
  if len(args) > 2:
    remainder = ' '.join(args[2:])
  return command, arg1, remainder


class KeyValueStore(object):

  def __init__(self):

    print("Init")

#Main dictionary to be used when using the Telnet connection
    self.myDict = {}

  def GetValue(self, key, max_age_in_sec=None):

    print("Get Values")
    return self.myDict.get(key)



  def StoreValue(self, key, value):

    ###########################################
    #TODO: Implement StoreValue Function
    ###########################################
    print("Store Values")
    self.myDict[key] = value


  def Keys(self):
    """Returns a list of all keys in the datastore."""

    ###########################################
    #TODO: Implement Keys Function
    ###########################################
    print("Printing Keys")
    for key in self.myDict:
        self.listKeys.append(key)

    return self.listKeys
