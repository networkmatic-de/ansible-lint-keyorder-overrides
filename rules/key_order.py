# Copyright 2024 networkmatic GmbH
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.


from ansiblelint.rules import key_order


"""Custom key order configuration for Ansible Lint.

This module overrides the default key order defined in ansible-lint's key_order rule
to enforce a specific ordering of task attributes that better aligns with our coding standards.
"""

key_order.SORTER_TASKS = (
    "name",
    "hosts",
    "connection",
    "delegate_to",
    "delegate_facts",
    "gather_facts",
    "become",
    "no_log",
    "check_mode",
    "module_defaults",
    "vars_prompt",
    "vars_files",
    "vars",
    "args",
    "environment",
    "run_once",
    "handlers",
    "pre_tasks",
    "roles",
    "tasks",
    "post_tasks",
    "action",
    None,
    "register",
    "until",
    "retries",
    "delay",
    "changed_when",
    "failed_when",
    "notify",
    "when",
    "loop",
    "loop_control",
    "tags",
    "listen",
    "block",
    "rescue",
    "always",
)
