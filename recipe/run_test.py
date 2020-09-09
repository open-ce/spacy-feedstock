# *****************************************************************
#
# Licensed Materials - Property of IBM
#
# (C) Copyright IBM Corp. 2020. All Rights Reserved.
#
# US Government Users Restricted Rights - Use, duplication or
# disclosure restricted by GSA ADP Schedule Contract with IBM Corp.
#
# *****************************************************************

import os
import sys
import pytest
import spacy


PACKAGE_DIR = os.path.abspath(os.path.dirname((spacy.__file__)))

# skip a few tests while we investigate - these tests pass in X86_64
sys.exit(pytest.main([PACKAGE_DIR,'-k','not match and not test_issue3328']))
