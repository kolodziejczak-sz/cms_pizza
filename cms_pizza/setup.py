from base.setup import init as base_init
from gallery.setup import init as gallery_init
from contact.setup import init as contact_init

def init(clear = False):
  base_init(clear)
  gallery_init(clear)
  contact_init(clear)
