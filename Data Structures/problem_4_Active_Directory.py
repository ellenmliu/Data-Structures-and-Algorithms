class Group(object):
    def __init__(self, _name):
        self.name = _name
        self.groups = []
        self.users = []

    def add_group(self, group):
        self.groups.append(group)

    def add_user(self, user):
        self.users.append(user)

    def get_groups(self):
        return self.groups

    def get_users(self):
        return self.users

    def get_name(self):
        return self.name


parent = Group("parent")
child = Group("child")
sub_child = Group("subchild")

sub_child_user = "sub_child_user"
sub_child.add_user(sub_child_user)

child.add_group(sub_child)
parent.add_group(child)

def is_user_in_group(user, group):
    """
    Return True if user is in the group, False otherwise.

    Args:
      user(str): user name/id
      group(class:Group): group to check user membership against
    """
    if user in group.get_users():
        return True
    for sub_group in group.get_groups():
        if is_user_in_group(user, sub_group):
            return True
    return False

test_cases = [
{
    "user": "sub_child_user",
    "group": sub_child,
    "expected": True
},
{
    "user": "sub_child_user",
    "group": child,
    "expected": True
},
{
    "user": "sub_child_user",
    "group": parent,
    "expected": True
},
{
    "user": "sub_child_user_false",
    "group": sub_child,
    "expected": False
},
{
    "user": "",
    "group": sub_child,
    "expected": False
}
]

for case in test_cases:
    print("Finding {} in group {}: ".format(case["user"], case["group"].get_name()), "pass" if is_user_in_group(case["user"], case["group"]) == case["expected"] else "fail")
