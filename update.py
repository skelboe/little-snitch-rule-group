import urllib.request
import json


def exlucded_domains():
    with open('./overrides.json') as fp:
        return json.load(fp)['domains']


def fetch_source():
    uri = "https://raw.githubusercontent.com/naveednajam/Little-Snitch---Rule-Groups/master/unified_hosts_gambling-porn-social/sb_unified_hosts_gambling-porn-social.lsrules"
    with urllib.request.urlopen(uri) as url:
        return json.loads(url.read().decode())


def build_rules(source):
    excluded = exlucded_domains()
    rules = []
    for r in source['rules']:
        if r['remote-domains'] not in excluded:
            rules.append(r)
    return rules


# Build the new rules list
source = fetch_source()
source['rules'] = build_rules(source)

# Write the changes
with open('./unified-hosts.lsrules', 'w') as fp:
    json.dump(source, fp)
