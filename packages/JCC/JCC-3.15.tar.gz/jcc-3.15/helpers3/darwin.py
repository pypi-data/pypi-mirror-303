#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.

import sys, os

global JAVAHOME, JAVAFRAMEWORKS
JAVAHOME = None
JAVAFRAMEWORKS = None

if sys.platform == "darwin":

    if 'JAVA_HOME' in os.environ:
        _path = os.environ['JAVA_HOME']
        if os.path.exists(os.path.join(_path, "include", "jni.h")):
            JAVAHOME = _path
            print('found JAVAHOME =', JAVAHOME, file=sys.stderr)        

    if JAVAHOME is None:
        # figure out where the JDK lives
        from subprocess import run, PIPE

        try:
            args = ['/usr/libexec/java_home']
            process = run(args, stdout=PIPE, stderr=PIPE, encoding='utf8')
        except Exception as e:
            print("%s: %s" %(e, args), file=sys.stderr)
        else:
            if process.returncode == 0:
                _path = process.stdout.strip()
                if os.path.exists(os.path.join(_path, "include", "jni.h")):
                    JAVAHOME = _path
                    print('found JAVAHOME =', JAVAHOME, file=sys.stderr)
            else:
                print(process.stderr, file=sys.stderr)

    # figure out where the JDK Frameworks lives
    import platform, re
    _os_version = re.match(r"[0-9]+\.[0-9]+", platform.mac_ver()[0]).group(0)

    # this is where Apple says we should look for headers
    _path = "/System/Library/Frameworks/JavaVM.framework"
    if os.path.exists(os.path.join(_path, "Headers", "jni.h")):
        JAVAFRAMEWORKS = _path
        print('found JAVAFRAMEWORKS =', JAVAFRAMEWORKS, file=sys.stderr)
    else:
        # but their updates don't always match their documentation,
        # so look up the same path in the OS's /Developer tree
        _path = "/Developer/SDKs/MacOSX%s.sdk%s" %(_os_version, _path)
        if os.path.exists(os.path.join(_path, "Headers", "jni.h")):
            JAVAFRAMEWORKS = _path
            print('found JAVAFRAMEWORKS =', JAVAFRAMEWORKS, file=sys.stderr)

    # monkeypatch build_ext so that it doesn't mess with a Library's extension
    from setuptools.command.build_ext import build_ext as _build_ext
    from setuptools.extension import Library

    class build_ext_(_build_ext):
        def get_ext_filename(self, fullname):
            if fullname in self.ext_map:
                ext = self.ext_map[fullname]
                if isinstance(ext, Library):
                    return "lib%s.dylib" %(fullname)
            return _build_ext.get_ext_filename(self, fullname)

    # monkeypatch _customize_compiler_for_shlib with missing LDCXXSHARED
    from distutils.sysconfig import customize_compiler
    from distutils.sysconfig import _config_vars as _CONFIG_VARS

    def _customize_compiler_for_shlib_(compiler):
        tmp = _CONFIG_VARS.copy()
        try:
            _CONFIG_VARS['LDSHARED'] = (
                "gcc -Wl,-x -dynamiclib -undefined dynamic_lookup"
            )
            _CONFIG_VARS['LDCXXSHARED'] = (
                "gcc -Wl,-x -dynamiclib -undefined dynamic_lookup"
            )
            _CONFIG_VARS['CCSHARED'] = " -dynamiclib"
            _CONFIG_VARS['SO'] = ".dylib"
            customize_compiler(compiler)
        finally:
            _CONFIG_VARS.clear()
            _CONFIG_VARS.update(tmp)

    from setuptools.command import build_ext
    build_ext.build_ext = build_ext_
    build_ext._customize_compiler_for_shlib = _customize_compiler_for_shlib_
