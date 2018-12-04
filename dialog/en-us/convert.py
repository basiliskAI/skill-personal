import glob
for filename in glob.glob('*.dialog'):
   name = filename.replace('.dialog', '')
   handle = name.replace('.', '_')
   at = '@intent_file_handler("' + name + '.intent")\n'
   de = 'def handle_' + handle + '(self, message):\n'
   se = '    self.speak_dialog("' + name + '")\n'
   print(at + de + se)
