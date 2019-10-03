"""
Eth-Teacher Multi Hash
Skrypt
Copyright (C) 2018 Skryptek
 
This program is for informational testing purposes ONLY.
@ Dev Needs Pickle Login / Save / Load Features
@ Dev ^^ Don't Think We Need This.
"""
global THOUGHT_SPEED
THOUGHT_RATE = 0.0
print(''' Welcome To Eth Learner Please Be Patient While I Import The Following Modules And Packages.''')
################ Import Section #############################################
try:
 print('Attempting To Import [os] Module.')
 import os
except Exception as bad_os_mod:
 print('Error Importing [os] Module. Instructing Program To Exit.')
 print('Error: '+str(bad_os_mod))
 exit()

try:
 print('Attempting To Import [argparse] Module.')
 import argparse
except Exception as bad_argparse_mod:
 print('Error Importing [argparse] Module. Instructing Program To Exit.')
 print('Error: '+str(bad_argparse_mod))
 exit()

try:
 print('Attempting To Import [binascii] Module.')
 import binascii
except Exception as bad_binascii_mod:
 print('Error Importing [binascii] Module. Instructing Program To Exit.')
 print('Error: '+str(bad_binascii_mod))
 exit()

try:
 print('Attempting To Import [sha3] Module.')
 import sha3
except Exception as bad_sha3_mod:
 print('Error Importing [sha3] Module. Instructing Program To Exit.')
 print('Error: '+str(bad_sha3_mod))
 exit()
 
try:
 print('Attempting To Import [time] Module.')
 import time
except Exception as bad_time_mod:
 print('Error Importing [time] Module. Instructing Program To Exit.')
 print('Error: '+str(bad_time_mod))
 exit()

try:
 print('Attempting To Import [string] Module.')
 import string
except Exception as bad_string_mod:
 print('Error Importing [string] Module. Instructing Program To Exit.')
 print('Error: '+str(bad_string_mod))
 exit()

try:
 print('From [ecdsa] Attempting To Import [SigningKey, SECP256k1] Methods.')
 from ecdsa import SigningKey, SECP256k1
except Exception as bad_ecdsa_mod:
 print('Error Importing [SigningKey, SECP256k1] Methods From [ecdsa] Module. Instructing Program To Exit.')
 print('Error: '+str(bad_ecdsa_mod))
 exit()

try:
 print('Attempting To Import [pickle] Module.')
 import pickle
 try_pickle = True
except Exception as bad_pickle_mod:
 print('Error Importing [pickle] Module. Instructing Program To Turn Off Pickle DB.')
 print('Error: '+str(bad_pickle_mod))
 try_pickle = False

try:
 print('From [bitcoin] Attempting To Import [sha256] Method.')
 from bitcoin import sha256 as sha
except Exception as bad_btcsha_mod:
 print('Error Importing [sha256] Method From [bitcoin] Module. Instructing Program To Exit.')
 print('Error: '+str(bad_btcsha_mod))
 exit()

try:
 os.mkdir('./System Memory/')
except Exception:
 pass

################ Objectt Section #############################################


