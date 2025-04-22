# ansible-lint-keyorder-overrides

Custom key order definitions for [ansible-lint](https://github.com/ansible/ansible-lint)
that enforce consistent structure across Ansible playbooks, tasks, roles, and blocks.

This module extends ansible-lint's built-in key-order rule to provide a structured ordering of YAML keys
in your Ansible code.
The result is readable, maintainable, and consistently structured playbooks.

> This is the key ordering standard we use at [networkmatic](https://networkmatic.de) to ensure consistency across our
> infrastructure-as-code repositories.
> It's designed to enhance readability and comprehension of automation code.

## Why Use Custom Key Ordering?

By default, ansible-lint provides a basic key ordering that focuses primarily on having `name` first,
followed by arbitrary module parameters, and concluding with block structures.
This ordering may be insufficient for complex playbooks where organization becomes important for maintainability.

### The Problem

Ansible's flexible YAML structure is powerful but comes with considerations:

- Inconsistent organization of playbook elements
- Important attributes can be hard to locate within tasks
- Code review focus diverted to formatting issues
- Increased maintenance complexity as codebases grow

### The Solution

This custom key order implements a structured approach that:

- Creates consistent positioning of key elements
- Groups related concepts for better readability
- Establishes predictable patterns across your codebase
- Shifts code review focus to functionality rather than formatting

By adopting a standardized key order, your Ansible code becomes more consistent, easier to scan, and well-structured,
whether you're working solo or in a team environment.

## Usage

First, clone this repository to a location of your choice:

```bash
git clone https://github.com/networkmatic/ansible-lint-keyorder-overrides.git
```

### Method 1: Command Line

Run ansible-lint with the custom rules:

```bash
ansible-lint -R -r /path/to/ansible-lint-keyorder-overrides/rules
```

The `-r` parameter specifies the directory containing your custom rules, and the `-R` parameter ensures that the default
rules are kept alongside your custom rules.
The `-R` flag is especially important in this case because we're overriding the configuration for a default rule
(`key-order`), not just adding new rules.

### Method 2: VS Code Integration

Add the following to your VS Code settings (settings.json):

```json
"ansible.validation.lint.arguments": "-R -r /path/to/ansible-lint-keyorder-overrides/rules"
```

VS Code's Ansible extension will now use your custom key order when linting playbooks.

## Example

Before:

```yaml
- name: Install package
  tags: [install]
  when: ansible_os_family == "Debian"
  ansible.builtin.apt:
    name: vim
```

After:

```yaml
- name: Install package
  ansible.builtin.apt:
    name: vim
  when: ansible_os_family == "Debian"
  tags: [install]
```

## Custom Key Order

Our custom key ordering enforces the following sequence:

1. `name` - Task identification
2. `hosts`, `connection` - Target and connection config
3. `delegate_to`, `delegate_facts` - Delegation settings
4. `gather_facts`, `become` - Execution context
5. `no_log`, `check_mode` - Task behavior settings
6. `module_defaults`, `vars_prompt`, `vars_files`, `vars` - Variable definitions
7. `args`, `environment` - Parameters and environment
8. `run_once`, `handlers`, `pre_tasks`, `roles`, `tasks`, `post_tasks` - Execution flow
9. `action` followed by module arguments - The actual operation
10. `None` - Catch-all for module names and any other keys not explicitly defined in the ordering
11. `register`, `until`, `retries`, `delay` - Result handling
12. `changed_when`, `failed_when`, `notify` - Status handling
13. `when` - Conditional execution
14. `loop`, `loop_control` - Iteration settings
15. `tags`, `listen` - Targeting and notifications
16. `block`, `rescue`, `always` - Block structures

This ordering prioritizes readability by grouping related concepts together, with the most important identifiers at the top.

While this is our preferred arrangement for organizing Ansible code, it's certainly not the only valid approach.
The key benefit is adopting a consistent structure, regardless of the specific ordering you choose.
This implementation represents one opinionated but practical solution to the problem of inconsistent YAML structures.

## Compatibility

This override depends on internal `ansible-lint.rules.key_order` structures.
It is compatible with ansible-lint 25.2.1 and may require updates for future versions.

## License

MIT License – see [LICENSE](./LICENSE) file.
