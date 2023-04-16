import os

pwdi = ''.join(list(os.path.dirname(os.path.realpath(__file__))).copy())

recipient = str('%s/scriptsbackup/console.py' % pwdi)
script = str('%s/scriptsbackup/console.sh' % pwdi)
storage = '/usr/share/mcconsole'
scriptstorage='/usr/share/mcconsole/console.sh'
binary = '/usr/bin/mcconsole'

os.system(str('sudo mkdir --parents %s' % storage))
os.system(str('sudo cp %s %s' % (recipient, storage)))
os.system(str('sudo cp %s %s' % (script, storage)))
os.system(str('sudo chmod +x %s' % scriptstorage))
os.system(str('sudo ln -sf %s %s' % (scriptstorage,binary)))
