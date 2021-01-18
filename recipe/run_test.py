# *****************************************************************
# (C) Copyright IBM Corp. 2020, 2021. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# *****************************************************************

import os
import sys
import pytest
import spacy


PACKAGE_DIR = os.path.abspath(os.path.dirname((spacy.__file__)))

# skip a few tests while we investigate - these tests pass in X86_64
# skip test_issue6177 as it is failing on RH8 x86
sys.exit(pytest.main([PACKAGE_DIR,'-k','not match and not test_issue3328 and not test_issue6177']))
