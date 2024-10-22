import configparser
import os
from dataclasses import dataclass

from .svc import svc


# --------------------
## contains all configuration objects and values
@dataclass
class Cfg:
    ## the version string held in mod_dir_name/lib/version.json
    version = 'notset'
    ## the module name (with dashes)
    mod_name = 'notset'
    ## the local directory name for the module (with underscores)
    mod_dir_name = 'notset'
    ## flag indicating this is a python module (True) or an app (False)
    is_module = True
    ## the module/app type: public or private
    mod_type = 'notset'
    ## the tech for this project: python, cpp, arduino
    mod_tech = 'python'

    ## the license for the module
    license = 'notset'
    ## the license string for the classifier section
    classifier_license = 'notset'
    ## the url for the homepage link
    homepage_url = 'notset'
    ## the url for the download link
    download_url = 'notset'
    ## the author name
    author = 'notset'
    ## the contact email
    email = 'notset'
    ## the type of the description file used
    long_desc_type = 'notset'

    # ----
    ## attributes specific for do_publish script
    @dataclass
    class do_publish:  # pylint: disable=invalid-name
        ## list of projects to disallow
        disallow = []

    # ----
    ## attributes specific for do_lint script
    @dataclass
    class do_lint:  # pylint: disable=invalid-name
        ## if True, include tools directory in lint
        include_tools = False

    # ----
    ## attributes specific for do_doc script
    @dataclass
    class do_doc:  # pylint: disable=invalid-name
        ## the type: "Module" or "App"
        doxy_type = 'notset'
        ## the Doxyfile project description
        doxy_desc = 'notset'
        ## additional directories to exclude in the Doxyfile
        doxy_exclude = []
        ## additional directories to specifically include in the Doxyfile
        doxy_include = []

    # ----
    ## attributes specific for do_post_ver script
    @dataclass
    class do_post_ver:  # pylint: disable=invalid-name
        ## the destination directory for verification reports and files
        dst_dir = 'notset'
        ## directory to get verification html files
        src_dir = 'notset'
        ## web slug
        slug = 'notset'
        ## PyPi URL for python modules; use 'N/A' not a module
        pypi_url = 'notset'
        ## repo URL
        repo_url = 'notset'

    # ----
    ## attributes specific for do_ut script
    @dataclass
    class do_ut:  # pylint: disable=invalid-name
        ## set of directories for coverage
        cov_dirs = []

    # ----
    ## attributes specific for cpip
    @dataclass
    class cpip:  # pylint: disable=invalid-name
        ## the root directory of the cpip database
        root_dir = 'notset'
        ## the default server root url for pulls
        server_root = 'https://arrizza.com/web-cpip'
        ## the packages to use
        packages = []

    # == private from here

    ##  holds the root dir; usually '.'
    _root_dir = None
    ## flag indicates if the cfg values have been initialized
    _initialized = False

    # --------------------
    ## loads cfg values from xplat.cfg file
    #
    # @param root_dir    root directory to find .cfg file
    # @param init_once   (optional) if True, initialized only once
    # @return None
    @classmethod
    def load(cls, root_dir, init_once=True):
        if init_once and cls._initialized:
            return

        cls._load_cfg_file(root_dir, 'xplat.cfg', init_once)

    # --------------------
    ## load the xplat configuration file
    #
    # @param root_dir   location of the cfg file
    # @param fname      name of the cfg file
    # @param init_once  initialize only once
    @classmethod
    def _load_cfg_file(cls, root_dir, fname, init_once):
        if init_once and cls._initialized:
            return

        cls._root_dir = root_dir
        path = os.path.join(root_dir, fname)
        config = configparser.ConfigParser()
        config.read(path)

        cls._load_xplat(config)
        cls._load_do_publish(config)
        cls._load_do_lint(config)
        cls._load_do_doc(config)
        cls._load_do_post_ver(config)
        cls._load_do_ut(config)
        cls._load_cpip(config)

        ## see class doc
        cls._initialized = True

    # --------------------
    ## loads values from xplat section
    #
    # @param config  reference to ConfigParser object
    # @return None
    @classmethod
    def _load_xplat(cls, config):
        section = 'xplat'
        # uncomment to debug
        # print(f'==== section {section}')
        values = dict(config.items(section))

        for opt, orig_val in values.items():
            val = cls._parse_str(opt, orig_val)
            setattr(cls, opt, val)

            if opt == 'mod_name':
                if '_' in cls.mod_name:
                    svc.abort(f'mod_name should not have underscores: "{val}"')
                else:
                    setattr(cls, 'mod_dir_name', cls.mod_name.replace('-', '_'))

            elif opt == 'version':
                ## see class doc
                cls.long_version = cls.version.replace('.', '_')

    # --------------------
    ## loads values from do_publish section
    #
    # @param config  reference to ConfigParser object
    # @return None
    @classmethod
    def _load_do_publish(cls, config):
        section = 'do_publish'
        # uncomment to debug
        # print(f'==== section {section}')
        values = dict(config.items(section))
        for opt, orig_val in values.items():
            val = cls._parse_str(opt, orig_val)
            ## see doc above
            setattr(cls.do_publish, opt, val)

    # --------------------
    ## loads values from do_lint section
    #
    # @param config  reference to ConfigParser object
    # @return None
    @classmethod
    def _load_do_lint(cls, config):
        section = 'do_lint'
        # uncomment to debug
        # print(f'==== section {section}')
        values = dict(config.items(section))
        for opt, orig_val in values.items():
            if opt in ['src_dirs']:
                val = cls._parse_list(opt, orig_val)
            else:
                val = cls._parse_str(opt, orig_val)
            ## see doc above
            setattr(cls.do_lint, opt, val)

    # --------------------
    ## loads values from do_doc section
    #
    # @param config  reference to ConfigParser object
    # @return None
    @classmethod
    def _load_do_doc(cls, config):
        section = 'do_doc'
        # uncomment to debug
        # print(f'==== section {section}')
        values = dict(config.items(section))
        for opt, orig_val in values.items():
            if opt in ['doxy_exclude', 'doxy_include']:
                val = cls._parse_list(opt, orig_val)
            else:
                val = cls._parse_str(opt, orig_val)

            ## see doc above
            setattr(cls.do_doc, opt, val)

        if cls.is_module:
            setattr(cls.do_doc, 'doxy_type', 'Module')
        else:
            setattr(cls.do_doc, 'doxy_type', 'App')

    # --------------------
    ## loads values from do_post_ver section
    #
    # @param config  reference to ConfigParser object
    # @return None
    @classmethod
    def _load_do_post_ver(cls, config):
        section = 'do_post_ver'
        values = dict(config.items(section))
        for opt, orig_val in values.items():
            val = cls._parse_str(opt, orig_val)
            ## see doc above
            setattr(cls.do_post_ver, opt, val)

    # --------------------
    ## loads values from do_ut section
    #
    # @param config  reference to ConfigParser object
    # @return None
    @classmethod
    def _load_do_ut(cls, config):
        section = 'do_ut'
        # uncomment to debug
        # print(f'==== section {section}')
        values = dict(config.items(section))
        for opt, orig_val in values.items():
            if opt in ['cov_dirs']:
                val = cls._parse_list(opt, orig_val)
            else:
                val = cls._parse_str(opt, orig_val)

            ## see doc above
            setattr(cls.do_ut, opt, val)

    # --------------------
    ## loads values from cpip section
    #
    # @param config  reference to ConfigParser object
    # @return None
    @classmethod
    def _load_cpip(cls, config):
        section = 'cpip'

        values = dict(config.items(section))
        for opt, orig_val in values.items():
            if opt in ['packages']:
                val = cls._parse_list(opt, orig_val)
            else:
                val = cls._parse_str(opt, orig_val)
            ## see doc above
            setattr(cls.cpip, opt, val)

    # --------------------
    ## Debug: report all values found in the cfg file
    #
    # @return None
    @classmethod
    def report(cls):
        # uncomment to debug
        print('==== Cfg')
        cls._report('cls', cls)
        cls._report('do_publish', cls.do_publish)
        cls._report('do_lint', cls.do_lint)
        cls._report('do_doc', cls.do_doc)
        cls._report('do_post_ver', cls.do_post_ver)
        cls._report('do_ut', cls.do_ut)

    # --------------------
    ## Debug: report all values found in a section
    #
    # @param sectname   section name to report
    # @param subclass   the location (a dataclass) of the attributes to report
    # @return None
    @classmethod
    def _report(cls, sectname, subclass):
        for opt, val in vars(subclass).items():
            if opt.startswith('__'):
                continue
            if callable(getattr(subclass, opt)):
                continue

            optname = f'{sectname}.{opt}'
            if opt == 'long_desc':
                optval = val[0]
            else:
                optval = val

            # sfx = ''
            # if val == 'notset':
            #     sfx = '; WARN value is not set'
            msg = f'{optname: <25}: [{type(optval).__name__: <4}]; {optval}'
            if val == 'notset':
                svc.log.warn(f'{msg}; value is not set')
            else:
                svc.log.line(msg)

    # --------------------
    ## substitue common values if found in a cfg string
    # e.g.: {mod_name}, {mod_dir_name}
    #
    # @param opt  the optional being used
    # @param val  the value to convert
    # @return None
    @classmethod
    def _sub_common(cls, opt, val):
        common_tags = {
            ## see doc above
            '{mod_name}': cls.mod_name,
            ## see doc above
            '{mod_dir_name}': cls.mod_dir_name,
            ## see doc above
            '{mod_type}': cls.mod_type,
        }

        for tag_name, tag_val in common_tags.items():
            if val.find(tag_name) != -1:
                val = val.replace(tag_name, tag_val)

        # report an invalid tag_name
        if '{' in val or '}' in val:
            svc.log.warn(f'{opt}: check for invalid tag_name: \'{val}\'')

        return val

    # --------------------
    ## parse the given string value and substitute any common values
    #
    # @param opt   the cfg name
    # @param val   the cfg value (a string)
    # @return the updated value
    @classmethod
    def _parse_str(cls, opt, val):  # pylint: disable=unused-argument
        val = val.strip("'")
        val = cls._sub_common(opt, val)

        # handle bool
        if '"' in val:
            svc.log.warn(f'{opt}: double quotes are not parsed out: \'{val}\'')
        elif val.lower() == 'true':
            val = True
        elif val.lower() == 'false':
            val = False

        # note: integers and floats are returned as strings

        # uncomment to debug
        # print(f'{opt: <25}: {val}')
        return val

    # --------------------
    ## parse the given list value and substitute any common values in each list item
    #
    # @param opt   the cfg name
    # @param val   the cfg value (a list)
    # @return the updated value
    @classmethod
    def _parse_list(cls, opt, val):
        val_list = []
        if '\n' in val:
            subvals = val.split('\n')
            for subval in subvals:
                if '[' in subval or ']' in subval:
                    svc.log.warn(f'{opt}: square brackets are not parsed out: \'{subval}\'')

                if subval == '':  # if empty don't add to list
                    svc.log.warn(f'{opt}: empty value in: \'{val}\'')
                else:
                    subval = cls._parse_str(opt, subval)
                    val_list.append(subval)
        elif ',' in val:
            subvals = val.split(',')
            for subval in subvals:
                subval = subval.strip(' ')
                if '[' in subval or ']' in subval:
                    svc.log.warn(f'{opt}: square brackets are not parsed out: \'{subval}\'')

                if subval == '':  # if empty don't add to list
                    svc.log.warn(f'{opt}: empty value in: \'{val}\'')
                else:
                    subval = cls._parse_str(opt, subval)
                    val_list.append(subval)
        elif val != '':  # if empty don't add to list
            val = cls._parse_str(opt, val)
            val_list.append(val)
        return val_list
