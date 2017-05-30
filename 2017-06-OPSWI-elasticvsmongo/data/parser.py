from domain import Class, Package
import json


paths = []
repo_path = 'C:/Users/verca/.m2/repository/'  # local maven repository

packages = {}
my_json = []


def load_paths():
    with open(repo_path + 'paths.txt') as f:
        global paths
        paths = f.read().splitlines()
    f.close


def load_data():
    for path in paths:
        try:
            with open(repo_path + path[2:] + '/methods.txt', 'r') as f:
                content = f.read().split('PATH: ')
            f.close()

            for i, soubor in enumerate(content):
                if i > 0:
                    process(soubor)
        except IOError:
            print 'Path ' + repo_path + path[2:] + ' does not contain methods.txt'


def process(filename):
    lines = filename.split('\n')
    (path, version, methods) = lines[0], lines[1], lines[4:-2]

    try:
        (package, clazz) = path.rsplit('/', 1)
    except ValueError:
        package = ''
        clazz = path
    package = str(package).replace('/', '.')
    version = str(version).replace('VERSION: ', '')

    c = Class(clazz)
    for m in methods:
        c.add_method(str(m).strip())

    if (package, version) in packages:
        packages[(package, version)].add_class(c)
    else:
        p = Package(package, version)
        p.add_class(c)
        packages[(package, version)] = p


def parse_data():
    for key in packages:
        package = {}
        package["package"] = key[0]
        package["version"] = packages[key].version
        classes = []
        for c in packages[key].classes:
            clazz = {}
            clazz["name"] = c.name
            methods = []
            for m in c.methods:
                method = {}
                method["header"] = m
                methods.append(method)
            clazz["methods"] = methods

            classes.append(clazz)
        package["classes"] = classes
        my_json.append(package)

load_paths()
load_data()
parse_data()

# print json.dumps(my_json, sort_keys=True, indent=4, separators=(',', ': '))
with open(repo_path + 'data.json', 'w') as outfile:
    json.dump(my_json, outfile)
