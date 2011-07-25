from ninfo import PluginBase
import cymruwhois

class cymru_whois(PluginBase):
    name = 'cymruwhois'
    title = 'Cymru Whois'
    description = 'Cymru Whois lookup'
    long_description = 'This plugin returns the owners name and ASN of this ip'
    types = ['ip']
    local = False

    def setup(self):
        self.c=cymruwhois.Client()

    def get_info(self, ip):
        #Don't bother looking up on-campus hosts
        info = self.c.lookup(ip)
        return info.__dict__

plugin_class = cymru_whois
