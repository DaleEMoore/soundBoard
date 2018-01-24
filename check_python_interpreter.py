# From https://intellij-support.jetbrains.com/hc/en-us/requests/1107821

# kivy examples https://github.com/kivy/kivy/tree/master/examples/widgets/recycleview
# don't work in PyCharm because they get "ImportError: No module named 'kivy._clock'";
# but, examples run from the command line work fine.

# From https://gist.github.com/vlasovskikh/968240f877117cb6c882

import sys
import os
import pkg_resources
from pprint import pprint
import socket


pprint({
    'sys.version_info': sys.version_info,
    'sys.prefix': sys.prefix,
    'sys.path': sys.path,
    'pkg_resources.working_set': list(pkg_resources.working_set),
    'PATH': os.environ['PATH'].split(os.pathsep),
    'HOSTNAME': socket.gethostname(),
})