class TeachVivEthereum():
 def __init__(self):
  print('Setting Up Data and Live Connections Now')
  self.open_data_container()
  self.set_constant_storage()
  self._set_database()
  self.setup_menu()
  
 def open_data_container(self):
  global data_storage
  data_storage = dict()

 def set_constant_storage(self):
  global data_storage
  global learned_this_session
  data_storage['file_num'] = 0
  data_storage['stop_point'] = 10
  data_storage['start_time'] = time.localtime()
  data_storage['chars'] = dict()
  data_storage['record file'] = dict()
  data_storage['btc file'] = dict()
  data_storage['last int file'] = dict()
  data_storage['chars']['menu'] = dict()
  data_storage['chars']['menu']['item 1'] = list("0123456789")
  data_storage['chars']['menu']['item 1 size'] = len(data_storage['chars']['menu']['item 1'])
  data_storage['chars']['menu']['item 2'] = list("0123456789abcdef")
  data_storage['chars']['menu']['item 2 size'] = len(data_storage['chars']['menu']['item 2'])
  data_storage['chars']['menu']['item 3'] = list("!@#$%^&*()")
  data_storage['chars']['menu']['item 3 size'] = len(data_storage['chars']['menu']['item 3'])
  data_storage['chars']['menu']['item 4'] = list("0abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#0123456789")[:66]
  data_storage['chars']['menu']['item 4 size'] = len(data_storage['chars']['menu']['item 4'])
  data_storage['chars']['menu']['item 5'] = list(string.printable)[:]
  data_storage['chars']['menu']['item 5 size'] = len(data_storage['chars']['menu']['item 5'])
  data_storage['constant_pointer'] = 0
  data_storage['clear_pointer'] = 0
  data_storage['solved'] = False
  data_storage['digits'] = list()
  data_storage['length capacity'] = 14
  learned_this_session = 0

 def update_time(self):
  global our_clock
  timed = time.localtime()
  our_clock = str(timed[1])+'/'+str(timed[2])+'/'+str(timed[0])+' '+str(timed[3])+':'+str(timed[4])+':'+str(timed[5])
  

 def _set_database(self):
  global DATABASE_PATH
  global SYSTEM_MEMORY_PATH
  global EthBrain_System
  self.update_time()

  SYSTEM_MEMORY_PATH = './System Memory/EthBrain-System.vnm'
  try:
   print('Trying to import Pickle Ethereum Brain System DB File From Memory Directory Just A Moment.')
   EthBrain_System = pickle.load(open(SYSTEM_MEMORY_PATH,'rb'))
  except Exception as E:
   print('Need To System Unit For Ethereum Brain Just A Moment')
   EthBrain_System = dict() 
   EthBrain_System['Total Files Consumed'] = 0
   EthBrain_System['Neural Units'] = 0
   EthBrain_System['Hard Cells'] = 0
   EthBrain_System['Checks Cleared'] = 0
   EthBrain_System['Total Learned'] = 0
   EthBrain_System['Total Links'] = 0
   EthBrain_System['Creation Date'] = ''
   if EthBrain_System['Neural Units'] == 0:
    EthBrain_System['Creation Date'] = our_clock
   pickle.dump(EthBrain_System, open(SYSTEM_MEMORY_PATH,'wb'))
  
 def setup_menu(self):
  global data_storage
  data_storage['chars']['current'] = data_storage['chars']['menu']['item 5']
  data_storage['chars']['base'] = len(data_storage['chars']['current'])
  data_storage['chars']['size'] = data_storage['chars']['menu']['item 5 size']
  try:
   starting_at = pickle.load(open('./System Memory/EnglishKeyboard.vnm','rb'))
  except Exception:
   starting_at = 0
   pickle.dump(starting_at,open('./System Memory/EnglishKeyboard.vnm','wb'))
  try:
   int_check = int(starting_at) + 1
   data_storage['constant_pointer'] = int(starting_at)
   self.start_lesson()
  except Exception as NI:
   print('You Need To Start With An Integer Returning To Setup Menu')
   print(starting_at)
   print('Error: '+str(NI))
   self.setup_menu()
 
 def numberToBase(self, cont_pointer, char_base):
  global data_storage
  data_storage['digits'] = []
  while cont_pointer:
    data_storage['digits'].append(int(cont_pointer % char_base))
    cont_pointer /= char_base
  return data_storage['digits'][::-1]


 def clear_screen(self):
  global data_storage
  os.system('cls')
  data_storage['clear_pointer'] = 0

 def hash_calculations(self,word_used, word_size):
  global data_storage
  global learned_this_session
  global address
  word = word_used
  word_for_hash = str(word[-word_size:])
  data_storage['hashed'] = sha(word_for_hash)
  private_key = binascii.unhexlify(data_storage['hashed'])
  keccak = sha3.keccak_256()
  keccak.update(SigningKey.from_string(private_key, curve=SECP256k1).get_verifying_key().to_string())
  address = "0x{0}".format(keccak.hexdigest()[24:])
  time.sleep(THOUGHT_RATE)
  print('Last Int: [{0}] Last Word [{1}]'.format(data_storage['constant_pointer'],str(word[-word_size:])))
  learned_this_session += 1
  self.learn_algorithm(address,data_storage['hashed'])
  data_storage['constant_pointer'] += 1
  data_storage['clear_pointer'] += 1
  pickle.dump(data_storage['constant_pointer'],open('./System Memory/EnglishKeyboard.vnm','wb'))
  if data_storage['clear_pointer'] >= 1000:
   os.system('cls')
   data_storage['clear_pointer'] = 0

 def try_cell(self,try_cell_load):
   try:
    a_cell = try_cell_load[0] # Current Cell Slot
    b_cell = try_cell_load[1] # +1 Cell Slot
    c_cell = try_cell_load[2] # +2 Cell Slot
    d_cell = try_cell_load[3] # +3 Cell Slot
    e_cell = try_cell_load[4] # +4 Cell Slot
    f_cell = try_cell_load[5] # +5 Cell Slot
    g_cell = try_cell_load[6] # +6 Cell Slot
    h_cell = try_cell_load[7] # +7 Cell Slot
    p_cell = try_cell_load[8] # Current Data
    position = try_cell_load[9] # Current Cloister Section
    CELL_LOCATION = './MicroCells(8)/{0}/{1}/AP-{2}.vnm'.format(str(position),str(a_cell[0])+str(b_cell[0]),a_cell)
    EthBrain_System = pickle.load(open(SYSTEM_MEMORY_PATH, 'rb'))
    memory_cell = pickle.load(open(CELL_LOCATION, 'rb'))
    if a_cell in memory_cell['Link Binder']:
     if b_cell in memory_cell['Link Binder'][a_cell]:
      if c_cell in memory_cell['Link Binder'][a_cell][b_cell]:
       if d_cell in memory_cell['Link Binder'][a_cell][b_cell][c_cell]:
        if e_cell in memory_cell['Link Binder'][a_cell][b_cell][c_cell][d_cell]:
         if f_cell in memory_cell['Link Binder'][a_cell][b_cell][c_cell][d_cell][e_cell]:
          if g_cell in memory_cell['Link Binder'][a_cell][b_cell][c_cell][d_cell][e_cell][f_cell]:
           if h_cell in memory_cell['Link Binder'][a_cell][b_cell][c_cell][d_cell][e_cell][f_cell][g_cell]:
            if a_cell in memory_cell['Link Binder'][a_cell][b_cell][c_cell][d_cell][e_cell][f_cell][g_cell][h_cell]:
             if p_cell in memory_cell['Link Binder'][a_cell][b_cell][c_cell][d_cell][e_cell][f_cell][g_cell][h_cell][a_cell]:
              print('Cell Has Cleared Check Total Cells In Cluster [{0}]'.format(len(memory_cell['Link Binder'][a_cell][b_cell][c_cell][d_cell][e_cell][f_cell][g_cell][h_cell][a_cell])))
             else:
              print('Cell Binder Duplicate Linkage Found Adding [{}] To Dupe List Now.'.format(ADDRESS))
              memory_cell['Links Found'] += 1
              EthBrain_System['Total Links'] += 1
              EthBrain_System['Total Learned'] += 1
              memory_cell['Link Binder'][a_cell][b_cell][c_cell][d_cell][e_cell][f_cell][g_cell][h_cell][a_cell].append(p_cell)
              if ADDRESS not in EthBrain_System['Dupe List']:
               EthBrain_System['Total Dupes'] += 1
               EthBrain_System['Dupe List'].append(ADDRESS)
              pickle.dump(memory_cell, open(CELL_LOCATION, 'wb'))
              pickle.dump(EthBrain_System, open(SYSTEM_MEMORY_PATH, 'wb'))
            else:
             print('Creating Merkle For [{0}]=>[{3}]=>[{1}]=> Data Appended [{2}].'.format(str(position),a_celll,p_data,h_cell))
             memory_cell['Links Found'] += 2
             EthBrain_System['Total Links'] += 2
             EthBrain_System['Total Learned'] += 1
             memory_cell['Link Binder'][a_cell][b_cell][c_cell][d_cell][e_cell][f_cell][g_cell][h_cell][a_cell] = []
             memory_cell['Link Binder'][a_cell][b_cell][c_cell][d_cell][e_cell][f_cell][g_cell][h_cell][a_cell].append(p_cell)
             pickle.dump(memory_cell, open(CELL_LOCATION, 'wb'))
             pickle.dump(EthBrain_System, open(SYSTEM_MEMORY_PATH, 'wb'))
           else:
            print('Creating Merkle For [{0}]=>[{1}]=>[{2}]=>[{3}]=> Data Appended [{4}].'.format(str(position),g_cell,h_cell,a_cell,p_cell))
            memory_cell['Links Found'] += 3
            EthBrain_System['Total Links'] += 3
            EthBrain_System['Total Learned'] += 1
            memory_cell['Link Binder'][a_cell][b_cell][c_cell][d_cell][e_cell][f_cell][g_cell][h_cell] = dict()
            memory_cell['Link Binder'][a_cell][b_cell][c_cell][d_cell][e_cell][f_cell][g_cell][h_cell][a_cell] = []
            memory_cell['Link Binder'][a_cell][b_cell][c_cell][d_cell][e_cell][f_cell][g_cell][h_cell][a_cell].append(p_cell)
            pickle.dump(memory_cell, open(CELL_LOCATION, 'wb'))
            pickle.dump(EthBrain_System, open(SYSTEM_MEMORY_PATH, 'wb'))
          else:
           print('Creating Merkle For [{0}]=>[{1}]=>[{2}]=>[{3}]=>[{4}]=> Data Appended [{5}].'.format(str(position),f_cell,g_cell,h_cell,a_cell,p_cell))
           memory_cell['Links Found'] += 4
           EthBrain_System['Total Links'] += 4
           EthBrain_System['Total Learned'] += 1
           memory_cell['Link Binder'][a_cell][b_cell][c_cell][d_cell][e_cell][f_cell][g_cell] = dict()
           memory_cell['Link Binder'][a_cell][b_cell][c_cell][d_cell][e_cell][f_cell][g_cell][h_cell] = dict()
           memory_cell['Link Binder'][a_cell][b_cell][c_cell][d_cell][e_cell][f_cell][g_cell][h_cell][a_cell] = []
           memory_cell['Link Binder'][a_cell][b_cell][c_cell][d_cell][e_cell][f_cell][g_cell][h_cell][a_cell].append(p_cell)
           pickle.dump(memory_cell, open(CELL_LOCATION, 'wb'))
           pickle.dump(EthBrain_System, open(SYSTEM_MEMORY_PATH, 'wb'))
         else:
          print('Creating Merkle For [{0}]=>[{1}]=>[{2}]=>[{3}]=>[{4}]=>[{5}]=> Data Appended [{6}].'.format(str(position),e_cell,f_cell,g_cell,h_cell,a_cell,p_cell))
          memory_cell['Links Found'] += 5
          EthBrain_System['Total Links'] += 5
          EthBrain_System['Total Learned'] += 1
          memory_cell['Link Binder'][a_cell][b_cell][c_cell][d_cell][e_cell][f_cell] = dict()
          memory_cell['Link Binder'][a_cell][b_cell][c_cell][d_cell][e_cell][f_cell][g_cell] = dict()
          memory_cell['Link Binder'][a_cell][b_cell][c_cell][d_cell][e_cell][f_cell][g_cell][h_cell] = dict()
          memory_cell['Link Binder'][a_cell][b_cell][c_cell][d_cell][e_cell][f_cell][g_cell][h_cell][a_cell] = []
          memory_cell['Link Binder'][a_cell][b_cell][c_cell][d_cell][e_cell][f_cell][g_cell][h_cell][a_cell].append(p_cell)
          pickle.dump(memory_cell, open(CELL_LOCATION, 'wb'))
          pickle.dump(EthBrain_System, open(SYSTEM_MEMORY_PATH, 'wb'))
        else:
         print('Creating Merkle For [{0}]=>[{1}]=>[{2}]=>[{3}]=>[{4}]=>[{5}]=>[{6}]=> Data Appended [{7}].'.format(str(position),d_cell,e_cell,f_cell,g_cell,h_cell,a_cell,p_cell))
         memory_cell['Links Found'] += 6
         EthBrain_System['Total Links'] += 6
         EthBrain_System['Total Learned'] += 1
         memory_cell['Link Binder'][a_cell][b_cell][c_cell][d_cell][e_cell] = dict()
         memory_cell['Link Binder'][a_cell][b_cell][c_cell][d_cell][e_cell][f_cell] = dict()
         memory_cell['Link Binder'][a_cell][b_cell][c_cell][d_cell][e_cell][f_cell][g_cell] = dict()
         memory_cell['Link Binder'][a_cell][b_cell][c_cell][d_cell][e_cell][f_cell][g_cell][h_cell] = dict()
         memory_cell['Link Binder'][a_cell][b_cell][c_cell][d_cell][e_cell][f_cell][g_cell][h_cell][a_cell] = []
         memory_cell['Link Binder'][a_cell][b_cell][c_cell][d_cell][e_cell][f_cell][g_cell][h_cell][a_cell].append(p_cell)
         pickle.dump(memory_cell, open(CELL_LOCATION, 'wb'))
         pickle.dump(EthBrain_System, open(SYSTEM_MEMORY_PATH, 'wb'))
       else:
        print('Creating Merkle For [{0}]=>[{1}]=>[{2}]=>[{3}]=>[{4}]=>[{5}]=>[{6}]=>[{7}]=> Data Appended [{8}].'.format(str(position),c_cell,d_cell,e_cell,f_cell,g_cell,h_cell,a_cell,p_cell))
        memory_cell['Links Found'] += 7
        EthBrain_System['Total Links'] += 7
        EthBrain_System['Total Learned'] += 1
        memory_cell['Link Binder'][a_cell][b_cell][c_cell][d_cell] = dict()
        memory_cell['Link Binder'][a_cell][b_cell][c_cell][d_cell][e_cell] = dict()
        memory_cell['Link Binder'][a_cell][b_cell][c_cell][d_cell][e_cell][f_cell] = dict()
        memory_cell['Link Binder'][a_cell][b_cell][c_cell][d_cell][e_cell][f_cell][g_cell] = dict()
        memory_cell['Link Binder'][a_cell][b_cell][c_cell][d_cell][e_cell][f_cell][g_cell][h_cell] = dict()
        memory_cell['Link Binder'][a_cell][b_cell][c_cell][d_cell][e_cell][f_cell][g_cell][h_cell][a_cell] = []
        memory_cell['Link Binder'][a_cell][b_cell][c_cell][d_cell][e_cell][f_cell][g_cell][h_cell][a_cell].append(p_cell)
        pickle.dump(memory_cell, open(CELL_LOCATION, 'wb'))
        pickle.dump(EthBrain_System, open(SYSTEM_MEMORY_PATH, 'wb'))
      else:
       print('Creating Merkle For [{0}] =>[{1}]=>[{2}]=>[{3}]=>[{4}]=>[{5}]=>[{6}]=>[{7}]=>[{8}]=> Data Appended [{9}].'.format(str(position),b_cell,c_cell,d_cell,e_cell,f_cell,g_cell,h_cell,a_cell,p_cell))
       memory_cell['Links Found'] += 8
       EthBrain_System['Total Links'] += 8
       EthBrain_System['Total Learned'] += 1
       memory_cell['Link Binder'][a_cell][b_cell][c_cell] = dict()
       memory_cell['Link Binder'][a_cell][b_cell][c_cell][d_cell] = dict()
       memory_cell['Link Binder'][a_cell][b_cell][c_cell][d_cell][e_cell] = dict()
       memory_cell['Link Binder'][a_cell][b_cell][c_cell][d_cell][e_cell][f_cell] = dict()
       memory_cell['Link Binder'][a_cell][b_cell][c_cell][d_cell][e_cell][f_cell][g_cell] = dict()
       memory_cell['Link Binder'][a_cell][b_cell][c_cell][d_cell][e_cell][f_cell][g_cell][h_cell] = dict()
       memory_cell['Link Binder'][a_cell][b_cell][c_cell][d_cell][e_cell][f_cell][g_cell][h_cell][a_cell] = []
       memory_cell['Link Binder'][a_cell][b_cell][c_cell][d_cell][e_cell][f_cell][g_cell][h_cell][a_cell].append(p_cell)
       pickle.dump(memory_cell, open(CELL_LOCATION, 'wb'))
       pickle.dump(EthBrain_System, open(SYSTEM_MEMORY_PATH, 'wb'))
     else:
      memory_cell['Links Found'] += 9
      EthBrain_System['Total Links'] += 9
      EthBrain_System['Total Learned'] += 1
      print('Creating Merkle For [{0}] =>[{1}]=>[{2}]=>[{3}]=>[{4}]=>[{5}]=>[{6}]=>[{7}]=>[{8}]=>[{1}]=> Data Appended [{9}].'.format(str(position),a_cell,b_cell,c_cell,d_cell,e_cell,f_cell,g_cell,h_cell,p_cell))
      memory_cell['Link Binder'][a_cell][b_cell] = dict()
      memory_cell['Link Binder'][a_cell][b_cell][c_cell] = dict()
      memory_cell['Link Binder'][a_cell][b_cell][c_cell][d_cell] = dict()
      memory_cell['Link Binder'][a_cell][b_cell][c_cell][d_cell][e_cell] = dict()
      memory_cell['Link Binder'][a_cell][b_cell][c_cell][d_cell][e_cell][f_cell] = dict()
      memory_cell['Link Binder'][a_cell][b_cell][c_cell][d_cell][e_cell][f_cell][g_cell] = dict()
      memory_cell['Link Binder'][a_cell][b_cell][c_cell][d_cell][e_cell][f_cell][g_cell][h_cell] = dict()
      memory_cell['Link Binder'][a_cell][b_cell][c_cell][d_cell][e_cell][f_cell][g_cell][h_cell][a_cell] = []
      memory_cell['Link Binder'][a_cell][b_cell][c_cell][d_cell][e_cell][f_cell][g_cell][h_cell][a_cell].append(p_cell)
      pickle.dump(memory_cell, open(CELL_LOCATION, 'wb'))
      pickle.dump(EthBrain_System, open(SYSTEM_MEMORY_PATH, 'wb'))
    else:
     print('Creating New Merkle For [{0}][NEW] =>[{1}]=>[{2}]=>[{3}]=>[{4}]=>[{5}]=>[{6}]=>[{7}]=>[{8}]=>[{1}]=> Data Appended [{9}].'.format(str(position),a_cell,b_cell,c_cell,d_cell,e_cell,f_cell,g_cell,h_cell,p_cell))
     memory_cell['Links Found'] += 10
     EthBrain_System['Total Links'] += 10
     EthBrain_System['Total Learned'] += 1
     memory_cell['Link Binder'][a_cell] = dict()
     memory_cell['Link Binder'][a_cell][b_cell] = dict()
     memory_cell['Link Binder'][a_cell][b_cell][c_cell] = dict()
     memory_cell['Link Binder'][a_cell][b_cell][c_cell][d_cell] = dict()
     memory_cell['Link Binder'][a_cell][b_cell][c_cell][d_cell][e_cell] = dict()
     memory_cell['Link Binder'][a_cell][b_cell][c_cell][d_cell][e_cell][f_cell] = dict()
     memory_cell['Link Binder'][a_cell][b_cell][c_cell][d_cell][e_cell][f_cell][g_cell] = dict()
     memory_cell['Link Binder'][a_cell][b_cell][c_cell][d_cell][e_cell][f_cell][g_cell][h_cell] = dict()
     memory_cell['Link Binder'][a_cell][b_cell][c_cell][d_cell][e_cell][f_cell][g_cell][h_cell][a_cell] = []
     memory_cell['Link Binder'][a_cell][b_cell][c_cell][d_cell][e_cell][f_cell][g_cell][h_cell][a_cell].append(p_cell)
     pickle.dump(memory_cell, open(CELL_LOCATION, 'wb'))
     pickle.dump(EthBrain_System, open(SYSTEM_MEMORY_PATH, 'wb'))

   except Exception as Unit_Fault:
    if CELL_LOCATION in str(Unit_Fault):
     self.create_cell(CELL_LOCATION,try_cell_load)
    if SYSTEM_MEMORY_PATH in str(Unit_Fault):
     print('Critical Error With System Please Investigate.')
     exit()

 def create_cell(self,current_location,create_cell_load):
    global memory_cell
    global EthBrain_System
    EthBrain_System = pickle.load(open(SYSTEM_MEMORY_PATH, 'rb'))
    CELL_LOCATION = current_location
    a_cell = create_cell_load[0]
    b_cell = create_cell_load[1]
    c_cell = create_cell_load[2]
    d_cell = create_cell_load[3]
    e_cell = create_cell_load[4]
    f_cell = create_cell_load[5]
    g_cell = create_cell_load[6]
    h_cell = create_cell_load[7]
    p_cell = create_cell_load[8]
    position = create_cell_load[9]
    memory_cell = dict()
    memory_cell['Link Binder'] = dict()
    memory_cell['Link Binder'][a_cell] = dict()
    memory_cell['Link Binder'][a_cell][b_cell] = dict()
    memory_cell['Link Binder'][a_cell][b_cell][c_cell] = dict()
    memory_cell['Link Binder'][a_cell][b_cell][c_cell][d_cell] = dict()
    memory_cell['Link Binder'][a_cell][b_cell][c_cell][d_cell][e_cell] = dict()
    memory_cell['Link Binder'][a_cell][b_cell][c_cell][d_cell][e_cell][f_cell] = dict()
    memory_cell['Link Binder'][a_cell][b_cell][c_cell][d_cell][e_cell][f_cell][g_cell] = dict()
    memory_cell['Link Binder'][a_cell][b_cell][c_cell][d_cell][e_cell][f_cell][g_cell][h_cell] = dict()
    memory_cell['Link Binder'][a_cell][b_cell][c_cell][d_cell][e_cell][f_cell][g_cell][h_cell][a_cell] = [p_cell]
    memory_cell['Links Found'] = 8
    EthBrain_System['Total Links'] += 8
    EthBrain_System['Neural Units'] += 1
    EthBrain_System['Hard Cells'] += 1
    EthBrain_System['Total Learned'] += 1
    pickle.dump(memory_cell, open(CELL_LOCATION, 'wb'))
    pickle.dump(EthBrain_System, open(SYSTEM_MEMORY_PATH, 'wb'))
    print('Created Memory Cell For [{0}] In Position [{1}]'.format(a_cell, position))



 def learn_algorithm(self,eth_address,eth_priv):
   global ADDRESS
   global learned_this_session
   ADDRESS = address
   print('Total Combinations Learned This Session: '+str(learned_this_session))
   print('Creating Packages From Address: [{0}]  Private Key: [{1}] '.format(eth_address,eth_priv))
   A_SEQ_0 = eth_address[2:7]
   P_SEQ_0 = eth_priv[0:8]   
   A_SEQ_1 = address[7:12]
   P_SEQ_1 = eth_priv[8:16]
   A_SEQ_2 = address[12:17]
   P_SEQ_2 = eth_priv[16:24]
   A_SEQ_3 = address[17:22]
   P_SEQ_3 = eth_priv[24:32]
   A_SEQ_4 = address[22:27]
   P_SEQ_4 = eth_priv[32:40]
   A_SEQ_5 = address[27:32]
   P_SEQ_5 = eth_priv[40:48]
   A_SEQ_6 = address[32:37]
   P_SEQ_6 = eth_priv[48:56]
   A_SEQ_7 = address[37:42]
   P_SEQ_7 = eth_priv[56:64]
                    
   #                     a_cell  b_cell  c_cell  d_cell  e_cell  f_cell  g_cell  h_cell  p_cell  pos.
   try_cell_package = [[A_SEQ_0,A_SEQ_1,A_SEQ_2,A_SEQ_3,A_SEQ_4,A_SEQ_5,A_SEQ_6,A_SEQ_7,P_SEQ_0, 0],
                       [A_SEQ_1,A_SEQ_2,A_SEQ_3,A_SEQ_4,A_SEQ_5,A_SEQ_6,A_SEQ_7,A_SEQ_0,P_SEQ_1, 1],
                       [A_SEQ_2,A_SEQ_3,A_SEQ_4,A_SEQ_5,A_SEQ_6,A_SEQ_7,A_SEQ_0,A_SEQ_1,P_SEQ_2, 2],
                       [A_SEQ_3,A_SEQ_4,A_SEQ_5,A_SEQ_6,A_SEQ_7,A_SEQ_0,A_SEQ_1,A_SEQ_2,P_SEQ_3, 3],
                       [A_SEQ_4,A_SEQ_5,A_SEQ_6,A_SEQ_7,A_SEQ_0,A_SEQ_1,A_SEQ_2,A_SEQ_3,P_SEQ_4, 4],
                       [A_SEQ_5,A_SEQ_6,A_SEQ_7,A_SEQ_0,A_SEQ_1,A_SEQ_2,A_SEQ_3,A_SEQ_4,P_SEQ_5, 5],
                       [A_SEQ_6,A_SEQ_7,A_SEQ_0,A_SEQ_1,A_SEQ_2,A_SEQ_3,A_SEQ_4,A_SEQ_5,P_SEQ_6, 6],
                       [A_SEQ_7,A_SEQ_0,A_SEQ_1,A_SEQ_2,A_SEQ_3,A_SEQ_4,A_SEQ_5,A_SEQ_6,P_SEQ_7, 7]]

   
   # Memory Check / Creation For Position 0 - {A_SEQ_0, P_SEQ_0}
   self.try_cell(try_cell_package[0])
   # Memory Check / Creation For Position 1 - {A_SEQ_1, P_SEQ_1}
   self.try_cell(try_cell_package[1])
   # Memory Check / Creation For Position 2 - {A_SEQ_2, P_SEQ_2}
   self.try_cell(try_cell_package[2])
   # Memory Check / Creation For Position 3 - {A_SEQ_3, P_SEQ_3}
   self.try_cell(try_cell_package[3])
   # Memory Check / Creation For Position 4 - {A_SEQ_4, P_SEQ_4}
   self.try_cell(try_cell_package[4])
   # Memory Check / Creation For Position 5 - {A_SEQ_5, P_SEQ_5}
   self.try_cell(try_cell_package[5])
   # Memory Check / Creation For Position 6 - {A_SEQ_6, P_SEQ_6}
   self.try_cell(try_cell_package[6])
   # Memory Check / Creation For Position 7 - {A_SEQ_7, P_SEQ_7}
   self.try_cell(try_cell_package[7])
    
   
 def start_lesson(self):
  try:
   if not data_storage['solved']:
     while int(data_storage['constant_pointer']) < (int(data_storage['chars']['base']) ** int(data_storage['length capacity'])) - int(data_storage['constant_pointer']):
      lst = self.numberToBase(data_storage['constant_pointer'], data_storage['chars']['base'])
      word = ''
      for x in lst:
       word += str(data_storage['chars']['current'][x])
      if data_storage['clear_pointer'] >= data_storage['stop_point']:
       self.clear_screen()
      if data_storage['constant_pointer'] >= 0 and data_storage['constant_pointer'] <= data_storage['chars']['size'] ** 1:
       self.hash_calculations(word, 1)
      elif data_storage['constant_pointer'] > data_storage['chars']['size'] ** 1 and data_storage['constant_pointer'] <= data_storage['chars']['size'] ** 2:
       self.hash_calculations(word, 2)
      elif data_storage['constant_pointer'] > data_storage['chars']['size'] ** 2 and data_storage['constant_pointer'] <= data_storage['chars']['size'] ** 3:
       self.hash_calculations(word, 3)
      elif data_storage['constant_pointer'] > data_storage['chars']['size'] ** 3 and data_storage['constant_pointer'] <= data_storage['chars']['size'] ** 4:
       self.hash_calculations(word, 4)
      elif data_storage['constant_pointer'] > data_storage['chars']['size'] ** 4 and data_storage['constant_pointer'] <= data_storage['chars']['size'] ** 5:
       self.hash_calculations(word, 5)
      elif data_storage['constant_pointer'] > data_storage['chars']['size'] ** 5 and data_storage['constant_pointer'] <= data_storage['chars']['size'] ** 6:
       self.hash_calculations(word, 6)
      elif data_storage['constant_pointer'] > data_storage['chars']['size'] ** 6 and data_storage['constant_pointer'] <= data_storage['chars']['size'] ** 7:
       self.hash_calculations(word, 7)
      elif data_storage['constant_pointer'] > data_storage['chars']['size'] ** 7 and data_storage['constant_pointer'] <= data_storage['chars']['size'] ** 8:
       self.hash_calculations(word, 8)
      elif data_storage['constant_pointer'] > data_storage['chars']['size'] ** 8 and data_storage['constant_pointer'] <= data_storage['chars']['size'] ** 9:
       self.hash_calculations(word, 9)
      elif data_storage['constant_pointer'] > data_storage['chars']['size'] ** 9 and data_storage['constant_pointer'] <= data_storage['chars']['size'] ** 10:
       self.hash_calculations(word, 10)
      elif data_storage['constant_pointer'] > data_storage['chars']['size'] ** 10 and data_storage['constant_pointer'] <= data_storage['chars']['size'] ** 11:
       self.hash_calculations(word, 11)
      elif data_storage['constant_pointer'] > data_storage['chars']['size'] ** 11 and data_storage['constant_pointer'] <= data_storage['chars']['size'] ** 12:
       self.hash_calculations(word, 12)
      elif data_storage['constant_pointer'] > data_storage['chars']['size'] ** 12 and data_storage['constant_pointer'] <= data_storage['chars']['size'] ** 13:
       self.hash_calculations(word, 13)
      elif data_storage['constant_pointer'] > data_storage['chars']['size'] ** 13 and data_storage['constant_pointer'] <= data_storage['chars']['size'] ** 14:
       self.hash_calculations(word, 14)
      else:
       print('All Lessons Up To 14 Characters Learned! Thanks For Teaching!')
       exit()
  except KeyboardInterrupt as KI:
   try:
    print('Welcome To The Pause Section. PRESS CTRL+C AGAIN TO EXIT.')
    paused = input('Press Enter Or Input Extra Options To Continue. >>: ')
    if paused.lower() == '':
     self.start_lesson()
    elif paused.lower() == 'help':
     print('You Need A Lot More Then Help')
     self.start_lesson()
   except KeyboardInterrupt as KI2:
    print('Instructing Program To Exit.')
    exit()

print('Starting Teaching Program You May Press CTRL+C At Any Time To Enter Pause Section. Happy Teaching!')
teach_viv_ethereum = TeachVivEthereum()
