from ansible.cli.doc import DocCLI
from ansible.utils import module_docs
from ansible.plugins import module_loader

def get_ansible_modules():
    d = DocCLI(['doc', '-l'])
    d.parse()

    # find modules
    if d.options.list_dir:
        paths = module_loader._get_paths()
        for path in paths:
            d.find_modules(path)

    return sorted(set(d.module_list))

def print_module_snippet(module):
    try:
        filename = module_loader.find_plugin(module, mod_type='.py', ignore_deprecated=True)

        doc, plainexamples, returndocs, metadata = \
            module_docs.get_docstring(filename, verbose=False)

        options = doc['options']
        keys = [k for k in options]
        keys.sort(key=lambda k: options[k].get('required') or k)

        print("snippet {}".format(module))

        print("{}:".format(module))

        for i, k in enumerate(keys, start=1):
            o = options[k]
            default = options[k].get('default','')
            if default == False:
                default = 'no'
            choices = "|".join(str(c) if c != default else "#" + str(c) for c in options[k].get('choices',''))

            text = ''
            if choices:
                text = ":" + choices
            else:
                if default:
                    text = ':' + str(default)
                if o.get('required'):
                    text = ':# REQUIRED'

            print("\t{}: ${{{}{}}}".format(k, i, text))

        print("endsnippet")
    except Exception:
        # ignore corrupt/incomplete modules
        pass
    # from pprint import pprint
    # pprint(options)


if __name__ == "__main__":
    modules = get_ansible_modules()

    for module in modules:
        # if m != 'pacman':
        #     continue
        d = DocCLI(['doc', module])
        d.parse()

        for module in d.args:
            print_module_snippet(module)
